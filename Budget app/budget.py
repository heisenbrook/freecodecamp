def create_spend_chart(cat_list):
    chart = list()
    chart.insert(0, 'Percentage spent by category')
    i = int()
    percentage = 100
    for i in range(1,23):
        if i % 2 == 0:
            chart.insert(i, f"{str(percentage):>4}" + '|') 
            percentage -= 10
        else:
            chart.insert(i,' ')
    print(*chart, sep='\n')





        

    return None



class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.balance = 0.0
        pass

    def __str__(self):
        title = self.category.center(30,'*')
        ledger = str()
        for line in self.ledger:
            ledger += (f"{line['description'][0:23]:23}"+f"{line['amount']:>7.2f}") +'\n'
        total = 'Total:' + str(self.balance)   
        return title + '\n' + ledger + total
   
    def deposit(self, amount, description =' '):
        self.balance += amount
        status = self.check_funds(amount)
        if status == True:
            self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description =' '):
        self.balance -= amount
        status = self.check_funds(amount)
        if status == True:    
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category_new):
        if self.balance > 0:
            self.withdraw(amount, 'Transfer to ' + category_new.category)
            category_new.deposit(amount, 'Transfer from ' + self.category)
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
        





        
