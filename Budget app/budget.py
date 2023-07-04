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
            ledger.append(f"{line['amount']:< 23}{line['description']:> 7}")
        total = 'Total:' + str(round(self.balance,2))    
        return title,'\n',ledger,'\n',total

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
   
    def deposit(self, amount, description =' '):
        status = self.check_funds(amount)
        if status == True:
            self.balance += amount
            self.ledger['amount'].append(round(float(amount),2))
            self.ledger['description'].append(description)


    def withdraw(self, amount, description =' '):
        status = self.check_funds(amount)
        if status == True:    
            self.balance -= amount
            self.ledger['amount'].append(round(float(-amount),2))
            self.ledger['description'].append(description)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category_new):
        self.balance -= amount
        if self.balance > 0:
            self.ledger['amount'].append(round(float(amount),2))
            self.ledger['description'].append('Transfer to' + category_new.balance)
            self.ledger['amount'].append(round(float(-amount),2))
            self.ledger['description'].append('Transfer from' + self.balance)
            return True
        else:
            return False
        





        
