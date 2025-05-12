import json 
import os

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

    #os.chdir("/Users/jiajunhuang/capstone_test/scarlet_&_violet_database") # This needs to change
    first_letter = search_name[0]
    image_list = [] #What we will be returning/outputting
    pokemon_list = [] #What pokemon cards will be added to the final image_list

    space_check = False
    apostrophe_check = False

    pokemon_name = search_name.strip().lower().capitalize()

    #Formatting the input and to make 2nd word capitalize if user didn't 
    if " " in pokemon_name:
        space_check = True
        space_index = pokemon_name.find(" ")
        if 0 <= space_index < len(pokemon_name):
            pokemon_name = pokemon_name[:space_index+1] + pokemon_name[space_index+1].upper() + pokemon_name[space_index+2:]

    with open("151.json", encoding="utf-8") as file:
        page_data = json.load(file)

    for card in page_data:
        if card[0:len(pokemon_name)] == pokemon_name:
            pokemon_list.append(card)

    if not pokemon_list:
        if space_check:
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

    with open("obsidian_flames.json", encoding="utf-8") as file:
        page_data = json.load(file)

    for card in page_data:
        if card[0:len(pokemon_name)] == pokemon_name:
            pokemon_list.append(card)

    if not pokemon_list:
        if space_check:
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