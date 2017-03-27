#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 15-6-2014 Maken eindscherm.
"""

import wx

from KnoppenPaneel import KnoppenPaneel
from SubPaneel import SubPaneel


class EindFrame(wx.Frame):
    """
    Klasse maakt en toont eindframe. Zie documentatie __init__ voor
    meer informatie.
    """
    def __init__(self, parent, butid, info, id=wx.ID_ANY, title="DNA-Mind",
                 pos=wx.DefaultPosition, size=(250, 400),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="EindScherm"):
        """
        Maakt en toont Eindframe. De __init__ methode heeft 9 paramters.
            parent
                De ouder van het paneel.
            butid
                Getal die gebruikt wordt om door te sturen naar
                KnoppenPaneel. Zie documentatie KnoppenPaneel
                voor meer informatie.
            info
                Lijst mer daarin informatie over de eindstand van
                DNA-Mind.
            id=wx.ID_ANY
                id voor frame. Als er geen id aanwezig is, dan zal
                deze aangemaakt worden met de library van wx python.
            title="DNA-Mind"
                Naam voor het scherm. Als er geen waarde aanwezig is
                zal de naam automatisch "DNA-Mind zijn.
            pos=wx.DefaultPosition
                Positie van de frame. Als er geen waarde aanwezig is
                zal er een standaard waarde gegenereerd worden door
                wx python.
            size=(450, 300)
                Formaat van de frame. Als deze niet meegegeven is zal er
                voor een standaard grote van 450 x 300 gekozen worden.
            style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU )
                Zorgt voor een default frame style zonder resize,
                sluit knop en systeem menu.
            name="EindScherm"
                Geeft windowname EindScherm mee.
        De methode maakt gebruik van de volgende modules:
            SubPaneel(self)
            KnoppenPaneel(self.Paneel, butid, id)
            Boodschap()
        Als eerste wordt de frame aangemaakt. Vervolgens wordt het
        paneel aangemaakt. Daarna wordt het knoppenpaneel aangeroepen.
        Als dat gedaan is wordt er een tekst gemaakt met de methode
        Boodschap(). Daarna worden de knoppenpaneel en text toegevoegt
        aan de VERTICAL BoxSizer Vbox. Als laatste wordt de size van de
        paneel goedgezet en wordt het frame getoont.
        """
        super(EindFrame, self).__init__(parent, id, title, pos,
                                        size, style, name)
        self.info = info
        self.Paneel = SubPaneel(self)
        self.Knoppen = KnoppenPaneel(self.Paneel, butid, id, label="Opnieuw")
        tekst = wx.StaticText(self.Paneel, id, "".join(self.Boodschap()))
        font = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        tekst.SetFont(font)
        Vbox = wx.BoxSizer(wx.VERTICAL)
        Vbox.Add(tekst, 1, wx.ALL | wx.EXPAND)
        Vbox.Add(self.Knoppen, 1, wx.ALL | wx.EXPAND)
        self.Paneel.SetSizer(Vbox)
        self.Show()

    def Boodschap(self):
        """
        Functie maakt een lijst door een if statement. uit te voeren op
        self.info op positie 0. Als deze True is, dan heeft de gebruiker
        gewonnen. Als laatste wordt er aan de lijst een algemeen stuk
        tekst toegevoegt. De functie geeft de t lijst terug.
        """
        if self.info[0]:
            t = ["Gefeliciteerd! Je hebt gewonnen! \nDe gemaakte keten van  ",
                 "de computer:\n\t", ";".join(self.info[1]), "\nDe geraden ",
                 "keten:\n\t", ";".join(self.info[2]), "\nBenodigde kansen",
                 ":\n\t", str(self.info[3])]
        else:
            t = ["Helaas! Je hebt verloren!\nDe gemaakte keten van de ",
                 "computer:\t", ";".join(self.info[1])]
        t.append("\nOm opnieuw te spelen druk je op de knop Opnieuw.")
        return t
