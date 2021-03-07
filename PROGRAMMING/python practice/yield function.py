def ch_gen():
    ch_list=['a','b','c']
    for ch in ch_list:
        yield ch

def main():
    remote=ch_gen()
    print(remote)
    print(remote.__next__())
    print(remote.__next__())
    print(remote.__next__())

main()