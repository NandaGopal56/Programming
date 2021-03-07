def swapcase_method(str):
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = "abcdefghijklmnopqrstuvwxyz"
    s = ''

    for i in range(len(str)):
        if str[i].isalpha():
            if str[i] in u:
                i=u.index(str[i])
                s=s+l[i]
            elif str[i] in l:
                i=l.index(str[i])
                s=s+u[i]
        else:
            s=s+str[i]

    print(s)




swapcase_method("nanda gopal")
swapcase_method("NanDa GopAL")
swapcase_method("NA#ndA$@GopA*l")