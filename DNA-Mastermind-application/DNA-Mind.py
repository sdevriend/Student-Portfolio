#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 13-6-14 Maken van applicatie scherm.
Sebastiaan de Vriend 15-6-14 Maken documentatie.
"""

import wx

from BeginScherm import BeginFrame
from EindScherm import EindFrame
from GameEngine import GameEngine
from InvoerScherm import InvoerFrame
from SpeelScherm import SpeelFrame


class DNAMind(wx.App):
    """
    Klasse roept de modules op die nodig zijn voor DNA-Mind. Ook zorgt
    de Klasse ervoor dat de frames op de juiste manier getoont worden
    en de juiste informatie naar elkaar toe sturen.
    """
    def OnInit(self):
        """
        Bij het opstarten  wordt de self.SchermTeller op 0 gezet zodat
        deze begint bij het juiste frame.
        Ook worden er 2 knopID's aangemaakt. Deze zijn voor de 2 knoppen
        die voor scherm routering zorgt.
        Daarna worden de 4 frames in een lijst gezet en wordt de functie
        self.SchermBeheer() gestart om het juiste scherm te tonen.
        Daarna wordt er een bind aangezet zodat er gerouteerd kan worden
        tussen schermen.
        De functie keert een True terug voor wx.
        """
        self.SchermTeller = 0
        self.KnopID1 = wx.NewId()
        self.KnopID2 = wx.NewId()
        self.SchermLijst = [BeginFrame, InvoerFrame, SpeelFrame, EindFrame]
        self.SchermBeheer()
        self.Bind(wx.EVT_BUTTON, self.KnopHandeling)
        return True

    def SchermBeheer(self):
        """
        Methode maakt frames aan door te kijken naar self.SchermTeller.
        Als deze < 2 is dan wordt er BeginFrame of InvoerFrame gestart
        met de waarde van self.KnopID1.
        Als deze == 2 is dan wordt het SpeelFrame gestart.
        Hieraan worden 2 knopid's meegegeven en de lengte van de DNA
        keten.
        Als het niet < 2 of == 2 is. Dan wordt het EindFrame getoont.
        Daaraan wordt KnopID1 meegegeven en de lijst self.Endinfo.
        """
        if self.SchermTeller < 2:
            self.frame = self.SchermLijst[self.SchermTeller](None,
                                                             self.KnopID1)
        elif self.SchermTeller == 2:
            self.frame = self.SchermLijst[2](None, self.KnopID1, self.KnopID2,
                                             lengte=self.gegevens[2])
        else:
            self.frame = self.SchermLijst[3](None, self.KnopID1, self.Endinfo)

    def KnopHandeling(self, event):
        """
            Methode pakt GetId om te kijken welke knop er is gebruikt.
            Als de knop dezelfde ID heeft als self.KnopID1, dan wordt de
            methode Knop1Beheer() gestart. Zie documentatie Knop1Beheer
            voor meer informatie.
            Als de event hetzelfde ID heeft als self.KnopID2, dan wordt
            de functie Knop2Beheer gestart. Zie documentatie Knop2Beheer
            voor meer informatie.
        """
        event_id = event.GetId()
        if event_id == self.KnopID1:
            self.Knop1Beheer()  # Opnieuw knop of doorgaan knop.
        if event_id == self.KnopID2:
            self.Knop2Beheer()  # Raad knop.
        else:
            if self.SchermTeller == 2:
                self.frame.VeranderStrand(event_id)

    def Knop1Beheer(self):
        """
            Functie checkt de nummer van de SchermTeller. Als deze 0
            is zal de funtie SchermWissel gestart worden.
            Als deze 1 is zal er een lijst opgehaald worden van
            self.frame. Als positie 3 een True bevat zal de gameconfig
            gemaakt worden en de functie schermwissel gestart worden.
            Als de teller 2 is of hoger dan wordt de schermteller op 1
            gezet zodat deze in de schermwissel functie naar 2 gaat voor
            het scherm te wisselen naar speelscherm. Ook wordt de
            RemakeGame functie aangeroepen van GCONFIG om een nieuwe
            keten te maken. Als laatste wordt SchermWissel opgeroepen.
        """
        if self.SchermTeller == 0:
            self.SchermWissel()
        elif self.SchermTeller == 1:
            self.gegevens = self.frame.GetInvulgegevens()
            if self.gegevens[3]:
                self.GCONFIG = GameEngine(self.gegevens[0], self.gegevens[2])
                self.SchermWissel()
        elif self.SchermTeller >= 2:
            self.SchermTeller = 1
            self.GCONFIG.RemakeGame()
            self.SchermWissel()

    def Knop2Beheer(self):
        """
        Functie haalt het antwoord van de gebruiker op uit de methode
        self.frame.GetDNA(). Als deze geen "X" bevat dan heeft de
        gebruiker alles ingevuld. Als antw daar niet aan voldoet wordt
        de methode self.frame.SetWaarschuwing() gedaann.
        Als de gebruiker wel alles heeft ingevuld, dan wordt ant
        doorgestuurt naar self.GCONFIG.BeurtCheck(antw).
        Dan wordt er gekeken of de gebruiker nog Kansen heeft en of
        de gebruiker al gewonnen heeft. Als dit zo is, dan wordt er
        spelinformatie opgehaald van self.GCONFIG.GetTotaalPakket() en
        wordt deze in de globale variabel self.Endinfo gezet. Daarna
        wordt schermwissel gebruikt. Als de gebruiker nog verder moet,
        dan wordt de methode self.frame.SetSpeelScherm() gestart.
        Hieraan worden de score en eerdere antwoorden aan meegegeven.
        """
        antw = self.frame.GetDNA()
        if "X" not in antw:
            self.GCONFIG.BeurtCheck(antw)
            if self.GCONFIG.GetKansen() == 0 or self.GCONFIG.GetGewonnen():
                self.Endinfo = self.GCONFIG.GetTotaalPakket()
                self.SchermWissel()
            else:
                self.frame.SetSpeelScherm(self.GCONFIG.GetScore(),
                                          self.GCONFIG.GetAntwlijst())
        else:
            self.frame.SetWaarschuwing()

    def SchermWissel(self):
        """
        Methode vernietigt de huidige frame, zet de teller 1 omhoog
        en roept self.SchermBeheer() aan om de volgende scherm te tonen.
        """
        self.frame.Destroy()
        self.SchermTeller += 1
        self.SchermBeheer()

app = DNAMind(False)
app.MainLoop()
