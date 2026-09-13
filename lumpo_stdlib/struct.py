# lumpo_stdlib/struct.py — basic binary packing/unpacking for lumpo
import struct as _struct


def pack_int(n, size=4, byteorder="big", signed=True):
    endian = ">" if byteorder == "big" else "<"
    fmt_map = {1: "b" if signed else "B",
               2: "h" if signed else "H",
               4: "i" if signed else "I",
               8: "q" if signed else "Q"}
    if size not in fmt_map:
        raise ValueError(f"unsupported size: {size}")
    return list(_struct.pack(f"{endian}{fmt_map[size]}", int(n)))


def unpack_int(bytes_list, byteorder="big", signed=True):
    raw = bytes([int(b) & 0xff for b in bytes_list])
    size = len(raw)
    endian = ">" if byteorder == "big" else "<"
    fmt_map = {1: "b" if signed else "B",
               2: "h" if signed else "H",
               4: "i" if signed else "I",
               8: "q" if signed else "Q"}
    if size not in fmt_map:
        raise ValueError(f"unsupported byte length: {size}")
    return _struct.unpack(f"{endian}{fmt_map[size]}", raw)[0]


def hex_to_bytes(hex_str):
    return list(bytes.fromhex(hex_str))


def bytes_to_hex(bytes_list):
    return bytes([int(b) & 0xff for b in bytes_list]).hex()
