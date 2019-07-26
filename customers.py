"""Customers at Hackbright."""
# filepath = "customers.txt"

class Customer(object):
    """Ubermelon customer."""

    def __init__(self, firstname, lastname, email, password):
        """Initialize attributes."""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password


    def __repr__(self):
        """Represent object with first name, last name, and email."""
        return f"<Customer: {self.firstname} {self.lastname}, {self.email}>"

    
    


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {id: customer object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (firstname,
             lastname,
             email,
             password) = line.strip().split("|")
    
            customers[email] = Customer(firstname,
                                        lastname,
                                        email,
                                        password)

    return customers


def get_by_email(email, filepath):
    """Look up customer info based on `email`."""

    customers = read_customers_from_file(filepath)

    return customers[email]