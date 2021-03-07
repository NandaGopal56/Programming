class check:
    def prime(self,n):
        self.n = n
        count = 0
        for i in range(1, self.n + 1):
            if self.n % i == 0:
                count += 1
        if count == 2:
            return 1
        else:
            return 0

if __name__=='__main__':
    x=1
    y=10000
    prime=[]
    obj=check()
    for i in range(x,y+1):
        c=obj.prime(i)
        if c==1:
            prime.append(i)

    for i in range(0,len(prime)):
        for j in range(i+1,len(prime)):
            if prime[j]-prime[i]==6:
                print('[',prime[i],prime[j],']')
