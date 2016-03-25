import os
from os.path import isfile, join

from shutil import copy2

# Directory were to look for files
BASE_DIR = "C:\\Users\\hp\\Desktop\\NorskSjomat\\PlayFolder"

# Folder were you wan't to save files
SAVE_DIR = "C:\\Users\\hp\\Desktop\\NorskSjomat\\PlayFolder"

# Lot number separator from trash text
SEPARATOR = "_"


def start():
	input("Press Enter to Start")

	for filename in os.listdir(BASE_DIR):
		print(filename)

	for file in os.listdir(BASE_DIR):
		if isfile(join(BASE_DIR,file)):
			process_file(file)

	input("Press Enter to Close")

def get_lotnr(file):
	lot_nr = ''.join(file.split(SEPARATOR, 1)[:1])
	return lot_nr

def get_file_ext(file):
	ext = file.split(".", 1)
	ext = "." + ext[1]
	return ext

def process_file(file):
	lot_nr = get_lotnr(file)
	file_full_path = join(BASE_DIR, file)
	dir_full_path = join(BASE_DIR, lot_nr)

	if not os.path.exists(dir_full_path):
		os.makedirs(dir_full_path)
		os.chmod(dir_full_path, 0o777)
		copy2(file_full_path, dir_full_path + "/" + lot_nr + get_file_ext(file_full_path))

start()