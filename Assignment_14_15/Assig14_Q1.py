Square = lambda sqr : sqr * sqr
 
def main():
    Num = int(input("Enter the number :"))
    ret = Square(Num)
    print(ret)
if __name__ == "__main__":
    main()



# #Functional part 
# checkEVen = lambda No : (No % 2 == 0)
     
# #procedural part 
# def main():
#     value = int(input("Enter the number: "))
#     Ret = checkEVen(value)   #Ret = value % 2 == 0) 
#     print(Ret)

#     if(Ret == True):
#         print("its even ")
#     else:
#         print("its odd")



# if __name__ == "__main__":
#     main()
