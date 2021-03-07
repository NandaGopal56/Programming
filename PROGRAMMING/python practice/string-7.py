"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given
 string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

def string_correction(str):

    if str.find('not') != -1 and str.find('poor') != -1:

        if str.index('not') < str.index('poor'):
            new='good'
            i=str.index('not')
            j=str.index('poor')+4
            #print(i,j)

            old=str[i:j]
            str=str.replace(old,new)
        print(str)
    else:
        print(str)


string_correction('The lyrics is not that poor!')
string_correction('The lyrics is poor!')