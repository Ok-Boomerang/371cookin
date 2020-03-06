import requests
from bs4 import BeautifulSoup

CUISINES = ['Italian', 'Mexican', 'Chinese', 'Indian', 'Thai', 'Japanese', 'Korean', 'Pakistani', 'Bangladeshi',
            'Persian', 'Filipino', 'Indonesian', 'Malaysian', 'Vietnamese', 'Asian', 'Caribbean', 'South American',
            'Latin American', 'Mediterranean', 'Lebanese', 'Turkish', 'Israeli', 'Middle Eastern',
            'North African', 'South African', 'East African', 'African', 'Greek', 'French', 'Spanish', 'German',
            'Portuguese', 'UK and Ireland', 'Czech', 'Hungarian', 'Polish', 'Russian', 'Eastern European', 'Dutch',
            'Belgian', 'Austrian', 'Scandinavian', 'Swiss', 'European', 'Australian and New Zealander', 'Canadian',
            'Amish and Mennonite', 'Jewish', 'Soul Food', 'Southern', 'Tex-Mex', 'Cajun and Creole', 'U.S.']

MEALS = ['Breakfast and Brunch', 'Dinners', 'Lunch']

DIETARY = ['Diabetic', 'Low Carb Recipes', 'Dairy Free Recipes', 'Gluten Free', 'Heart-Healthy Recipes',
           'High Fiber Recipes', 'Low Calorie', 'Low Cholesterol Recipes', 'Low Fat', 'Weight-Loss Recipes',
           'Paleo', 'Vegan', 'Vegetarian']
# nut free
STYLE = ['Pressure Cooker', 'Slow Cooker']

SKILL = ['Gourmet', "Quick & Easy"]

DISH = ['Main Dishes', 'Soups, Stew, and Chili Recipes', 'Appetizers & Snacks', 'Desserts']

TYPES = ['Pizza', 'Sandwiches', 'Pasta Recipes', 'Cookie Recipes', 'Casserole Recipes', 'Cake Recipes', 'Bread Recipes',
         'Pie Recipes']

INGREDIENTS = ['Beef', 'Beans and Legumes', 'Chicken Recipes', 'Chocolate', 'Fruit', 'Game Meats', 'Grains', 'Mushrooms',
               'Pork Recipes', 'Potatoes', 'Poultry', 'Rice', 'Salmon', 'Seafood', 'Shrimp', 'Tofu and Tempeh',
               'Turkey', 'Vegetable Recipes']


class Recipe:
    def __init__(self, name, rating, ingredients, cuisine, meal, course, cooktime, calories, methods, restriction):
        self.name = name
        self.rating = rating
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.meal = meal
        self.course = course
        self.cooktime = cooktime
        self.calories = calories
        self.methods = methods
        self.restriction = restriction


def parse_recipe(soup):
    name = parse_name(soup)
    rating = parse_rating(soup)
    ingredients = parse_ingredients(soup)
    cuisine, meal, dietary, style, skill, dish, type, ingredient = parse_cuisine(soup)
    cooktime = parse_time(soup)
    calories = parse_calories(soup)
    methods = parse_methods(soup)
    restriction = parse_restrictions(soup)
    return Recipe(name, rating, ingredients, cuisine, meal, course, cooktime, calories, methods, restriction)


def parse_name(soup):
    name = soup.find("h1", {"id": "recipe-main-content"}).text
    return name


def parse_rating(soup):
    rating = soup.find("div", {"class":"rating-stars"}).find("data-ratingstars").text
    return rating


def parse_ingredients(soup):
    ingredient_groups = [group.text for group in soup.find_all('span', {'data-id': '0'})]
    ingredients = [ingredient.text for ingredient in soup.find_all('span', {'itemprop': 'recipeIngredient'})
                   if ingredient.text not in ingredient_groups]
    for ingredient in ingredients:
        pass


def parse_cuisine(soup):
    cuisine = None
    meal = None
    dietary = None
    style = None
    skill = None
    dish = None
    type = None
    ingredient = None
    breadcrumbs = soup.find('ol', {'class': 'breadcrumbs'})
    if breadcrumbs:
        for crumb in breadcrumbs.findAll('li'):
            bc = crumb.find('span').text
            for cuis in CUISINES:
                if all([char in bc for char in cuis]):
                    cuisine = cuis
            for m in MEALS:
                if all([char in bc for char in m]):
                    meal = m
            for diet in DIETARY:
                if all([char in bc for char in diet]):
                    dietary = diet
            for s in STYLE:
                if all([char in bc for char in s]):
                    style = s
            for sk in SKILL:
                if all([char in bc for char in sk]):
                    skill = sk
            for d in DISH:
                if all([char in bc for char in d]):
                    dish = d
            for t in TYPES:
                if all([char in bc for char in t]):
                    type = t
            for ing in INGREDIENTS:
                if all([char in bc for char in ing]):
                    ingredient = ing

    return cuisine, meal, dietary, style, skill, dish, type, ingredient


def parse_time(soup):
    time = soup.find("span", {"class": "ready-in-time"}).text
    return time


def parse_calories(soup):
    calories = soup.find("span", {"class": "calorie-count"}).text
    return calories


def parse_methods(soup):
    directions = [direction.text.strip() for direction in
                  soup.find_all('span', {'class': 'recipe-directions__list--item'})
                  if direction.text.strip()]
    for direction in directions:
       pass


def parse_restrictions(soup):
    pass


if __name__ == "__main__":
    with open('recipe_urls.txt', 'r') as f:
        recipe_list = f.readlines()
    for url in recipe_list:
        website_url = requests.get(url).text
        soup = BeautifulSoup(website_url, 'lxml')
        parse_recipe(soup)
