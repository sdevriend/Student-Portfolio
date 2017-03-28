package com.myapp.wicket;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import javax.servlet.ServletContext;
import static org.apache.wicket.ThreadContext.getApplication;
import org.apache.wicket.protocol.http.WebApplication;
import org.apache.wicket.util.file.File;
import org.apache.wicket.util.io.IClusterable;

/**
 * De class maakt de vraag aan voor de quiz. De class heeft Aminozuren.csv nodig
 * om data op te halen. De class maakt gebruikt van veel global variabelen. De
 * integers zijn voor posities in de csv file, arrdata is de gehele csv file De
 * overige stings zijn keuzes en strings voor vagen.
 *
 * @author Sebastiaan
 */
public class Vraag implements IClusterable {
    private boolean speciaal = false;
    private int vanPos;
    private int naarPos;
    private int aminoPos;
    private int vraagPos;
    private ArrayList alData = new ArrayList();
    private ArrayList alRadkeuzes = new <String>ArrayList();
    private String Vraagzin;
    private String VraagWoord;
    private String keuze = "";
    private String goedKeuze = "abc";
    private String[] zurenafk = new String[]{"H", "T", "S", "N"};

    /**
     * De methode maakt een vraag aan op basis van input. De input is
     * index-index-index De methodes readcsv wordt gebruikt voor alle data uit
     * te lezen. datasplit wordt gebruikt om alle indexen van de input te
     * verdelen. Daarna worden stuurVragen en maakVraag aangeroepen.
     *
     * @param data
     * @throws IOException
     */
    public Vraag(String data) throws IOException {
        readCSV();
        String[] datasplit = data.split("-");
        this.vanPos = Integer.parseInt(datasplit[0]);
        this.naarPos = Integer.parseInt(datasplit[1]);
        this.aminoPos = Integer.parseInt(datasplit[2]);
        stuurVragen();
        maakVraag();
    }

    /**
     * De methode kijkt naar de van positie en naar positie. Als de van positie
     * groter is dan naar positie, en naar positie kleiner dan 3, en van positie
     * groter dan 2, dan is het een speciale vraag van het laatste blok. Hier
     * wordt de vraag positie met 4 verhoogt, en wordt maakBlok 3 aangeroepen.
     * Als de van en naar positie kleiner zijn dan 3, dan is de vraag uit het
     * eerste blok. Hiervoor wordt maakKeuzes1 aangeroepen.
     *
     * de laatste vragen worden naar de preBlok2vragen gestuurd om zo de
     * juiste funcie aan te roepen.
     */
    private void stuurVragen() {
        if (this.vanPos > this.naarPos && this.naarPos < 3 && this.vanPos > 2) {
            this.vraagPos = 4 + (this.vanPos);
            maakBlok3();
            if (this.vanPos == 5) {
                this.speciaal = true;
            }
        } else if (this.vanPos < 3 && this.naarPos < 3) {
            this.vraagPos = this.naarPos;
            maakKeuzes1();
        } else {
            this.vraagPos = this.naarPos;
            preBlok2vragen();
        }
    }

    /**
     * De methode switched het getal naarPos om te bepalen welke vraag er
     * getoont gaat worden.
     */
    private void preBlok2vragen(){
        switch (this.naarPos) {
            case 3:
                maakBlok2("Hydrofoob", "Tussenin", "Hydrofiel");
                break;
            case 4:
                maakBlok2("Klein", "Middel", "Groot");
                break;
            case 5:
                maakBlok2("+", "0", "-");
                break;
            case 6:
                maakPref1();
                break;
        }
    }

    /**
     * De methode is wat langer, als eerste wordt het goede antwoord opgeslagen
     * in goedKeuze.
     *
     * Vervolgens worden er 3 Strings aangemaakt die gebruikt worden voor de
     * aminocheck. de eigens1, 2 en vreig zijn de eigenschappen voor de
     * aminozuren. vreig is de eigenschap van het goede antwoord. deze wordt
     * gecheckt in de for loop of deze niet overeenkomt met de 2 foute
     * antwoorden.
     *
     * In de for loop worden er random ints toegewezen aan de foute antwoorden
     * en die worden gechecked. Als laatste wordt alles doorgestuurd naar
     * voegKeuzesToe met de shuffle boolean.
     */
    private void maakBlok3() {
        this.goedKeuze = dataUitSet(this.aminoPos, this.naarPos);
        String eigens1, eigens2, vreig;
        int amino1 = 0, amino2 = 0;
        vreig = dataUitSet(this.aminoPos, this.vanPos);
        boolean uniek = false;
        while (uniek == false) {
            amino1 = new Random().nextInt(20);
            amino2 = new Random().nextInt(20);
            eigens1 = dataUitSet(amino1, this.vanPos);
            eigens2 = dataUitSet(amino2, this.vanPos);
            if (!vreig.equals(eigens1) && !vreig.equals(eigens2)) {
                if (amino1 != amino2) {
                    uniek = true;
                }
            }
        }
        voegKeuzesToe(this.goedKeuze, dataUitSet(amino1, this.naarPos), 
                dataUitSet(amino2, this.naarPos), true);
    }

