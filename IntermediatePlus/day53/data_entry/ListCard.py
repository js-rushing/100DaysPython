class ListCard:
    def __init__(self, card):
        self.card = card
        self.price = self.card.find(class_="list-card-price").get_text()
        self.address = self.card.find(class_="list-card-addr").get_text()
        self.link = self.get_link()

    def get_link(self):
        link = self.card.find(class_="list-card-link")['href']
        if link.split("/")[1] == 'b':
            link = f"https://www.zillow.com{link}"
        return link
