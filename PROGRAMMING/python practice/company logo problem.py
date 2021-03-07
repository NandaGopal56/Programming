if __name__ == '__main__':
    s = 'szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni'
    first = 0
    first_list=[]
    second = 0
    second_list=[]
    third = 0
    third_list=[]
    d = {}
    for i in s:
        if i not in d:
            count = s.count(i)
            d[i] = count
    copy=d.copy()

    print(d)

    for key in d:
        if d[key] > first:
            first=d[key]
    for key in d:
        if d[key]==first:
            first_list.append(key)
    first_list.sort()
    d.pop(first_list[0])




    for key in d:
        if d[key] > second:
            second=d[key]
    for key in d:
        if d[key]==second:
            second_list.append(key)
    second_list.sort()
    d.pop(second_list[0])



    for key in d:
        if d[key] > third:
            third=d[key]
    for key in d:
        if d[key]==third:
            third_list.append(key)
    third_list.sort()
    d.pop(third_list[0])

    print(first_list[0],copy[first_list[0]])
    print(second_list[0],copy[second_list[0]])
    print(third_list[0],copy[third_list[0]])