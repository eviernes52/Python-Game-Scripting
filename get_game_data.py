import os
import json
import shutil
from subprocess import PIPE, run
import sys 


#variable to say what needs to be looked at
GAME_DIR_PATTERN = "game"


#creation of new directory 
def create_dir(path):
    if not os.path.exists(path):    #if not in existance
        
        os.makedirs(path)            #create directory at said path

def find_all_game_paths(source):
    game_paths = []
    
    #walks recursivley through the source directory: Gives root directory -> directories -> files
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        
        break #only being run once
    return game_paths


def get_game_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path) #split path into directory and name/ use built in functions like this
        new_dir_name = dir_name.replace(to_strip,"") #strip the game from the name
        new_names.append(new_dir_name)
        return new_names

def copy_and_overwrite(source, dest): #recusive copy
    



def main(source, target):
    cwd = os.getcwd()  # Always do os.getcwd for good practice for multiple OS's
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_game_from_paths(game_paths, "_game")
    print(new_game_dirs)

    create_dir(target_path)     #create target directory

# Get source and target directory
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        raise Exception("ONLY PASS Source and Target directory")
    
    source, target, = args[1:]
    main(source, target)