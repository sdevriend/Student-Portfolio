#!/bin/bash

# Additional information:
# =======================
# Dit script converteerd paired end fastq files naar csv formaat,
# blacklist slechte reads en trimmed deze. Dit is in combinatie met
# trimline.py.
# Output files: trimmedpaired1 trimmedpaired2

if [ "$1" = "--h" ] || [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ "$1" = "-help" ]
then
	echo ""
	echo "Het script converteerd 2 fastq files naar csv,"
	echo " filtert slechte reads en trimmed de overgebleven reads."
	echo "Dit gebeurd in dit script in combinatie met trimline.py."
	echo ""
	echo "Gebruik:"
	echo "./trimfiles.sh <fastq1> <fastq2> <outputdirectory>"
	echo ""
	
	exit
fi

file1=$1
file2=$2
dir=$3
# Verander van directory om met lokale bestanden te werken.
cd ${dir}
# De bestanden worden geconverteerd en gechecked op slechte reads.
file1conversie="$(python ../trimline.py --convert ${file1} > Convert1)"
file1pyth="$(python ../trimline.py -l Convert1 > blacklistreads)"
file2conversie="$(python ../trimline.py --convert ${file2} > Convert2)"
file2pyth="$(python ../trimline.py -l Convert2 >> blacklistreads)"
# Om dubbele waardes te filteren, wordt de lijst gesorteerd en dubbele waardes worden verwijderd.
sortblacklist="$(cat blacklistreads | sort | uniq > blacklistgood)"
# De slechte reads worden niet meegenomen. Voor performance wordt grep in C uitgevoerd en wordt een fgrep gedaan omdat de input
# file een fixed string is. Dit scheelt een paar uur.
file1correct="$(cat Convert1 |  LC_ALL=C fgrep -v -f blacklistgood > Convert1Black)"
file2correct="$(cat Convert2 | LC_ALL=C fgrep -v -f blacklistgood > Convert2Black)"
# Converts worden direct verwijderd om de disk op te schonen.
rm Convert1
rm Convert2
# Bestanden worden getrimmed en worden geschreven naar nieuwe files.
file1blackpyth="$(python ../trimline.py -t Convert1Black > trimmedpaired1.fastq)"
file2blackpyth="$(python ../trimline.py -t Convert2Black > trimmedpaired2.fastq)"
# Tijdelijke bestanden die verwijderd kunnen worden.
rm Convert1Black Convert2Black blacklistgood blacklistreads
 
