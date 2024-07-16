from pprint import pprint
import operator
import os


file_name = "recipes.txt"

def get_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for product in file:
            meal = product.strip()
            cook_book[meal] = []
            ingredients_quantity = int(file.readline().strip())
            for item in range(ingredients_quantity):
                ingredient_dict = {}
                ingredient = file.readline().strip().split(' | ')
                ingredient_dict['ingredient_name'] = ingredient[0]
                ingredient_dict['quantity'] = int(ingredient[1])
                ingredient_dict['measure'] = ingredient[2]
                cook_book[meal].append(ingredient_dict)
            file.readline()
    return cook_book

new_file = get_cook_book(file_name)
pprint(new_file)


def get_shop_list_by_dishes(dishes, number_of_persons):
    ingeridients = {}
    for dish in dishes:
        if dish in new_file.keys():
            for ingredient in new_file[dish]:
                if ingredient['ingredient_name'] not in ingeridients:
                    ingeridients[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': (number_of_persons*ingredient['quantity']) }
                else:
                    ingeridients[ingredient['ingredient_name']]['quantity'] += number_of_persons*ingredient['quantity']
    return ingeridients

ingredients_and_quantity_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(ingredients_and_quantity_dict)
