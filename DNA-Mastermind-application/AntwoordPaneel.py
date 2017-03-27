#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 5-6-14 Antwoord Paneel maken
Sebastiaan de Vriend 13-6-14 Multipaneel toevoegen
Sebastiaan de Vriend 14-6-14 Documentatie toevoegen
"""

import wx

from MultiPaneel import MultiPaneel


class AntwoordPaneel(wx.Panel):
    """Klasse maakt een paneel met daarop panelen. Zie __init__"""
    def __init__(self, parent, beurtaantal, id=wx.ID_ANY):
        """
        Methode maakt antwoordpaneel. De __init__ heeft 3 parameters
            parent
                De ouder van het paneel.
            beurtaantal
                De lengte van de DNA keten.
            id=wx.ID_ANY
                id voor frame. Als er geen id aanwezig is, dan zal
                deze aangemaakt worden met de library van wx python.
        Methode maakt als eerste een paneel aan.
        Vervolgens wordt beurtaantal global gemaakt. Daarna worden de
        static texten aangemaakt voor dit paneel vervolgt door het
        aanmaken van de scrollpanelen. Als laatste worden de texten en
        panelen toegevoegt aan een VERTICAL BoxSizer. Ook wordt de
        layout gerefreshed en de sizer gezet op de totaalbox.
        """
        self.AntwoordPaneeltje = wx.Panel.__init__(self, parent, id)
        self.beurtaantal = beurtaantal
        Raadtxt = wx.StaticText(self, id, "Score:")
        Antwtxt = wx.StaticText(self, id, "Eerder geven antwoorden:")
        self.XYPaneel = MultiPaneel(self, self.beurtaantal)
        self.AntwPan = MultiPaneel(self, self.beurtaantal)
        totaalbox = wx.BoxSizer(wx.VERTICAL)
        totaalbox.Add(Raadtxt)
        totaalbox.Add(self.XYPaneel, 2, wx.EXPAND)
        totaalbox.Add(Antwtxt)
        totaalbox.Add(self.AntwPan, 2,  wx.EXPAND | wx.ALL)
        self.SetAutoLayout(1)
        self.SetSizer(totaalbox)

    def SetUpdatePanelen(self, score, antw):
        """Methode stuurt invoer door naar juiste paneel."""
        self.XYPaneel.SetUpdatePanelen(score)
        self.AntwPan.SetUpdatePanelen(antw)
