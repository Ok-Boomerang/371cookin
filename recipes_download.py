import requests
from bs4 import BeautifulSoup

CUISINES = ['African', 'American', 'Asian', 'British', 'Cajun/Creole', 'Californian', 'Caribbean',
            'Central/S. American', 'Chinese', 'Cuban', 'Eastern European', 'English', 'European', 'French', 'German',
            'Greek', 'Indian', 'Irish', 'Italian', 'Italian American', 'Japanese', 'Jewish', 'Korean', 'Latin American',
            'Mediterranean', 'Mexican', 'Middle Eastern', 'Moroccan', 'Nuevo Latino', 'Scandinavian', 'South American',
            'South Asian', 'Southeast Asian', 'Southern', 'Southwestern', 'Spanish/Portuguese', 'Tex-Mex', 'Thai',
            'Turkish', 'Vietnamese', 'Vegan', 'Vegetarian', 'Organic', 'Kosher', 'Canada']

MEALS = ['Breakfast', 'Brunch', 'Dinner', 'Lunch']

DISH = ['Side', 'Appetizer', 'Dessert', 'Buffet', 'Salad', "Hors D'oeuvre"]

DIETARY = ['Healthy', 'High Fiber', 'Kid-Friendly', 'Low Cholesterol', 'Low Fat', 'Low Sodium',
           'Low/No Sugar', 'Wheat/Gluten-Free', 'Dairy Free', 'Peanut Free',
           'Soy Free', 'Tree Nut Free', 'Paleo', 'Pescatarian', 'High Protein']

STYLE = ['Bake', 'Barbecue', 'Boil', 'Braise', 'Brine', 'Broil', 'Chill', 'Deep Fry', 'Freeze', 'Fry', 'Marinate',
         'No-Cook', 'Pan-Fry', 'Poach', 'Roast', 'Sauté', 'Simmer', 'Steam', 'Stew', 'Stir-Fry', 'Grill', 'Backyard BBQ']

SKILL = ['Quick & Easy', "Advance Prep Req'd", 'Gourmet']

TYPES = ['Bread', 'Brownie', 'Casserole/Gratin', 'Dip', 'Flat Bread', 'Frozen Dessert', 'Pastry', 'Sandwich',
         'Soup/Stew', 'Pasta']

INGREDIENTS = ['Absinthe', 'AleBeer', 'AlfredoSauce', 'ArtificialFoodColoring', 'Asparagus-Foodstuff', 'Bacon', 'Bagel',
               'BakingChocolate-Unsweetened', 'BakingPowder', 'BalsamicVinegar', 'BarbecueSauce', 'Barley-TheGrain',
               'Beef', 'Beer', 'Beet-Foodstuff', 'BellPepper', 'Biscuit', 'BlueCheese', 'BoiledEgg',
               'Bologna', 'Brandy-Liquor', 'Bread', 'Broccoli-Foodstuff', 'BrownRice-Foodstuff', 'BrownSugar', 'BrusselsSprout',
               'BuffaloWing', 'Butter', 'Buttermilk', 'Cabbage-Foodstuff', 'CakeMix', 'CannelloniNoodle', 'Caper-TheCondiment',
               'Carrot-Foodstuff', 'Caviar', 'Chicken-Meat', 'ChilePepper', 'Chocolate', 'Cinnamon-Spice', 'Clove-Spice',
               'CocktailSauce', 'Cocoa-ThePowder', 'CoconutMeat', 'CoconutMilk', 'CoconutOil', 'Coffee-Beverage', 'Cognac-Liquor',
               'CornMeal', 'CornSyrup', 'CottageCheese', 'CowsMilk-Product', 'Cracker-FoodItem', 'Cream-Dairy', 'CreamOfRice',
               'CreamOfWheat', 'Cucumber-Foodstuff', 'DijonMustard', 'DistilledWater', 'DriedFish', 'Duck-Meat', 'Egg-Chickens',
               'EggWhites-Food', 'EggYolk-Food', 'EnglishMuffin', 'Fennel', 'FettuciniNoodle', 'Frosting', 'Garlic', 'GoatCheese',
               'Goose-Meat', 'Granola', 'GroundBeef', 'GroundTurkey', 'HalfAndHalf', 'Guacamole', 'Honey', 'HoneyMustard',
               'Horseradish-Condiment', 'HotSauce', 'IceCream', 'IrishWhiskey', 'JalapenoPepper', 'Jam-Foodstuff', 'Jelly-Foodstuff',
               'Ketchup', 'Lamb-Meat', 'LasagnaNoodle', 'LemonJuice', 'Lettuce-Foodstuff', 'LimeJuice', 'MacaroniNoodle',
               'MapleSyrup', 'Margarine', 'MarinaraSauce', 'Marshmallow', 'MascarponeCheese', 'Matzo', 'Mayonnaise', 'Molasses',
               'Muesli', 'Mushroom-Broadly', 'Mutton', 'Nutmeg', 'Oat-TheGrain', 'Oatmeal', 'Olive-Foodstuff', 'OliveOil',
               'Onion-Foodstuff', 'OrangeJuice', 'PalmOil', 'Pea-Foodstuff', 'PeanutButter', 'PeanutOil', 'Pepper-TheSpice',
               'Pepperoni', 'PestoSauce', 'Pickle', 'PieCrust', 'Pistachio-TheNut', 'PitaBread', 'PizzaCrust', 'Pork',
               'Potato-Foodstuff', 'PrimeRib-MeatCut', 'Prune', 'Pumpkin-Foodstuff', 'Radish-Foodstuff', 'Raisin', 'RamenNoodle',
               'Ravioli', 'RedWineVinegar', 'Rice-Foodstuff', 'RiceFlour', 'RiceNoodle', 'RoastBeef-LunchMeat', 'Rum',
               'Rye-TheGrain', 'Saffron', 'Salami', 'Salsa-TheCondiment', 'Sausage', 'ScotchWhisky', 'SesameOil', 'SesameSeed',
               'Soybean-Foodstuff', 'SoyMilk', 'SpaghettiNoodle', 'SpicyBrownMustard', 'Spinach-Foodstuff', 'Steak-Beef-MeatCut',
               'SteakSauce', 'SweetPotato-Foodstuff', 'TabascoSauce', 'TartarSauce', 'Tequila', 'Tomato-Foodstuff',
               'Turkey-Meat', 'VanillaExtract', 'Veal', 'VegetableOil', 'Venison', 'VermicelliNoodle', 'Vermouth',
               'Vinegar', 'Vodka', 'WheatFlour', 'WheatGerm', 'Whey', 'WhippedCream', 'Whisky', 'WhiteRice-Foodstuff',
               'WhiteWineVinegar', 'WholeMilk', 'Wine', 'WineVinegar', 'Yam-Foodstuff', 'Yeast', 'YellowMustard', 'Yogurt',
                'Zucchini-Foodstuff']

