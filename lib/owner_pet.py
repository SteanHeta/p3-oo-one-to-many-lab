class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        """Returns a list of all pets belonging to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Adds a pet to this owner with type validation"""
        if not isinstance(pet, Pet):
            raise Exception("Input must be a Pet instance")
        pet.owner = self
        
    def get_sorted_pets(self):
        """Returns a list of pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
    
    def __repr__(self):
        return f"<Owner name={self.name}>"


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  # This uses the property setter
        self.owner = owner        # This uses the property setter
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
        
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Pet type must be one of: {Pet.PET_TYPES}")
        self._pet_type = pet_type
        
    @property
    def owner(self):
        return self._owner
        
    @owner.setter
    def owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise TypeError("Owner must be an Owner instance")
        self._owner = owner
        
    def __repr__(self):
        return f"<Pet name={self.name}, type={self.pet_type}, owner={self.owner.name if self.owner else None}>"