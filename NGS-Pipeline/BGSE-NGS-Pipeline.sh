#!/bin/bash

# Additional information:
# =======================
# Dit script roept alle losse scripts aan die
# nodig zijn om paired end fastq bestanden om te analyseren,
# te trimmen, te mappen en daarna te converteren aan.
#
# Het script heeft een run naam nodig en 2 fastq bestanden.

if [ "$1" = "--h" ] || [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ "$1" = "-help" ]
then
	echo ""
	echo "Het script zorgt ervoor dat twee paired end fastq bestanden"
	echo "geanalyseerd, getrimmed en gealigned worden door losse scripts"
	echo "aan te roepen."
	echo ""
	echo "Manier van gebruik:"
	echo "./StartBGSE-NGS-Pipeline.sh voor interactief."
	echo "of:"
	echo "./BGSE-NGS-Pipeline.sh <fastq_file1> <fastq_file2> <lege_directory> "
	echo ""
	
	exit
fi
# defineren van vaste variabelen.
fastq1=$1
fastq2=$2
runnaam=$3 

python Readinventarisatie.py ${runnaam} pre_trim ${fastq1} 1
python Readinventarisatie.py ${runnaam} pre_trim ${fastq2} 1
echo "Pre-statistiek is klaar."
sh ./trimfiles.sh ${fastq1} ${fastq2} ${runnaam}
echo "Trimmen is klaar."
python Readinventarisatie.py ${runnaam} post_trim ${runnaam}/trimmedpaired1.fastq 2
python Readinventarisatie.py ${runnaam} post_trim ${runnaam}/trimmedpaired2.fastq 2
echo "Post-statistiek is klaar."

sh ./Alligner.sh ${fastq1} ${fastq2} ${runnaam}
echo "De pipeline is klaar. De bestanden zijn terug te vinden in de map" ${runnaam}