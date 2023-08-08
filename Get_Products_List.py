from Groceries import Groceries

class Get_Products_List(Groceries):
    def __init__(self, *args):
        self.args = args

    def get_list(self):
        for i in range(len(self.args)):
            print(f'{i+1}.{self.args[i-1]}')

