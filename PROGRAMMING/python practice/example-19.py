class Product:
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty

class Store :
    def __init__(self,sname,saddress,products):
        self.sname=sname
        self.saddress=saddress
        self.products=products

    def totalProductsPriceForCategory(self,category):
        price=0
        for i in self.products:
            if category == i.name.split('-')[0]:
                price=price+(i.price*i.qty)
        return price
        
    def checkProductAvailability(self,names):
        dic={}
        flag=True
        for product in names:
            flag=True
            for i in self.products:
                if i.name == product:
                    if i.qty > 0:
                        dic[i.name]='Available'
                        flag=False
                    elif i.qty == 0:
                        dic[i.name] = 'Out of stock'
                        flag=False
            if flag:
                dic[product] = 'Not Available'
                
        return dic
    
    def calculateBill(self,names):
        new_name=[]
        bill=0
        dic = s.checkProductAvailability(names)
        for product in names:
            for key in dic:
                if product == key:
                    if dic[key] == 'Available':
                        new_name.append(key)
        for i in new_name:
            for j in self.products:
                if i==j.name:
                    bill+=j.price
            
        return bill

            


if __name__ == '__main__':
    s = Store('ABC','XYZ',products=[])
    pno = int(input()) # reads the number of products to input
    for i in range(pno):
        name = input()
        price = float(input())
        qty = int(input())
        p = Product(name,price,qty)
        s.products.append(p)
    names = []
    category=input()
    n = int(input())#reads number of products you wish to purchase
    for i in range(n):
        pname = input()
        names.append(pname)

    print(s.totalProductsPriceForCategory(category))
    d=s.checkProductAvailability(names)
    for i in d:
        print(i,d[i])
    print(s.calculateBill(names))