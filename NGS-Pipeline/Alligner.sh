#!/bin/bash
# Additional information:
# =======================
# Het script mapt de fastq's tegen het referentie genoom en convert de sam naar bam.
# Tevens wordt er vcf file gemaakt en een consensus sequentie. Als laatste worden losse files verwijderd.
#
# Het script heeft een run naam nodig en 2 fastq bestanden.

if [ "$1" = "--h" ] || [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ "$1" = "-help" ]
then
	echo ""
	echo "Het script mapt twee fastq files tegen een referentie genoom van Wolbachia."
	echo "Daarnaast maakt het script een bam file, een vcf file en consensus"
	echo ""
	echo "Manier van gebruik:"
	echo "./Alligner.sh <fastq_file1> <fastq_file2> <output_directory> "
	echo ""
	
	exit
fi

ref="Wolbachia_Genome"

wget -O ${ref} "ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Wolbachia_endosymbiont_of_Culex_quinquefasciatus_Pel_uid61645/NC_010981.fna"
# defineren van vaste variabelen.
fastq1=$1
fastq2=$2
runnaam=$3 

bowtie2-build ${ref} ${runnaam}/index_output

bowtie2 -x ${runnaam}/index_output -1 ${fastq1} -2 ${fastq2} -S ${runnaam}/result.sam

samtools view -bS -T ${ref} ${runnaam}/result.sam | samtools sort - ${runnaam}/result_sorted

samtools faidx ${ref}
samtools mpileup -uf ${ref} ${runnaam}/result_sorted.bam > ${runnaam}/result.pileup

bcftools view -bvcg ${runnaam}/result.pileup > ${runnaam}/result.bcf
bcftools view  ${runnaam}/result.bcf > ${runnaam}/result.vcf

samtools mpileup -uf ${ref} ${runnaam}/result_sorted.bam | bcftools view -cg - | perl ./home/BGSE/vcfutils.pl vcf2fq > ${runnaam}/consensus.fastq  
rm *.fai
rm ${runnaam}/index*
rm ${runnaam}/result.bcf
mv ${ref} ${runnaam}