#item id: https://raw.githubusercontent.com/kwsch/pkNX/master/pkNX.Structures.FlatBuffers.SV/Schemas/Shared/ItemID.fbs
#binaries and bfbs are at world/data/item/hiddenItemDataTable

from Randomizer.Shared.ItemID import ItemID
from Randomizer.Shared.banned_item import BannedItem
import json
import secrets
import os

def randomize(config, filename):
    item_ids = [getattr(ItemID, attr) for attr in dir(ItemID) if not callable(getattr(ItemID, attr)) and not attr.startswith("__")] #lmao wtf
    banned_item = BannedItem
    file = open(os.getcwd() + '/Randomizer/FieldItem/' + filename + '_clean.json', 'r')
    data = json.load(file)
    file.close()

    for entry in data['values']:
        for item in entry.values():
            if isinstance(item, dict) and "itemId" in item:
                if item['itemId'] != "ITEMID_NONE":
                    choice = secrets.choice(item_ids)
                    while banned_item.is_banned(choice) == True:
                        choice = secrets.choice(item_ids)
                    item["itemId"] = choice
    
    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/FieldItem/" + filename + ".json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation done !")