class bill:
    def __init__(self,mobileNo,billAmt):
        self.mobileNo=mobileNo
        self.billAmt=billAmt

class mobile_bill:
    def __init__(self,sp,mb,vc,du,pt):
        self.serviceProvider=sp
        self.mobileNo=mb
        self.voiceCalls=vc
        self.dataUsed=du
        self.paymentType=pt

    def getBill_Amt(self,lst):
        finalres=[]
        for k in lst:
            finalbill=0
            if k.serviceProvider=='JIO':
                finalbill=k.dataUsed*10
            if k.serviceProvider=='AIRTEL':
                finalbill=k.dataUsed*11
                if k.paymentType=='PAYTM':
                    finalbill=finalbill-(finalbill*0.10)
            finalres.append(bill(k.mobileNo,finalbill))
        return finalres
if __name__=='__main__':
    lst=[]
    count=int(input('enter count: '))
    for i in range(count):
        sp=input('enter service provider: ')
        mb=int(input('enter mobile no: '))
        vc=int(input('voice calls: '))
        du=int(input('data used: '))
        pt=input('payment type: ')
        lst.append(mobile_bill(sp,mb,vc,du,pt))
        demo_obj=mobile_bill("",0,0,0,"")
    res=demo_obj.getBill_Amt(lst)
    for i in res:
        print(i.mobileNo,i.billAmt)