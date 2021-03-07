from random import randint
class book:
    @classmethod
    def createsdm(cls):   #for creating static data member
        cls.pubname=input("enter publisher name: ")
        cls.pubaddr=input("enter publisher address: ")
    def creatensdm(self):   #for creating non-static data member
        self.bname=input("enter book name: ")
        self.aname=input("enter author name: ")
        self.bprice=int(input("enter vook price: "))
        self.bedn=int(input("enter book eddition: "))
        self.bid=self.bargen()
    def read(self):
        print("pubname: ",self.__class__.pubname)
        print("pubaddr: ",self.__class__.pubaddr)

        print("bname: ",self.bname)
        print("anmae: ",self.aname)
        print("bprice: ",self.bprice)
        print("bedn: ",self.bedn)
        print("bid: ",self.bid)
    @staticmethod
    def bargen():
        bar="ISIN"+str(randint(100,999)).zfill(7)
        return bar
def main():
    obj1=book()
    obj2=book()
    obj3=book()

    book.createsdm()

    obj1.creatensdm()
    obj2.creatensdm()
    obj3.creatensdm()

    obj1.read()
    obj2.read()
    obj3.read()

main()


