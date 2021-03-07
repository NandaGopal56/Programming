max=10
var=10

dict={'apple':['iphone',max,'maxpro'],'samsung':'galaxy','huawei':'honor',
      'tata':{'car':'nexon','steel':'tiscon'},
      'dell':'inspiron','lenovo':'ideapad','acer':[1,2,3,4,5],
       var:'it is a variable kay'
     }

for key in dict:
    print(key,'=',dict[key])
print()

print(dict['tata']['car'])
print(dict['apple'][1])
print(dict[var])
for i in range(len(dict['acer'])):
    print(dict['acer'][i], end=" ")



