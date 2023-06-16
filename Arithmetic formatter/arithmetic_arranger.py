def arithmetic_arranger(numlist, args = True):
    
    #check n of problems
    if len(numlist) > 5:
        return('Error: Too many problems')
    
    #splitting the operators
    firstoper = list()
    secoper = list()
    operators = list()
    for line in numlist:   
        nums = line.split()
        firstoper.append(nums[0])
        secoper.append(nums[2])
        operators.append(nums[1])
    
    #check operators
    for symbol in operators:
        if symbol == ('/') or symbol == ('*'):
            return('Error: Operator must be + or -')
        
    #check n of digits
    #check if only digits in operands
    for digits in firstoper:
        if len(digits) > 4:
            return('Error: Numbers cannot be more than four digits')
        for i in range(len(digits)):
            try:
                letter = int(digits[i])
            except:
                return('Error: Numbers must only contain digits')

    for digits in secoper:
        if len(digits) > 4:
            return('Error: Numbers cannot be more than four digits')
        for i in range(len(digits)):
            try:
                letter = int(digits[i])
            except:
                return('Error: Numbers must only contain digits')
    
    results = list()
    firstline = list()
    secline = list()
    dashes = list()

    #get results
    for k in range(len(firstoper)):
        if operators[k] == '+':
            z = int(firstoper[k]) + int(secoper[k])
            results.append('  ' + str(z))
        else:
            z = int(firstoper[k]) - int(secoper[k])
            results.append('  ' + str(z))
    
    #print(results)

    #get dashes
    for k in range(len(firstoper)):
        if len(firstoper[k]) > len(secoper[k]):
            ndash = ('-' * (len(firstoper[k]) + 2))
            dashes.append(ndash)
        else:
            ndash = ('-' * (len(secoper[k]) + 2))
            dashes.append(ndash)
    
    #print(dashes)

    #making first line
    for i in range(len(firstoper)):
        if len(firstoper[i]) > len(secoper[i]):
            firstline.append(' '*2 + firstoper[i])
        else:
            firstline.append(' '*(len(secoper[i]) - len(firstoper[i]) + 2) + firstoper[i])

    #making second line
    for i in range(len(secoper)):
        if operators[i] == '+':
            if len(secoper[i]) > len(firstoper[i]):
                secline.append('+' + ' ' + secoper[i])
            else:
                secline.append('+' + ' ' + (' '*(len(firstoper[i]) - len(secoper[i]))) + secoper[i])
        else:
            if len(secoper[i]) > len(firstoper[i]):
                secline.append('-' + ' ' + secoper[i])
            else:
                secline.append('-' + ' ' + (' '*(len(firstoper[i]) - len(secoper[i]))) + secoper[i])
    
    #print(firstline,'\n',secline)

    #display problems formatted
    arranged = str()
    
    if args == True:
        arranged ='    '.join(firstline) + '\n' + '    '.join(secline) + '\n' + '    '.join(dashes) + '\n' + '    '.join(results)
    else:
        arranged ='    '.join(firstline) + '\n' + '    '.join(secline) + '\n' + '    '.join(dashes)
    
    return arranged



        
        

            


        


    
