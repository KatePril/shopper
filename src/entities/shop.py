class Shop:
    def __init__(self, name, description, email, phone_number, category_id, shop_id):
        if shop_id is not None:
            self.shop_id = shop_id
        self.name = name
        self.description = description
        self.email = email
        self.phone_number = phone_number
        self.category_id = category_id

    @classmethod
    def from_dict(cls, shop_dict):
        return cls(
            shop_dict['shop_id'],
            shop_dict['name'],
            shop_dict['description'],
            shop_dict['email'],
            shop_dict['phone_number'],
            shop_dict['category_id']
        )

    def to_dict(self):
        shop = {
            'name': self.name,
            'description': self.description,
            'email': self.email,
            'phone_number': self.phone_number,
            'category_id': self.category_id
        }
        if self.shop_id is not None:
            shop['shop_id'] = self.shop_id
        return shop

    def __eq__(self, other):
        if not isinstance(other, Shop):
            return NotImplemented
        return (
            self.shop_id == other.shop_id and
            self.name == other.name and
            self.description == other.description and
            self.email == other.email and
            self.phone_number == other.phone_number and
            self.category_id == other.category_id
        )