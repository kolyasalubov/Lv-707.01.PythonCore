def get_tomato_marinade(user_value):
    ingredients_tomato = {"вода": 1.5, "цукор": 6, "оцет": 85, "сіль": 1.5}
    new_ingredients_tomato = []
    units_of_measure =  [" л.", " ст.л.", " мл.", " ст.л."]

    for key, value in ingredients_tomato.items():
        ingredients_tomato[key] = round((value * user_value) / 1.5, 1)

    for key, value in ingredients_tomato.items():
        new_ingredients_tomato.append(f"{key} - {value}")
    
    for item in range(len(new_ingredients_tomato)):
        new_ingredients_tomato[item] += units_of_measure[item]
        
    result = "; ".join(new_ingredients_tomato)
    
    return result

def get_cucumber_marinade(user_value):
    ingredients_cucmber = {"вода": 1, "цукор": 100, "оцет": 120, "сіль": 1}
    new_ingredients_cucumber = []
    units_of_measure =  [" л.", " г.", " мл.", " ст.л."]

    for key, value in ingredients_cucmber.items():
        ingredients_cucmber[key] = round(value * user_value, 2)

    for key, value in ingredients_cucmber.items():
        new_ingredients_cucumber.append(f"{key} - {value}")
    
    for item in range(len(new_ingredients_cucumber)):
        new_ingredients_cucumber[item] += units_of_measure[item]
        
    result = "; ".join(new_ingredients_cucumber)

    return result
