package com.myapp.wicket;

import org.apache.wicket.ajax.AbstractAjaxTimerBehavior;
import org.apache.wicket.ajax.AjaxRequestTarget;
import org.apache.wicket.markup.html.WebPage;
import org.apache.wicket.util.time.Duration;

/**
 * @author Sebastiaan de Vriend
 * De class toon het welkomsscherm voor 5 seconden en schakelt dan door naar
 * Introductiescherm.class.
 */
public final class Welkomstscherm extends WebPage {
    /**
     * De class voegd aan ajaxtimer toe die 5 seconden loopt. Vervolgens wordt
     * er in de overgeschreven methode overgeschakeld naar 
     * het Introductiescherm.
     */
    public Welkomstscherm() {
        super();
        add(new AbstractAjaxTimerBehavior(Duration.seconds(5)) {
            @Override
            protected void onTimer(AjaxRequestTarget target) {
                setResponsePage(Introductiescherm.class);
            }
        });
    }
}
