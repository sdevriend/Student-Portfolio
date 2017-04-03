#!/bin/bash

# Additional information:
# =======================
# Het script is de startup voor de BGSE NGS Pipeline.
# Tijdens de startup worden er een vraag gesteld aan
# de gebruiker wat de naam is voor de run. Hiervoor
# wordt een map gemaakt waar de output bestanden
# in komen te staan.
# 
rm -r a
if [ "$1" == "--h" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ] || [ "$1" == "-help" ]
then
	echo "" 
	echo "Dit script is voor de startup van de pipeline."
	echo "Er wordt een run naam gevraagd en daarna start"
	echo "de pipeline."
	echo ""
	echo "Gebruikt als volgt:"
	echo ""
	echo "./StartBGSE-NGS-Pipeline.sh" 
	
	exit
fi

fastq1="/home/BGSE/s_2_1_sequence.txt"
fastq2="/home/BGSE/s_2_2_sequence.txt"


check=0
echo "Welkom bij de BGSE NGS pipeline. "
echo "De pipeline wordt gestart nadat er een directory bekend is voor de resultaten."
while [ ${check} == 0 ]
do
	read -p "Voer de naam van de run in: " dirname
	if  [ ! -f ${dirname} ] && [ ! -d ${dirname} ] 
	then
		check=1
	else
		echo "Bestand of map bestaat al!"
	fi
done

mkdir ${dirname}
echo "De pipeline maakt een pre statistiek, trimmed vervolgend de fastqfiles en maakt daarna een post statistiek."
echo "Vervolgens worden er sam en bam files gemaakt en daarvanuit wordt een vcf en sequentie gemaakt."
sh ./BGSE-NGS-Pipeline.sh ${fastq1} ${fastq2} ${dirname}
	