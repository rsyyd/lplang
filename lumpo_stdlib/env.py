# lumpo_stdlib/env.py
import os

def get(key, default_val=""):
    return os.environ.get(key, default_val)

def set(key, val):
    os.environ[key] = str(val)

def has(key):
    return key in os.environ
