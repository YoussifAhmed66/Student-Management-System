class Entity:
    """
    This is the parent class of all entity classes and it's only purpose to pass the connection object to it's child classes
    to avoid the redundancy in the constructor of each class
    """

    db = None
