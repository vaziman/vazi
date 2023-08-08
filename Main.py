from Basket.Models.Chocolate import Chocolate
from Basket.Models.Grocery import Grocery
from Basket.Models.Snickers import Snickers


list_of_products = [Snickers(), Chocolate()]
list_of_chosen_products = []


for i in range(len(list_of_products)):
    print(f'{i + 1}.{list_of_products[i].name}')

value = int(input())

selected_product = list_of_products[value - 1]
list_of_chosen_products.append(selected_product.ask())
list_of_chosen_products.append(Chocolate())
print(selected_product.name)
print(list_of_chosen_products)
total = 0
for product in list_of_chosen_products:
    summa = product.get_price()
    total += summa
print(total)


