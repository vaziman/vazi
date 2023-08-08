class Main:
    pass




#-----------------------------------------------------------------------------------------------
class Groceries(Main):  # список продуктов

    choco = 'choco'
    snickers = 'snickers'
    gros_list = [choco, snickers]

#-----------------------------------------------------------------------------------------------
class Get_Products_List(Groceries):  # Вывод списка продуктов

    def get_list(self):
        for i in range(len(self.gros_list)):
            print(f'{i+1}.{self.gros_list[i]}')

#-----------------------------------------------------------------------------------------------
class Choose_product(Groceries):  # Ф-ция выбора продукта из списка
    chosen_product = ''
    def choose_your_product(self):
        print(f'Choose product: ')
        product = int(input())
        for i in range(len(self.gros_list)):
            if product == i+1:
                self.chosen_product = str(self.gros_list[i])
                print(self.chosen_product)
        return self.chosen_product

#-----------------------------------------------------------------------------------------------


class ChoseAmount():  # Ф-ция добавления кол-ва продуктов
    print(f'Choose amount:')
    amount = int(input())
    def chose_amount(self):
        return self.amount


#-----------------------------------------------------------------------------------------------
class GroceryCost(Groceries):
   def gross_cost(self):
       cost_of_snickers = 15
       cost_of_choco = 21



#----------------------------------------------------------------------------------------------
class Basket(Groceries,ChoseAmount, Choose_product):
    def __init__(self):
        self.basket = []
        self.basket_count = []
        self.basket_cost = []

    def add_groceries_to_basket(self):
        self.basket.append(self.chosen_product)

    def add_count_to_basket(self):
        self.basket_count.append(self.amount) #count

    def add_cost_to_basket(self):
        self.basket_cost.append('1') #cost
#---------------------------------------------------------------------------------------------------


class PrintBasket(Basket, GroceryCost):
    def print(self):
        for i in range(len(self.chosen_product)):
            print(f'{i}.{self.basket[i]} x {self.cost} = {self.basket_count * self.basket_cost}')


a = Get_Products_List()
a.get_list()
while True:
    a1 = Choose_product()
    a1.choose_your_product()
    a2 = ChoseAmount()
    a2.chose_amount()