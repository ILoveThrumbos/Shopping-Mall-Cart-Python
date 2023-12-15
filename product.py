class Product:
    """
    The Product class is a product with attributes such as barcode, name, desc and price
    """

    def __init__(self, barcode, name, desc, price):
        """
        Initialises a new instance of the Product Class.

        Includes attributes:
        barcode: The barcode of the product
        name: The name of the product
        desc: The description of the product
        price: The price of the product
        """
        self.barcode = barcode
        self.name = name
        self.desc = desc
        self.price = float(price)


    """
    getters that retrieve the barcode, description, price, and name of the product. 
    Also, returns the barcode, description, price and name of the product.
    """
    def get_barcode(self):
        return self.barcode

    def get_desc(self):
        return self.desc

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name