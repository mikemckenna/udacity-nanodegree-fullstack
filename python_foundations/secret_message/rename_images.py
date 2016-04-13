import os
import shutil

images_src = "images_original"
images_dest = "images_renamed"


def init():
    copy_images()
    print("--- Get Files ---")
    rename_files()


def copy_images():
    shutil.rmtree(images_dest, ignore_errors=True, onerror=None)
    print("Directory & contents deleted")
    shutil.copytree(images_src, images_dest)
    print("Source copied into destination")


def strip_numbers(file_name):
    return file_name.translate(None, "0123456789")


def rename_files():
    file_list = os.listdir(images_dest)
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(images_dest)

    for file_name in file_list:
        new_file = strip_numbers(file_name)
        print("Old File: " + file_name)
        print("New File: " + new_file)
        os.rename(file_name, new_file)

    os.chdir(saved_path)

init()
