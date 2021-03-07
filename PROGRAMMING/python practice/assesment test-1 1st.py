class emp:
    def __init__(self,basic,hra,ita):
        self.basic=basic
        self.hra=hra
        self.ita=ita
class emp2:
    def __init__(self):
        self.a=10
    def highestpf(self,l):
        temp=[]
        for i in l:
            temp.append(int(0.12*i.basic))
        return max(temp)
if __name__=='__main__':
    c=int(input("enter count: "))
    l=[]
    for i in range(c):
        basic=int(input("enter basic: "))
        hra=int(input("enter hra: "))
        ita=int(input("enter ita: "))
        l.append(emp(basic,hra,ita))
    obj=emp2()
    print(obj.highestpf(l))