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
#paleo, nut free
STYLE = ['Pressure Cooker', 'Slow Cooker']

SKILL

DISH = ['Main Dishes', 'Soups, Stew, and Chili Recipes', 'Appetizers & Snacks', 'Desserts']


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
    cuisine = parse_cuisine(soup)
    meal = parse_meal(soup)
    course = parse_course(soup)
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
    breadcrumbs = soup.find('ol', {'class': 'breadcrumbs'})
    if breadcrumbs:
        for crumb in breadcrumbs.findAll('li'):
            poss_cuisine = crumb.find('span').text
            for cuis in CUISINES:
                if all([char in poss_cuisine for char in cuis]):
                    cuisine = cuis
    return cuisine


def parse_meal(soup):
    pass


def parse_course(soup):
    pass


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
