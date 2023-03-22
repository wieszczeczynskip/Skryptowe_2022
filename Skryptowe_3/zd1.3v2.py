def emailsList():
    try:
        emails = []
        while True:
            email = input("Type in your email address. End - [0]\n")
            if email == "0":
                break
            if not("@" in email):
                raise ValueError("Musisz podać adres email.")
            emails.append(email)

        domains = []
        for i in emails:
            domains.append(i.split("@")[1])

        print("Domain       Count");
        counted = "%-12s %5d"

        while len(domains) > 0:
            counter = 0
            domain = domains[0]
            for i in domains:
                if i == domain:
                    counter += 1
            print(counted % (domain, counter))
            domains = [i for i in domains if i != domain]
    except ValueError as e:
        print(e)

emailsList()