class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.balance = 0.0
        pass

    def __repr__(self):
        title = self.category.center(30,'*')
        ledger = list()
        for line in self.ledger:
            
        pass

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
   
    def deposit(self, amount, description =' '):
        status = self.check_funds(amount)
        if status == True:
            self.balance += amount
            self.ledger.append({'amount': float(amount), 'description': description})

    def withdraw(self, amount, description =' '):
        status = self.check_funds(amount)
        if status == True:    
            self.balance -= amount
            self.ledger.append({'amount': float(-amount), 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, balance_new, category_new):
        self.balance -= amount
        if self.balance > 0:
            balance_new += amount
            self.ledger.append({'amount': float(amount), 'description': 'Transfer to' + category_new})
            self.ledger.append({'amount': float(-amount), 'description': 'Transfer from' + category_new})
            return True
        else:
            return False
    
        





        
