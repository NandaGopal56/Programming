
str='{vja{,js{as},san},zd,{} }'

opening=str.count('{')
closing=str.count('}')

if opening==closing:
    print('balanced parenthesis')
    print('no on parenthesis is:',opening+closing)
else:
    print('not balanced parenthesis')