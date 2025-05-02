class ShopCategory:
    def __init__(self, shop_category_id, name, description):
        self.shop_category_id = shop_category_id
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, shop_category_dict):
        return cls(
            shop_category_dict['shop_category_id'],
            shop_category_dict['name'],
            shop_category_dict['description']
        )

    def to_dict(self):
        return {
            'shop_category_id': self.shop_category_id,
            'name': self.name,
            'description': self.description
        }

    def __eq__(self, other):
        if not isinstance(other, ShopCategory):
            return NotImplemented
        return (
            self.shop_category_id == other.shop_category_id and
            self.name == other.name and
            self.description == other.description
        )