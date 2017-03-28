/**
 * Application.java
 *
 * Created on May 23, 2015, 4:28 PM
 *
 */
package com.myapp.wicket;

import org.apache.wicket.protocol.http.WebApplication;

/**
 *
 * @author Sebastiaan de Vriend
 * @version 1.0 De class zorgt voor afhandeling van de applicatie.
 */
public class Application extends WebApplication {

    /**
     * Constructor.
     */
    public Application() {
    }

    /**
     * De class geeft de beginpagina terug.
     *
     * @return Welkomstscherm, het eerste scherm.
     */
    @Override
    public Class getHomePage() {
        return Welkomstscherm.class;
    }

}
