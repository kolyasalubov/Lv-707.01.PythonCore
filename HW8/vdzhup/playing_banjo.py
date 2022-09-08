def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("bravo"))
