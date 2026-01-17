from multipledispatch import dispatch

class Plants:
    def __init__(self, name) -> None:
        self.name = name

    def water_plant(self):
        print("watering plants")
        

class Herbs(Plants):
    def __init__(self, name, climate) -> None:
        super().__init__(name)
        self.climate = climate

    def water_plant(self):
        print("watering herbs")

    @dispatch(int, int)
    def adding(self, a, b):
        return a + b
    
    @dispatch(int, int, int)
    def adding(self, a, b, c):
        return a + b + c

class Rose(Herbs):
    def __init__(self, name, climate, color) -> None:
        super().__init__(name, climate)
        self.color = color

def main():
    p1 = Plants("Banyan")
    h1 = Herbs("Rose", "Humid")
    print(p1.name)
    print(h1.name)
    print(h1.climate)
    p1.water_plant()
    h1.water_plant()
    print(h1.adding(1, 2, 4))
    r1 = Rose("Rose", "Humid", "pink")
    print(r1.climate)
    print(r1.color)

if __name__ == "__main__":
    main()