EVENT = ['Anniversary', 'Bastille Day', 'Birthday', 'Christmas', 'Christmas Eve', 'Cinco de Mayo', 'Cocktail Party', 'Easter',
         'Engagement Party', 'Fall', 'Family Reunion', "Father's Day", 'Fourth of July', 'Graduation', 'Halloween',
         'Hanukkah', 'Kentucky Derby', 'Mardi Gras', "Mother's Day", "New Year's Day", "New Year's Eve", "Oscars", 'Party',
         'Passover', 'Picnic', 'Poker/Game Night', 'Potluck', 'Ramadan', 'Rosh Hashanah', 'Shower', 'Spring',
         "St. Patrick's Day", 'Summer', 'Superbowl', 'Tailgating', 'Thnaksgiving', "Valentine's Day", 'Wedding', 'Winter']


class Recipe:
    def __init__(self, name, url, rating, ingredients, cuisine, meal, course, cooktime, calories, methods, restriction,
                 type, skill):
        self.name = name
        self.url = url
        self.rating = rating
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.meal = meal
        self.course = course
        self.cooktime = cooktime
        self.calories = calories
        self.methods = methods
        self.restriction = restriction
        self.type = type
        self.skill = skill


def parse_recipe(url, soup, id, f):
    name = parse_name(soup)
    rating = parse_rating(soup)
    ingredients = parse_ingredients(soup)
    cuisine, meal, dietary, style, skill, course, type = parse_tags(soup)
    cooktime = parse_time(soup)
    calories = parse_calories(soup)
    insert_kb(Recipe(name, url, rating, ingredients, cuisine, meal, course, cooktime, calories, style, dietary, type, skill), id, f)


def parse_name(soup):
    name = soup.find("h1", {"itemprop": "name"}).text
    name = name.replace(" ", "")
    name = name.replace(",","")
    name = name.replace("-","")
    if '(' in name:
        ind = name.index('(')
        name = name[:ind]
    return remove_accents(name)


def parse_rating(soup):
    rating = soup.find("span", {"class": "rating"}).text
    return rating[0]


