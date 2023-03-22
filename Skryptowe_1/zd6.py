names = []
surnames = []
fullnames = []
emails = []
switch = True

while switch:
    name = input("Type in your name.\n")
    names.append(name)
    surname = input("Type in your surname.\n")
    surnames.append(surname)
    fullname = name + " " + surname
    fullnames.append(fullname)
    email = name.casefold() + "." + surname.casefold() + "@pwr.edu.pl"
    emails.append(email)
    print("Hello " + fullname + "! Your email address: " + email + ". Have a good day!")
    while switch:
        choose = input("[1] Another person\n[2] List of names\n[3] List of surnames\n[4] List of full names\n[5] List of emails\n\n[0] End\n")
        if choose == "1":
            break
        if choose == "2":
            print("Names:")
            for i in names:
                print(i)
        if choose == "3":
            print("Surnames:")
            for i in surnames:
                print(i)
        if choose == "4":
            print("Names        Surnames")
            fullname = "%-13s%s"
            for i in range(len(fullnames)):
                print(fullname % (names[i], surnames[i]))
        if choose == "5":
            print("Emails:")
            for i in emails:
                print(i)
        if choose == "0":
            switch = False