import json 
import os

def data_process(page_data, pokemon_name, space_check):
    pokemon_list = []
    image_list = []
    apostrophe_check = False

    for card in page_data:
        if card[0:len(pokemon_name)] == pokemon_name:
            pokemon_list.append(card)

    if not pokemon_list and space_check:
        space_index = pokemon_name.find(" ")
        if pokemon_name[space_index-1] == "s":
            apostrophe_check = True
            pokemon_name = pokemon_name[:space_index-1] + "'s " + pokemon_name[space_index+1:]

        if apostrophe_check:
            for card in page_data:
                if card[0:len(pokemon_name)] == pokemon_name:
                    pokemon_list.append(card)

    for pokemon in pokemon_list:
        for card in page_data[pokemon]:
            image_list.append(card["images"])

    return image_list

def return151images_given_name(search_name):

    """ 
    This functions reads in a string input parameter and outputs a list of images. 
    It modifies the format of the input parameter to conform it to the pokemon cards, 
    capitalized, lowercase trailing letters and exclamation mark if it's a trainer card
    that has one. 

    Args: 
        arg1: search_name 

    Returns: 
        A list of images pertaining to the input parameter 
    """

    first_letter = search_name[0]
    image_list = []

    space_check = False
    pokemon_name = search_name.strip().lower().capitalize()

    if " " in pokemon_name:
        space_check = True
        space_index = pokemon_name.find(" ")
        if 0 <= space_index < len(pokemon_name):
            pokemon_name = pokemon_name[:space_index+1] + pokemon_name[space_index+1].upper() + pokemon_name[space_index+2:]

    with open("151.json", encoding="utf-8") as file:
        page_data = json.load(file)

    image_list += data_process(page_data, pokemon_name, space_check)

    with open("twilight_masquerade.json", encoding="utf-8") as file:
        page_data = json.load(file)

    image_list += data_process(page_data, pokemon_name, space_check)

    return image_list