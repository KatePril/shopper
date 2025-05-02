class Customer:
    def __init__(self, first_name, last_name, email, phone_number, password, customer_id=None):
        if customer_id is not None:
            self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__password = password

    @classmethod
    def from_dict(cls, customer_dict):
        return cls(
            customer_dict['first_name'],
            customer_dict['last_name'],
            customer_dict['email'],
            customer_dict['phone_number'],
            customer_dict['password'],
            customer_dict['customer_id']
        )

    def to_dict(self):
        customer = {
                'first_name': self.__first_name,
                'last_name': self.__last_name,
                'email': self.__email,
                'phone_number': self.__phone_number,
                'password': self.__password
            }
        if self.__customer_id is not None:
            customer['customer_id'] = self.__customer_id
        return customer

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented
        return (
            self.__customer_id == other.customer_id and
            self.__first_name == other.first_name and
            self.__last_name == other.last_name and
            self.__email == other.email and
            self.__phone_number == other.phone_number and
            self.__password == other.password
        )