    /**
     * Dit is de functie voor het maken van vragen op basis van aminozuren die
     * meerdere preferanties hebben voor 3D. De functie maakt 2 string aan,en
     * haalt de prefetanties op. Deze worden gekort en omgezet in een char
     * array. Daarna wordt er gekozen welke eigenschap er random gebruikt gaat
     * worden dan wordt er vervolgens in een for loop 2 andere eigenschappen
     * gepulled die vergeleken worden met elkaar, met de vraag preferentie, en
     * de overgebleven preferentie. De opties worden terug gegven als array.
     *
     * @return String array met unieke optie 2 en optie 3.
     */
    public String[] maakPref2() {
        String optie2 = "";
        String optie3 = "";
        String pref = dataUitSet(this.aminoPos, this.naarPos);
        boolean uniek = false;
        pref = pref.replaceAll(" ", "");
        char keuze1g, keuze2f;
        char[] prefoptie = pref.toCharArray();
        int randomkeuze = new Random().nextInt(1);
        if (randomkeuze == 1) {
            keuze1g = prefoptie[1];
            keuze2f = prefoptie[0];
        } else {
            keuze1g = prefoptie[0];
            keuze2f = prefoptie[1];
        }
        while (uniek == false) {
            optie2 = zurenafk[new Random().nextInt(zurenafk.length)];
            optie3 = zurenafk[new Random().nextInt(zurenafk.length)];
            if (optie2 != optie3) {
                if (optie2 != String.valueOf(keuze1g) && optie2 != String.valueOf(keuze2f)) {
                    if (optie3 != String.valueOf(keuze1g) && optie3 != String.valueOf(keuze2f)) {
                        this.goedKeuze = String.valueOf(keuze1g);
                        uniek = true;
                    }
                }
            }
        }
        return new String[]{optie2, optie2};
    }

    /**
     * De functie maakt de vragen die aminozuur preferentie gebruiken op 1 stuk
     * Deze wordt gemaakt door random elementen uit de globale array pakken.
     * Deze worden vergeleken met de gekozen array uit het bestand. Bij 2
     * preferenties, wordt gebruik gemaakt van de maakPref2 methode. het
     * resultaat daarvan wordt in optie 2 en 3 gezet. het goede antwoord wordt
     * opgeslagen, en alle opties worden doorgestuurt naar voegKeuzesToe met
     * shuffle mogelijkheid.
     */
    private void maakPref1() {
        String pref = dataUitSet(this.aminoPos, this.naarPos);
        String optie2 = "";
        String optie3 = "";
        boolean uniek = false;
        if (pref.length() == 1) {
            this.goedKeuze = pref;
            while (uniek == false) {
                optie2 = zurenafk[new Random().nextInt(zurenafk.length)];
                optie3 = zurenafk[new Random().nextInt(zurenafk.length)];
                if (pref != optie2 && pref != optie3 && optie2 != optie3) {
                    uniek = true;
                }
            }
        } else {
            String[] opties = maakPref2();
            optie2 = opties[0];
            optie3 = opties[1];
        }
        this.goedKeuze = prefString(this.goedKeuze);
        voegKeuzesToe(this.goedKeuze, prefString(optie2), prefString(optie3), true);
    }

    /**
     * De methode switched letters naar volledige woorden.
     *
     * @param letter
     * @return preffer, woord.
     */
    private String prefString(String letter) {
        String preffer = "";
        switch (letter) {
            case "H":
                preffer = "Helix";
                break;
            case "T":
                preffer = "Turn";
                break;
            case "S":
                preffer = "Strand";
                break;
            case "N":
                preffer = "Geen";
                break;
            case "+":
                preffer = "Positief";
                break;
            case "0":
                preffer = "Neutraal";
                break;
            case "-":
                preffer = "Negatief";
                break;
        }
        return preffer;
    }

    /**
     * De methode zet het goede antwoord in het geheugen en geeft de leesbare
     * optie mee aan voegKeuzeToe
     *
     * @param optie1: String met optie
     * @param optie2: String met optie
     * @param optie3: String met optie
     */
    private void maakBlok2(String optie1, String optie2, String optie3) {
        this.goedKeuze = dataUitSet(this.aminoPos, this.naarPos);
        voegKeuzesToe(optie1, optie2, optie3, false);

    }

