#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 3-6-14 Knoppen paneel Maken
Sebastiaan de Vriend 9-6-14 Documentatie schrijven
Sebastiaan de Vriend 10-6-14 Paneel verwijderen, documentatie aanpassen.
"""

# import modules
import sys
import wx


class KnoppenPaneel(wx.Panel):
    """
    De klasse maakt een Paneel aan met daarop twee knoppen. Zie __init__
    documentatie voor meer informatie.
    """
    def __init__(self, parent, BUTID, id=wx.ID_ANY, label="Doorgaan",
                 size=wx.DefaultSize):
        """
        De methode maakt een paneel met daarop twee knoppen met
        daartussen 1 paneel. De methode heeft 5 parameters.
            parent
                De ouder van het paneel.
            BUTID
                De id voor de knop die verschillende labels kan hebben.
            id=wx.ID_ANY
                id voor stop knop. Als deze niet wordt opgegeven zal er
                een id aangemaakt worden door wx.
            label="Doorgaan"
                Label voor de knop die een gespecificeerde id nodig
                heeft. Als er geen label wordt meegegeven wordt het
                standaard label gebruikt.
            size=wx.DefaultSize)
                formaat voor de paneel. Als deze niet wordt meegegeven
                wordt het standaard formaat gebruikt van wx.
        De methode heeft een Bind die gebruik maakt van de volgende
        methode:
            Stoppen(event)
        Als eerste wordt er een paneel aangemaakt met de naam
        self.KnoppenPaneeltje. Daarna wordt er een knop gemaakt
        die BUTID en label gebruikt van de init. Vervolgens wordt er
        een stop button aangemaakt en deze wordt ook gebind. Zie
        documentatie Stoppen() voor meer informatie.
        De knoppen worden toegevoegd aan een HORIZONTAL boxsizer.
        """
        self.KnoppenPaneeltje = wx.Panel.__init__(self, parent, id, size=size)
        self.DoorgaanKnopje = wx.Button(self, BUTID, label)
        self.StopKnopje = wx.Button(self, id, "stop")
        self.Bind(wx.EVT_BUTTON, self.Stoppen, self.StopKnopje)
        bbox = wx.BoxSizer(wx.HORIZONTAL)
        bbox.Add(self.DoorgaanKnopje, 1, wx.EXPAND | wx.ALL)
        bbox.Add(self.StopKnopje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(bbox)

    def Stoppen(self, event):
        """ sys.exit wordt aangeroepen om programma af te sluiten """
        sys.exit()
