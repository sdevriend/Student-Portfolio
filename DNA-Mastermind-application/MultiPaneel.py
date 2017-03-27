#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 13-6-14 Maken scrollPaneel
Sebastiaan de Vriend 14-6-14 Documentatie toevoegen.
"""

import wx
import wx.lib.scrolledpanel as scrolledpanel

from SubPaneel import SubPaneel


class MultiPaneel(scrolledpanel.ScrolledPanel):
    """
    Klasse maakt speciale scroll paneel met daarop panelen. Zie
    documentatie __init__ voor meer informatie.
    """
    def __init__(self, parent, beurtaantal,
                 style=wx.TAB_TRAVERSAL | wx.BORDER_SUNKEN):
        """
        Methode maakt scroll paneel. De __init__ methode heeft 3
        parameters.
            parent
                De ouder van het paneel.
            beurtaantal
                integer tussen de 4-10 die gebruikt wordt om het
                aantal panelen te bepalen.
            style=wx.TAB_TRAVERSAL|wx.BORDER_SUNKEN
                Style voor het paneel
        De methode gebruikt de volgende methodes:
            self.MaakPanelen()
        Methode maakt als eerste het paneel aan. Vervolgens worden de
        parameters self.id, self.beurtaantal gemaakt. Vervolgens wordt
        de paramter self.panelenaantal gemaakt die de bijbehorende
        waarde uit de dictionary Paneelnr pakt. Vervolgens wordt de
        methode MaakPanelen() opgeroepen en als laatste wordt de layout
        goed gezet en wordt scrolling aangezet.
        """
        super(MultiPaneel, self).__init__(parent, style=style)
        self.id = wx.ID_ANY
        self.beurtaantal = beurtaantal
        Paneelnr = {4: 12, 5: 14, 6: 18, 7: 24, 8: 30, 9: 38, 10: 50}
        self.panelenaantal = Paneelnr[beurtaantal]
        self.MaakPanelen()
        self.SetAutoLayout(1)
        self.SetupScrolling()

    def MaakPanelen(self):
        """
        Methode maakt subpanelen. Als eerste wordt er een lijst
        gemaakt waar de objecten ingaan. Vervolgens wordt VBOX , een
        VERTICAL BoxSizer gemaakt.
        Dan wordt er een for loop gestart die tussen de 12 en 50x zal
        lopen.
        In deze loop wordt de tijdelijke HORIZONTAL BoxSizer, HBOX
        gemaakt. Deze zal een Temptekst bevatten. De Temptekst is een
        statictekst met daarin de waarde van x+1. Vervolgens wordt er
        een templijst gemaakt en een loop gemaakt die tussen de 4-10x
        zal lopen.
            In de 2e loop wordt er een SubPaneel aangemaakt. Deze
            subpaneel krijgt een grijze achtergrondkleur en wordt in
            de HBOX boxsizer + in de templijst geplaatst.
        Na de 2e loop wordt de HBOX toegevoegt aan VBOX en wordt de
        templijst toegevoegt aan self.PanelenLijst.
        Na de eerste loop wordt de self.SetSizer(VBOX) aangeroepen.
        """
        self.PanelenLijst = []
        VBOX = wx.BoxSizer(wx.VERTICAL)
        for x in range(self.panelenaantal):
            HBOX = wx.BoxSizer(wx.HORIZONTAL)
            TempTekst = wx.StaticText(self, self.id, str(x+1)+":")
            HBOX.Add(TempTekst, 1,  wx.EXPAND | wx.ALL)
            templijst = []
            for y in range(self.beurtaantal):
                z = SubPaneel(self, style=wx.BORDER_SUNKEN, size=(10, 10))
                z.SetBackgroundColour("grey")
                templijst.append(z)
                HBOX.Add(z, 1,  wx.EXPAND | wx.ALL)
            VBOX.Add(HBOX, 1,  wx.EXPAND | wx.ALL)
            self.PanelenLijst.append(templijst)
        self.SetSizer(VBOX)

    def ConvtKleuren(self, invoer):
        """
        Methode converteerd invoer naar een kleurenlijst. Als eerste
        wordt er een lege global lijst gemaakt met de naam
        self.kleurlijst.
        Daarna wordt er een loop gestart met de waarde van invoer
            In de eerste loop wordt er een templijst aangemaakt.
            Daarna wordt er een tweede loop gestart voor elke waarde
            in x.
                In deze loop wordt er via een try statement de
                bijbehorende waarde van KleurConv[y] toegevoegt aan
                de templijst.
            Na de 2e loop wordt de templijst toegevoegt aan de globale
            lijst self.kleurlijst
        """
        KleurConv = {"A": "red", "T": "yellow", "G": "sky blue", "C": "blue",
                     "R": "white", "Y": "black", "X": "black", "W": "white"}
        self.kleurlijst = []
        for x in invoer:
            tempkleurlijst = []
            for y in x:
                try:
                    tempkleurlijst.append(KleurConv[y])
                except KeyError:
                    pass
            self.kleurlijst.append(tempkleurlijst)

    def SetUpdatePanelen(self, lijst):
        """
        Methode converteerd als eerste de invoer met de methode
        self.ConvtKleuren(lijst). Daarna worden er 2 loops gestart.
        De eerste is voor range self.panelenaantal.
            Vervolgens wordt er in de eerste loop een 2e loop gestart
            in de range van self.beurtaantal. Hierdoor worden alle
            panelen nagelopen.
                In de 2e loop wordt de methode self.SetPaneeltje()
                aangeroepen. Deze staat onder een try: statement.
                De rede hiervoor is dat de invoer soms korter kan zijn
                (X/W panelen) dan de normale lengte.
        Aan het einde wordt de layout gerefreshed.
        """
        self.ConvtKleuren(lijst)
        for x in range(self.panelenaantal):
            for y in range(self.beurtaantal):
                try:
                    self.SetPaneeltje(x, y)
                except IndexError:
                    pass
        self.Refresh()

    def SetPaneeltje(self, p1, p2):
        """Functie veranderd kleur paneel met de kleur van kleurlijst"""
        self.PanelenLijst[p1][p2].SetBackgroundColour(self.kleurlijst[p1][p2])
