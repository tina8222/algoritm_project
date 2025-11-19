


# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!  

   
def are_you_playing_banjo(name): 
    if name.startswith(('r','R')):
        print(f"{name} plays jango")
    else:
        print(f"{name} does not play bango")
    return name


are_you_playing_banjo("Robert")
are_you_playing_banjo("tina") 
