import csv
import json
import random
import os
import secrets
import Randomizer.Shared.pla as pla

def fetch_devname(index: int, csvdata):
    #print(csvdata[index])
    return str.strip(csvdata[index])


alt_forms = {
    1028: {
        "species": 26,
        "form": 1
    },
    1033: {
        "species": 50,
        "form": 1
    },
    1034: {
        "species": 51,
        "form": 1
    },
    1035: {
        "species": 52,
        "form": 1
    },
    1036: {
        "species": 52,
        "form": 2
    },
    1037: {
        "species": 53,
        "form": 1
    },
    1038: {
        "species": 58,
        "form": 1
    },
    1039: {
        "species": 59,
        "form": 1
    },
    1046: {
        "species": 79,
        "form": 1
    },
    1048: {
        "species": 80,
        "form": 2
    },
    1050: {
        "species": 88,
        "form": 1
    },
    1051: {
        "species": 89,
        "form": 1
    },
    1053: {
        "species": 100,
        "form": 1
    },
    1054: {
        "species": 101,
        "form": 1
    },
    1061: {
        "species": 128,
        "form": 1
    },
    1062: {
        "species": 128,
        "form": 2
    },
    1063: {
        "species": 128,
        "form": 3
    },
    1067: {
        "species": 144,
        "form": 1
    },
    1068: {
        "species": 145,
        "form": 1
    },
    1069: {
        "species": 146,
        "form": 1
    },
    1072: {
        "species": 157,
        "form": 1
    },
    1074: {
        "species": 194,
        "form": 1
    },
    1075: {
        "species": 199,
        "form": 1
    },
    1104: {
        "species": 211,
        "form": 1
    },
    1107: {
        "species": 215,
        "form": 1
    },
    1148: {
        "species": 422,
        "form": 1
    },
    1149: {
        "species": 423,
        "form": 1
    },
    1155: {
        "species": 479,
        "form": 1
    },
    1156: {
        "species": 479,
        "form": 2
    },
    1157: {
        "species": 479,
        "form": 3
    },
    1158: {
        "species": 479,
        "form": 4
    },
    1159: {
        "species": 479,
        "form": 5
    },
    1160: {
        "species": 483,
        "form": 1
    },
    1161: {
        "species": 484,
        "form": 1
    },
    1162: {
        "species": 487,
        "form": 1
    },
    1181: {
        "species": 503,
        "form": 1
    },
    1183: {
        "species": 549,
        "form": 1
    },
    1185: {
        "species": 550,
        "form": 2
    },
    1186: {
        "species": 550,
        "form": 1
    },
    1191: {
        "species": 570,
        "form": 1
    },
    1192: {
        "species": 571,
        "form": 1
    },
    1200: {
        "species": 628,
        "form": 1
    },
    1201: {
        "species": 641,
        "form": 1
    },
    1202: {
        "species": 642,
        "form": 1
    },
    1203: {
        "species": 645,
        "form": 1
    },
    1295: {
        "species": 705,
        "form": 1
    },
    1296: {
        "species": 706,
        "form": 1
    },
    1303: {
        "species": 713,
        "form": 1
    },
    1310: {
        "species": 720,
        "form": 1
    },
    1311: {
        "species": 724,
        "form": 1
    },
    1316: {
        "species": 745,
        "form": 1
    },
    1317: {
        "species": 745,
        "form": 2
    },
    1368: {
        "species": 876,
        "form": 1
    },
    1373: {
        "species": 892,
        "form": 1
    },
    1375: {
        "species": 898,
        "form": 1
    },
    1376: {
        "species": 898,
        "form": 2
    },
    1378: {
        "species": 905,
        "form": 1
    },
    1328: {
        "species": 37,
        "form": 1
    },
    1329: {
        "species": 38,
        "form": 1
    },
    1330: {
        "species": 74,
        "form": 1
    },
    1331: {
        "species": 75,
        "form": 1
    },
    1332: {
        "species": 76,
        "form": 1
    },
    1333: {
        "species": 110,
        "form": 1
    },
    1334: {
        "species": 1011,
        "form": 1
    },
    1335: {
        "species": 1011,
        "form": 2
    },
    1336: {
        "species": 1011,
        "form": 3
    },
    1337: {
        "species": 901,
        "form": 1
    },
    1338: {
        "species": 492,
        "form": 1
    },
    1400: {
        "species": 646,
        "form": 1
    },
    1401: {
        "species": 646,
        "form": 2
    },
    1402: {
        "species": 647,
        "form": 1
    },
    1403: {
        "species": 386,
        "form": 1
    },
    1404: {
        "species": 386,
        "form": 2
    },
    1405: {
        "species": 386,
        "form": 3
    },
    1406: {
        "species": 800,
        "form": 1
    },
    1407: {
        "species": 800,
        "form": 2
    },
    1408: {
        "species": 741,
        "form": 1,
    },
    1409: {
        "species": 741,
        "form": 2,
    },
    1410: {
        "species": 741,
        "form": 3,
    }
}

