class Product:
    def __init__(self, name, description, price, quantity, shop_id, product_id=None):
        if product_id is not None:
            self._product_id = product_id
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity
        self._shop_id = shop_id

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
        product = {
            'product_id': self._product_id,
            'name': self._name,
            'description': self._description,
            'price': self._price,
            'quantity': self._quantity,
            'shop_id': self._shop_id
        }
        if self._product_id is not None:
            product['product_id'] = self._product_id
        return product

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (
            self._product_id == other.product_id and
            self._name == other.name and
            self._description == other.description and
            self._price == other.price and
            self._quantity == other.quantity and
            self._shop_id == other.shop_id
        )