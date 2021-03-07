def push(stack,sp):   #sp=stack pointer
    if sp==len(stack)-1:
        print("stack is full")
    else:
        data=input("enter data")
        sp+=1
        stack[sp]=data
    return sp
def pop(stack,sp):
    if sp==-1:
        print("stack si empty")
    else:
        stack[sp]==0
        sp-=1
    return sp

def traverse(stack,sp):
    while sp>=0:
        print(stack[sp])
        sp-=1

def main():
    stack=[0,0,0,0,0]
    sp=-1
    while True:
        print("1 for push")
        print("2 for pop")
        print("3 for exit")
        ch=int(input("enter your choice: "))
        if ch==1:
            sp=push(stack,sp)
            traverse(stack,sp)
        elif ch==2:
            sp=pop(stack,sp)
            traverse(stack,sp)
        elif ch==3:
            break
        else:
            print("invalid choice ")
main()