def parse_ingredients(soup):
    ingredients = [ingredient.text for ingredient in soup.find_all('li', {'class': 'ingredient'})]
    measurements = ['bunch', 'can', 'clove', 'cup', 'ounce', 'package', 'pinch', 'pint', 'pound', 'teaspoon',
                    'tablespoon', 'container', 'dash', 'quart', 'pod', 'bunch', 'clove', 'gram', 'lb', 'oz',
                    'Tbsp', 'Tbs', 'tsp', 'Tsp', '½', '⅓', '¼']
    descriptions = ['finely', 'fine', 'chopped', 'large', 'medium', 'head', 'of', 'double-concentrated', 'grated',
                    'soft', 'small', 'sprigs', 'ripe', 'leaves', 'fresh']
    delete = ['Equipment', ':', ';']
    ret = []
    for ing in ingredients:
        if all([dele not in ing for dele in delete]):
            if '(' in ing:
                first = ing.index('(')
                second = ing.index(')')
                ing = ing.replace(ing[first:second + 1], "")
            if '(' in ing:
                first = ing.index('(')
                second = ing.index(')')
                ing = ing.replace(ing[first:second + 1], "")
            if ',' in ing:
                ind = ing.index(',')
                ing = ing[:ind]
            ing = ing.replace('-', " ")
            arr = ing.split()
            if "or" in arr:
                ind = arr.index("or")
                arr = arr[:ind]
            for meas in measurements:
                if meas in ing:
                    for i, word in enumerate(arr):
                        if meas in word:
                            arr = arr[i + 1:]
            for word in arr:
                for x in word:
                    if x.isdigit():
                        arr.remove(word)
                        break
                if word == "g" or word == "g.":
                    arr.remove(word)
            for desc in descriptions:
                if desc in arr:
                    arr.remove(desc)
            for i, word in enumerate(arr):
                arr[i] = word[0].upper() + word[1:]
            if arr:
                ingredient = remove_accents("".join(arr))
                ret.append(ingredient)

    return ret


def parse_tags(soup):
    cuisine = []
    meal = []
    dish = []
    dietary = []
    styles = []
    skill = None
    types = []
    events = []
    tags = [tag.text for tag in soup.find_all('dt', {'itemprop': 'recipeCategory'})] + \
           [tag.text for tag in soup.find_all('dt', {'itemprop':'recipeCuisine'})]
    for tag in tags:
        for cuis in CUISINES:
            if tag == cuis:
                cu = cuis
                if cuis == "Cajun/Creole":
                    cu = "Cajun"
                elif cuis == "Eastern European":
                    cu = "EasternEuropeanFood"
                elif cuis == "Southeast Asian":
                    cu = "SouthEastAsian"
                elif cuis == "Southern":
                    cu = "SouthernStyle"
                elif cuis == "Kosher":
                    cu = "KosherFood"
                elif cuis == "Canada":
                    cu = "Canadian"
                cu = cu.replace("-", "")
                cu = cu.replace(" ", "")
                cu = cu.replace("/", "")
                cu = cu.replace(".", "")
                cuisine.append(cu)
        for m in MEALS:
            if tag == m:
                if m == "Dinner":
                    m = "Supper"
                meal.append(m)
        for d in DISH:
            if tag == d:
                dis = d
                if d == "Hors D'oeuvre":
                    dis = "HorsDoeuvre"
                dish.append(dis)
        for diet in DIETARY:
            if tag == diet:
                di = diet
                if diet == "Low/No Sugar":
                    di = "LowSugar"
                elif diet == "Wheat/Gluten-Free":
                    di = "GlutenFree"
                di = di.replace("-", "")
                di = di.replace("/", "")
                di = di.replace(" ", "")
                dietary.append(di)
        for style in STYLE:
            if tag == style:
                s = style
                if style == "Bake":
                    s = "Baked"
                elif style == "Barbecue" or style == "Backyard BBQ":
                    s == "Barbecued"
                elif style == "Boil":
                    s = "Boiled"
                elif style == "Braise":
                    s = "Braised"
                elif style == "Brine":
                    s = "Brined"
                elif style == "Broil":
                    s = "Broiled"
                elif style == "Chill":
                    s = "Chilled"
                elif style == "Deep Fry":
                    s = "DeepFried"
                elif style == "Freeze":
                    s = "Frozen"
                elif style == "Fry":
                    s = "Fried"
                elif style == "Marinate":
                    s = "Marinated"
                elif style == "No-Cook":
                    s = "AssembledFood"
                elif style == "Pan-Fry":
                    s = "PanFried"
                elif style == "Poach":
                    s = "Poached"
                elif style == "Roast":
                    s = "Roasted"
                elif style == 'Sauté':
                    s = "Sauteed"
                elif style == "Simmer":
                    s = "Simmered"
                elif style == "Steam":
                    s = "Steamed"
                elif style == "Stew":
                    s = "Stewed"
                elif style == 'Stir-Fry':
                    s = 'StirFried'
                elif style == 'Grill':
                    s = 'Grilled'
                styles.append(s)
        for sk in SKILL:
            if tag == sk:
                skill = sk
        for type in TYPES:
            if tag == type:
                t = type
                if type == 'Casserole/Gratin':
                    t = "Casserole"
                elif type == 'Soup/Stew':
                    t = "Soup"
                elif type == "Pastry":
                    t = "Pastry-Stuff"
                elif type == "Pasta":
                    t = "PastaDish"
                t = t.replace(" ", "")
                types.append(t)

    return cuisine, meal, dietary, styles, skill, dish, types


