"""
Naam: Datum: Notitie:
Sebastiaan de Vriend 04-05-2014 Eerste documenten opzetten
Sebastiaan de Vriend 08-05-2014 Engine opzetten.
Sebastiaan de Vriend 15-6-2014 Documentatie toevoegen.
"""


from random import choice


class GameEngine:
    """
        Klasse maakt spel aan en kan een score bijhouden. Zie
        documentatie __init__ voor meer informatie.
    """
    def __init__(self, opslaan, beurtaantal):
        """
            Maakt het spel aan. De __init__ methode heeft 2 parameters.
                opslaan
                    Bestandsnaam
                beurtaantal
                    int voor lengte keten en aantal beurten.
            De init kijkt of de lengte van opslaan groter is dan 0. Als
            dit zo is dan heeft de gebruiker ervoor gekozen om opslaan
            aan te zetten. Dan wordt opslaan een globale variable en
            wordt de methode CreateFile() aangeroepen. Ook wordt
            self.opslaanAAN op True gezet. Als de lengte 0 is wordt
            self.opslaanAAn op False gezet.
            Vervolgens wordt beurtaantal globaal gemaakt en wordt de
            methode NewGame aangeroepen.
        """
        if len(opslaan) > 0:
            self.opslaan = opslaan
            self.CreateFile()
            self.opslaanAAN = True
        else:
            self.opslaanAAN = False
        self.beurtaantal = beurtaantal
        self.NewGame()

    def NewGame(self):
        """
        Methode roept de __dna_maker functie aan om de dna strengen te
        maken. Vervolgens worden de globale waardes gereset, op false
        gezet en leeg gemaakt.
        """
        self.__dna_maker(self.beurtaantal)
        self.kansenaantal = {4: 12, 5: 14, 6: 18, 7: 24, 8: 30, 9: 38, 10: 50}
        self.__kansen = self.kansenaantal[self.beurtaantal]
        self.__Gewonnen = False
        self.__score = []
        self.antwoordenlijst = []

    def GetKansen(self):
        """ returns het aantal kansen. int """
        return self.__kansen

    def GetGewonnen(self):
        """ returns Boolean """
        return self.__Gewonnen

    def CreateFile(self):
        """
            Methode maakt een bestand aan met de opgegeven bestandsnaam
            met daarachter .txt om overschrijvingen te voorkomen met
            .py bestanden. Ook wordt er eenmalig een regel ingeschreven.
        """
        self.bestand = open(self.opslaan+".txt", "w")
        self.bestand.write("Kansen\tVolgorde\tAntwoord\n")

    def __dna_maker(self, lengte):
        """
        Input:
            lengte: Integer voor aantal karakters dna streng.

        Er wordt een lijst gemaakt met daarin karakters van de
        dictionary dna. De lengte hiervan wordt bepaald door de string
        lengte.
        Na het aanmaken van de lijst wordt er een complementaire lijst
        gemaakt. Dit wordt gedaan met de lijst die aangemaakt is in de
        vorige stap. De nieuwe lijst wordt uitgebreid met de dictionary
        waarde. Van de lijsten worden 2 tuples gemaakt en globale
        variablen. Er is gekozen voor tuples om te voorkomen dar er
        eenvoudig vals gespeeld kan worden.
        """
        dna = {'A': 'T', 'T': 'A', 'R': 'Y', 'G': 'C', 'C': 'G', 'Y': 'R'}
        dna_streng = []
        for x in range(0, lengte):
            dna_streng.append(choice(list(dna.keys())))
        reverse_streng = []
        for x in dna_streng:
            reverse_streng.append(dna[x])
        self.__dna_streng = tuple(dna_streng)
        self.__dna_reverse_streng = tuple(reverse_streng)

    def GetDNAReversed(self):
        """ returns tupple """
        return self.__dna_reverse_streng

    def GetTotaalPakket(self):
        """
        Methode maakt een lijst met daarin waardes van globale
        variabelen. Deze wordt ook gereturned.
        """
        lijst = []
        lijst.append(self.__Gewonnen)
        lijst.append(self.__dna_streng)
        lijst.append(self.__dna_reverse_streng)
        lijst.append(self.kansenaantal[self.beurtaantal] - self.__kansen)
        return lijst

    def BeurtCheck(self, invoer):
        """
        Functie kijkt in de eerste loop of de karakters van de 2 lijsten
        overeen komen met elkaar Als dit zo is wordt er een X aan result
        toegevoegd. Zo niet worden de niet overeenkomende karakters in 2
        nieuwe lijsten gestopt.
        Vervolgens wordt er per karakter van gebruiker gekeken of deze
        voorkomt in computer. Als dit zo is wordt er een W toegevoerd
        aan result en wordt de karakter uit de computer lijst gehaald.
        Als laatste wordt de functie self.afhandelen aangeroepen.
        """
        result = ""
        gebruiker_new_list = []
        computer_new_list = []
        gebruiker = list(invoer)
        for x in range(0, len(self.__dna_reverse_streng)):
            if gebruiker[x] == self.__dna_reverse_streng[x]:
                result += "X"
            else:
                gebruiker_new_list.append(gebruiker[x])
                computer_new_list.append(self.__dna_reverse_streng[x])
        for x in gebruiker_new_list:
            if x in computer_new_list:
                computer_new_list.remove(x)
                result += "W"
        self.afhandelen(result, invoer)

    def afhandelen(self, resultaat, invoer):
        """
            Methode haalt 1 kans van het totale aantal kansen af.
            Vervolgens wordt er aan de globale lijst het resultaat
            toevoegt. en daarna word de invoer toegevoegt aan de
            lijst met eerder gegeven antwoorden.
            Als opslaanAAN True is dat wordt de huidige kans, met
            de huidige score en invoer bijgeschreven.
            Als laatste wordt er gecheckt of de gebruiker gewonnen
            heeft door het aantal "X" in resultaat te toetsen aan
            het self.beurtaantal * "X". Als de dit zo is dan wordt
            self.__Gewonnen op True gezet.
        """
        self.__kansen -= 1
        self.__score.append(resultaat)
        self.antwoordenlijst.append(invoer)
        if self.opslaanAAN:
            self.bestand.write(str(self.__kansen) + "\t" +
                               "".join(resultaat) + "\t\t" +
                               "".join(invoer) + "\n")
        if resultaat == self.beurtaantal*"X":
            self.__Gewonnen = True

    def GetScore(self):
        """ Methode returns lijst met score erin. """
        return self.__score

    def RemakeGame(self):
        """
            Methode kijkt of opslaanAAN True is om een stuk tekst in
            self.bestand te zetten.
            Na de if wordt de methode self.NewGame() aangeroepen.
        """
        if self.opslaanAAN:
            self.bestand.write("Spel is gereset. Nieuwe keten gevormd!\n")
        self.NewGame()

    def GetAntwlijst(self):
        """ Returns self.antwoordenlijst. Een lijst met antwoorden """
        return self.antwoordenlijst
