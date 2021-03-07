def enq(q,fp,rp):
    if rp==len(q)-1:
        print("queue is full")
    elif fp==rp==-1:
        data=int(input("enter data: "))
        fp+=1
        rp+=1
        q[rp]=data
    else:
        data=int(input("enter data: "))
        rp+=1
        q[rp]=data
    return fp,rp

def deq(q,fp,rp):
    if fp==rp==-1:
        print("queue is empty")

    elif fp==rp==0:
        q[fp]=0
        fp-=1
        rp-=1
    else:
        k=fp
        while k<rp:
            q[k]=q[k+1]
            k+=1
        q[rp]=0
        rp-=1
    return fp,rp

def traverse(q):
    for data in q:
        if data!=0:
            print(data,end=",")


def main():
    q=[0,0,0,0,0]
    fp=-1
    rp=-1
    while True:
        print("1 for insert:")
        print("2 for pop: ")
        print("3 for exit: ")

        ch=int(input("enter choce: "))
        if ch==1:
            fp,rp=enq(q,fp,rp)
            traverse(q)
        elif ch==2:
            fp,rp=deq(q,fp,rp)
            traverse(q)
        elif ch==3:
            break
        else:
            print("invalid choice")

main()



















