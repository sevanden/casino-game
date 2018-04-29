# coding=utf-8


class Asset:
    """
        Base class for all products available for purchase in the game.
    """
    def __init__(self, name, description, value, image):
        """
        :param name:            A unique name for this asset.
        :param description:     A description for this asset.
        :param value:           The value of this asset when purchased.
        :param image:           An image representing the asset.
        """
        self.name = name
        self.description = description
        self.value = value
        self.image = image


class Property(Asset):
    """
        Base class for properties (land/buildings/business/vehicle/...) available for purchase in the game.
    """
    def __init__(self, name, description, value, image, rentable=True, rent=0):
        """
        :param name:            A unique name for this property.
        :param description:     A description for this property.
        :param value:           The value of this property when purchased.
        :param image:           An image representing the property.
        :param rentable:        True if this property can be rented.
        :param rent:            The rent value for this property if :param rentable is True.
        """
        super().__init__(name=name, description=description, value=value, image=image)
        self.rentable = rentable
        self.rent = rent


class Building(Property):
    """
        Base class for buildings available for purchase in the game.
    """
    def __init__(self, name, description, value, image, rentable, rent):
        """
        :param name:            A unique name for this building.
        :param description:     A description for this building.
        :param value:           The value of this building when purchased.
        :param image:           An image representing the building.
        :param rentable:        True if this building can be rented.
        :param rent:            The rent value for this building if :param rentable is True.
        """
        super().__init__(name=name, description=description, value=value, image=image, rentable=rentable, rent=rent)


class House(Building):
    """
        A class for all kinds of houses available for purchase in the game.
    """
    def __init__(self, name, description, value, image, rentable, rent):
        """
        :param name:            A unique name for this house.
        :param description:     A description for this house.
        :param value:           The value of this house when purchased.
        :param image:           An image representing the house.
        :param rentable:        True if this house can be rented.
        :param rent:            The rent value for this house if :param rentable is True.
        """
        super().__init__(name=name, description=description, value=value, image=image, rentable=rentable, rent=rent)


#class Vehicle(Asset):
#    def __init__(self, name, description, value, image):
#        super().__init__(name=name, description=description, value=value, image=image)

#class Car(Vehicle):
#    def __init__(self, name, description, value, image):
#        super().__init__(name=name, description=description, value=value, image=image)

#class Business(Asset):
#    def __init__(self, name, description, value, image):
#        super().__init__(name=name, description=description, value=value, image=image)

#class Restuarant(Business):
#    def __init__(self, name, description, value, image):
#        super().__init__(name=name, description=description, value=value, image=image)
