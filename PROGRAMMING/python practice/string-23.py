"""
Write a Python program to create a Caesar encryption. Go to the editor

Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
   is one of the simplest and most widely known encryption techniques.
   It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some
   fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
   by A, E would become B, and so on.
   The method is named after Julius Caesar, who used it in his private correspondence
"""

def caesar_encrypt(str,no):
    shift_type=input('left_shift = "1", right_shift = "2" :Enter a single choice :')
    u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l="abcdefghijklmnopqrstuvwxyz"

    code=''

    if shift_type=="1":
        for i in str:
            if i.isupper():
                index=u.index(i)
                code = code + u[index-no]
            else:
                index=l.index(i)
                code = code + l[index - no]
    elif shift_type=="2":
        for i in str:
            if i.isupper():
                index=u.index(i)
                code = code + u[index+no]
            else:
                index=l.index(i)
                code = code + l[index + no]
    print(code)


caesar_encrypt('abc', 2)
caesar_encrypt("DE",3)

