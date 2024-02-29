#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:19:27 2024

@author: attari.v
"""

import os
import shutil

# Define the folder structure
folders1 = [
    "BAA/DED-A-01-08",
    "BAA/DED-B-01-08",
    "BAA/DED-C-01-08",
]

folders2 = [
    "BAA/DED-B-09-16",
    "BAA/DED-A-09-16",
    "BAA/DED-C-09-16",
]

subfolders1 = [
    "BAA01", "BAA02", "BAA03", "BAA04", "BAA05", "BAA06", "BAA07", "BAA08",
]

subfolders2 = [
    "BAA09", "BAA10", "BAA11", "BAA12", "BAA13", "BAA14", "BAA15", "BAA16"
]

nested_subfolders = [
    "Compression (SHPT)", "EDS-EBSD", "NI-SRJT", "SPT", "XRD"
]

vam_subfolders = [
    "Compression (SHPT)", "EDS", "Microhardness", "NI-HSR", "NI-SRJT",
    "LIPIT", "SPT", "syn", "Tensile", "XRD"
]


def create_and_delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)  # Delete the folder and all its contents
        print(f"Folder '{folder_path}' already exists. Deleting...")
    
    os.makedirs(folder_path)  # Create the folder
    print(f"Folder '{folder_path}' created successfully.")

# Function to create folders recursively
def create_folders(parent_dir, folders_list, subfolders1, subfolders_list):
    for folder in folders_list:
        folder_path = os.path.join(parent_dir, folder)
        os.makedirs(folder_path)
        if subfolders1:
            for subfolder in subfolders1:
                os.makedirs(os.path.join(folder_path, subfolder))
        if subfolders_list:
            for sub1 in subfolders1:
                for sub2 in subfolders_list:
                    os.makedirs(os.path.join(folder_path, sub1, sub2))

# Example usage
folder_name = "BAA"

create_and_delete_folder(folder_name)

# Create folders for BAA and DED
create_folders(".", folders1, subfolders1, nested_subfolders)
create_folders(".", folders2, subfolders2, nested_subfolders)

print("Folder structure created successfully!")
