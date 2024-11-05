# item id: https://raw.githubusercontent.com/kwsch/pkNX/master/pkNX.Structures.FlatBuffers.SV/Schemas/Shared/ItemID.fbs

from Randomizer.Shared.ItemID import ItemID
from Randomizer.Shared.banned_item import BannedItem
import json
import secrets
import os

def randomize(config: any):
    item_ids = [getattr(ItemID, attr) for attr in dir(ItemID) if not callable(getattr(ItemID, attr)) and not attr.startswith("__")] #lmao wtf
    banned_item = BannedItem
    file = open(os.getcwd() + '/Randomizer/Shop/' + 'friendlyshop_lineup_data_array_clean.json', 'r')
    data = json.load(file)
    file.close()

    for entry in data['values']:
        if entry['item'] != "ITEMID_NONE" and entry['lineupid'] != 'shop_00_lineup':
            choice = secrets.choice(item_ids)
            while banned_item.is_banned(choice) == True:
                choice = secrets.choice(item_ids)
            entry["item"] = choice
    
    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/Shop/" +"friendlyshop_lineup_data_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation done !")