def parse_time(soup):
    directions = [direction.text.strip() for direction in soup.find_all('li', {'class': 'preparation-step'})]
    TIMES = ['minute', 'hour']
    time = 0
    for t in TIMES:
        for direction in directions:
            if t in direction:
                direc = direction.split()
                for ind, word in enumerate(direc):
                    if t in word:
                        num = direc[ind - 1]
                        if num.isdigit():
                            if t == 'minute':
                                time += int(num)
                            elif t == 'hour':
                                time += 60 * int(num)
    return time


def parse_calories(soup):
    calories = soup.find("span", {"itemprop": "calories"}).text
    return int(calories)


def insert_kb(recipe, id, f):
    f.write('(isa Recipe-CW %s)' % id)
    f.write('\n')
    f.write('(recipeName %s %s)' % (recipe.name, id))
    f.write('\n')
    f.write('(recipeURL %s %s)' % (recipe.url, id))
    f.write('\n')
    f.write('(recipeRating %s %s)' % (recipe.rating, id))
    f.write('\n')
    for cuis in recipe.cuisine:
        if cuis == "Irish" or cuis == "LatinAmerican":
            f.write('(recipeCuisine %sFood %s)' % (cuis, id))
            f.write('\n')
        else:
            f.write('(recipeCuisine %sCuisine %s)' % (cuis, id))
            f.write('\n')
    for meal in recipe.meal:
        f.write('(recipeMealType %s %s)' % (meal, id))
        f.write('\n')
    for course in recipe.course:
        f.write('(recipeCourse %s %s)' % (course, id))
        f.write('\n')
    for diet in recipe.restriction:
        f.write('(recipeDiet %sDiet %s)' % (diet, id))
        f.write('\n')
    for type in recipe.type:
        f.write('(recipeDishType %s %s)' % (type, id))
        f.write('\n')
    for style in recipe.methods:
        f.write('(cookMethodOf %s %s)' % (style, id))
        f.write('\n')
    cal = recipe.calories
    if cal < 200:
        f.write('(recipeCalories low %s)' % id)
        f.write('\n')
    elif 200 < cal < 400:
        f.write('(recipeCalories moderate %s)' % id)
        f.write('\n')
    elif cal > 400:
        f.write('(recipeCalories high %s)' % id)
        f.write('\n')
    skill = recipe.skill
    if skill == "Quick & Easy":
        f.write('(skillLevelOf beginner %s)' % id)
        f.write('\n')
    elif skill == "Advanced Prep Req'd" or skill == "Gourmet":
        f.write('(skillLevelOf advanced %s)' % id)
        f.write('\n')
    cooktime = recipe.cooktime
    if cooktime < 30:
        f.write('(recipeCookTime short %s)' % id)
        f.write('\n')
    elif 30 < cooktime < 60:
        f.write('(recipeCookTime medium %s)' % id)
        f.write('\n')
    elif cooktime > 60:
        f.write('(recipeCookTime long %s)' % id)
        f.write('\n')
    for ingredient in recipe.ingredients:
        broken = False
        for ing in INGREDIENTS:
            ing_comp = ing
            if "-" in ing:
                ind = ing.index("-")
                ing_comp = ing[:ind]
            if ing_comp in ingredient:
                f.write('(ingredientOf %s %s)' % (ing, id))
                f.write('\n')
                broken = True
                break
        if not broken:
            f.write('(isa %s DefaultDisjointEdibleStuffType)' % ingredient)
            f.write('\n')
            f.write('(ingredientOf %s %s)' % (ingredient, id))
            f.write('\n')
            INGREDIENTS.append(ingredient)


def remove_accents(obj):
    accents = {"ç": "c",
               "è": "e",
               "î": "i",
               "ñ": "n"}
    for accent in accents.keys():
        obj = obj.replace(accent, accents[accent])
    return obj


if __name__ == "__main__":
    with open('recipe_urls.txt', 'r') as f:
        recipe_list = f.read().splitlines()
    for recipe in recipe_list:
        if recipe_list.count(recipe) > 1:
            recipe_list.remove(recipe)
    count = 1
    with open('recipes.krf', 'w') as f:
        f.write('(in-microtheory CookingMastersMt)')
        f.write('\n')
        for url in recipe_list:
            website_url = requests.get(url).text
            soup = BeautifulSoup(website_url, 'lxml')
            url = '"' + url + '"'
            parse_recipe(url, soup, "recipe%d" % count, f)
            count += 1

