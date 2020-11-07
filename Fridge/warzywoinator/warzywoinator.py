import json

# f = open("test1.json", "r")
# recipes = f.read()
# recipes = recipes.replace('}', '},')
# g = open("result.json", "w+")
# g.write(recipes)

# h = open("result.json", "r")
# recipes = h.read()

forbidden_words = ['cup', 'ml', 'and', 'or', 'of', 'bunch', 'sliced', 'trimmed', 'fennel', 'very',
                   'brushed', 'ounces', 'dried', 'crushed', 'deeply', 'dicedgreat', 'finely',
                   '&amp;', 'medium', 'dozen', 'fresh', '/', 'fine', 'cloves', 'teaspoon', 'ideas', 'in', 'white',
                   'baby', 'pound', 'large', 'tablespoons', 'toppingrose', 'for', 'more', 'plus']

with open('result.json') as json_file:
    recipes = json.load(json_file)

    for recipe in recipes:
        ingredients_all = recipe['ingredients']
        ingredients_all = ingredients_all.replace('\n', '')
        ingredients_all = ingredients_all.replace(',', '')
        ingredients_all = ingredients_all.split(' ')
        for ing in ingredients_all:
            if any(char.isdigit() for char in ing):
                continue
            if ing in forbidden_words:
                continue
            print(ing)
