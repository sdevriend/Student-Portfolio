#!/usr/bin/python
import csv
import os
import re
import sys


def showUsageInformation():
    print
    print "trimline is een kleine toolsuite die meerdere dingen kan."
    print "1: Het converteren van een fastq naar een csv. Dit kan met:"
    print "\t ./trimline.py --convert fastqbestand."
    print "Let op! Dit moet in bash weggeschreven worden naar een bestand "
    print "voor performance."
    print
    print "Dit kan gedaan worden met het volgende commando:"
    print "\t ./timline.py -l converted_fastq_file"
    print "Let op! Dit moet in bash weggeschreven worden naar een bestand  "
    print "voor performance."
    print
    print "3: Het trimmen van fastq sequenties en omzetten van slechte "
    print "waardes naar N met een score van 25 of lager."
    print "Dit kan gedaan worden met het volgende commando:"
    print "\t ./trimfile.py -t converted_fastq_file"
    print "Let op! Dit moet in bash weggeschreven worden naar een bestand"
    print "  voor performance."


def checkline(header, qualityseq):
    """
    Input: 2
        header: header van de kwaliteits seq.
        qualityseq: Kwaliteitsscore.
    De functie zet de kwaliteiheader om naar een getalreeks
    op basis van de asci converteer score met ord. Daar wordt
    64 van afgehaald.
    Als de sequentie gemiddeld lager is dan 20, dan is de score niet
    hoog genoeg om door te gaan. De sequentie
    wordt dan geprint en de laatste posities worden verwijderd.
    """
    qual = [ord(x) - 64 for x in qualityseq]
    score = sum(qual)/len(qual)
    if score < 20:
        newheader = header.strip()
        print newheader[:-4]


def fastqgenerator(fastqfile):
    """
    Input: fastqfile: De bestandsnaam voor de fastq om in te lezen.
    De functie opent met een buffer van 1 de fastq file in. Dit is voor
    performance. Daarna zet de reader de fastq om als csv bestand met
    een tab als delimiter. Daarna wordt elke row als een yield
    opgehaald. Als de reader op is, dan wordt er een None geyield.
    """
    fastq = open(fastqfile, 'rb', buffering=1)
    reader = csv.reader(fastq, delimiter="\t")
    for item in reader:
        yield item
    yield None


def trimline(fastqline):
    """
    Input: enkele fastq line in lijst vorm.
    Als eerste wordt er een reguliere expressie
    filter aangemaakt die zorgt ervoor dat
    alles met en score onder de 25 wordt opgevangen
    die vier keer voorkomt.
    Daarna wordt de filter toegepast en in matches opgeslagen.
    Daarna wordt de sequentie omgezet naar een lijst.
    Vervolgens wordt er door de matches heengeloopt
    en de lijst aangepast op basis van de matches posities naar
    N.
    Daarna worden de N's links en rechts op de uiteindes weggehaald.
    Dit wordt vervolgens opgeslagen in een variable om zo de lengtes
    te bepalen en de kwaliteits header op de juiste manier te strippen.
    Als laatste wordt het resultaat in fastq getoont.
    """
    filter = re.compile("[A-Z]{4}")
    matches = filter.finditer(fastqline[3])
    seq = list(fastqline[1])
    for match in matches:
        loc = match.span()
        seq[loc[0]] = "N"
        seq[loc[0] + 1] = "N"
        seq[loc[0] + 2] = "N"
        seq[loc[1] - 1] = "N"
    newseq = "".join(seq)
    leftstrip = len(newseq) - len(newseq.lstrip("N"))
    rightstrip = len(newseq.rstrip("N"))
    newfast0 = fastqline[0].strip()
    newfast1 = fastqline[2].strip()
    print newfast0
    print newseq[leftstrip:rightstrip]
    print newfast1
    print fastqline[3][leftstrip:rightstrip]


def FastQnaarCSV(fastq):
    """
    Input: fastq, datagenerator.
    De methode loopt door de datagenerator en stopt als de datagenerator
    geen items meer heeft. De methode haalt de drie overige lines op die
    voor de sequentie, 2e header staan en de kwaliteitscontrolle.
    De methode print alles op een enkele regel met een \t delim.
    """
    while True:
        header1 = fastq.next()
        if header1 is None:
            break
        seq = fastq.next()
        header2 = fastq.next()
        qualityseq = fastq.next()
        print header1[0], "\t", seq[0], "\t", header2[0], "\t", qualityseq[0]


def blacklistfile(data):
    """
    Input: data, bestands generator.
    De functie loopt door de generator heen
    en kijkt in een if statement of de row None is.
    Als dit zo is, dan wordt de loop stop gezet.
    Anders wordt trimline gestart.
    """
    while True:
        row = data.next()
        if row is None:
            break
        else:
            checkline(row[0], row[3])


def trimfile(data):
    """
    Input: data, bestands generator.
    De functie loopt door de generator heen
    en kijkt in een if statement of de row None is.
    Als dit zo is, dan wordt de loop stop gezet.
    Anders wordt trimline gestart.
    """
    while True:
        row = data.next()
        if row is None:
            break
        else:
            trimline(row)


def main(argv):
    """
    De functie kijkt of er een argument value wordt meegegeven.
    Als dit zo is, dan wordt  er gekeken of de help argument wordt
    meegegeven. Dan wordt showUsageInformation gestart.
    Als het argument -l is, dan wordt het blacklist systeem gestart.
    Als het argument -t is, dan wordt het trim systeem gestart.
    Als het argument --convert is, dan wordt het converteer systmeem
    gestart. Alle systemen gebruiken een data generator als input.
    """
    if len(argv) >= 2:
        if argv[1] == "-h" or argv[1] == "--h" or argv[1] == "-help" or argv[1] == "--help":
            showUsageInformation()
        elif argv[1] == "-l":
            data = fastqgenerator(argv[2])
            blacklistfile(data)
        elif argv[1] == "-t":
            data = fastqgenerator(argv[2])
            trimfile(data)
        elif argv[1] == "--convert":
            data = fastqgenerator(argv[2])
            FastQnaarCSV(data)

if __name__ == "__main__":
    main(sys.argv)
