#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_colab.py - Script hỗ trợ chạy Lite-Avatar trên Google Colab
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

def setup_environment():
    """Cấu hình môi trường chạy."""
    # Tạo thư mục cần thiết
    os.makedirs("data", exist_ok=True)
    os.makedirs("result", exist_ok=True)
    
    # Kiểm tra fake_typeguard đã có chưa
    if not os.path.exists("fake_typeguard.py"):
        print("❌ Thiếu file fake_typeguard.py!")
        return False
    
    # Kiểm tra fix_imports đã chạy chưa
    if os.path.exists("fix_imports.py"):
        subprocess.run(["python", "fix_imports.py"])
    
    # Copy fake_typeguard vào các thư mục cần thiết
    subprocess.run(["cp", "fake_typeguard.py", "funasr_local/"])
    subprocess.run(["cp", "fake_typeguard.py", "funasr_local/tasks/"])
    
    return True

def validate_files(data_dir, audio_file):
    """Kiểm tra các file đầu vào."""
    # Kiểm tra ảnh
    if not os.path.exists(data_dir):
        print(f"❌ Thư mục {data_dir} không tồn tại!")
        return False
    
    image_found = False
    for f in os.listdir(data_dir):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_found = True
            break
    
    if not image_found:
        print(f"❌ Không tìm thấy file ảnh trong {data_dir}")
        return False
    
    # Kiểm tra audio
    if not os.path.exists(audio_file):
        print(f"❌ Không tìm thấy file audio: {audio_file}")
        return False
    
    return True

def run_lite_avatar(data_dir, audio_file, result_dir):
    """Chạy Lite-Avatar."""
    cmd = [
        "python", "lite_avatar.py",
        "--data_dir", data_dir,
        "--audio_file", audio_file,
        "--result_dir", result_dir
    ]
    
    print(f"🚀 Chạy lệnh: {' '.join(cmd)}")
    subprocess.run(cmd)
    
    # Kiểm tra kết quả
    if os.path.exists(result_dir):
        result_files = [f for f in os.listdir(result_dir) if f.endswith('.mp4')]
        if result_files:
            print(f"\n✅ Tạo video thành công!")
            print(f"📹 File output: {os.path.join(result_dir, result_files[0])}")
            return True
    
    print(f"\n❌ Không tìm thấy video output trong {result_dir}")
    return False

def main():
    parser = argparse.ArgumentParser(description='Run Lite-Avatar on Google Colab')
    parser.add_argument('--data_dir', type=str, default='./data', help='Directory with images')
    parser.add_argument('--audio_file', type=str, required=True, help='Audio file name')
    parser.add_argument('--result_dir', type=str, default='./result', help='Output directory')
    args = parser.parse_args()
    
    # Cấu hình môi trường
    if not setup_environment():
        print("❌ Cấu hình môi trường thất bại!")
        return 1
    
    # Kiểm tra file
    if not validate_files(args.data_dir, args.audio_file):
        print("❌ Kiểm tra file thất bại!")
        return 1
    
    # Chạy Lite-Avatar
    success = run_lite_avatar(args.data_dir, args.audio_file, args.result_dir)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
