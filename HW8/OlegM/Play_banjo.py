def are_you_playing_banjo(name: str) -> str:
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"


print(are_you_playing_banjo('_Rikko'))