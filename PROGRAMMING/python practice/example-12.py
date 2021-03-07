class bill:
    def __init__(self,mob,amt):
        self.mobileNo=mob
        self.BillAmount=amt

class mobile:
    def __init__(self,sp,mb,vc,du,pt):
        self.serviceprovider=sp
        self.mobilenumber=mb
        self.voicecall=vc
        self.dataused=du
        self.paymenttype=pt

    def getbillamount(self,lst):
        finalres=[]
        for k in lst:
            finalbill=0
            if k.serviceprovider=='jio':
                finalbill=k.dataused*10
            if k.serviceprovider=='airtel':
                finalbill=k.dataused*11
                if k.paymenttype=='paytm':
                    finalbill=finalbill-(finalbill*0.10)
            finalres.append(bill(k.mobilenumber,finalbill))
        #for i in finalres:
            #print(i.BillAmount,i.mobileNo)
        return finalres


if __name__=='__main__':
    lst=[]
    for _ in range(int(input('count:'))):
        sp=input('sp:')
        mb=int(input('mb:'))
        vc=int(input('vc:'))
        du=int(input('du:'))
        pt=input('pt:')
        lst.append(mobile(sp,mb,vc,du,pt))
        demo_obj=mobile('',0,0,0,'')
    res=demo_obj.getbillamount(lst)
    for i in res:
        print(i.mobileNo,i.BillAmount)