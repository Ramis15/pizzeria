def proverka(object):
    if (isinstance(object, int) or isinstance(object, float)) and object < 0:
        raise ValueError(f'Значение {object} не может быть только отрицательным')
    elif object == '':
        raise ValueError(f'Значение {object} не может быть пустым')
    else:
        return object

class Product:
    def __init__(self, title, calorific, cost):
        self.title = proverka(title)
        self.calorific = proverka(calorific)
        self.cost = proverka(cost)

class Ingredient:
    def __init__(self, product, weight):
        self.product = proverka(product)
        self.weight = weight

    def get_calorific(self, product):
        return self.weight/100 * product.calorific

    def get_cost(self, product):
        return self.weight/100 * product.cost

class Pizza:
    def __init__(self, title, ingredients):
        self.title = proverka(title)
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.title} ({self.get_calorific()} kkal) - {self.get_cost()} руб'

    def get_calorific(self):
        summ = 0
        for ingredient in self.ingredients:
            summ += ingredient.get_calorific(ingredient.product)
        return summ

    def get_cost(self):
        summ = 0
        for ingredient in self.ingredients:
            summ += ingredient.get_cost(ingredient.product)
        return summ
