import time
import sys

target="Nanda gopal pattanayak"
guess=""

for c in target:
    #print(i,c)
    j=ord(' ')  # Return the Unicode code point for a one-character string.
    #print(j)
    while True:
        sys.stdout.write(f'\r{guess}{chr(j)}')
        #print(j)
        #sys.stdout.flush()
        time.sleep(0.1)
        if chr(j)==c:
            guess+=c
            break
        j+=1
print('\n\nACCESS GRANTED')