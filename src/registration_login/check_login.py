SELECT_BY_EMAIL_QUERY = """
    SELECT customer_id, password
    FROM customer
    WHERE email = %s
"""

def check_login(email, password, cursor):
    cursor.execute(SELECT_BY_EMAIL_QUERY, (email,))
    fetched_data = cursor.fetchone()

    if fetched_data:
        if password == fetched_data[1]:
            return fetched_data[0]
    else:
        return None