    /**
     * De methode zet de opties bij alRadkeuzes en shuffeld de antwoorden aan
     * de hand van de shuffle boolean.
     * @param vK1: Optie 1
     * @param vK2: Optie 2
     * @param vK3: Optie 3
     * @param vKS : Shuffle boolean, bij true, dan wordt er geshuffeld.
     */
    private void voegKeuzesToe(String vK1, String vK2, String vK3, boolean vKS){
        this.alRadkeuzes.add(vK1);
        this.alRadkeuzes.add(vK2);
        this.alRadkeuzes.add(vK3);
        if(vKS == true){
            Collections.shuffle(alRadkeuzes);
        }
    }

    /**
     * De methode schrijft de vraagzin voor de gebruiker. Dit wordt gedaan met
     * vraagzin en de data uit dataUitSet. Bij 1 speciaal geval moet de waarde
     * geconverteerd worden. Dit wordt gedaan als speciaal op true staat.
     */
    private void maakVraag() {
        this.Vraagzin = dataUitSet(20, this.vraagPos);
        this.VraagWoord = dataUitSet(this.aminoPos, this.vanPos);
        if (speciaal == true) {
            this.VraagWoord = prefString(dataUitSet(this.aminoPos, this.vanPos));
        }
        this.Vraagzin = this.Vraagzin.replace("@@", VraagWoord);
    }

    /**
     * De methode pakt het goede antwoord en maakt 2 foute antwoorden aan via
     * een while loop. De keuzes worden net zolang vergeleken totdat ze uniek
     * zijn. Als laatste wordt alle data doorgestuurt aan voegKeuzesToe met
     * de shuffle boolean.
     */
    private void maakKeuzes1() {
        int keuze1 = 0;
        int keuze2 = 0;
        Random rand = new Random();
        boolean uniek = false;
        while (uniek != true) {
            if (keuze1 != keuze2 && this.aminoPos != keuze1 && this.aminoPos != keuze2) {
                uniek = true;
            }
            keuze1 = rand.nextInt(20);
            keuze2 = rand.nextInt(20);
        }
        this.goedKeuze = dataUitSet(this.aminoPos, this.naarPos);
        voegKeuzesToe(this.goedKeuze, dataUitSet(keuze1, this.naarPos),
                dataUitSet(keuze2, this.naarPos), true);
    }

    /**
     * Methode geeft de opties terug in een array.
     *
     * @return Array met opties
     */
    public ArrayList getRadoptie() {
        return this.alRadkeuzes;
    }

    /**
     * Een van de belangrijkste methodes. Deze methode maakt het mogelijk om een
     * element uit de array te selecteren op basis van rij en kolom. Hiermee
     * kunnen vragen, antwoorden en opties uitgelezen worden.
     *
     * @param row
     * @param col
     * @return
     */
    private String dataUitSet(int row, int col) {
        ArrayList arrTemp = (ArrayList) this.alData.get(row);
        return (String) arrTemp.get(col);
    }

    /**
     * De methode maakt gebruik van Servlet, filereader en buffered reader om de
     * Aminozuren csv open te maken en in te laden waar alle data staat voor de
     * quiz. In een while loop wordt alle data uitgelezen en in een arraylist
     * geplaatst doormiddel van een ;. De totale output is een multiarray waar
     * dit object data uit kan halen.
     *
     * @throws FileNotFoundException
     * @throws IOException
     */
    private void readCSV() throws FileNotFoundException, IOException {
        final ServletContext ctx = ((WebApplication) getApplication()).getServletContext();
        String naam = "Aminozuren.csv";
        FileReader frBestand = new FileReader(new File(ctx.getRealPath(naam)));
        BufferedReader brAmino = new BufferedReader(frBestand);
        String sCurrentLine;
        while ((sCurrentLine = brAmino.readLine()) != null) {
            String[] splitdata = sCurrentLine.split(";");
            ArrayList Adata = new ArrayList();
            Adata.addAll(Arrays.asList(splitdata));
            this.alData.add(Adata);
        }
    }

    /**
     * Methode geeft de vraag terug in String.
     *
     * @return Vraagzin, string.
     */
    public String getVraagzin() {
        return this.Vraagzin;
    }

    /**
     * De methode geeft de keuze terug in string. De keuze is het antwoord wat
     * de gebruiker heeft opgegeven.
     *
     * @return this.keuze, string.
     */
    public String getKeuze() {
        return this.keuze;
    }

    /**
     * De methode zorgt voor de input van de gebruiker en zet deze in
     * this.Keuze.
     *
     * @param Keuze_invoer Keuze van de gebruiker.
     */
    public void setKeuze(String Keuze_invoer) {
        this.keuze = Keuze_invoer;
    }

    /**
     * De methode kijkt of de keuze van de gebruiker overeenkomt met het goede
     * antwoord. Als dit zo is, dan wordt er een 1 terug gegeven. Als de keuze
     * niet het goede antwoord is, dan wordt er een 0 teruggegeven.
     * 
     * @return punt, int.
     */
    public int getPunt() {
        int punt = 0;
        if (this.keuze.equals(this.goedKeuze)) {
            punt += 1;
        }
        return punt;
    }
}
