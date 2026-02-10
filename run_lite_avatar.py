#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_lite_avatar.py - Helper script để chạy lite-avatar trên Colab
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

# Parse arguments
parser = argparse.ArgumentParser(description='Run Lite-Avatar with fixed imports')
parser.add_argument('--data_dir', type=str, default='./data', help='Directory containing source.png')
parser.add_argument('--audio_file', type=str, required=True, help='Audio file name')
parser.add_argument('--result_dir', type=str, default='./result', help='Output directory')
args = parser.parse_args()

# Tạo thư mục nếu chưa có
os.makedirs(args.data_dir, exist_ok=True)
os.makedirs(args.result_dir, exist_ok=True)

# Kiểm tra file
data_files = os.listdir(args.data_dir)
image_found = any(f.endswith(('.png', '.jpg', '.jpeg')) for f in data_files)

if not image_found:
    print(f"❌ Không tìm thấy file ảnh trong {args.data_dir}")
    print("Hãy upload ảnh vào thư mục data!")
    sys.exit(1)

if not os.path.exists(args.audio_file):
    print(f"❌ Không tìm thấy file âm thanh: {args.audio_file}")
    sys.exit(1)

# Chạy fix_imports.py nếu có
if os.path.exists('fix_imports.py'):
    print("🔧 Đang sửa các import trong mã nguồn...")
    subprocess.run(['python', 'fix_imports.py'])

# Chạy lite_avatar.py
print(f"🚀 Đang chạy lite-avatar với:")
print(f"   🖼️  Ảnh từ: {args.data_dir}")
print(f"   🎵 Audio: {args.audio_file}")
print(f"   📂 Output: {args.result_dir}")

cmd = [
    'python', 'lite_avatar.py',
    '--data_dir', args.data_dir,
    '--audio_file', args.audio_file,
    '--result_dir', args.result_dir
]

try:
    subprocess.run(cmd)
    
    # Kiểm tra kết quả
    result_files = [f for f in os.listdir(args.result_dir) if f.endswith('.mp4')]
    
    if result_files:
        print(f"\n✅ Tạo video thành công!")
        print(f"📹 File output: {os.path.join(args.result_dir, result_files[0])}")
    else:
        print(f"\n❌ Không tìm thấy video output trong {args.result_dir}")
        
except Exception as e:
    print(f"\n❌ Lỗi: {e}")
