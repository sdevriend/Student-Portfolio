#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 4-6-14 Aantal zetten slider maken
Sebastiaan de Vriend 10-6-14 Documentatie toevoegen.
"""

import wx


class ZettenPaneel(wx.Panel):
    """Klasse maakt een paneel met text en een slider."""
    def __init__(self, parent, id):
        """
        De methode maakt een paneel met daarop een slider en een
        statictext. De methode heeft 2 parameters.
            parent
                De ouder van het paneel.
            id
                Id voor het paneel.
        De methode maakt als eerste een paneel aan. Vervolgens wordt er
        een slider aangemaakt met de default setting op 4 in de range
        4 tot 10. De slider wordt toegevoegd aan de VERTICAL BoxSizer
        box. Vervolgens wordt er een static text gemaakt en aangepast
        met een groter lettertype. De tekst wordt als laatste toegevoegd
        aan box.
        """
        wx.Panel.__init__(self, parent, id, size=(300, 180),
                          style=wx.BORDER_SUNKEN)
        box = wx.BoxSizer(wx.VERTICAL)
        self.Slider = wx.Slider(self, id, 4, 4, 10,
                                style=wx.SL_AUTOTICKS | wx.SL_LABELS)
        box.Add(self.Slider, 1, wx.EXPAND | wx.ALL)
        info = ("Beweeg de schuifbalk naar het gewenste nummer voor de",
                " lengte van de te raden DNA keten. De standard lengte",
                " is 4 en kan maximaal op 10 gezet worden.")
        tekst = wx.StaticText(self, id, "".join(info))
        tekstfontje = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        tekst.SetFont(tekstfontje)
        box.Add(tekst, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

    def GetZetten(self):
        """Haalt de waarde op van self.Slider en returnt deze."""
        return self.Slider.GetValue()
