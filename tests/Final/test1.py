class Element:
# The first missing goes here but write it below
    def __str__(self):
        answer = self.name + " has atomic number " + str(self.atomic_number)
        if self.is_noble_gas():
            answer += " and is a noble gas."
        else:
            answer += "."
        return answer
# The second missing method goes here but write it below
    def __init__(self, atomic_number, name):
        self.name = name
        self.atomic_number = atomic_number


    def is_noble_gas(self):
        if self.name.lower() == ("helium" or "neon" or "argon" or "krypton"):
            return True
        else:
            return False


# -------------------------------------------------------
hydrogen = Element(1, "hydrogen")
print(hydrogen)
helium = Element(2, "helium")
print(helium)
