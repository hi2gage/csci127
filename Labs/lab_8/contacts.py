class Contacts:
    def __init__(self,name,number,relationship):
        self.name = name
        self.number = number
        self.relationship =relationship

    def get_name(self):
        return self.name

def main():
    friend_1 = Contacts("gage", "503-349-0332", "friend")
    friend_2 = Contacts("cam", "503-", "friend")

    print(friend_1.name)
    print(friend_2.get_name())



main()
