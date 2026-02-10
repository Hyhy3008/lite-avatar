#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_imports.py - Script tự động sửa tất cả các file có import typeguard
"""

import os
import sys
import glob

def fix_file(file_path):
    """Sửa file Python để thay thế import typeguard."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    # Thay thế import
    modified = False
    
    # Các pattern import cần thay thế
    replacements = [
        ('from typeguard import check_argument_types', 
         'from fake_typeguard import check_argument_types'),
        ('from typeguard import typechecked', 
         'from fake_typeguard import typechecked'),
        ('from typeguard import check_return_type', 
         'from fake_typeguard import check_return_type'),
        ('from typeguard import check_argument_types, typechecked', 
         'from fake_typeguard import check_argument_types, typechecked'),
        ('from typeguard import check_argument_types, check_return_type', 
         'from fake_typeguard import check_argument_types, check_return_type'),
        ('from typeguard import typechecked, check_return_type', 
         'from fake_typeguard import typechecked, check_return_type'),
        ('from typeguard import check_argument_types, check_return_type, typechecked', 
         'from fake_typeguard import check_argument_types, check_return_type, typechecked'),
        ('import typeguard', 
         'import fake_typeguard as typeguard')
    ]
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            modified = True
    
    if modified:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed: {file_path}")
            return True
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return False
    
    return False

def scan_directory(directory):
    """Tìm tất cả file Python trong thư mục và sửa chúng."""
    fixed_count = 0
    
    for py_file in glob.glob(os.path.join(directory, "**/*.py"), recursive=True):
        if fix_file(py_file):
            fixed_count += 1
    
    return fixed_count

if __name__ == "__main__":
    root_dir = "."  # Thư mục hiện tại
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    
    print(f"Scanning {root_dir} for Python files...")
    fixed_count = scan_directory(root_dir)
    print(f"Fixed {fixed_count} files.")
    
    # Copy fake_typeguard.py vào các thư mục cần thiết
    try:
        os.system("cp fake_typeguard.py funasr_local/")
        os.system("cp fake_typeguard.py funasr_local/tasks/")
        print("Copied fake_typeguard.py to necessary directories")
    except Exception as e:
        print(f"Error copying fake_typeguard.py: {e}")
