package com.myapp.wicket;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

/**
 * @author Sebastiaan De class zorgt voor het bijhouden van de naam, score, het
 * aantal vragen en alle vraag objecten. In dit object is ook de cijferopdracht
 * toegevoegd samen met Vraag.
 */
public class Data {
    private static String naam = "";
    private static int AntVragen = 0;
    private static int punten = 0;
    private static List<Vraag> listVragenobj;

    /**
     * Methode om de naam van de speler toe te voegen.
     *
     * @param newNaam: Naam van de speler
     */
    public static void setNaam(String newNaam) {
        naam = newNaam;
    }

    /**
     * Methode geeft naam van de speler terug.
     *
     * @return naam, String.
     */
    public static String getNaam() {
        return naam;
    }

    /**
     * Methode set aantal vragen om de quiz mee te spelen.
     *
     * @param vragen, int
     */
    public static void setAntVragen(int vragen) {
        AntVragen = vragen;
    }

    /**
     * De methode geeft het aantal vragen terug die de gebruiker wilt doen.
     *
     * @return AntVragen, integer.
     */
    public static int getAntVragen() {
        return AntVragen;
    }

    /**
     * De methode zet het aantal punten wat de gebruiker heeft gehaald voor de
     * quiz.
     * @param sPunt, integer.
     */
    public static void setPunten(int sPunt) {
        punten = sPunt;
    }

    /**
     * De methode geeft een string terug van de score van de gebruiker.
     *
     * @return String van punten.
     */
    public static String getPunten() {
        return String.valueOf(punten);
    }

    /**
     * Input: int size: groote deel van vragen
     * Bijvoorbeeld: Aantal vragen = 20 = 2x 7 = 14 + 6
     * Daarvan moet je een van de grotere nemen. 
     *
     * Vervolgens wordt de vragenlijst gemaakt waar alle string
     * waardes inkomen
     *
     * In de for loop wordt er geloopt door het aantal vragen.
     * Daarna wordt de stop bool aangemaakt die gebruikt wordt voor de while
     * loop die erachter aankomt.
     * Die loopt net zolang door dat stop false is.
     * In de loop wordt de bool nieuw aangemaakt. Die is later nodig om 
     * te bepalen of een vraag uniek is.
     *
     * Als eerste wordt in de while loop de functie RandomMaker aangeroepen
     * waar de teller en size wordt meegegeven.
     * Daarna wordt alles van de int array omgezet naar strings en in
     * 1 string gemerged. Die wordt meegegeven samen met de vragenlijst aan
     * de methode CheckUnqiue. De boolean waarde van de methode wordt
     * gegeven aan nieuw. In de if statement wordt gecheked of nieuw true is, dan
     * wordt er in de if statement de vraag in de vragenlijst gestopt en wordt
     * de while loop gestopt. De for loop eindigt met een volledige, unieke
     * vragenlijst.
     * Deze wordt teruggegeven.
     * @param size: Integer van grootte vragen array.
     * @param klein: Kleinste aantal vragen. Integer.
     * @return een unieke vragen array.
     */
    private static String[] vragenGenerator(int size, int klein) {
        String[] arrVragenlijst = new String[2 * size + klein];
        for (int i = 0; i < 2 * size + klein; i++) {
            boolean stop = false;
            while (stop != true) {
                boolean nieuw = true;
                int[] types = randomMaker(i, size);
                String type1 = Integer.toString(types[0]);
                String type2 = Integer.toString(types[1]);
                String AA = Integer.toString(types[2]);
                String totaal = type1 + "-" + type2 + "-" + AA;
                nieuw = checkUniek(arrVragenlijst, totaal);
                if (nieuw == true) {
                    arrVragenlijst[i] = totaal;
                    stop = true;
                }
            }
        }
        return arrVragenlijst;
    }

