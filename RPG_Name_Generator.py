import random

def name_chosing(constant,vovel,length):
    first = []
    length = int(int(length)/2)
    for i in range(length):
        first.append((random.choice(vovel))) or first.append((random.choice(constant)))
    return first

def alias_choising():
    list_of_alias = ["The Great", "Traitor", "The Little", "The Young", "The Old" , "Nobleman", "The Scientist"]
    name = random.choice(list_of_alias)
    return name

def main():
    length = int(input("Input length of the name: "))
    constant = list("aeyiou")
    vovel = list("bcdfghjklmnprstwzx")
    name = name_chosing(constant, vovel, length)
    name = "".join(name)
    name = name.title()
    alias = alias_choising()
    name += " "
    name += alias
    print(name)

main()