allowed_species = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 25, 26, 27, 28, 35, 36, 37, 38, 39, 40, 43, 44, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 69, 70, 71, 72, 73, 74, 75, 76, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 100, 101, 102, 103, 106, 107, 109, 110, 111, 112, 113, 116, 117, 123, 125, 126, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 167, 168, 170, 171, 172, 173, 174, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 203, 204, 205, 206, 209, 210, 211, 212, 214, 215, 216, 217, 218, 219, 220, 221, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 242, 243, 244, 245, 246, 247, 248, 249, 250, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 270, 271, 272, 273, 274, 275, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 296, 297, 298, 299, 302, 307, 308, 311, 312, 313, 314, 316, 317, 322, 323, 324, 325, 326, 328, 329, 330, 331, 332, 333, 334, 335, 336, 339, 340, 341, 342, 349, 350, 353, 354, 355, 356, 357, 358, 361, 362, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 401, 402, 403, 404, 405, 408, 409, 410, 411, 415, 416, 417, 418, 419, 422, 423, 424, 425, 426, 429, 430, 433, 434, 435, 436, 437, 438, 440, 442, 443, 444, 445, 446, 447, 448, 449, 450, 453, 454, 456, 457, 459, 460, 461, 462, 464, 466, 467, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 522, 523, 529, 530, 532, 533, 534, 540, 541, 542, 546, 547, 548, 549, 550, 551, 552, 553, 559, 560, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 585, 586, 590, 591, 594, 595, 596, 602, 603, 604, 607, 608, 609, 610, 611, 612, 613, 614, 615, 619, 620, 622, 623, 624, 625, 627, 628, 629, 630, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 650, 651, 652, 653, 654, 655, 656, 657, 658, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 677, 678, 686, 687, 690, 691, 692, 693, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 712, 713, 714, 715, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 747, 748, 749, 750, 751, 752, 753, 754, 757, 758, 761, 762, 763, 764, 765, 766, 769, 770, 774, 775, 778, 779, 782, 783, 784, 789, 790, 791, 792, 800, 801, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 833, 834, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 854, 855, 856, 857, 858, 859, 860, 861, 863, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025]
legends = [998, 999, 493, 487, 483, 484, 382, 383, 384, 150, 151, 144, 146, 145, 720, 721, 719, 889, 888, 890, 897, 896, 898, 894, 895, 893, 995, 996, 997, 891, 892, 642, 645, 641, 648, 482, 481, 480, 801, 905, 1011, 1334, 1335, 1336, 489, 490, 491, 492, 1014, 1015, 1016, 385, 243, 244, 245, 249, 250, 380, 381, 638, 639, 640, 643, 644, 646, 791, 792, 800, 1021, 1022, 386]
tera_types = ['normal','kakutou', 'hikou', 'doku', 'jimen', 'iwa', 'mushi', 'ghost', 'hagane', 'honoo', 'mizu', 'kusa', 'denki', 'esper', 'koori', 'dragon', 'aku', 'fairy', 'niji']
def check_important_trainer(id: str):
    prefixes = ['leader', 'chair', "e4"]
    for prefix in prefixes:
        if prefix in id:
            return True
    return False

