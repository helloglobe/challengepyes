class Apple():

    def __init__(self, color, weight, stem_length, circumference):

        self.color = color

        self.weight = weight

        self.stem_length = stem_length

        self.circumference = circumference

        print("Created!")


apple = Apple("green", 250, 5, 2)

print(apple.color)

print(apple.weight)
