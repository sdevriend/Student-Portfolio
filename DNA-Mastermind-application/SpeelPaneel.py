#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 4-6-14 SpeelPaneel maken.
Sebastiaan de Vriend 14-6-14 Documentatie + functies toevoegen.
"""

import wx

from SubPaneel import SubPaneel


class SpeelPaneel(wx.Panel):
    """Klasse maakt speelpaneel. Zie __init__ voor meer documentatie."""
    def __init__(self, parent, BUTID2, id, knopaantal):
        """
        Methode maakt speelpaneel. De __init__  heeft 4 paramters.
            parent
                De ouder van het paneel.
            BUTID2
                int voor id raadknop
            id
                int voor id
            knopaantal
                De lengte van de gekozen DNA keten.
        De methode roept de volgende methodes op:
            self.createIDs()
            self.PaneelLijst()
            self.MaakKnoppen()
        Methode maakt als eerste een paneel aan. Vervolgens wordt
        knopaantal global gemaakt. Daarna wordt de raadknop gemaakt.
        Vervolgens wordt een lijst gemaakt met knopaantal x "X". Daarna
        worden de 3 methodes opgeroepen en wordt er een waarschuwing
        gemaakt die wordt verborgen. Als laatste worden de onderdelen
        van het speelpaneel in een VERTICAL BoxSizer geplaatst en de
        self.SetSizer wordt op TotaalBox aangepast.
        """
        wx.Panel.__init__(self, parent, id, size=(650, 600),
                          style=wx.BORDER_SUNKEN)
        self.knopaantal = knopaantal
        self.Raden = wx.Button(self, BUTID2, "Raden")
        self.DNALijst = list(knopaantal*"X")
        self.createIDs()
        self.PaneelLijst()
        knoppen = self.MaakKnoppen()
        self.Waarschuwing = wx.StaticText(self, id, "Niet alles is ingevuld!")
        self.Waarschuwing.Hide()
        TotaalBox = wx.BoxSizer(wx.VERTICAL)
        TotaalBox.Add(knoppen, 9, wx.ALL | wx.EXPAND)
        TotaalBox.Add(self.Raden, 1, wx.ALL | wx.EXPAND)
        TotaalBox.Add(self.Waarschuwing, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(TotaalBox)

    def MaakKnoppen(self):
        """
        Methode maakt de knoppen voor speelpaneel. Als eerste wordt er
        een HORIZONTAL BoxSizer met de naam knoppenbox gemaakt.
        Daarna wordt er een loop gestart.
            In de eerste loop wordt er een Vertical Boxsizer gemaakt.
            Daarna wordt er meteen een 2e loop gestart.
                y wordt een knop met self, id van lijst, kleur van lijst
                en size. Daarna wordt de background bepaald op positie
                van x. Als de kleur van de knop zwart of blauw is, dan
                wordt de letterkleur wit. Dit is voor duidelijkheid.
                De y knop wordt vervolgens aan de tijdelijke BoxSizer
                toegevoegd.
            Na de 2e loop wordt er aan de tijdelijke BoxSizer een paneel
            toegevoegt. Vervolgens wordt de BoxSizer toegevoegt aan
            KnoppenBox
        returns:
            Knoppenbox
                HORIZONTAL BoxSizer met knoppen en panelen.
        """

        Knoppenbox = wx.BoxSizer(wx.HORIZONTAL)
        for z in self.ButtonInfo:
            buttonlist = wx.BoxSizer(wx.VERTICAL)
            for x in z[1]:
                y = wx.Button(self, x[2], x[1], size=(5, 10))
                y.SetBackgroundColour(x[0])
                if x[0] == 'black' or x[0] == 'blue':
                    y.SetForegroundColour("White")
                buttonlist.Add(y, 1, wx.ALL | wx.EXPAND)
            buttonlist.Add(self.Minipanelen[z[0]], 1, wx.ALL |
                           wx.EXPAND)
            Knoppenbox.Add(buttonlist, 1, wx.ALL | wx.EXPAND)
        return Knoppenbox

    def createIDs(self):
        """
        Methode maakt een globale lijst voor knop id's. Door een for
        loop in de range van self.knopaantal kan het juiste aantal
        id's aangemaakt worden voor de knoppen.
        In de for loop wordt een tijdelijke lijst gemaakt met daarin
        de waarde van x, en een lijst in een lijst. In de lijst staan
        de kleuren, label en de id voor de nieuwe knoppen.
        De tijdelijke lijst wordt elke keer aan het einde aan de global
        lijst toegevoegt.
        """
        self.ButtonInfo = []
        for x in range(self.knopaantal):
            temp = []
            temp.append(x)
            temp.append([['red', 'A', wx.NewId()],
                         ['yellow', 'T', wx.NewId()],
                         ['sky blue', 'G', wx.NewId()],
                         ['blue', 'C', wx.NewId()],
                         ['white', 'R', wx.NewId()],
                         ['black', 'Y', wx.NewId()]])
            self.ButtonInfo.append(temp)

    def VeranderStrand(self, knop):
        """
        Methode loopt alle knoppen na door 2 loops.
        Als een knop overeenkomt met de invoer knop, dan wordt er een
        global lijst gemaakt met daarin het nummer van x, en de letter
        van y[1]. Ook wordt het minipaneel van de lijst
        self.Minipanelenlijst op positie x[0], de achtergrondkleur
        veranderd naar de kleur van y[0]. Als laatste wordt de functie
        self.Lijstbijhouden() gebruikt.
        """
        knopID = knop

        for x in self.ButtonInfo:
            for y in x[1]:
                if knopID == y[2]:
                    self.mutatie = [x[0], y[1]]
                    self.Minipanelen[x[0]].SetBackgroundColour(y[0])
                    self.Minipanelen[x[0]].Refresh()
                    self.Lijsbijhoudem()

    def Lijsbijhoudem(self):
        """
        Methode past self.DNALijst lijst aan op positie van
        self.mutatie[0] naar de letter van self.mutatie[1]
        """
        self.DNALijst[self.mutatie[0]] = self.mutatie[1]

    def GetDNALijst(self):
        """returns self.DNALijst, een lijst met letters."""
        return self.DNALijst

    def PaneelLijst(self):
        """
        Functie maakt subpanelen aan in een for loop. Het aantal
        panelen = self.knopaantal. De background van elke paneel
        is standaard grijs voor zichtbaarheid en wodt in de globale
        lijst self.Minipanelen gezet.
        """
        self.Minipanelen = []
        for x in range(self.knopaantal):
            z = SubPaneel(self, style=wx.BORDER_SUNKEN)
            z.SetBackgroundColour("grey")
            self.Minipanelen.append(z)

    def ResetPaneel(self):
        """
            Methode reset de DNALijst naar begin waarde van __init__ en
            veranderd voor elke paneel in de self.Minipanelen list naar
            grijs zodat de gebruikt een visueel beeld heeft dat de raad
            keten is gereset.
        """
        self.DNALijst = list(self.knopaantal*"X")
        for x in self.Minipanelen:
            x.SetBackgroundColour("grey")
            x.Refresh()
        self.Waarschuwing.Hide()
        self.Layout()

    def SetWaarschuwing(self):
        """
        De methode toont self.waarschuwing in het textpaneel en
        veranderd de backgroundkleur naar rood. Als laaste wordt de
        layout functie aangegroepen om de waarschuwing op de juiste plek
        te zetten.
        """
        self.Waarschuwing.Show()
        self.Waarschuwing.SetBackgroundColour("red")
        self.Layout()
