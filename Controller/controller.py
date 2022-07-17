from Model.acronym import *

# test without ui
userinput = input("type your word here: ")

abb = Acronym(userinput)

print(abb.createAcronym())
