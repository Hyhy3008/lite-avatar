#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup.py - Script cài đặt và cấu hình Lite-Avatar
"""

import os
import sys
import shutil
import subprocess
import argparse

def install_dependencies():
    """Cài đặt các dependency cần thiết."""
    print("📦 Cài đặt dependencies...")
    
    # Cài từ requirements.txt
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Cài thêm một số thư viện quan trọng
    important_packages = [
        "typeguard==2.7.1",
        "loguru",
        "onnxruntime",
        "pydub",
        "imageio",
        "imageio-ffmpeg",
        "jamo",
    ]
    
    for package in important_packages:
        subprocess.run(["pip", "install", package])
    
    # Cài jamo từ GitHub nếu cài thông thường thất bại
    try:
        import jamo
        print("✓ jamo đã được cài đặt")
    except ImportError:
        print("! Cài jamo từ GitHub...")
        subprocess.run(["pip", "install", "git+https://github.com/JDongian/python-jamo.git"])

def fix_typeguard_imports():
    """Sửa các import typeguard."""
    print("🔧 Sửa import typeguard...")
    if os.path.exists("fix_imports.py"):
        subprocess.run(["python", "fix_imports.py"])
    else:
        print("❌ Không tìm thấy fix_imports.py")

def setup_folders():
    """Tạo các thư mục cần thiết."""
    print("📂 Tạo thư mục dữ liệu...")
    os.makedirs("data", exist_ok=True)
    os.makedirs("result", exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Setup Lite-Avatar")
    parser.add_argument("--skip-deps", action="store_true", help="Skip dependency installation")
    args = parser.parse_args()
    
    # Tạo thư mục
    setup_folders()
    
    # Cài dependencies
    if not args.skip_deps:
        install_dependencies()
    
    # Sửa imports
    fix_typeguard_imports()
    
    print("\n✅ Cài đặt hoàn tất!")
    print("""
HƯỚNG DẪN SỬ DỤNG:
1. Đặt ảnh vào thư mục 'data/'
2. Đặt file audio vào thư mục gốc
3. Chạy lệnh: python lite_avatar.py --data_dir ./data --audio_file your_audio.mp3 --result_dir ./result
4. Video kết quả sẽ được lưu trong 'result/'
""")

if __name__ == "__main__":
    main()
