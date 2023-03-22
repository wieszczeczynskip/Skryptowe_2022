class Calculator:

    produkt = ""
    pln = 0
    __marza = 0
    _kursEUR = 4.75
    _kursUSD = 4.30
    cenaEUR = 0
    cenaUSD = 0
    cenaEURmarza = 0
    cenaUSDmarza = 0

    def __init__(self, pln, produkt):
        self.produkt = produkt
        self.cenaPLN = pln
        self.__marza = 0.3 * pln
        self.cenaPLNmarza = self.cenaPLN + self.__marza
        self.cenaUSD = pln / self._kursUSD
        self.cenaEUR = pln / self._kursEUR
        self.cenaUSDmarza = (pln + self.__marza) / self._kursUSD
        self.cenaEURmarza = (pln + self.__marza) / self._kursEUR

    def printProdukt(self):
        message = "%10s%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f"
        print(
            message
            % (
                self.produkt,
                self.cenaPLN,
                self.cenaPLNmarza,
                self.cenaUSD,
                self.cenaUSDmarza,
                self.cenaEUR,
                self.cenaEURmarza,
            )
        )


produkty = []
produkty.append(Calculator(25, "Mis"))
produkty.append(Calculator(2, "Chleb"))
produkty.append(Calculator(6, "Zelki"))
tabelka = "%10s%10s%10s%10s%10s%10s%10s"
print(
    tabelka
    % (
        "Produkt",
        "Cena PLN",
        "Cena PLNm",
        "Cena USD",
        "Cena USDm",
        "Cena EUR",
        "Cena EURm",
    )
)
for x in produkty:
    x.printProdukt()