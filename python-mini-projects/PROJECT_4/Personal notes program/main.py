# A personal notes program
while True :
    print("-----wELCOME TO PERSONAL NOTES------")
    print("1.Add a note")
    print("2.View all notes")
    print("3.Exit")

    choose = int(input("Choose an optin (1-3) :"))
   

    if choose == 1:
        note = input(str("enter the note : "))
       
        with open("note.txt","a") as f:
            f.write(note + "\n")
        print("----your note is saved----")
    elif choose ==2:
       print("-----your saved notes----")
       with open("note.txt") as f:
           a = f.read()
           print(a)
    elif choose ==3:
        print("Goodbye!")
        break
    else:
        print("Oops! you entered an invalid option")        
