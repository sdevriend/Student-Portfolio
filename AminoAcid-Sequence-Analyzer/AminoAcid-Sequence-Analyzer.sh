#!/bin/bash
function kiestaak(){
	# De functie laat de gebruiker een keuze maken
	# en stopt de loop pas als de keuze 1 of 2 is.
	local opties="Zoeken Analyse Stoppen"
	echo "Welkom bij badup programma. Je hebt de keuze tussen 2 taken."
	echo "Voer je keuze in:"
	select optie in ${opties}
	do
		if [ "${REPLY}" = '1' ] || [ "${REPLY}" = '2' ]
		then
			break
		elif [ "${REPLY}" = '3' ]
		then
			exit
		else
			echo "Ongeldige keuze opgegeven. Voer een 1 in voor zoeken, voor een 2 in voor de analyse en 3 om te stoppen."
			echo "Voer je keuze in: "
			echo ${opties}
		fi
	done
	taak=${REPLY}
}

function openFile(){
	mode=$1
	
	read -p "Voer hier je bestand in:" filenameUnchecked
	filenameformatted=$(echo $filenameUnchecked | sed 's/ /\\ /')
	if [ -f ${filenameformatted} ]
	then
		if [ ${mode} == seq ]
		then
			readSeq
		else
			cons="$(cat ${filenameformatted} | awk '{print $1}')"
		fi
	else	
		error=1
		echo "Er is een ongeldige bestand opgegeven."
	fi

}



function readSeq(){
	aantal_seq="$(egrep ^">" < ${filenameformatted} | wc -l)"
	if [ ${aantal_seq} -gt 1  ]
	then
		error=1
		echo "Er zijn meerdere sequenties gedetecteerd."
	elif [ ${aantal_seq} == 0 ]
	then
		error=1
		echo "Er zijn geen sequenties gedetecteerd."
	else
		sequentieNaam="$(awk '{ if(substr($1, 1, 1) == ">")print $1; }' < ${filenameformatted} | tr -d '>')"
		sequentie="$(awk '{ if(substr($1, 1, 1) != ">")print toupper($1); }' < ${filenameformatted} | tr '\n' ' ' | tr -d ' ')"
		fi
}

function Analyse(){
	echo "U heeft gekozen voor de analyse taak. Geeft een bestand op met daarin een sequentie."
	openFile seq
	if [ ${error} = 0 ]
	then
		printf "Sequentie naam:   %19s \n" ${sequentieNaam}
		printf "Aantal aminozuren:%19s \n" "$(egrep -o "[A-Z]" <<< ${sequentie} | egrep -o "[^BJOUXZ]" | wc -l)"
		printf "Aantal iminozuren:%19s \n" "$(egrep -o "P" <<< ${sequentie} |  wc -l)"
		printf "Aantal Hydrofoob: %19s \n" "$(egrep -o "[A C F G H I K L M S T V W Y]" <<< ${sequentie} | wc -l)"
		printf "Aantal hydrofiel: %19s \n" "$(egrep -o "[D E H K R]" <<< ${sequentie} | wc -l)"
		printf "Aantal positief:  %19s \n" "$(egrep -o "[H K R]" <<< ${sequentie} | wc -l)"
		printf "Aantal negatief:  %19s \n" "$(egrep -o "[D E]" <<< ${sequentie} | wc -l)"
		nonacid="$(egrep -o "[^A C D E F G H I K L M N P Q R S T V W Y]" <<< ${sequentie} | wc -l)"
		if [ "$nonacid" -gt 0 ]
		then
			printf "Aantal onbekend:  %19s \n" ${nonacid}
			grep -oab "[^A C D E F G H I K L M N P Q R S T V W Y]" <<< ${sequentie} | awk -F ':' '{print $1+1, $2}'
		fi
		
	fi
	
}

function Consensus(){
	echo "U heeft gekozen voor de consensus taak. Geef een bestand op met daarin een sequentie."
	openFile seq
	if [ ${error} = 0 ]
	then
		local consopties=("Intypen Bestand")
		select conskeuze in ${consopties}
		do
			if [ "${REPLY}" = '1' ] || [ "${REPLY}" = '2' ]
				then
					break
				else
					echo "Voer een geldige keuze in. 1 voor intypen. 2 voor bestand."
				fi
		done
		if [ ${conskeuze} = "Bestand" ]
		then
			openFile File
		else
			read -p "Voer een consensus in:" consunchecked
			cons=$(awk '{ print $1}' <<< ${consunchecked})
		fi
		if [ ${error} = 0 ]
		then
			if [ ${#cons} -gt "9" ] && [ ${#cons} -lt "21" ]
			then
				maakCons
				if [ ${error} = 0 ]
				then
					
					matches="$(egrep -o "${cons_str}" <<< ${sequentie} | wc -l)"
					echo "Resultaat voor sequentie: ${sequentieNaam}"
					if [ "$matches" -gt 0 ]
					then
						echo "Er is een hit voor: ${cons}"
						echo "De hit komt ${matches} voor."
						echo "Hit Positie"
						grep -oab "${cons_str}" <<< ${sequentie} | awk -F ':' '{print $2, $1+1}'
					else
						echo "Er is geen hit gevonden voor: ${cons}. Probeer het met een andere concensus."
					fi
				fi
			else
				echo "De consensus moet minimaal 10 en maximaal 20 karakters lang zijn. "
				echo "De lengte van je gekoze consensus is: ${#cons}"
				error=1
			fi
		fi
	fi

}

function maakCons(){
	cons_str=""
	for ((i; i < ${#cons}; i++))
	do
		char="${cons:$i:1}"
		case ${char} in
		[ACDEFGHIKLMNPQRSTVWY])
			cons_str+="${char}"
			;;
		o)
		    cons_str+="[S T]"
			;;
		l)
			cons_str+="[I L V]"
			;;
		.)
			cons_str+="[A C D E F G H I K L M N P Q R S T V W Y]"
			;;
		a)
			cons_str+="[F H W Y]"
			;;
		c)
			cons_str+="[D E H K R]"
			;;
		h)
			cons_str+="[A C F G H I K L M S T V W Y]"
			;;
		"-")
			cons_str+="[D E]"
			;;
		p)
			cons_str+="[C D E H K N Q R S T]"
			;;
		+)
			cons_str+="[H K R]"
			;;
		s)
			cons_str+="[A C D G N P S T V]"
			;;
		u)
			cons_str+="[A G S]"
			;;
		t)
			cons_str+="[A C D E G H K N Q R S T]"
			;;
		*)
			echo "Fout teken opgeven. ${char}"
			
			error=1
			;;
		esac
	
	done
	
}

function main(){
	until [ "${Stoppen}" = 1 ]
	do
		error=0
		kiestaak
		if [ ${taak} = "1" ]
		then
			Consensus
		elif [ ${taak} = "2" ]
		then
			Analyse
		fi
	done
}
main