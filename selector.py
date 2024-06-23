import ksl
def kslselector():
    option = ""
    while option != "q":
        print("1. contact info")
        print("2. view docs")
        print("3. run interpreter")
        print("q. Quit")
        option = input("Select an option: ")
        if option == "1":
            print("Contact info selected")
            ksl.contact()
        elif option == "2":
            suboption = ""
            while suboption != "q":
                print("1 main docs")
                print("2 extra docs")
                print("q. Go back")
                suboption = input("Select a suboption: ")
                if suboption == "1":
                    print("Main docs selected")
                    ksl.docmain()
                elif suboption == "2":
                    print("Extra docs selected")
                    ksl.docex()
                elif suboption == "q":
                    print("Going back to main menu")
                else:
                    print("Invalid suboption")
        elif option == "3":
            suboption = ""
            while suboption != "q":
                print("1 main")
                print("2 extra")
                print("q. Go back")
                suboption = input("Select a suboption: ")
                if suboption == "1":
                    print("Main interpreter selected")
                    ksl.main()
                elif suboption == "2":
                    print("Extra interpreter selected")
                    ksl.ex()
                elif suboption == "q":
                    print("Going back to main menu")
                else:
                    print("Invalid suboption")
        elif option == "q":
            print("Exiting the program")
        else:
            print("Invalid option")
kslselector()