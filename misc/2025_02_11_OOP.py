from testing_ground import loadr

class MobilePhone:

    has_touchscreen = True



    def __init__(self, brand, model):

        self.brand = brand

        self.model = model



    def os(self):

        if self.brand == "Apple":

            print ("iOS")
            import time
            time.sleep(3)

        else:

            print ("Android")



Jim_phone = MobilePhone("Apple", "iPhone 15")

Aisha_phone = MobilePhone("Samsung", "Galaxy S22")



print (Jim_phone.brand)

MobilePhone.os(Jim_phone)

print (Aisha_phone.brand)

MobilePhone.os(Aisha_phone)
