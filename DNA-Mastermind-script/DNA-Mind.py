"""
Naam:                 Datum:         Notitie:
Sebastiaan de Vriend  11:40 02-01-14 herstart schrijven
Sebastiaan de Vriend  12:30 23-01-14 Functie check schrijven
Sebastiaan de Vriend  15:00 24-01-14 Invoer rewrite en afmaken programma
Sebastiaan de Vriend  14:30 27-01-14 Documentatie schrijven
Sebastiaan de Vriend  13:30 09-02-14 Last minute aanpassingen
Sebastiaan de Vriend  15:00 09-02-14 Functie laad_configuratie schrijven
Sebastiaan de Vriend  20:30 09-02-14 Documentatie herschrijven

Dna mind is een spel waarbij de gebruiker moet raden wat de
complementaire streng is die de computer heeft gegenereerd. De gebruiker
krijgt een aantal beurten afhankelijk van de lengte van de dna streng.
De gebruiker krijgt na elke invoer te zien welke letters er goed staan
en welke er goed zijn, maar niet op de juiste positie. Als de gebruiker
gewonnen heeft krijgt deze een felicitatie en daarbij ook zijn
statistieken te zien. Als de gebruiker verloren heeft krijgt deze de
dna streng te zien die de computer heeft gemaakt. Na de game zal de
gebruiker gevraagt worden of hij/zij nog een game wilt spelen.
"""

from random import choice
from sys import exit as afsluiten

dna = {'A': 'T', 'T': 'A', 'R': 'Y', 'G': 'C', 'C': 'G', 'Y': 'R'}


def victory(conf):
    """
    Input:
    conf: dictionary met spel gegevens en statistieken.

    Functie print een overwinningsboodschap met daarin de input.

    Output:
    Boolean
    """
    print("Gefeliciteerd,je hebt de complementaire keten geraden.",
          "Het DNA stukje ziet er als volgt uit:")
    print(" \t \t Computer:", "".join(conf['DNA']))
    print(" \t \t Jij:     ", "".join(conf['DNA_COMPL']))
    print("Je hebt", conf['T_Beurt'] - conf['Beurten'], " poging(en) nodig",
          " gehad om alle basen allemaal op de correcte posities in de keten",
          " te plaatsen. \nStatistiek:")
    print ("Aantal keren correcte positie goed geraden:", conf["X"])
    print ("Aantal keren goed geraden:", conf["XW"])
    print ("Aantal fout geraden:", conf["F"])
    return False


def dna_check(gebruiker, computer):
    """
    Input:
    gebruiker: Lijst met karakters van gebruiker.
    computer: Lijst met karakters van computer

    Functie kijkt in de eerste loop of de karakters van de 2 lijsten
    overeen komen met elkaar Als dit zo is wordt er een X aan result
    toegevoegd. Zo niet worden de niet overeenkomende karakters in 2
    nieuwe lijsten gestopt.
    Vervolgens wordt er per karakter van gebruiker gekeken of deze
    voorkomt in computer. Als dit zo is wordt er een W toegevoerd aan
    result en wordt de karakter uit de computer lijst gehaald.

    Output:
    result: String met karakters.
    """
    result = ""
    
    gebruiker_new_list = []
    computer_new_list = []
    gebruiker = list(gebruiker)
    for x in range(0, len(computer)):
        if gebruiker[x] == computer[x]:
            result += "X"
        else:
            gebruiker_new_list.append(gebruiker[x])
            computer_new_list.append(computer[x])
    for x in gebruiker_new_list:
        if x in computer_new_list:
            computer_new_list.remove(x)
            result += "W"
    return result


def dna_fout_checker(invoer_gebruiker):
    """
    Input:
    invoer_gebruiker: Een string met characters.

    De functie checkt of de string geen andere karakters bevat dan de
    dna dictionary. Als er een karakter niet aanwezig zal de fout string
    vergroot worden. Bij een lengte van 1 of hoger zullen de foute
    karakters op het scherm getoond worden.

    Output:
    fout: De string met foute karakters.
    """
    fout = ""
    for x in invoer_gebruiker:
        if x not in dna:
            fout += x
    if len(fout) == 1:
        print("De letter (", fout, ") is niet toegestaan. Probeer opnieuw.",
              sep="")
    elif len(fout) > 1:
        print("De letters (", ";".join(fout),
              ") zijn niet toegestaan. Probeer opnieuw.", sep="")
    return fout


