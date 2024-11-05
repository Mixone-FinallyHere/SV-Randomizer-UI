import secrets

def shuffle_array(arr):
    shuffled_arr = []
    while arr:
        element = secrets.choice(arr)
        arr.remove(element)
        shuffled_arr.append(element)
    return shuffled_arr