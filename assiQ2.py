a = 10
b = 10
print(id(a))
print(id(b))
#if your variable name is diff but data type and value is same you dont have to diff memory location or ID both have same memory id  ,,,int,str,tuple reuse in python and share memory  
#and
a = [10]
b = [10]
print(id(a))
print(id(b))
#in list they ctreate diff list obj 