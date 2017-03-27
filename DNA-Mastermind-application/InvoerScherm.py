#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 3-6-14 Invoerscherm maken.
Sebastiaan de Vriend 4-6-14 Methoden maken om gegevens te verzamelen.
Sebastiaan de Vriend 9-6-14 Documentatie toevoegen.
"""

# import modules
import wx

from KnoppenPaneel import KnoppenPaneel
from OpslaanPaneel import OpslaanPaneel
from SubPaneel import SubPaneel
from ZettenPaneel import ZettenPaneel


class InvoerFrame(wx.Frame):
    """
    Klasse maakt een frame met daarin een opslag module en de
    mogelijkheid om aantal zetten te bepalen voor DNA-Mind.
    Zie documentatie __init__ voor meer informatie.
    """
    def __init__(self, parent, butid, id=wx.ID_ANY, title="DNA-Mind",
                 pos=wx.DefaultPosition, size=(300, 450),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="InvoerScherm"):
        """
        Maakt en toont InvoerScherm. De __init__ methode heeft
        8 parameters nodig.
             parent
                De ouder van het paneel.
            butid
                Getal die gebruikt wordt om door te sturen naar
                KnoppenPaneel. Zie documentatie KnoppenPaneel
                voor meer informatie.
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
            name="InvoerScherm"
                Geeft windowname InvoerScherm mee.
        Als eerste wordt de frame aangemaakt. Vervolgens wordt er de
        hoofd paneel aangemaakt. Daarna worden de modules Opslaan,
        Knoppen en Zetten opgeroepen en worden ze in een horizontale
        boxsizer gezet. Als laatste wordt de frame zichtbaar gemaakt.
        """
        super(InvoerFrame, self).__init__(parent, id, title, pos,
                                          size, style, name)
        self.Paneel = SubPaneel(self)
        self.Opslaan = OpslaanPaneel(self.Paneel, id)
        self.Knoppen = KnoppenPaneel(self.Paneel, butid, id)
        self.Zetten = ZettenPaneel(self.Paneel, id)
        allbox = wx.BoxSizer(wx.VERTICAL)
        allbox.Add(self.Opslaan, 1, wx.ALL | wx.EXPAND)
        allbox.Add(self.Zetten, 1, wx.ALL | wx.EXPAND)
        allbox.Add(self.Knoppen, 1, wx.ALL | wx.EXPAND)
        self.Paneel.SetSizer(allbox)
        self.Show()

    def GetInvulgegevens(self):
        """
        Methode haalt een lijst op van Opslaan.GetTxt(). Hiervan komt
        een lijst terug. Deze wordt append met Zetten.GetZetten().
        de a lijst wordt returnt
        """
        a = self.Opslaan.GetTxt()
        a.append(self.Zetten.GetZetten())
        if a[1] == 1 and len(a[0]) == 0:
            self.Opslaan.SetWaarschuwing()
            a.append(False)
        else:
            a.append(True)
        return a
