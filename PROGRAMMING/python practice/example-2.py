class stock:
    def __init__(self,name,type,choice):
        self.name=name
        self.type=type
        self.price=price
    def check(self,ch):
        self.ch=ch
        if self.type==ch and self.price>=500:
            print(self.name)

if __name__=='__main__':
    l=[]
    for i in range(int(input('enter count: '))):
        name=input('enter company name: ')
        type=input('enter stock type: ')
        price=int(input('enter stock price: '))
        l.append(stock(name,type,price))
    ch=input('enter the choice type: ')
    for i in l:
        i.check(ch)