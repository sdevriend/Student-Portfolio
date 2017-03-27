"""
Sebastiaan de Vriend 3-6-14 Welkomsbericht schrijven
Sebastiaan de Vriend 4-6-14 Veranderen naar universeel tekstpaneel.
Sebastiaan de Vriend 9-6-14 Toevoegen documentatie.
Sebastiaan de Vriend 14-6-14 Aanpassen tekst voor ttype 2
Sebastiaan de Vriend 15-6-14 Fucntie schrijven voor tekst ttype 2
"""

# import modules
import wx


class TekstPaneel(wx.Panel):
    """Klasse maakt een paneel aan met daarop tekst."""
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize, ttype=1):
        """
        Maakt een paneel met daarop tekst. Deze wordt bepaald door
        de parameter ttype. De __init__ methode bevat de volgende
        4 parameters
            parent
                De ouder van het paneel.
            id=wx.ID_ANY
                id voor frame. Als er geen id aanwezig is, dan zal
                deze aangemaakt worden met de library van wx python.
            size=wx.DefaultSize
                Size van Paneel. Als er geen waarde is meegegeven zal
                de standaard waarde van wx python gebruikt worden.
            ttype=1
                Parameter om de tekst van het paneel te bepalen. 1 staat
                voor beginscherm en 2 staat voor gamescherm.
        Methode roept volgende functie(s) aan:
            schermtype()
        Maakt als eerste een paneel aan. Vervolgens een boxsizer.
        Daarna komt de static tekst waarin de functie schermtype()
        wordt aangeroepen. Deze geeft een tupple terug. Zie documentatie
        schermentype() voor meer informatie.
        Daarna wordt er met font, de grootte en lettertype aangepast.
        Deze wordt toegepast op de tekst en wordt als laatste in de
        boxsizer geplaatst.
        """
        WelkomsPaneel = wx.Panel.__init__(self, parent, id, size=size,
                                          style=wx.BORDER_SUNKEN)
        self.ttype = ttype
        box = wx.BoxSizer()
        tekst = wx.StaticText(self, id, "".join(self.schermtype()))
        if ttype == 1:
            fsize = 18
        else:
            fsize = 12
        font = wx.Font(fsize, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        tekst.SetFont(font)
        box.Add(tekst, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)

    def schermtype(self):
        """
        methode returns een tupple aan de hand van een if op self.ttype.
        """
        if self.ttype == 1:
            return ("Welkom bij DNA-mind. Het doel is het correct raden van",
                    " de complementaire DNA-strand.\nEen DNA-strand bestaat",
                    " uit basen met de volgende codes: \n",
                    "\t A; T; C; G; R en Y")
        elif self.ttype == 2:
            return self.schermtekst()

    def schermtekst(self):
        """ Methode returnt een tupple met tekst. """
        return ("In het midden van het scherm staan gekleurde knoppen. Deze ",
                "knoppen staan voor de letters A; T; C; G; R en Y. Zoals je ",
                "kan zien hebben alle knoppen een letter en een kleur:\n\tA:",
                ": Rood\n\tT: Geel\n\tC: Lichtblauw\n\tG: Donderblauw\n\tR: ",
                "Wit\n\tY: Zwart\nRechts op het scherm zijn de gegeven ",
                "antwoorden te vinden. Samen met het aantal kansen en je ",
                "score.\nDe zwarte vakjes betekenen dat een letter op de ",
                "juiste positie staat met de juiste kleur en een wit vakje ",
                "betekend dat een kleur goed is, maar nog niet op de juiste ",
                "plek staat\nOnderaan het scherm staan vakjes die je kan ",
                "kleuren door op de knopjes te drukken. Nadat alles gekleurd",
                " is kan je op raden drukken om te kijken of je alles goed ",
                "hebt.\nVeel succes!")
