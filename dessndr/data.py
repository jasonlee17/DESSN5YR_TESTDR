#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  data.py
#
#  Copyright 2024 bruno <bsanchez@cppm.in2p3.fr>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# my_package/data_handler.py
import os
import requests
from tqdm import tqdm
import diskcache
import subprocess


# Remote address
DES5YRDR_URL = """https://github.com/des-science/DES-SN5YR"""

# Local download
DES5YRDR_DATA_ROOT = os.getenv("DES5YRDR_DATA_ROOT")
DES5YRDR_DATA = os.getenv("DES5YRDR_DATA")
if DES5YRDR_DATA_ROOT is None:
    DES5YRDR_DATA_ROOT = os.path.join(os.getenv("HOME"), "DES5YRDR_DATA_ROOT")
    DES5YRDR_DATA = os.path.join(DES5YRDR_DATA_ROOT, "DES-SN5YR")

def clone_repo(repo_url=DES5YRDR_URL, dest_folder=DES5YRDR_DATA_ROOT):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    clone_path = os.path.join(dest_folder, repo_name)
    
    if os.path.exists(clone_path):
        print(f"{clone_path} already exists. Skipping cloning.")
    else:
        subprocess.run(['git', 'clone', repo_url, clone_path], check=True)
    
    os.environ['DES5YRDR_DATA'] = clone_path
    print(f"Repository cloned to: {clone_path}")
    print(f"Environment variable DES5YRDR_DATA set to: {clone_path}")


def download_all(*args, **kwargs):
    clone_repo()


def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    filename = os.path.join(dest_folder, url.split('/')[-1])
    
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping download.")
        return filename
    
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR: Something went wrong with the download")
    
    return filename


def get_data(url):
    dest_folder = os.path.join(os.path.expanduser('~'), '.my_package_data')
    return download_file(url, dest_folder)


def load_data(file_path, cache_dir=".cache"):
    """Load data from a cached file, using caching."""
    cache = diskcache.Cache(cache_dir)

    if file_path in cache:
        return cache[file_path]
    else:
        with open(file_path, 'r') as file:
            data = file.read()
        cache[file_path] = data
        return data

def read_data(data):
    """Read and process the loaded data."""
    processed_data = data.upper()
    return processed_data
