class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        # returns a full list of the owner's pets.

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be Pet")
        pet.owner = self
        # checks that the the pet is of type Pet and adds the owner to the pet.
            
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
        # returns a sorted list of pets by their names. test

