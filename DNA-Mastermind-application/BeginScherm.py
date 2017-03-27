#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 03-06-14 Frame opzetten.
Sebastiaan de Vriend 4-6-14 Welkomsbericht aanpassen naar Tekstpaneel.
Sebastiaan de Vriend 9-6-14 Documentatie toevoegen
"""

# import modules
import wx

from KnoppenPaneel import KnoppenPaneel
from SubPaneel import SubPaneel
from TekstPaneel import TekstPaneel


class BeginFrame(wx.Frame):
    """
    De klassa maakt een frame met daarin een boodschap en heeft twee
    knoppen. Zie documentatie __init__ voor meer informatie.
    """
    def __init__(self, parent, butid, id=wx.ID_ANY, title="DNA-Mind",
                 pos=wx.DefaultPosition, size=(450, 300),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="BeginScherm"):
        """
        Maakt en toont de Beginscherm voor DNA-Mind. De __init__
        methode heeft 8 parameters:
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
            name="BeginScherm"
                Geeft windowname BeginScherm mee.
        De methode maakt gebruik van de volgende modules:
            SubPaneel(self)
            KnoppenPaneel(self.Paneel, butid, id)
            TekstPaneel(self.Paneel, id, size=(450, 250), ttype=1)
            Zie documentatie SubPaneel, KnoppenPaneel en TekstPaneel
            voor meer informatie.
        Als eerste maakt methode een frame aan. Vervolgens maakt de
        methode  een Paneel aan en geeft deze door aan KnoppenPaneel en
        TekstPaneel om zo twee subschermen te maken.
        Deze worden op elkaar gestapeld in een vertical boxsizer met de
        parameter naam allbox. Paneel wordt gesized op allbox en als
        laatste wordt de frame getoont.
        """
        super(BeginFrame, self).__init__(parent, id, title, pos,
                                         size, style, name)
        self.Paneel = SubPaneel(self)
        self.Knoppen = KnoppenPaneel(self.Paneel, butid, id)
        self.Welkom = TekstPaneel(self.Paneel, id, size=(450, 250), ttype=1)
        allbox = wx.BoxSizer(wx.VERTICAL)
        allbox.Add(self.Welkom, 1, wx.ALL | wx.EXPAND)
        allbox.Add(self.Knoppen, 1, wx.ALL | wx.EXPAND)
        self.Paneel.SetSizer(allbox)
        self.Show()
