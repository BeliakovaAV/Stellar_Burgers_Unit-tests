def get_ingredients_by_type(ingredients_list, ingredient_type):
    return [ing for ing in ingredients_list if ing.type == ingredient_type]