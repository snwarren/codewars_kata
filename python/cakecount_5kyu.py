def cakes(recipe, available):
    num_cakes = {}
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        else:
            num_cakes[ingredient] = int(available[ingredient] / recipe[ingredient])
    return min(num_cakes.values())
