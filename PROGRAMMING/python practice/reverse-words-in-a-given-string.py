S = "i.like.this.program.very.much"

S = S.split('.')
revString = []
for i in range(len(S)-1, -1, -1):
    revString.append(S[i])
revString = '.'.join(revString)

print(revString)

'''
https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
'''