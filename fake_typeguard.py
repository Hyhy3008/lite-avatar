#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fake_typeguard.py - Thay thế cho thư viện typeguard
"""

def check_argument_types():
    """Always return True to bypass type checking."""
    return True

def check_return_type(retval, func=None):
    """Always return the value to bypass return type checking."""
    return retval

def typechecked(func=None, **kwargs):
    """Fake decorator that just returns the original function."""
    if func is None:
        # When called with parameters like @typechecked(...)
        return lambda f: f
    # When called directly like @typechecked
    return func
