import json
import os
import Randomizer.WildEncounters.wildrando as WildRandomizer
import Randomizer.Trainers.trainerrando as TrainerRandomizer
import Randomizer.PersonalData.personal_randomizer as PersonalRandomizer
import Randomizer.Starters.randomize_starters as StarterRandomizer
import Randomizer.StaticSpawns.statics as StaticRandomizer
import Randomizer.Scenes.patchscene as PatchScene
import Randomizer.FileDescriptor.fileDescriptor as FileDescriptor
import Randomizer.Textures.textures as PatchTextures
import Randomizer.FieldItem.fielditem as FieldItemRandomizer
import Randomizer.Shop.shop as ShopRandomizer
import Randomizer.Tms.tms as TmRandomizer
import Randomizer.Shared.pla as pla
import Randomizer.Shared.output as output
import shutil
import subprocess

#thanks zadenowen for the function
def generateBinary(schema: str, json: str, path: str):
    flatc = "flatc/flatc.exe"
    outpath = os.path.abspath("output/romfs/" + path)
    #print(outpath)
    proc = subprocess.run(
        [os.path.abspath(flatc),
        "-b",
        "-o",
        outpath,
        os.path.abspath(schema),
        os.path.abspath(json)
        ], capture_output=True
    )
    #print(proc)
    return proc

def open_config():
    file = open("config.json", "r")
    config = json.load(file)
    file.close()
    return config

def create_modpack():
    if os.access("output/romfs", mode=777) == True: #exists
        shutil.rmtree("output/")
    os.makedirs("output/romfs", mode=777, exist_ok=True)

def create_batch_modpack():
    if os.access("batchOutput", mode=777) == True: #exists
        shutil.rmtree("batchOutput")
    os.makedirs("batchOutput", mode=777, exist_ok=True)

paths = {
    "wilds": "world/data/encount/pokedata/pokedata",
    "wilds_dlc1": "world/data/encount/pokedata/pokedata_su1",
    "wilds_dlc2": "world/data/encount/pokedata/pokedata_su2",
    "trainers": "world/data/trainer/trdata",
    "gifts": "world/data/event/event_add_pokemon/eventAddPokemon",
    "personal": "avalon/data",
    "statics": "world/data/field/fixed_symbol/fixed_symbol_table",
    "tms": "world/data/item/itemdata",
    "catalog": "pokemon/catalog/catalog",
    "scenes": "world/scene/parts/event/event_scenario/main_scenario/common_0070_",
    "textures": "pokemon/data",
    "trpfd": "arc",
    "field_item": "world/data/item/hiddenItemDataTable",
    "shop": "world/data/ui/shop/friendlyshop/friendlyshop_lineup_data",
    "tms": "world/data/item/itemdata",
    "fieldItem_dlc1": "world/data/item/hiddenItemDataTable_su1",
    "fieldItem_dlc2": "world/data/item/hiddenItemDataTable_su2"
}

