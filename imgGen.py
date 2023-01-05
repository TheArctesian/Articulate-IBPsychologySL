import json
import html2image


class Card:
    def __init__(self, Cog, Abnor, Socul, Bio, EMT, ERQ):
        self.Cognitive = Cog
        self.Biological = Bio
        self.SocioCultural = Socul
        self.Abnormal = Abnor
        self.EMT = EMT
        self.ERQ = ERQ

    def dict(self):
        return {
            "Cogn": self.Cognitive,
            "Bio": self.Biological,
            "Soc": self.SocioCultural,
            "Abn": self.Abnormal,
            "EMT": self.EMT,
            "ERQ": self.ERQ,
        }


def imgGen(card):
    html=f"<h1>Psychology Articulate</h1><br>"
    image = html2image.screenshot()


if __name__ == "__main__":
    with open("cards.json") as JF:
        cards = json.load(JF)
        print(cards[0]["ERQ"])
