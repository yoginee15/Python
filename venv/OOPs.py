# class Computer:
#     def __init__(self):
#         print("in init")
#
#     def config(self):
#         print("in config")
#
# comp1 = Computer()
# comp1.config()

class Computer:
    brand = "Dell"
    def __init__(self,cpu,ram):
        print("in init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", Computer.brand, self.cpu, self.ram)

    def compare(self,other):
        if self.ram == other.ram :
            return  True
        else:
            return False

comp1 = Computer('i5','12')
comp1.config()

comp2 = Computer('i7','16')
comp2.config()

print("Is ram same",comp1.compare(comp2))