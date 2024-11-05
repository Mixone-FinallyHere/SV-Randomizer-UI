import json
import os
import shutil
import random
import secrets

def determineIfShiny(rate):
    if rate == 1:
        return True
    if rate == 0:
        return False
    for i in range(3): #3 tries like old games
        #random_num = random.randint(1, rate)
        random_num = secrets.randbelow(rate)
        if random_num == secrets.randbelow(rate): #technically works ???
            return True
    return False

def get_texture_path(original_path: str):
    #"pm0278/pm0278_00_00/pm0278_00_00.trmdl" example
    splitted_string = original_path.split('/')
    path = splitted_string[0] + "/" + splitted_string[1]
    return path

def patchTextures(config):
    romfs_path = config['romfs_path'] + "/pokemon/data/"
    starter_index = 1012 #index in the catalog, way easier
    catalogfile = open(os.getcwd() + "/Randomizer/Scenes/poke_resource_table.json", "r") #we are going to assume an edited file is present
    catalog = json.load(catalogfile)
    catalogfile.close()

    if os.access(config['romfs_path'], mode=777) == False:
        print("Cannot access game RomFS ! Make sure correct path is set in config.")
    else:
        for i in range(3):
            if determineIfShiny(config['shiny_rate']) is True:
                texture_folders = get_texture_path(catalog['unk_1'][starter_index]['model'])
                texture_dir = romfs_path + texture_folders
                os.makedirs("output/romfs/pokemon/data/" + texture_folders , mode=777, exist_ok=True) #i need to refactor this at some point
                files: list[str] = os.listdir(texture_dir)
                for filename in files:
                    if filename.find("rare") != -1:
                        shutil.copyfile(texture_dir + "/" +filename, "output/romfs/pokemon/data/" + texture_folders + '/' + filename.replace("_rare", '')) #my god i feel like i could simplify this
            starter_index = starter_index + 1



