class Person:
    def __init__(self, nick, email, password):
        self.nick = nick
        self.email = email
        self.password = password
        self.loggedIn = False
        self._key1 = list("abcdefgoprstuwxyz1236789")
        self._key2 = list("9876321zyxwutsrpogfedcba")

    def __str__(self):
        return f"{self.nick};{self.email};{self.password}"

    def cypherObject(self):
        self.nick = self.__cipher(self.nick)
        self.email = self.__cipher(self.email)
        self.password = self.__cipher(self.password)

    def decipherObject(self):
        self.nick = self.__decipher(self.nick)
        self.email = self.__decipher(self.email)
        self.password = self.__decipher(self.password)

    def __cipher(self, toCipher):
        tmp = list(toCipher)
        for i in range(len(tmp)):
            try:
                tmp[i] = self._key2[self._key1.index(tmp[i])]
            except AttributeError:
                continue
            except ValueError:
                continue
        return listToString(tmp)

    def __decipher(self, toDeCipher):
        tmp = list(toDeCipher)
        for i in range(len(tmp)):
            try:
                tmp[i] = self._key1[self._key2.index(tmp[i])]
            except AttributeError:
                continue
            except ValueError:
                continue
        return listToString(tmp)


def listToString(list):
    tmp = ""
    for ch in list:
        tmp += ch
    return tmp