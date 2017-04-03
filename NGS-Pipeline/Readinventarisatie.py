#!/usr/bin/python
import os
import sys
from itertools import izip_longest


def showUsageInformation():
    print
    print "Readinventarisatie toont per input de statistiek die gemaakt wordt."
    print "De gebruiker krijgt:"
    print "\t -Het aantal reads."
    print "\t -De lengtes."
    print "\t -De globale gc percentage."
    print "\t -De gc percentage per frame."
    print
    print "De output zal weggeschreven worden naar een textbestand."
    print
    print "Hoe te gebruiken:"
    print
    print "RunNaam fase bestand"
    print
    print "Voorbeeld:"
    print
    print "python Readinventarisatie.py testrun fase1 /home/bgse/s_1_1.txt"
    sys.exit()


def openBestand(bestandsnaam, x_trim):
    """
    De functie opent een bestand en yield elke rij. Als er geen lines meer
    zijn, dan wordt het bestand gesloten en wordt None geyield.
    """
    n = int(x_trim)
    fastqbestand = open(bestandsnaam, 'rb', buffering=1)
    while True:
        data = fastqbestand.readline()
        if not data:
            break

        yield data[:-n]
    fastqbestand.close()
    yield None


def StatNaarFile(RunNaam, fase, reads, langste, kortste, perc,
                 perclist, bestandsnaam):
    """
    Input: 8
        RunNaam: String, naam van de run.
        fase: String, fase waar de run is.
        reads: int, aantal reads in het bestand.
        langste: int, langste read.
        kortste: int, kortste read.
        perc: float, percentage gc.
        perclist: lijst, gc percentage per frame.
        bestandsnaam: Input bestandsnaam.
    De methode maakt een bestand aan in een opgegeven map met de naam
    van de fase die opgegeven wordt. Dit kan gebruikt worden om
    meerdere files te maken.
    De functies schrijft de input en vervolgens een lijst
    naar het bestand en sluit deze vervolgens.
    """
    originfile = bestandsnaam.split("/")[-1]
    path = RunNaam + "/" + fase + "_" + originfile + ".txt"
    statfile = open(path, 'wb')
    statfile.write("Statistiek voor: " + originfile + "\n")
    statfile.write("Aantal reads: \t" + str(reads) + "\n")
    statfile.write("Langste read: \t" + str(langste) + "\n")
    statfile.write("Kortste read: \t" + str(kortste) + "\n")
    statfile.write("Percentage gc content: \t" + "{:.2f}".format(perc) + "%\n")
    statfile.write("Frame\tGC percentage:\n")
    for x in range(len(perclist)):
        statfile.write(str(x+1) + "\t" + "{:.2f}".format(perclist[x]) + "%\n")
    statfile.close()


def StatVanRead(bestandgenerator, langste, kortste, at, cg):
    """
    Input: 4
        bestandgenerator: yield functie van fastq file.
        langste: int voor de langste read.
        kortste: int voor kortste. is een groot getal.
        at: float voor a en t percentage.
        cg: float voor c en g percentage.
    De functie maakt een tijdelijke string aan samen met
    de reads lijst. Daarna wordt er geloopt totdat
    de variable rij None is.
    In de while loop wordt een for loop gestart die 4 keer loopt.
    Bij elke run wordt de sequentie gepakt en wordt er gekeken
    naar het aantal cg, en wordt de langste en korste read
    getoetst. Als laatste wordt de rij als tuple toegevoegd
    voor performance. Als laatste worden alle variables
    terug gegeven.
    """
    rij = "temp"
    reads = []
    while rij is not None:
        for x in range(4):
            rij = bestandgenerator.next()
            if rij is not None:
                if x == 1:
                    at += rij.count("A") + rij.count("T")
                    cg += rij.count("C") + rij.count("G")
                    if len(rij) > langste:
                        langste = len(rij)
                    if len(rij) < kortste:
                        kortste = len(rij)
                    reads.append(tuple(rij))
            else:
                break
    return reads, langste, kortste, at, cg


def Inventarisatie(Runnaam, Fase, bestandsnaam, x_trim):
    """
    Input: 3
        Runnaam: String, Naam voor de run / folder.
        Fase: String, Unieke naam voor het bestand.
        bestandsnaam: String, Bestandnaam van fastq.
    De functie maakt een generator aan op basis van een opgegeven file.
    Daarna worden de standaard variabelen aangemaakt voor de statistiek.
    korste is expres hoog zodat deze snel wordt verworpen.

    Om de lijsten om te draaien die van StatVanRead komen, wordt de
    module izip_longest gebruikt. Daarna wordt er door zipped
    heengeloopt om de gc percentage per read te berekenen.
    Met de berekening wordt N niet meegenomen.
    Als laatste wordt StatNaarFile aangeroepen om het resultaat naar
    een bestand te schrijven.
    """
    bestandgenerator = openBestand(bestandsnaam, x_trim)
    langste = 0
    kortste = 5000
    at = 0.0
    cg = 0.0
    reads, langste, kortste, at, cg = StatVanRead(bestandgenerator, langste,
                                                  kortste, at, cg)
    perc = (cg / (cg + at)) * 100
    zipped = izip_longest(*reads)
    perc_reads = []
    for item in zipped:
        g = float(item.count('G'))
        c = float(item.count('C'))
        a = float(item.count('A'))
        t = float(item.count('T'))
        try:
            temp_perc = ((c + g) / (a + t + c + g)) * 100
        except ZeroDivisionError:
            temp_perc = 0
        perc_reads.append(temp_perc)
    StatNaarFile(Runnaam, Fase, len(reads), langste,
                 kortste, perc, perc_reads, bestandsnaam)


def main(argv):
    """
    De methode kijkt of het eerste argument een help argument is.
    Als dit zo is,dan wordt de help informatie getoont. Anders
    wordt de inventarisatie gestart.
    """
    if len(argv) >= 2:
        if argv[1] == "-h" or argv[1] == "--h" \
                           or argv[1] == "-help" or argv[1] == "--help":
            showUsageInformation()

        else:
            Inventarisatie(argv[1], argv[2], argv[3], argv[4])

if __name__ == "__main__":
    main(sys.argv)
