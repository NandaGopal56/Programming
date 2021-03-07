
d={1:'a',2:'b',3:'c',1:'b'}

print(d)

d[3]='d'
print(d)

#types of data type supported as key

d={1:'a'}    #tuple is supported as key

d={1.1:'a'}  #tuple is supported as key

d={1+2j:'a'}  #tuple is supported as key

d={1000000000000000000000:'a'}  #tuple is supported as key

d={"str":'a'}   #tuple is supported as key

#  d={[1,2,3]:'a'}  #list is not supported

d={(1,2,3):'a'}  #tuple is supported as key

#   d={{1:'n'}:'a'}  #dict is not supported as key