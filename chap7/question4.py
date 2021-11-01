class FAN():
    def __init__(self):
        self.__my_attr_speed = 2
        self.__my_attr_on = "False"
        self.__my_attr_radius = 5
        self.__my_attr_color = "Blue"

    def set_my_attr_speed(self,speed,on,radius,color):
        self.__my_attr_speed = speed
        self.__my_attr_on = on
        self.__my_attr_radius = radius
        self.__my_attr_color = color

    def get_my_attr_speed(self):

        return str(self.__my_attr_speed) + "," + str(self.__my_attr_on) + "," + str(self.__my_attr_radius) + "," + str(self.__my_attr_color)

print("\n******* FAN CLass ******\n Speed constant\n 1. SLOW \n 2. MEDIUM \n 3. FAST")

myObject = FAN()

print("\nDefault values:\n")

print (myObject.get_my_attr_speed())
print("\n****************************")
print("\nFirst FAN object with maximum speed, radius 10, color yellow, and on:\n")

myObject1 = FAN()
myObject1.set_my_attr_speed(3,"True",10,"Yellow")

print (myObject1.get_my_attr_speed())
print("\n****************************")
print("\nSecond FAN object with medium speed, radius 5, color blue, and off:\n")

myObject2 = FAN()

myObject2.set_my_attr_speed(1,"False",5,"Blue")
print (myObject2.get_my_attr_speed())