average_level = 0
def make_poke(pokeEntry, index: str, csvdata, config):
    if config['force_6_pokemons_on_important_trainers'] == 'yes' and check_important_trainer(pokeEntry['trid']) == True:
        #chosenmon = allowed_species[random.randint(0, 475)]
        chosenmon = secrets.choice(allowed_species)
        form = 0
        if chosenmon > 1025: #this is an alt form
            form = alt_forms.get(chosenmon)["form"]
            chosenmon = alt_forms.get(chosenmon)["species"]
        pokeEntry['poke' + index]['devId'] = chosenmon
        pokeEntry['poke' + index]['formId'] = form
        pokeEntry['poke' + index]['sex'] = "DEFAULT"
        pokeEntry['poke' + index]['level'] = pokeEntry['poke1']['level']
        if (random.randint(0, 100) < 50):
            pokeEntry['poke' + index]['level'] = pokeEntry['poke' + index]['level'] + 1
        pokeEntry['poke' + index]['wazaType'] = "DEFAULT"
        pokeEntry['poke' + index]['waza1']['wazaId'] = "WAZA_NULL"
        pokeEntry['poke' + index]['waza2']['wazaId'] = "WAZA_NULL"
        pokeEntry['poke' + index]['waza3']['wazaId'] = "WAZA_NULL"
        pokeEntry['poke' + index]['waza4']['wazaId'] = "WAZA_NULL" #6 mons on gyms, elite 4 champ
        if config['force_perfect_ivs'] == "yes":
            talentvalue = {
                "hp": 31,
                "atk": 31,
                "def": 31,
                "spAtk": 31,
                "spDef": 31,
                "agi": 31
            }
            pokeEntry['poke' + index]['talentValue'] = talentvalue
        if (config['randomize_fixed_tera_type'] == "yes" and pokeEntry['poke' + index]['gemType'] != "DEFAULT") or config['randomize_all_tera_type'] == "yes":
            pokeEntry['poke' + index]['gemType'] = secrets.choice(tera_types).upper()
    else:  
        if pokeEntry['poke' + index]['devId'] != "DEV_NULL":   
            chosenmon = secrets.choice(allowed_species)
            form = 0
            if chosenmon > 1025: #this is an alt form
                form = alt_forms.get(chosenmon)["form"]
                chosenmon = alt_forms.get(chosenmon)["species"]
            pokeEntry['poke' + index]['devId'] = chosenmon
            pokeEntry['poke' + index]['formId'] = form
            pokeEntry['poke' + index]['wazaType'] = "DEFAULT"
            pokeEntry['poke' + index]['waza1']['wazaId'] = "WAZA_NULL"
            pokeEntry['poke' + index]['waza2']['wazaId'] = "WAZA_NULL"
            pokeEntry['poke' + index]['waza3']['wazaId'] = "WAZA_NULL"
            pokeEntry['poke' + index]['waza4']['wazaId'] = "WAZA_NULL"
            if config['force_perfect_ivs'] == "yes":
                talentValue = {
                    "hp": 31,
                    "atk": 31,
                    "def": 31,
                    "spAtk": 31,
                    "spDef": 31,
                    "agi": 31
                }
                pokeEntry['poke' + index]['talentValue'] = talentValue
            if (config['randomize_fixed_tera_type'] == "yes" and pokeEntry['poke' + index]['gemType'] != "DEFAULT") or config['randomize_all_tera_type'] == "yes":
                pokeEntry['poke' + index]['gemType'] = secrets.choice(tera_types).upper()

def randomize(config):
    #load information
    file = open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/Trainers/" +"pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    if config['only_legendaries'] == 'yes':
        global allowed_species
        global legends
        allowed_species = legends

    for specie in alt_forms.keys():
        if alt_forms.get(specie)["species"] in allowed_species and specie not in allowed_species:
            allowed_species.append(specie)

    for entry in data['values']:
        i = 1

        while i < 7:
            make_poke(entry, str(i), csvdata, config)
            i = i + 1
        if config['make_ai_smart_for_all_trainers'] == "yes":
            entry['aiBasic'] = True
            entry['aiHigh'] = True
            entry['aiExpert'] = True
            entry['aiChange'] = True
        if config['allow_all_trainers_to_terastalize'] == "yes":
            entry['changeGem'] = True

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation done !")

def main():
   randomize()

if __name__ == "__main__":
    main()
