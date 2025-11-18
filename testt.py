# import re

# #Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")
# ------------------------------------

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)

# ---------------------------------



# txt = "That will be 59 dollars  and 678 pownds"

# #Find all digit characters:

# x = re.findall("\d", txt)
# print(x)

# ---------------------------


# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("pl..et", txt)
# print(x)


# ----------------------------

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

# x = re.findall("he.*o", txt)

# print(x)
# ---------------------------------------



# txt = "heo planet"

# #Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

# x = re.findall("he.?o", txt)

# print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

# ---------------------------------



# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

# x = re.findall("he.+o", txt)

# print(x)

# # ----------------------


# txt = "helllo planet"

# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{3}o", txt)

# print(x)


import cowsay

cowsay.cow("hello sinaaaaaaaaaaa you are cows like me")




