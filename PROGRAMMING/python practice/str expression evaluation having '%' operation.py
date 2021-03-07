operator='56%'
operator=operator.split('%')
symbol=['+','-','*','/']

operator_list=[]

for expression in operator:
    if expression != '':
        print(expression)

        x=''
        if len(expression) > 1:
            for i in range(len(expression)-1,-1,-1):
                if expression[i] not in symbol:
                    x=x+expression[i]
                else:
                    break
        else:
            x=expression

        x=x[::-1]
        percentage=float(x)/100


        l=[]
        for item in expression:
            l.append(item)

        if len(expression) > 1:
            for i in range(len(expression)-1,-1,-1):
                print(l[i])
                if expression[i] not in symbol:
                    l[i]='$'
                else:
                    break
        else:
            l[0]='$'


        for i in range(len(l)):
            try:
                l.remove('$')
            except:
                print('can not remove')

        l.append(percentage)
        expression=''

        for item in l:
            expression=expression+str(item)

        print(expression)
        operator_list.append(expression)

operator=''.join(operator_list)
print(operator)


ans=eval(operator)
print(ans)