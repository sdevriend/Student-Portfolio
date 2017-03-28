package com.myapp.wicket;

import com.googlecode.wicket.jquery.ui.form.spinner.Spinner;
import org.apache.wicket.markup.html.WebPage;
import org.apache.wicket.markup.html.form.Form;
import org.apache.wicket.markup.html.form.TextField;
import org.apache.wicket.model.Model;

/**
 *
 * @author Sebastiaan
 * De class werkt op WebPage en maakt een Introductiescherm aan met daarin een
 * textfield en spinner. Als de gebruiker het Introductiescherm gecontroleerd, en
 * wordt de quiz gestart als de juiste gegevens zijn ingevuld.
 */
public final class Introductiescherm extends WebPage {
    private Form formData;
    private TextField tfNaam;
    private Spinner<Integer> spinVragen;
    /**
     *De methode maakt een textfield en een spinner. Bij de spinner wordt
     * een minimin en een maximum samen met een default value meegegeven.
     * Vervolgens wordt MaakForm aangeroepen om het formulier aan te maken.
     */
    public Introductiescherm() {
        super();
        tfNaam = new TextField("tfNaam", new Model(""));
        spinVragen = new Spinner("spinVragen", new Model(""), Integer.class);
        spinVragen.setMin(20);
        spinVragen.setMax(100);
        spinVragen.setStep(5);
        spinVragen.setModelObject(20);
        maakForm();
    }

    /**
     *De methode maakt een form aan en overschrijft de onSubmit methode.
     * In de onsubmit wordt worden de waardes van de textbox en de spinner
     * uit de modellen gehaald en in de variabelen vraag en naam gezet. 
     * Bij de naam wordt er gekeken of deze kleiner is dan 3. Als dit zo is,
     * dan wordt Introductiescherm opnieuw aangeroepen, anders wordt het dataobject
     * geupdate met naam en vraag en wordt vervolgens de quiz gestart.
     * 
     * Aan het Introductiescherm wordt de naam textfield en de spinner toegevoegd.
     * Ook wordt het Introductiescherm toegeveogd aan het wicket framework.
     */
    public void maakForm() {
        formData = new Form("formData") {
            @Override
            protected void onSubmit() {
                String naam = (String) tfNaam.getModelObject();
                int vraag = spinVragen.getModelObject();
                if (naam.isEmpty() || naam.length() < 2) {
                    setResponsePage(new Introductiescherm());
                } else {
                    Data.setNaam(naam);
                    Data.setAntVragen(vraag);
                    setResponsePage(VraagEnAntwoordscherm.class);
                }
            }
        };
        add(formData);
        formData.add(tfNaam);
        formData.add(spinVragen);
    }
}
