class _RangeError(Exception):
    pass


from Loader import Loader


class Console:
    def __init__(self):
        self.kraj = None
        self.isZgony = None
        self.miesiac = None
        self.dzien1 = None
        self.dzien2 = None
        self.start = None
        self.koniec = None
        self.loader = Loader()

    @staticmethod
    def get_string(
        message,
        name="string",
        default=None,
        minimum_length=0,
        maximum_length=80,
        force_lower=False,
    ):
        message += ": " if default is None else " [{0}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line:
                    if default is not None:
                        return default
                    if minimum_length == 0:
                        return ""
                    else:
                        raise ValueError("{0} may not be empty".format(name))
                if not (minimum_length <= len(line) <= maximum_length):
                    raise ValueError(
                        "{0} must have at least {1} and at most {2} characters".format(
                            name, minimum_length, maximum_length
                        )
                    )
                return line if not force_lower else line.lower()
            except ValueError as err:
                print("ERROR", err)

    @staticmethod
    def get_integer(
        message,
        name="integer",
        default=None,
        minimum=None,
        maximum=None,
        allow_zero=True,
    ):
        message += ": " if default is None else " [{0}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line and default is not None:
                    return default
                x = int(line)
                if x == 0:
                    if allow_zero:
                        return x
                    else:
                        raise _RangeError("{0} may not be 0".format(name))
                if (minimum is not None and minimum > x) or (
                    maximum is not None and maximum < x
                ):
                    raise _RangeError(
                        "{0} must be between {1} and {2} inclusive{3}".format(
                            name, minimum, maximum, (" (or 0)" if allow_zero else "")
                        )
                    )
                return x
            except _RangeError as err:
                print("ERROR", err)
            except ValueError as err:
                print("ERROR {0} must be an integer".format(name))

    def app(self):
        while True:
            x = Console.get_string("Co chcesz zrobić?\n[1] Czytaj dane\n[2] Wyjście")
            if x == "1":
                self.isZgony = Console.get_integer(
                    "Wybierz:\n[0] Przypadki zachorowań\n[1] Zgony",
                    minimum=0,
                    maximum=1,
                    default=self.isZgony,
                )
                self.kraj = Console.get_string(
                    "Z którego kraju dane chcesz uzyskać? (po angielsku)",
                    default=self.kraj,
                )
                self.miesiac = Console.get_integer(
                    "Z którego miesiąca dane chcesz uzyskać? (numer miesiąca)",
                    default=self.miesiac,
                )
                self.dzien1 = Console.get_integer(
                    "Od którego dnia chcesz uzyskać dane?", default=self.dzien1
                )
                self.dzien2 = Console.get_integer(
                    "Do którego dnia chcesz uzyskać dane?", default=self.dzien2
                )
                counter = 0
                for x in range(self.dzien1, self.dzien2 + 1):
                    counter = counter + self.loader.getData(
                        self.isZgony, 2020, x, self.miesiac, self.kraj
                    )
                print(counter)
            elif x == "2":
                break
            else:
                print("Zła liczba")


if __name__ == "__main__":
    console = Console()
    console.app()
