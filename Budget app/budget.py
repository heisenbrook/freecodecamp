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
        percent_cat.append(round((cat)/(sum(tot_s))*100,2))
    
    
    #printing chart
    chart = list()
    chart.insert(0,'Percentage spent by category')
    percentage = 100
    for i in range(1,12):
        chart.insert(i, f"{str(percentage):>3}" + '|') 
        for percent in percent_cat:
            if percent >= percentage:
                chart[i] += ' o '
            else:
                chart[i] += '   '
        percentage -= 10
    dashes = '    -'
    for cat in cat_list:
        dashes += '---'

    
    max_list = 0
    for cat in cat_list:
        if len(str(cat.category)) > max_list:
            max_list = len(str(cat.category))

    footer = str()
    for i in range(max_list):
        foot ='    '
        for cat in cat_list:
            try: 
                str(cat.category)[i]
                foot += f" {cat.category[i]} "
            except:
                foot += '   '
        footer += f"{foot}\n"

    graph = '\n'.join(chart) + '\n' + dashes +'\n'+ footer

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
        total = 'Total: ' + str(self.balance)   
        return title + '\n' + ledger + total
   
    def deposit(self, amount, description =''):
        self.balance += amount
        status = self.check_funds(amount)
        if status == True:
            self.ledger.append({"amount": amount, "description": description})
        if description == ' ':
            self.ledger.append({"amount": amount, "description": ''})



    def withdraw(self, amount, description =''):
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
        if self.balance > 0 and amount < self.balance:
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




        
