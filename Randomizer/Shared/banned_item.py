
class BannedItem():
    def is_banned(itemNo):
        if itemNo >= 428 and itemNo <= 500: # explorer kit id to park ball
            return True
        elif itemNo in [0, 70, 71]: # None, Life Orb, Power Orb
            return True
        elif itemNo >= 65 and itemNo <= 69: # Blue Flute to White Flute
            return True
        elif itemNo >= 95 and itemNo <= 98: # Growth Mulch to Gooey Mulch
            return True
        elif itemNo >= 112 and itemNo <= 134: # Griseous Orb to Sweet Heart
            return True
        elif itemNo >= 137 and itemNo <= 148: # Greet Mail to Bridge Mail M
            return True
        elif itemNo == 155: # Oran Berry
            return True
        elif itemNo >= 159 and itemNo <= 212: # Figy Berry to Rowap Berry
            return True
        elif itemNo == 216: # Exp. Share
            return True
        elif itemNo == 236: # Light Ball
            return True
        elif itemNo >= 256 and itemNo <= 264: # Lucky Punch to Yellow Scarf
            return True
        elif itemNo >= 314 and itemNo <= 320: # Incenses
            return True
        elif itemNo == 16: #cherish ball
            return True
        elif itemNo == 1: #masterball
            return True
        elif itemNo >= 86 and itemNo <= 106: #treasure items
            return True
        elif itemNo == 254: #incense
            return True
        elif itemNo == 255: #incense
            return True
        elif itemNo >= 576 and itemNo <= 583: # Dream ball and item sold for money
            return True
        elif itemNo == 703: # adventure guide
            return True
        elif itemNo >= 851 and itemNo <= 856:
            return True
        elif itemNo == 1691: #kleavor item
            return True
        elif itemNo == 1692: #ursaluna item
            return True
        elif itemNo >= 1780 and itemNo <= 1843: #blank plate, strange ball, legend plate and scarvi key items, stuff to be sold
            return True
        elif itemNo >= 1862: #tera shards, picnic items and other bullshit
            return True
        else:
            return False