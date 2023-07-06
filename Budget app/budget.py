def create_spend_chart(cat_list):
    tot_s = list()
    for cat in cat_list:
        spent = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        tot_s.append(spent)
    
    #getting percentage
    percent_cat = list()
    for cat in tot_s:
        percent_cat.append(round(int((cat*100)//(sum(tot_s))),-1))
    
    #printing chart
    chart = list()
    chart.insert(0,'Percentage spent by category')
    percentage = 100
    for i in range(1,12):
        chart.insert(i, f"{str(percentage):>4}" + '|') 
        for percent in percent_cat:
            if percent >= percentage:
                chart[i] += ' o '
        percentage -= 10
    dashes = '     -'
    footer = list()
    for cat in cat_list:
        dashes += '---'
        foot = str()
        for l in range(len(str(cat.category))):
            foot += ' '+f'{str(cat.category)[l]}'+' '
        footer += '\n'.join(foot) 

    graph = '\n'.join(chart) + '\n' + dashes + '    '.join(footer)  

    return graph



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
        status = self.check_funds(amount)
        if status == True:    
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
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
        if self.balance >= amount:
            return True
        else:
            return False





        
