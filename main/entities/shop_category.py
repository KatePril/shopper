class ShopCategory:
    def __init__(self, name, description, shop_category_id=None):
        if shop_category_id is not None:
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
        shop_category = {
            'shop_category_id': self.shop_category_id,
            'name': self.name,
            'description': self.description
        }
        if self.shop_category_id is not None:
            shop_category['shop_category_id'] = self.shop_category_id
        return shop_category

    def __eq__(self, other):
        if not isinstance(other, ShopCategory):
            return NotImplemented
        return (
            self.shop_category_id == other.shop_category_id and
            self.name == other.name and
            self.description == other.description
        )