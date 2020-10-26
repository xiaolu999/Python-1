import random
import time


class Cat:
    role = 'cat'



    def __init__(self, name, breed, ):
        self.name = name
        self.breed = breed
        self.aggressivity = random.randint(60, 90)
        self.life = random.randint(200, 290)


    def attack(self,dog):      #猫的攻击
        dog.life -= self.aggressivity
        print('猫打了狗')
    def eat(self):
        self.life += 50
    def die(self):
        if self.life<=0:
            print(self.name, '已经被打死了')
        else:
            print(self.name, '的血量还有', self.life)



class Dog:
    role = 'dog'



    def __init__(self, name, breed,):
        self.name = name
        self.breed = breed
        self.life = random.randint(200, 290)
        self.aggressivity= random.randint(60, 90)


    def attack(self,cat):      #狗的攻击
        cat.life -=self.aggressivity
        print('狗打了猫')
    def eat(self):
        self.life += 40
    def die(self):
        if self.life<=0:
            print(self.name, '已经被打死了')
        else:
            print(self.name, '的血量还有',self.life)


cat_1 = Cat('小辉','波斯猫')
dog_1 = Dog('小蓝','哈士奇')
dog_1.die()
cat_1.die()


while True:
    for i in range(1, 4):
        time.sleep(2)
        print('-------------------开始战斗----现在是第%s句---------' %i)

        cat_1.attack(dog_1)
        dog_1.attack(cat_1)
        dog_1.die()
        cat_1.die()
    if cat_1.life<=0 and dog_1.life>0:
        print('狗赢了血量量还有', dog_1.life)
        break


    elif  cat_1.life>0 and dog_1.life<=0:
        print('猫赢了血量还有', cat_1.life)
        break
    else:
        print('平局了')
        break