def dna_maker(lengte):
    """
    Input:
    lengte: Integer voor aantal karakters dna streng.

    Er wordt een lijst gemaakt met daarin karakters van de global
    dictionary dna. De lengte hiervan wordt bepaald door de string
    lengte.
    Na het aanmaken van de lijst wordt er een complementaire lijst
    gemaakt. Dit wordt gedaan met de lijst die aangemaakt is in de
    vorige stap. De nieuwe lijst wordt uitgebreid met de dictionary
    waarde.

    Output:
    dna_streng: lijst met karakters
    reverse_streng: lijst met karakters
    """
    dna_streng = []
    for x in range(0, lengte):
        dna_streng.append(choice(list(dna.keys())))
    reverse_streng = []
    for x in dna_streng:
        reverse_streng.append(dna[x])
    ##print(reverse_streng)
    return dna_streng, reverse_streng


def game_invoer(strenglengte, beurt):
    """
    Input:
    strenglengte: Integer met de gekoze lengte voor de dna streng.

    Functie gaat in een loop waar gevraagt wordt voor een input.
    Als eerste wordt het gechecked of het spel gestopt moet worden.
    Daarna wordt de input in caps gezet.
    Vervolgens wordt er gekeken of de aantal karakters van de invoer
    overeen komt met de strenglengte. Daarna wordt er gekeken of de
    invoer correct is. Als de invoer goed is zal deze terug worden
    gegeven.

    Output:
    game_vraag: gecontroleerde input. String met karakters.
    """
    while True:
        print("Aantal beuren:", beurt)
        game_vraag = input("Kies een combinatie. " +
                           "De volgende letters zijn toegestaan: A; T; C; " +
                           "G; R en Y.\nTyp alleen een “Q” in als je het " +
                           "spel wilt stoppen." +
                           "\nSchrijf de combinatie als 1 woord: ")
        check_quit(game_vraag)
        if len(game_vraag) == strenglengte:
            game_fout = dna_fout_checker(game_vraag.upper())
            if len(game_fout) == 0:
                return game_vraag.upper()
        else:
            print("De lengte komt niet overeen!")


def score_statistiek(totaal_stand, huidige_beurt):
    """
    Input:
    totaal_stand: Dictionary met daarin scores van gebruiker.
    huidige_beurt: string met resultaat van gebruiker.

    Als eerste wordt het aantal fout berekend. dit wordt gedaan door
    raad_lengte - de lengte van huidige beurt.
    Daarna wordt de dictionary geupdate met het aantal punten voor fout,
    aantal * "X" en de totaal lengte van de hudige stand.
    """
    fout = totaal_stand['lengte'] - len(huidige_beurt)
    totaal_stand["F"] += 1 * fout
    totaal_stand["X"] += 1 * huidige_beurt.count("X")
    totaal_stand["XW"] += 1 * len(huidige_beurt)


def laad_configuratie(beurtaantal):
    """
    Input 1:
    beurtaantal: integer

    Functie maakt een dictionary die gebruikt wordt om spel onderdelen
    bij te houden.
    Game bepaalt het aantal beurten doormiddel van input. Deze wordt
    opgezocht in dictionary kansen.
    Beurten wordt gebruikt om af te tellen.
    T_Beurt wordt gebruikt om de eerste beurt aan te geven.
    DNA wordt gebruikt voor de game
    DNA_COMPL wordt gebruikt voor de complementaire streng.
    DNA en DNA_COMPL worden gemaakt in de functie dna_maker.
    X, XW en F zijn voor statistieken bij te houden
    verloren wordt gebruikt voor print in de game functie.

    Output 1:
    game_conf: Dictionary
    """
    kansen = {4: 12, 5: 14, 6: 18, 7: 24, 8: 30, 9: 38, 10: 50}
    game_conf = {"Beurten": 0, "X": 0, "XW": 0, "F": 0, "DNA": "",
                 "DNA_COMPL": "", "verloren": True, "T_Beurt": 0,
                 "lengte": 0}
    game_conf['Beurten'] = kansen[beurtaantal]
    game_conf['T_Beurt'] = kansen[beurtaantal]
    game_conf['DNA'], game_conf['DNA_COMPL'] = dna_maker(beurtaantal)
    game_conf['lengte'] = beurtaantal
    return game_conf


