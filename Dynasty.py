
class Dynasty:
    def __init__(self,name):
        self._name=name # House name, for.ex."Martell"
        self.characters=[] # Family members ("Doran Martell","Ellaria Sand","Nymeria Sand",...)


    @property
    def name(self): # getter for the private instance attribute _name
        return self._name
       

    @name.setter
    def name(self, value):
        self._name = value
      

    def append(self, ch): # to append character to the House (during reading data from JSON-file)
        if type(ch) == str:
            self.characters.append(ch)
        else: 
            raise TypeError("Character must be a string")
        #this code will check if character is an instance
        #of the String class. If not, an exception will be raised


    def __iter__(self): # to loop threw the list of characters via IN operator (for ex. for person in house: ....)
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.characters):
            raise StopIteration
        value = self.characters[self.index]
        self.index += 1
        return value

    def __contains__(self, ch): # to check if the character belongs to the house (for ex., if person in house ...)
        if ch in self.characters:
            return True
        else: 
            return False
        # return True or False


    def __str__(self): # to print like print(house) - > display the house's name
        str = "This is House " + self._name + "!"
        return str
    
    def getStrength(self): # return N of family members in this house (int)
        strength = len(self.characters)
        return strength