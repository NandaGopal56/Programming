def split_method(str,arg):
    l=[]
    s=""
    for i in range(len(str)):
        if str[i] != arg and i!=len(str)-1:
            s=s+str[i]
        elif str[i] != arg :
            s=s+str[i]
            l.append(s)
        elif str[i] == arg:
            l.append(s)
            s=""

    print(l)


split_method("nanda gopal"," ")
split_method("nanda,gopal",",")
split_method("nanda,gopal patt good,hell of,what",",")