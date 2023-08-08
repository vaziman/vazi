from Main import Main



class Groceries(Main):
    def __init__(self, *args):
        self.args = list(args)
        # self.banana = 'banana'
        # self.snickers = 'snickers'
        # self.groceries_list = [self.banana, self.snickers]


    def return_value(self):
        return self.args

