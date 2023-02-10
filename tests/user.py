import hashlib

class User(object):

    """A user who will use the dashboard and web application.
    Args:
        email (str): Email address, required
        password (str): Password, required
    Attributes:
        email (str): Email address
        hashed_pass (bytes): Hash value of the password string
    Methods:
        hash_pass: Create a hashed value of the string password
        is_correct_pass: Checks if the string password matches the hashed password
    """

    def __init__(self, email, username=""):
        self.email = email
        self.username = username
        self.hash_pass = "testpass"

    def __repr__(self):
        """ String representation of a user object """
        return '{}, {}, {}, {}'.format(self.email, self.username)

    @property
    def password_hash(self):
        """ Creates a hashed password from the string
        Args:
            password (str): Password in string format
        Returns:
            None
        """
        return self.hash_pass

    @password_hash.setter
    def password_hash(self, password):

        """ Creates a hashed password from the string
        The bcrypt.hashpw() function takes a byte encoded arg, the password string therefore needs to be encoded.
        Args:
            password (str): Password in string format
        Returns:
            None
        """

        self.hash_pass = hashlib.sha256(str.encode(password)).hexdigest()

    def check_password(self, password):
        
        """ Checks whether the provided password string matches the hashed password
        The bcrypt.checkpw() function takes byte encoded args, the password string needs to be encoded.
        Args:
            password (str): The string value of the password as input by the user
        Returns:
            bool : True if there is a match and False if not
        """

        password_hash = hashlib.sha256(str.encode(password)).hexdigest()
        return password_hash == self.hash_pass
