class item:
    def __init__(self,item_id,item_name,item_price,quantity_available):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.quantity_available = quantity_available

    def calculate_price(self,check_quant):
        print(self.quantity_available,type(self.quantity_available))
        print(check_quant,type(check_quant))
        
        if self.quantity_available >= check_quant:
            return self.item_price*check_quant
        return 0

class store:
    def __init__(self,ilist):
        self.ilist = ilist

    def generate_bill(self,inp):
        bill = 0
        for key in inp:
            for obj in self.ilist:
                if key == obj.item_name:
                    bill += obj.calculate_price(inp[key])
        return bill




if __name__ == '__main__':
    ilist = []
    icount = 3
    for _ in range(icount):
        id = int(input('enter id:'))
        name = input("enter name:")
        price = int(input("enter price:"))
        quant = int(input("enter quant:"))

        i = item(id,name,price,quant)

        ilist.append(i)
    s = store(ilist)
    inp = {}
    inp_count = int(input('enter inp_count:'))
    for i in range(inp_count):
        name = input('enter name:')
        quantity = int(input("enter quantity:"))
        inp[name] = quantity
    print(ilist[0].calculate_price(2))
    print(s.generate_bill(inp))