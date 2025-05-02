class Customer:
    def __init__(self, first_name, last_name, email, phone_number, password, salt, customer_id=None):
        if customer_id is not None:
            self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.salt = salt

    @classmethod
    def from_dict(cls, customer_dict):
        return cls(
            customer_dict['first_name'],
            customer_dict['last_name'],
            customer_dict['email'],
            customer_dict['phone_number'],
            customer_dict['password'],
            customer_dict['salt'],
            customer_dict['customer_id']
        )

    def to_dict(self):
        customer = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'phone_number': self.phone_number,
                'password': self.password,
                'salt': self.salt
            }
        if self.customer_id is not None:
            customer['customer_id'] = self.customer_id
        return customer


    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented
        return (
            self.customer_id == other.customer_id and
            self.first_name == other.first_name and
            self.last_name == other.last_name and
            self.email == other.email and
            self.phone_number == other.phone_number and
            self.password == other.password and
            self.salt == other.salt
        )