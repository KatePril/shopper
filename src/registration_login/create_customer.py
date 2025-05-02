from src.entities.customer import Customer

INSERTION_QUERY = """
    INSERT INTO customer(first_name, last_name, email, phone_number, password)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING customer_id
"""

def create_customer(customer: Customer, cursor, conn):
    cursor.execute(
        INSERTION_QUERY,
        (
            customer.first_name,
            customer.last_name,
            customer.email,
            customer.phone_number,
            customer.password
        )
    )
    customer_id = cursor.fetchone()[0]
    conn.commit()
    return customer_id