#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sebastiaan de Vriend 03-06-14 Maken class om subpanelen te maken.
Sebastiaan de Vriend 9-6-14 Documentatie toevoegen
"""

# import modules
import wx


class SubPaneel(wx.Panel):
    """Klasse maakt een subpaneel. Zie init voor documentatie."""
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize,
                 style=wx.BORDER_DEFAULT):
        """
        Maakt een paneel. Heeft de volgende parameters.
            parent
                Ouder van het paneel
            id
                id voor frame. Als er geen id aanwezig is, dan zal
                deze aangemaakt worden met de library van wx python.
            size=wx.DefaultSize
                Size van Paneel. Als er geen waarde is meegegeven zal
                de standaard waarde van wx python gebruikt worden.
            style=wx.BORDER_DEFAULT
                Style voor de paneel. Als er geen waarde is meegegeven
                dan zal de standaard style van wx gebruikt worden.
        """
        super(SubPaneel, self).__init__(parent, id, size=size, style=style)
