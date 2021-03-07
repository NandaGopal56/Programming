
"""
import email.utils
import re
n=1
string=[]
for i in range(n):
    str1 = 'gopal@gmail.com'

    temp1 = email.utils.parseaddr(str1)

    temp1 = list(temp1)

    temp1 = str(temp1[1])

    if temp1[0] != "." or temp1[7]!=".":
        temp1 = temp1.replace("@", " ").replace(".", " ")

    temp1 = temp1.split(" ")

    while ("" in temp1):
        temp1.remove("")

    f1 = str(temp1[0])

    regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
    check = re.compile('[@!#$%^&*()-_.<>?/\|}{~:]')

    if len(temp1) == 3:
        if len(temp1[2]) <= 3 and temp1[2].isalpha() and check.search(temp1[2]) == None:
            if temp1[1].isalpha():
                if regex.search(temp1[0]) == None and check.search(f1[0]) == None:
                    string.append(str1)
n=len(string)
for i in range(n):
    print(string[i])






"""
#alternate code

import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)


"""
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
dheeraj <dheeraj-234@gmail.com>
crap <itsallcrap>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
mattp <matt23@@india.in>
harsh <.harsh_1234@rediff.in>
harsh <-harsh_1234@rediff.in>
vineet <vineet.iitg@gmail.com>
vineet <vineet.iitg@gmail.co>
vineet <vineet.iitg@gmail.c>
this <is@valid.com>
this <is_som@radom.stuff>
this <is_it@valid.com>
this <_is@notvalid.com>
teas <tea@didlld.gt>
vineet <vineet@gmail.com>
vineet <vineet@gma.il.co.m>
vineet <vineet@gma-il.co-m>
vineet <vineet@gma,il.co@m>
vineet <vineet@gmail,com>
vineet <.vin@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>
shashank <shashank@9mail.com>
shashank <shashank@gmail.9om>
shashank <shashank@gma_il.com>
shashank <shashank@mail.moc>
shashank <shashank@company-mail.com>
shashank <shashank@companymail.c_o>
"""