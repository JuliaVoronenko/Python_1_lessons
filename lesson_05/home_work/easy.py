import os

def show_files(path):
    print(os.listdir(path))

def delete_dir(path):
    os.rmdir(path)

def create_dir(path):
    os.mkdir(path)