    /**
     * De methode  maakt een int array aan die wordt gevuld aan de hand van een 
     * if op positie en teller. Deze maakt een positielijst.
     * @param teller: Nummer van de vraag.
     * @param size: Grootte van vraag secties.
     * @return int array voor posities.
     */
    private static int[] positieBepaler(int teller, int size) {
        int[] arrPostlijst = {6, 3, 3, 0};
        if (teller < size) {
            arrPostlijst[0] = 3;
            arrPostlijst[1] = 0;
            arrPostlijst[2] = 3;
            arrPostlijst[3] = 0;
        } else if (teller < 2 * size) {
            arrPostlijst[0] = 3;
            arrPostlijst[1] = 0;
            arrPostlijst[2] = 7;
            arrPostlijst[3] = 3;
        }
        return arrPostlijst;
    }

    /**
     * int teller: De teller van de vraag
     * int size: Vraag segmenten
     * De functie maakt als eerste een int array aan van het resultaat
     * van Positiebepaler waar teller en size aan worden meegegeven.
     * Daarna wordt de RM array aangemaakt met 3 posities.
     * Als eerste wordt de array gevuld met een random nummer
     * Die wordt gebruikt om te vergelijken tussen de de waardes
     * van positie 0 en 1. Die mogen namelijk niet overeenkomend zijn.
     * Nadat dit gedaan is in de while loop, wordt de laatste random waarde
     * gemaakt. Dan wordt de vraag teruggegven.
     * @param teller: De teller van de vraag
     * @param size± Vraag segmenten
     * @return: Een random vraag.
     */
    private static int[] randomMaker(int teller, int size) {
        int[] arrRMW = positieBepaler(teller, size);
        int[] arrRMlijst = new int[3];
        Random rand = new Random();
        Arrays.fill(arrRMlijst, rand.nextInt(arrRMW[0] - arrRMW[1]) + arrRMW[1]);
        while (arrRMlijst[0] == arrRMlijst[1]) {
            arrRMlijst[1] = rand.nextInt(arrRMW[2] - arrRMW[3]) + arrRMW[3];
        }
        arrRMlijst[2] = rand.nextInt(20);
        return arrRMlijst;
    }

    /**
     * De functie kijkt of de vraag voorkomt in de vragenlijst.
     * Als dit zo is, dan wordt een false boolean teruggegeven,
     * anders wordt er true terug gegeven.
     * @param lijst: De vragenlijst.
     * @param vraag: Vraag die gemaakt is.
     * @return: Boolean. True als de vraag uniek is, anders false.
     */
    private static boolean checkUniek(String[] lijst, String vraag) {
        boolean uniek = true;
        for (String item : lijst) {
            if (vraag.equals(item)) {
                uniek = false;
            }
        }
        return uniek;
    }

    /**
     * De methode maakt gebruik van het aantal vragen en splitst deze op in drie
     * groepen. De splitsing wordt in groot en klein gedaan, want een getal wat
     * niet door 3 gedeelt kan worden, kan anders voor problemen zorgen. De
     * grootte van de groepen worden meegegeven aan QuestionGenerator. Deze
     * geeft een array terug die vervolgens in een for loop wordt uitgelezen en
     * daarvan een Vraag object wordt aangemaakt die wordt toegevoegd aan
     * vragenobj. De try en catch methode wordt gebruikt omdat er in de vraag
     * methode een file wordt ingelezen, maar deze is altijd aanwezig, dus is
     * het voldoende om de catch leeg te laten.
     */
    public static void maakVragen() {
        int MVaantal = AntVragen;
        int MVgroot = (int) Math.ceil(MVaantal / 3);
        int MVklein = MVaantal - 2 * MVgroot;
        String[] arrMVlijst = vragenGenerator(MVgroot, MVklein);
        listVragenobj = new ArrayList<Vraag>();
        for (int i = 0; i < arrMVlijst.length; i++) {
            try {
                listVragenobj.add(new Vraag(arrMVlijst[i]));
            } catch (IOException ex) {
                System.out.println(ex);
            }
        }
    }

    /**
     * De methode geeft de list terug die gebruikt met daarin vragen.
     * @return vragenobj, list met vragen.
     */
    public static List getVragenobj() {
        return listVragenobj;
    }
}
