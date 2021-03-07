class BookStore:
    def __init__(self,bookdb):
        self.bookdb=bookdb
    def getBookdb(self):
        return self.bookdb
    def viewBooks(self):
        for i in self.bookdb:
            print(self.bookdb[i][0],self.bookdb[i][1],self.bookdb[i][2],self.bookdb[i][3])

if __name__=='__main__':
    name="let us c"
    tech="c"
    edt=2
    aut="nikhil"
    book1=[name,tech,edt,aut]

    name="advance python"
    tech="python"
    edt=3
    aut="gopal"
    book2=[name,tech,edt,aut]

    bookdb={1:book1,2:book2}

    b=BookStore(bookdb)
    bookstr=b.getBookdb()
    b.viewBooks