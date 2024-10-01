from random import random
import math
import copy
UINT_MAX = 4294967295
DEADBEEF = 3735928579

def scramble_seed()->None:
    """replicates the function 'scrambleSeed' from scummvm/common/random.cpp"""
    global SEED
    SEED ^= SEED >> 13
    SEED ^= SEED << 21
    SEED ^= SEED >> 11


def get_random_number(max:int)->int:
    """replicates the function 'scrambleSeed' from scummvm/common/random.cpp"""
    scramble_seed()
    if (max == UINT_MAX):
        return SEED*DEADBEEF
    return (SEED*DEADBEEF)%(max+1)

def get_random_number_RNG(min: int, max:int):
    return get_random_number(max - min) + min

def random_query(min: int, max:int):
    if(min==max):
        return min
    if(min>max):
        return get_random_number_RNG(max, min)
    return get_random_number_RNG(min,max)

SEED = math.floor(random()*100000000)
SEED = 2489215585
# SEED = 2492033534
# SEED = 2493309379
# SEED = 2497825187
original_seed = copy.copy(SEED)
print(random_query(1,2))
# my own helper 
def get_replic():
    val = random_query(1,2)
    if (val==1):
        return "Replicant"
    return "Human"

def game_sample():
    ## Izo, Gordo, Lucy, Dektora, Sadik, Luther
    var_izo = get_replic()
    var_gor = get_replic()
    var_luc = get_replic()
    var_dek = get_replic()
    var_sad = get_replic()
    var_lut = get_replic()
    ## Reroll Dekotora
    if var_gor == "Human" and var_luc == "Human" and var_dek == "Human":
        var_dek = "Replicant"

    print_string = "---\n"
    print_string += "Note: I have no fekkin clue about the mode\n"
    print_string += "---\n"
    print_string += f"Izo is a {var_izo} \n"
    print_string += f"Gordo is a {var_gor} \n"
    print_string += f"Lucy is a {var_luc} \n"
    print_string += f"Dektora is a {var_dek} \n"
    print_string += f"Sadik is a {var_sad} \n"
    print_string += f"Luther/Lance is a {var_lut} \n"
    print_string += "---\n"
    print_string += f"Random seed is {original_seed}\n"
    print_string += "---\n"

    print(print_string)

SEED = 2489215585
rep_vector = ["Human", "Replicant", "Human" ,"Replicant", "Human", "Human"]
replic_list = []

for _ in range(100):
    replic_list.append(get_replic())

print(replic_list)
for index in range(100):
    if rep_vector == replic_list[index:(index+len(rep_vector))]:
        print(index)
# 21
# print(replic_list[21:(21+len(rep_vector))])
SEED = 2492033534
rep_vector = ["Replicant", "Replicant", "Human" ,"Replicant", "Replicant", "Human"]
replic_list = []

for _ in range(100):
    replic_list.append(get_replic())

print(replic_list)
for index in range(100):
    if rep_vector == replic_list[index:(index+len(rep_vector))]:
        print(index)