def game(g_conf):
    """
    Input 1:
    g_conf: Dictionary met spel gegevens.

    Functie loopt door Beurten heen totdat de teller op 0 staat.
    Als eerste wordt de functie invoer aangegroep zodat de gebruiker
    zijn eigen invoer kan ingeven. Vervolgens wordt de invoer gecheckt
    in de spel vorm, na de spelvorm wordt de score van de gebruiker
    geupdate. Als de update klaar is wordt er een beurt van de
    gebruiker eraf gehaald.
    Vervolgens wordt er met een if statement gekeken of de gebruiker
    gewonnen heeft. Als g_dna_score_check evenveel "X" heeft als
    de lengte * "X", heeft de gebruiker gewonnen en wordt verloren
    de resultaat van de functie victory. Ook wordt het aantal beurten
    op 0 gezet. Als er niet aan de if functie wordt voldaan, wordt de
    resultaat van de gebruiker getoond.
    Zodra beurten 0 is, wordt er een if functie uitgevoerd op dict
    onderdeel verloren. Als deze True is zal er een print worden gedaan.
    Als de game is gewoonnen door de gebruiker, is verloren op False
    gezet door de functie victory.
    """
    while g_conf['Beurten'] != 0:
        g_invoer = game_invoer(g_conf['lengte'], g_conf['Beurten'])
        g_dna_score_check = dna_check(g_invoer, g_conf['DNA_COMPL'])
        score_statistiek(g_conf, g_dna_score_check)
        g_conf['Beurten'] -= 1
        if g_dna_score_check == "X" * g_conf['lengte']:
            g_conf['verloren'] = victory(g_conf)
            g_conf['Beurten'] = 0
        else:
            print(g_dna_score_check)
    if g_conf['Beurten'] == 0:
        if g_conf['verloren']:
            print ("Helaas jehebt de complementaire keten niet geraden. ",
                   "De keten die ik gemaakt had was:")
            print ("\t", "".join(g_conf['DNA_COMPL']))
        else:
            pass


def check_quit(c_invoer):
    """
    Input 1:
    c_invoer: string met karakters.

    Functie checkt of er een Q is ingevoerd om het spel te stoppen.
    """
    if c_invoer.upper() == "Q":
        afsluiten('Het programma wordt afgesloten')
    else:
        pass


def ronde_vraag():
    """
    Functie vraagt gebruiker voor invoer.

    Output 1:
    Boolean.
    """
    while True:
        g_volgende = input("Wil je het opnieuw proberen? J/N:")
        if g_volgende.upper() == "J":
            return False
        elif g_volgende.upper() == "N":
            return True


def main():
    """
    Functie print boodschap uit. Vervolgens word er via een input
    bepaald door de gebruiker hoe lang de DNA-strand moet zijn.
    Als eerste wordt de invoer doorgestuurd naar check_quit.
    Daarna wordt er een if statement uitgevoerd om te kijken of de
    invoer tussen de 3 en 11 lang is. Als dit zo is wordt de functie
    laad_configuratie gestart en de variabele daarvan wordt gestopt
    in game_configuratie. Deze wordt doorgeven aan game. Na de game
    functie wordt de functie ronde_vraag gestart en de uitkomst daarvan
    wordt opgeslagen in stoppen.
    Als de invoer geen getal is, zal er een waarschuwing getoond worden.
    Als de game gespeeld is en de gebruiker wilt ermee stoppen, dan zal
    de loop gestopt worden doormiddel van een if statement voor stoppen.
    """
    print("Welkom bij DNA-mind. Het doel is het correct raden van de",
          "complementaire DNA-strand.\nEen DNA-strand bestaat uit basen met",
          "de volgende codes: \n",
          "\t A; T; C; G; R en Y")
    while True:
        invoer = input("De lengte van de DNA-strand mag 4; 5; 6; 7; 8; 9 of" +
                       " 10 zijn. Wat is de lengte van de keten? \n" +
                       "Typ een getal tussen de 3 en de 11 of typ een “Q” " +
                       "om het spel te stoppen:")
        check_quit(invoer)
        try:
            invoer = int(invoer)
        except ValueError:
            pass
        stoppen = False
        if invoer in range(4, 11):
            game_configuratie = laad_configuratie(invoer)
            game(game_configuratie)
            stoppen = ronde_vraag()
        else:
            print("Helaas, de keuze (", invoer, ") is niet toegestaan.",
                  sep="")
        if stoppen:
            print("Tot de volgende keer!")
            break
        else:
            pass

main()
