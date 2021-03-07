def book_counts(input_string):
    input_string=input_string.split(" ")
    #print(input_string)
    d={}
    for i in input_string:
        count=input_string.count(i)
        d[i]=count
    return d

def get_max_occurence1(input_string):
    input_string=input_string.split(" ")
    max=0
    for i in range(len(input_string)):
        count=0
        for j in range(i+1,len(input_string)):
            if input_string[i]==input_string[j]:
                count+=1
        if count > max:
            max = count
    for i in range(len(input_string)):
        count=0
        for j in range(i+1,len(input_string)):
            if input_string[i] == input_string[j]:
                count+=1
                if count == max:
                    print(input_string[i],max+1)

def get_max_occurence2(input_string):
    max=1
    for key in d:
        if d[key] > max:
            max=d[key]
    for key in d:
        if d[key] ==max:
            print(key,max)

if __name__=='__main__':
    input_string='Nanda good gopal gopal Nanda Nanda Nanda gopal gopal gopal Nanda'
    d = book_counts(input_string)
    get_max_occurence1(input_string)
    get_max_occurence2(d)