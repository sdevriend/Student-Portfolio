"""
Sebastiaan de Vriend 4-6-14 Gamescherm maken.
"""

import wx

from AntwoordPaneel import AntwoordPaneel
from KnoppenPaneel import KnoppenPaneel
from SpeelPaneel import SpeelPaneel
from SubPaneel import SubPaneel
from TekstPaneel import TekstPaneel


class SpeelFrame(wx.Frame):
    """
    Klasse maakt speel frame aan. Deze bevat meerdere modules. Zie
    documentatie __init__ voor meer informatie.
    """
    def __init__(self, parent, butid, butid2, id=wx.ID_ANY, title="DNA-Mind",
                 pos=wx.DefaultPosition, size=(1300, 600),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="SpeelScherm", lengte=4, ):
        """
        De methode maakt en toont speelscherm. De __init__ heeft 10
        paremeters:
            parent
                De ouder van het paneel.
            butid
                Int voor opnieuw knop in knoppenPaneel
            butid2
                int voor raden knop in speelpaneel
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
            size=(1300, 600)
                Formaat van de frame. Als deze niet meegegeven is zal er
                voor een standaard grote van 450 x 300 gekozen worden.
            style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU )
                Zorgt voor een default frame style zonder resize,
                sluit knop en systeem menu.
            name="SpeelScherm"
                Geeft de windowsname  SpeelScherm mee.
            lengte=4
                De lengte van de gekozen DNA keten.
        Methode maakt als eerste een frame aan met daarin parent, id,
        title, pos, size, style en naam. Vervolgens wordt er een hoofd
        paneel aangemaakt met de naam self.Paneel. Daarna wordt de
        knoppen paneel aangemaakt in self.Knoppen. hieraan wordt
        self.Paneel, butid, id, label en size meegegeven. De label is
        nodig omdat er anders "Doorgaan" komt te staan.
        Vervolgens wordt self.Tekst aangemaakt, een TekstPaneel waaraan
        standaard waardes worden meegegeven op ttype na. Hiermee wordt
        aangegeven dat de speelschermuitleg er moet komen te staan.
        Daarna wordt self.Spelen aangemaakt. Dit is het speel paneel.
        Hieraan wordt butid2 meegegeven voor de raad knop en lengte,
        voor de lengte van de dna keten.
        Als laatste wordt het self.Antwoorden module aangeroepen.
        Hieraan worden de standaard waarden meegegven samen met lengte.
        Nadat alle modules aangeroepen zijn, worden deze in boxen
        geplaatst. self.Tekst en self.Knoppen komen in vbox, een
        VERTICAL BoxSizer te staan. vbox wordt daarna toegevoegt aan
        hbox samen met self.Spelen en self.Antwoorden. hbox is een
        HORIZONTAL BoxSizer. Daarna wordt self.Paneel aangepast op de
        size van hbox en als laatste wordt de frame getoont.
        """
        super(SpeelFrame, self).__init__(parent, id, title, pos,
                                         size, style, name)
        self.Paneel = SubPaneel(self)
        self.Knoppen = KnoppenPaneel(self.Paneel, butid, id, label="Opnieuw",
                                     size=(260, 150))
        self.Tekst = TekstPaneel(self.Paneel, id, size=(260, 450), ttype=2)
        self.Spelen = SpeelPaneel(self.Paneel, butid2, id, lengte)
        self.Antwoorden = AntwoordPaneel(self.Paneel, lengte, id)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.Tekst, 1, wx.ALL | wx.EXPAND)
        vbox.Add(self.Knoppen, 1, wx.ALL | wx.EXPAND)
        hbox.Add(vbox, 1, wx.ALL | wx.EXPAND)
        hbox.Add(self.Spelen, 1, wx.ALL | wx.EXPAND)
        hbox.Add(self.Antwoorden, 1, wx.ALL | wx.EXPAND)
        self.Paneel.SetSizer(hbox)
        self.Show()

    def GetDNA(self):
        """Methode roept functie GetDNALijst() aan en returnt deze."""
        return self.Spelen.GetDNALijst()

    def SetSpeelScherm(self, score, antw):
        """
        Methode roept self.Spelen.ResetPaneel() aan en
        self.Antwoorden.SetUpdatePanelen(score, antw)
        score en antw zijn lijsten.
        """
        self.Spelen.ResetPaneel()
        self.Antwoorden.SetUpdatePanelen(score, antw)

    def VeranderStrand(self, knopid):
        """Methode roept methode aan en geeft een int mee."""
        self.Spelen.VeranderStrand(knopid)

    def SetWaarschuwing(self):
        """Methode roept methode aan. """
        self.Spelen.SetWaarschuwing()
