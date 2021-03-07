def convert_uppercase(str):
    u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l="abcdefghijklmnopqrstuvwxyz"
    s=''
    for i in range(len(str)):
        if str[i].isalpha():
            if str[i] in u:
                s=s+str[i]
            elif str[i] not in u:
                i=l.index(str[i])
                s=s+u[i]
        else:
            s=s+str[i]

    print(s)

convert_uppercase("nanda gopal")
convert_uppercase("Nanda GoPal")
convert_uppercase("NaNda@ gopal")
convert_uppercase("nandA GOpaL")
