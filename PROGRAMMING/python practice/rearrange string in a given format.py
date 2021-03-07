def wrap(string, max_width):
    counter=0
    str=''
    for i in string:
        if counter!=max_width:
            str=str+i
            counter+=1
        else:
            str=str+'\n'+i
            counter=1


    return str

if __name__ == '__main__':
    string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_width=4
    result = wrap(string, max_width)
    print(result)