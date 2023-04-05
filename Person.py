class Person:
    def __init__(self, nick, email, password):
        self.nick = nick
        self.email = email
        self.password = password
        self._key1 = "abcdefgoprstuwxyz1236789"
        self._key2 = "9876321zyxwutsrpogfedcba"

    def __str__(self):
        return f"{self.nick};{self.email};{self.password}"

    def cypherObject(self):
        self.nick = self._cipher(self.nick)
        self.email = self._cipher(self.email)
        self.password = self._cipher(self.email)

    def decipherObject(self):
        self.nick = self._decipher(self.nick)
        self.email = self._decipher(self.email)
        self.password = self._decipher(self.email)

    def _cipher(self, toCipher):
        tmp = list(toCipher)
        for i in range(len(tmp)):
            tmp[i] = self._key2[self._key1.index(tmp[i])]
        return listToString(tmp)

    def _decipher(self, toDeCipher):
        tmp = list(toDeCipher)
        for i in range(len(tmp)):
            tmp[i] = self._key1[self._key2.index(tmp[i])]
        return listToString(tmp)


def listToString(list):
    tmp = ""
    for ch in list:
        tmp += ch
    return tmp