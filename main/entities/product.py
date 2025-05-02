class Product:
    def __init__(self, product_id, name, description, price, quantity, shop_id):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.shop_id = shop_id

    @classmethod
    def from_dict(cls, product_dict):
        return cls(
            product_dict['product_id'],
            product_dict['name'],
            product_dict['description'],
            product_dict['price'],
            product_dict['quantity'],
            product_dict['shop_id']
        )

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'shop_id': self.shop_id
        }

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (
            self.product_id == other.product_id and
            self.name == other.name and
            self.description == other.description and
            self.price == other.price and
            self.quantity == other.quantity and
            self.shop_id == other.shop_id
        )