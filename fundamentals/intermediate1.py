#1
import random
def randInt1(min=0, max=100):
    num = int(random.random()*100)
    return num
print(randInt1())

#2
import random
def randInt2(min=0, max=50):
    num = int(random.random()*50)
    return num
print(randInt2())

#3
import random
def randInt3(min=50, max=100):
    num = int(random.random()*50+50)
    return num
print(randInt3())

#4
import random
def randInt4(min=50, max=500):
    num = int(random.random()*450+50)
    return num
print(randInt4())

#5
import random
def randInt5(min=0, max=50):
    num = random.random()*50)
    return round(num)
print(randInt5())