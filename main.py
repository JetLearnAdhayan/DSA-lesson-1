class Fruit():
    #properties/attributes
    def __init__ (self, colour, shape, taste):
        self.colour = colour
        self.shape = shape
        self.taste = taste
    #fuctions/methods
    def displayDeatails(self):
        print("Hello I am a fruit with {} colour {} shape with {} taste".format(self.colour, self.shape, self.taste))


#objects
apple = Fruit("red", "round", "sweet")
apple.displayDeatails()