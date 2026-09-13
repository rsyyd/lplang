import os, shutil

def exists(path):
    return os.path.exists(path)

def is_dir(path):
    return os.path.isdir(path)

def is_file(path):
    return os.path.isfile(path)

def size(path):
    return os.path.getsize(path)

def mkdir(path):
    os.makedirs(path, exist_ok=True)
    return True

def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
    return True

def copy(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
    return True

def move(src, dst):
    shutil.move(src, dst)
    return True

def list_dir(path="."):
    return os.listdir(path)

def write_text(path, text):
    with open(path, 'w') as f:
        f.write(text)
    return True

def read_text(path):
    with open(path, 'r') as f:
        return f.read()

def append_text(path, text):
    with open(path, 'a') as f:
        f.write(text)
    return True
