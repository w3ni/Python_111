class Mobile:
    # def show_model(self):
    #     print("Realme X")

    def __init__(self):
        self.model = "Real me Z"

    def show_model(self, p):
        self.price = p
        print("Mobile : ", self.model, "Price :", self.price)

realme = Mobile()
# realme.model = "Poco m2 pro"
realme.show_model(100000)

# --------------------------------------

