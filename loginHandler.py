from Person import Person


class loginHandler:
    def __init__(self):
        n = input("1. Login.\n2. Register.\n3. Exit")
        self._people = self._getPeople()

    def _getPeople(self):
        people = list()
        file = open("Data/loginData.txt", "r")
        for line in file:
            parts = line.split(";")
            person = Person(parts[0], parts[1], parts[2])
            person.decipherObject()
            people.append(person)

        return people




    def register(self):
        try:
            nick = input("Input nick: ")
            email = input("Input your email:\t")
            rEmail = input("Repeat your email:\t")
            while email != rEmail:
                print("Email is not the same.")
                email = input("Input your email:\t")
                rEmail = input("Repeat your email:\t")
            password = input("Input your password:\t")
            rPassword = input("Repeat your password:\t")
            while password != rPassword:
                print("Password is not the same.")
                password = input("Input your password:\t")
                rPassword = input("Repeat your password:\t")

            person = Person(nick, email, password)
            # tutaj skończyłem ostatnio
            person.cypherObject()
            file = open("Data/loginData.txt", "a")
            file.write(person.__str__())

        except:
            print("")