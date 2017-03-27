#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 3-6-14 Maken Opslaan module.
Sebastiaan de Vriend 4-6-14 Get Methode maken.
Sebastiaan de Vriend 10-6-14 Documentatie + waarschuwing tekst toevoegen
"""

import wx

from SubPaneel import SubPaneel


class OpslaanPaneel(wx.Panel):
    """
    Klasse maakt een module die gebruikt kan worden om de gebruiker
    te vragen om een bestand op te slaan. Ook heeft de module een
    get() methode om een bestandsnaam op te halen en een set()
    methode om een waarschuwing aan te zetten.
    """
    def __init__(self, parent, id):
        """
        Maakt opslaan paneel met daarop een radiobox, txtctrl en text.
        De __init__ methode heeft 2 parameters.
            parent
                De ouder van het paneel
            id
                De id voor het paneel en het maken van widgets.
        De init roept de volgende methodes aan:
            TextPaneel()
            RadioPaneel()
        De methode maakt als eerste een paneel aan waar alles op komt.
        Vervolgens wordt er een vertical boxsizer aangemaakt die
        de TextPaneel() en RadioPaneel() methodes toevoegt.
        Als laatste wordt de SetSizer correct gezet voor self.
        """
        wx.Panel.__init__(self, parent, id, size=(300, 180),
                          style=wx.BORDER_SUNKEN)
        self.id = id
        totaal = wx.BoxSizer(wx.VERTICAL)
        totaal.Add(self.TextPaneel(), 1, wx.EXPAND | wx.ALL)
        totaal.Add(self.RadioPaneel(), 1, wx.EXPAND | wx.ALL)
        self.SetSizer(totaal)

    def TextPaneel(self):
        """
        Methode maakt een paneel aan. Daarop wordt vervolgens een
        statictext opgezet samen met een statictext met daarop een
        waarschuwing die op .Hide() staat. De font voor de waarschuwing
        wordt aangepast naar 16, bold. De static text boxen worden
        in een VERTICAL BoxSizer gezet. Deze wordt ook gereturnt.
        returns
            box
                VERTICAL boxsizer
        """
        box = wx.BoxSizer(wx.VERTICAL)
        self.TekstPaneel = SubPaneel(self)
        info = ("Bij DNA-Mind is het mogelijk om je zetten op te slaan",
                " Selecteer voor de optie opslaan en vul vervolgens de",
                " gewenste bestandsnaam in. Let wel op dat het bestand",
                "wordt overschreven!")
        self.tekst = wx.StaticText(self, self.id, "".join(info))
        self.Waarschuwing = wx.StaticText(self, self.id,
                                          "Niet alles is ingevuld!")
        waarschuwingfont = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.Waarschuwing.SetFont(waarschuwingfont)
        box.Add(self.Waarschuwing, 0.5, wx.EXPAND | wx.ALL)
        box.Add(self.tekst, 1, wx.EXPAND | wx.ALL)
        self.Waarschuwing.Hide()
        return box

    def RadioPaneel(self):
        """
        Methode maakt een paneel aan met daarop een radiobox die
        een bind krijgt. naar de methode RadioClick(). Ook wordt er
        een TextCtrl aangemaakt met de naam self.naam. Deze wordt
        standaard op Hide() gezet. Zie documentatie Radioclick()
        en GetTxt voor de informatie van self.naam.
        Als laatste worden de radiobox en textctrl in een VERTICAL
        boxsizer geplaatst.
        returns
            rbox
                Vertical boxsizer met daarin radiobox en txtctrl
        """
        self.RadioIndex = 0
        self.Radiolist = ["Niet opslaan", "Opslaan"]
        self.Radiobox = wx.RadioBox(self, self.id, choices=self.Radiolist,
                                    style=wx.RA_SPECIFY_ROWS)
        self.Bind(wx.EVT_RADIOBOX, self.Radioclick, self.Radiobox)
        self.naam = wx.TextCtrl(self, self.id,  size=(290, 20), name="vakje")
        rbox = wx.BoxSizer(wx.VERTICAL)
        rbox.Add(self.Radiobox, 1, wx.EXPAND | wx.ALL)
        rbox.Add(self.naam)
        self.naam.Hide()
        return rbox

    def Radioclick(self, event):
        """
        Methode handelt events af. Heeft 1 paramter
            event
                wx python waarde
        Methode pakt de radiobox object van de event funtie.
        Deze wordt vervolgens gebruikt om de waarde van de radiobox te
        checken. Als self.RadioIndex 0 is dan zal self.naam onzichtbaar
        gemaakt worden. Als self.RadioIndex een 1 is zal self.naam
        zichtbaar gemaakt worden. Als laatste wordt self.Layout()
        aangeroepen om de self.naam op de normale positie zichtbaar te
        maken. Dit voorkomt dat self.naam op het paneel zweeft.
        """
        RadioboxEv = event.GetEventObject()
        self.RadioIndex = RadioboxEv.GetSelection()
        if self.RadioIndex == 0:
            self.naam.Hide()
        elif self.RadioIndex == 1:
            self.naam.Show()
        self.Layout()

    def GetTxt(self):
        """
        Methode haalt waarde van self.naam + radiobox op en zet deze in
        de lijst totaal.
        returns
            totaal
                lijst
        """
        txt = self.naam.GetValue()
        totaal = [str(txt), self.RadioIndex]
        return totaal

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
