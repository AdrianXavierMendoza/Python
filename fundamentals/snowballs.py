class Ninja:

    name = ""
    health = 100
    sword = ""
    strength = 20

    def jump(self):
        self.health -= 5

    def crouch(self):
        self.health -= 3

    def rest(self):
        self.health += 10

    def throw_snowball(self, ninja_target):
        ninja_target.health -= self.strength
        self.strength += 2

    def __init__(self, name, sword):
        self.name = name
        self.sword = sword

# End Of Class

my_ninja = Ninja("Chris", "Shuriken")
opponent = Ninja("Vinson", "Pool Noodle")

print("Chris throws a snowball")
print(f"Chris strength:{my_ninja.strength} Vinson strength:{opponent.strength}")
my_ninja.throw_snowball(opponent)
print(f"Chris health:{my_ninja.health} Vinson health:{opponent.health}")

print("Vinson throws Snowball")
print(f"Chris strength:{my_ninja.strength} Vinson strength:{opponent.strength}")
opponent.throw_snowball(my_ninja)
print(f"Chris health:{my_ninja.health} Vinson health:{opponent.health}")