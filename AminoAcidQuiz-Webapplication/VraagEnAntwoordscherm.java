package com.myapp.wicket;

import java.util.ArrayList;
import java.util.List;
import org.apache.wicket.AttributeModifier;
import org.apache.wicket.ajax.AjaxRequestTarget;
import org.apache.wicket.ajax.form.AjaxFormChoiceComponentUpdatingBehavior;
import org.apache.wicket.markup.html.WebPage;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.form.Button;
import org.apache.wicket.markup.html.form.Form;
import org.apache.wicket.markup.html.form.RadioChoice;
import org.apache.wicket.markup.html.navigation.paging.PagingNavigator;
import org.apache.wicket.markup.repeater.Item;
import org.apache.wicket.markup.repeater.data.DataView;
import org.apache.wicket.markup.repeater.data.ListDataProvider;
import org.apache.wicket.model.Model;

/**
 * @author Sebastiaan
 * De class maakt de quiz backend. Er wordt gebruikt gemaakt van een array
 * list met vraag objecten die doorgegeven wordt aan een dataview die
 * veranderingen bijhoudt. De cijferopdracht is verwerkt in de class
 * Data en Vraag.
 */
public final class VraagEnAntwoordscherm extends WebPage {
    private Button btnHerlaad;
    private Button btnScore;
    private Button btnStop;
    private List<Vraag> lstVragen;
    private Form formNav;

    /**
     * De constructor maakt een label aan met de data van Data.getNaam en add
     * deze vervolgens aan wicket. Vervolgens worden de functies MaakVragen,
     * MaakKnoppen en toonVragen aangeroepen.
     */
    public VraagEnAntwoordscherm() {
        super();
        add(new Label("Naam", Data.getNaam()));
        maakVragen();
        maakKnoppen();
        toonVragen();
    }

    /**
     * De methode roept eerst de methode Data.maakVragen aan,en maakt daarna de
     * arraylist aan. Deze arraylist wordt gevuld met de vragen van
     * Data.getVragenobj.
     */
    public void maakVragen() {
        Data.maakVragen();
        lstVragen = new ArrayList<Vraag>();
        lstVragen = Data.getVragenobj();
    }

    /**
     * De methode declareerd als eerste de boolean leeg die op false staat, deze
     * wordt gebruikt om te kijken of alles nog leeg is. In de for loop wordt er
     * voor alle objecten van vragenobj geloopt en wordt getKeuze aangeroepen om
     * te kijken of er een String terugkomt met alleen "". Als dit zo is, dan is
     * nog niet alles ingevuld en wordt leeg op true gezet.
     *
     * Na de loop wordt gekeken of leeg false is, als dit zo is, dan wordt de
     * methode calcPunten opgeroepen.
     */
    private void checkVragen() {
        boolean leeg = false;
        for (Vraag vr : lstVragen) {
            if (vr.getKeuze() == "") {
                leeg = true;
            }
        }
        if (leeg == false) {
            calcPunten();
        }
    }

    /**
     * de Methode gebruit de int punten om de punten op te tellen. In een for
     * loop worden den punten van vragenobj opgetelt door de methode getPunt.
     * Als laatste wordt er een redirect ingesteld naar Scorescherm.class.
     */
    private void calcPunten() {
        int punten = 0;
        Data.setPunten(punten);
        for(Vraag vr : lstVragen) {
            punten = punten + vr.getPunt();
        }
        Data.setPunten(punten);
        setResponsePage(Scorescherm.class);
    }

    /**
     * De methode maakt gebruik van een DataView waar vragenobj aan wordt
     * meegegeven. In dataview wordt populateItem overschreven.
     *
     * In de overschrijving wordt er per vraag een Radiochoice aangemaakt met de
     * waardes van Vraag.getRadoptie. aan de RadioChoice wordt een Ajax methode
     * toegevoegd die kijkt naar veranderingen in de radiochoice. Daarin wordt
     * de methode onUpdate overschreven.
     *
     * In de methode onUpdate wordt de methode vraag.Setkeuze aangeroepen van
     * het item, en wordt de waarde van de radiochoice meegegeven. daarna wordt
     * de methode checkAlles aangeroepen.
     *
     * Ook wordt er aan de radiochoice een modelobject value gegeven om de keuze
     * van de gebruiker te onthouden. Als laatste wordt er in dataview de vraag
     * toegevoegd als label en wordt de radiochoice toegevoegd aan de dataview.
     *
     *
     * de Dataview wordt vervolgens toegevoegd aan wicket met 1 item per page,
     * en daaraan wordt een paging navigation toegevoegd.
     */
    public void toonVragen() {
        DataView<Vraag> dvVragen = new DataView<Vraag>("dvVragen",
                new ListDataProvider(lstVragen)) {
                    @Override
                    protected void populateItem(Item item) {
                        List lstROPTIE = ((Vraag) item.getModelObject())
                            .getRadoptie();
                        RadioChoice<String> rcItem = new RadioChoice<>
                            ("vraagKeuzes", new Model(""), lstROPTIE);
                        rcItem.add(new AjaxFormChoiceComponentUpdatingBehavior(){
                            @Override
                            protected void onUpdate(AjaxRequestTarget target){
                                ((Vraag) item.getModelObject()).
                                    setKeuze(getComponent()
                                    .getDefaultModelObjectAsString());
                                checkVragen();
                            }
                        });
                        rcItem.setModelObject(((Vraag) item.getModelObject())
                                .getKeuze());
                        item.add(rcItem);
                        item.add(new Label("toonVraag", ((Vraag) 
                            item.getModelObject()).getVraagzin()));
                        rcItem.setSuffix("</span>");
                        rcItem.setPrefix("<span>");
                    }
                };
        dvVragen.setItemsPerPage(1);
        add(dvVragen);
        add(new PagingNavigator("PaginNav", dvVragen));
    }

    /**
     * De methode maakt een formulier en 3 knoppen aan. De herlaad knop wordt
     * overschreven naar een nieuwe redirect naar VraagEnAntwoordscherm. 
     * De andere 2 knoppen worden geschreven om de functie calcPunten aan te 
     * roepen en de pagina af te sluiten. De knoppen
     * worden vervolgens toegevoegd aan een formulier om onSubmit methodes
     * makkelijker af te handelen. Als laatste wordt het formulier toegevoegd
     * aan wicket.
     */
    public void maakKnoppen() {
        btnHerlaad = new Button("btnHerlaad", new Model("")) {
            @Override
            public void onSubmit() {
                setResponsePage(new VraagEnAntwoordscherm());
            }
        };
        btnScore = new Button("btnScore", new Model("")) {
            @Override
            public void onSubmit() {
                calcPunten();
            }
        };
        btnStop = new Button("btnStop", new Model(""));
        btnStop.add(AttributeModifier.append("onclick", "open(location, '_self')"
                + ".close();return false;"));
        formNav = new Form("formNav", new Model(""));
        formNav.add(btnHerlaad);
        formNav.add(btnScore);
        formNav.add(btnStop);
        add(formNav);
    }
}