#Investigate using some kind of object built when the program boots that contains all paths to json files ?
#with some kind of processing if the pla mod is present... or force binary format ? requires romfs tho..
def randomize(config):
    create_modpack()
    if os.access("mods/", os.F_OK):
        shutil.copytree('mods/', 'output/romfs', dirs_exist_ok=True)
    if config['wild_randomizer']['is_enabled'] == "yes":
        WildRandomizer.randomize(config['wild_randomizer'], 'pokedata_array')
        WildRandomizer.randomize(config['wild_randomizer'], 'pokedata_su1_array')
        WildRandomizer.randomize(config['wild_randomizer'], 'pokedata_su2_array')
        generateBinary("Randomizer/WildEncounters/pokedata_array.bfbs", "Randomizer/WildEncounters/pokedata_array.json", paths["wilds"])
        generateBinary("Randomizer/WildEncounters/pokedata_su1_array.bfbs", "Randomizer/WildEncounters/pokedata_su1_array.json", paths["wilds_dlc1"])
        generateBinary("Randomizer/WildEncounters/pokedata_su2_array.bfbs", "Randomizer/WildEncounters/pokedata_su2_array.json", paths["wilds_dlc2"])
    if config['trainer_randomizer']['is_enabled'] == "yes":
        TrainerRandomizer.randomize(config['trainer_randomizer'])
        generateBinary("Randomizer/Trainers/trdata_array.bfbs", "Randomizer/Trainers/trdata_array.json", paths["trainers"])
    if config['personal_data_randomizer']['is_enabled'] == "yes":
        PersonalRandomizer.randomize(config['personal_data_randomizer'])
        generateBinary("Randomizer/PersonalData/personal_array.fbs", "Randomizer/PersonalData/personal_array.json", paths["personal"])
    if config['starter_randomizer']['is_enabled'] == "yes":
        StarterRandomizer.randomize(config['starter_randomizer'])
        generateBinary("Randomizer/Starters/eventAddPokemon_array.bfbs", "Randomizer/Starters/eventAddPokemon_array.json", paths["gifts"])
    if config['static_randomizer']['is_enabled'] == "yes":
        StaticRandomizer.randomize(config['static_randomizer'])
        generateBinary("Randomizer/StaticSpawns/fixed_symbol_table_array.bfbs", "Randomizer/StaticSpawns/fixed_symbol_table_array.json", paths["statics"])
    if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['show_starters_in_overworld'] == "yes":
        PatchScene.patchScenes(config)
        generateBinary("Randomizer/Scenes/poke_resource_table.fbs", "Randomizer/Scenes/poke_resource_table.json", paths['catalog'])
        os.makedirs("output/romfs/" + paths['scenes'], mode=777, exist_ok=True)
        shutil.copyfile("Randomizer/Scenes/common_0070_always_0.trsog", "output/romfs/" + paths['scenes'] + '/common_0070_always_0.trsog')
        shutil.copyfile("Randomizer/Scenes/common_0070_always_1.trsog", "output/romfs/" + paths['scenes'] + '/common_0070_always_1.trsog')
        #for textures we do it invertedly because i am NOT copying texture folders by assuming folder presence
        os.makedirs('output/romfs/' + paths['textures'], mode=777, exist_ok=True)
        PatchTextures.patchTextures(config)
    if config['field_item_randomizer']['is_enabled'] == "yes":
        FieldItemRandomizer.randomize(config['field_item_randomizer'], 'hiddenItemDataTable_array')
        FieldItemRandomizer.randomize(config['field_item_randomizer'], 'hiddenItemDataTable_su1_array')
        FieldItemRandomizer.randomize(config['field_item_randomizer'], 'hiddenItemDataTable_su2_array')
        generateBinary("Randomizer/FieldItem/hiddenItemDataTable_array.bfbs", "Randomizer/FieldItem/hiddenItemDataTable_array.json", paths['field_item'])
        generateBinary("Randomizer/FieldItem/hiddenItemDataTable_su1_array.bfbs", "Randomizer/FieldItem/hiddenItemDataTable_su1_array.json", paths['fieldItem_dlc1'])
        generateBinary("Randomizer/FieldItem/hiddenItemDataTable_su2_array.bfbs", "Randomizer/FieldItem/hiddenItemDataTable_su2_array.json", paths['fieldItem_dlc2'])
    if config['shop_randomizer']['is_enabled'] == "yes":
        ShopRandomizer.randomize(config['shop_randomizer'])
        generateBinary("Randomizer/Shop/friendlyshop_lineup_data_array.bfbs", "Randomizer/Shop/friendlyshop_lineup_data_array.json", paths["shop"])
    if config['tm_randomizer']['is_enabled'] == "yes":
        TmRandomizer.randomize()
        generateBinary("Randomizer/Tms/itemdata_array.bfbs", "Randomizer/Tms/itemdata_array.json", paths["tms"])
    if config['patch_trpfd'] == "yes":
        FileDescriptor.patchFileDescriptor()
        generateBinary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
    else:
        shutil.make_archive("output/randomizer", "zip", "output/romfs/")

def test():
    create_modpack()

def main():
    config = open_config()
    StarterRandomizer.configure_starters(config['starter_randomizer'])
    if config['number_of_files'] <= 1:
        randomize(config)
    else: #bigger than 1, gotta go loop mode
        i = 0
        create_batch_modpack()
        while i < config['number_of_files']:
            randomize(config)
            #create new output folder for mass outputs
            if config['patch_trpfd'] == 'yes':
                shutil.copytree('output/', 'batchOutput/randomizer' + str(i+1))
            else:
                shutil.copyfile("output/randomizer.zip", "batchOutput/randomizer" + str(i+1) + ".zip")
            i = i + 1
    output.output_starters()
if __name__ == "__main__":
    main()
