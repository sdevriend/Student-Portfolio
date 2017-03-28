package com.myapp.wicket;

import org.apache.wicket.AttributeModifier;
import org.apache.wicket.markup.html.WebPage;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.form.Button;
import org.apache.wicket.markup.html.form.Form;

/**
 *
 * @author Sebastiaan De class maakt twee labels en een form die navigeerd naar
 * de quiz.
 */
public final class Scorescherm extends WebPage {
    private Button btnStop;
    private Button btnOpnieuw;
    private Form formNav;
    /**
     * De methode maakt de label aan voor de naam en de score, vervolgens worden
     * er twee knoppen aangemakt en toegevoegd aan het formulier formNav. De
     * buttons hebben een eigen submit methode die de gebruiker terugstuurt naar
     * het welkomstscherm. Daarnaast bevat de stopknop een code snippet om het
     * scherm te sluiten.
     */
    public Scorescherm() {
        super();
        add(new Label("Naam", "Beste " + Data.getNaam()));
        add(new Label("Score",  Data.getPunten()));
        btnOpnieuw = new Button("btnOpnieuw") {
            @Override
            public void onSubmit() {
                setResponsePage(Welkomstscherm.class);
            }
        };
        btnStop = new Button("btnStop");
        btnStop.add(AttributeModifier.append("onclick", "open(location, '_self')"
                + ".close();return false;"));
        formNav = new Form("formNav");
        formNav.add(btnOpnieuw);
        formNav.add(btnStop);
        add(formNav);
    }
}
