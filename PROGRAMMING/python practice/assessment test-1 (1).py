class employee:
    def __init__(self,sal):
        self.sal=sal

    def highestpf(self):
        pf=[]

        len1=len(self.sal)
        for i in range(0,len1,3):
            print(self.sal[i])
            x=(self.sal[i]*12)/100
            pf.append(x)

        pf.sort(reverse=True)
        return pf[0]

def main():
    sal=[]
    for i in range(int(input("enter no. of employees: "))):
        basic=int(input("enter basic: "))
        hra=int(input("enter hra: "))
        ita=int(input("enter ita: "))
        sal.append(basic)
        sal.append(hra)
        sal.append(ita)
    obj=employee(sal)

    print(obj.highestpf())
main()