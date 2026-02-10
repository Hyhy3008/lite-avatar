#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fake_typeguard.py - Thay thế cho thư viện typeguard
"""

def check_argument_types():
    """Hàm giả lập check_argument_types, luôn trả về True."""
    return True

def typechecked(func=None, **kwargs):
    """Hàm giả lập typechecked decorator."""
    if func is None:
        # Được gọi với tham số như @typechecked(...)
        return lambda f: f
    # Được gọi trực tiếp như @typechecked
    return func

# Thêm các hàm khác từ typeguard nếu cần
