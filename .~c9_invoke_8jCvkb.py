class Car:
    def __init__(self, name, color, fuel):
        self.name = name
        self.color = color
        self.fuel = fuel
        self.milage = 0
        
        print("자동차를 만들겠습니다.")
        
matiz = Car("Matiz", "red", 100)
genesis = Car("Genesis", "black", 50)

print(matiz.name, matiz.color, matiz.fuel, matiz.milage)
print(genesis.name, genesis.color, genesis.fuel, genesis.milage)