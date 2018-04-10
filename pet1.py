class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Hes dead dude ")

    def sleep(self):
        if self.is_alive:
            print(self.name + "zzzzzzzzzzzzzz...")
        else:
            print("Dis boi ded.")

    def play(self):
        if self.is_alive:
            print(self.name + "Yippee!")
        else:
            print("The dead cant play ")

    def roll(self):
       if self.is_alive:
            print(self.name + " is rolling " )
       else:
            print("He rollin in his grave")
    


    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        other.is_alive = False

    def jump(self, other):
        print(self.name + " jumps over  " + other.name + "!")
       
  
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Sav Shav")
pet2 = Pet("Elvis Presley ")
pet3 = Pet("Bob Ross")

