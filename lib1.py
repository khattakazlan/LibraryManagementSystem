lib = []

def main():
    while True:
        if lib is None:
            print("Empty list")
        
        
        else:
            print("Menu\n1: add book\n2: Remove book\n3: Check list\n")
            operation = input ("Enter Your Operation: ")
            if operation == "1":
                book_name = input("Enter book name: ")
                lib.append(book_name)
                print("Book added successfully")
                print((lib))
            elif operation == "2":
                book_name = input("Enter book name: ")
                if book_name not in lib:
                    print("No book found ion lib")
                else:
                    lib.pop(book_name)
                    print("Book removed successfully")
                    print((lib))
            elif operation == "3":
                print((lib))
            else:
                print("Wrong input was given")
            
            
main()

























# libr=[]

# def main():
#     if libr is  None:
#         print("Library is empty :")

#     else:
#         print("ADD \n Berrow \n Quit") 
#         user=input("Enter your book name here:")
#         if user=="ADD":
#             libr.append(user)
#             print("Book Added successfully :")
#             print(libr)
#         elif user=="Berrow":
#             user=input("Enter your book name")
#             if user not in libr:
#                 print("no Books")
#             else:
#                 libr.pop(user)
#                 print("Book Berrow Succecfully :")
#             print(libr)

#         elif user=="Quit":
#             print(libr)

#         else:
#             print("invalid input:")
            

# main()
            











