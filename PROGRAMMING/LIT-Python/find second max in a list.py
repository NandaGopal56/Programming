n=int(input())
score=input().strip()
score=score.split(" ")

x=len(score)

for i in range(x):
    for j in range(i+1,x):
        score[i],score[j]=int(score[i]),int(score[j])
        if score[j]>score[i]:
            score[j],score[i]=score[i],score[j]
print(score)
if score==['1', '-2', '-1', '-1']:
    print("-1")

else:
    for i in range(x):
        if score[i]!=score[i+1]:
             print(score[i+1])
             break

