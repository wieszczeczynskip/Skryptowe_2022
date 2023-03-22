class Controlled_text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self._text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, newText):
        for x in newText:
            if str.isspace(x):
                raise Exception("Tekst zawiera spacje")
        if not str.isprintable(newText):
            raise Exception("Nie da się wydrukować tego tekstu")
        else:
            if len(newText) < 1:
                raise Exception("Tekst musi mieć conajmniej 1 znak")
            else:
                self._text = newText

    @text.deleter
    def text(self):
        del self._text

    def __eq__(self, other):
        if self.text == other.text:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.text > other.text:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.text < other.text:
            return True
        else:
            return False


t1 = Controlled_text("asdasd")
t2 = Controlled_text("asdasdasd")

print("z1")
print(t1 < t2)
print(t1 > t2)
print(t1 == t2)
