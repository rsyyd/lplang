# lumpo_stdlib/os.py — operating system interaction for lumpo
import os as _os
import sys as _sys


def platform():
    return _sys.platform


def cwd():
    return _os.getcwd()


def chdir(path):
    _os.chdir(str(path))
    return True


def args():
    return _sys.argv[2:] if len(_sys.argv) > 2 else []


def path_join(*parts):
    return _os.path.join(*[str(p) for p in parts])


def path_split(path):
    return list(_os.path.split(str(path)))


def path_ext(path):
    return _os.path.splitext(str(path))[1]


def path_stem(path):
    return _os.path.splitext(_os.path.basename(str(path)))[0]


def is_file(path):
    return _os.path.isfile(str(path))


def is_dir(path):
    return _os.path.isdir(str(path))
