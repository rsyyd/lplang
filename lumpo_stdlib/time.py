# lumpo_stdlib/time.py — time module for lumpo
import time as _time
from datetime import datetime as _dt


def now():
    """current unix timestamp in seconds (float)"""
    return _time.time()


def sleep(seconds):
    _time.sleep(float(seconds))


def clock():
    """monotonic clock for measuring intervals"""
    return _time.monotonic()


def iso():
    """current time as ISO-8601 string"""
    return _dt.now().isoformat()


def format(ts, fmt="%Y-%m-%d %H:%M:%S"):
    """format a unix timestamp"""
    return _dt.fromtimestamp(ts).strftime(fmt)
