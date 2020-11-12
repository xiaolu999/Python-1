

# -*- coding:utf-8 -*-
import pygame  # 导入pygame模块
from pygame.locals import *  # 导入pygame.locals模块
import time  # 导入time模块


# 子弹类
class Bullet(object):
    def __init__(self, screen_temp, x, y):  # 构造方法 初始化子弹对象的属性
        self.x = x + 40  # 子弹起始X坐标
        self.y = y - 20  # 子弹起始Y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./images/bullet.png")  # 创建一个子弹图片

    def display(self):  # 显示子弹图片的方法
        self.screen.blit(self.image, (self.x, self.y))  # 将创建的子弹图片按设定的坐标贴到窗口中

    def move(self):  # 子弹移动方法
        self.y -= 10  # 子弹Y坐标自减10

    def judge(self):  # 判断子弹是否越界的方法
        if self.y < 0:  # 如果子弹的Y坐标小于0
            return True  # 返回true正确
        else:
            return False  # 返回false错误


# 飞机类
class Aircraft_obj(object):
    def __init__(self, screen_temp):  # 构造方法 初始化飞机对象的属性
        self.x = 190  # 飞起起始X坐标
        self.y = 708  # 飞机起始Y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./images/hero1.png")  # 创建一个飞机图
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):  # 显示飞机图片的方法（这里包括了显示子弹的图片）
        self.screen.blit(self.image, (self.x, self.y))  # 将创建的飞机图片按设定的坐标贴到窗口中

        # 显示飞机发射的所有子弹
        for bullet in self.bullet_list:
            bullet.display()  # 显示子弹
            bullet.move()  # 移动子弹
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)  # 将子弹从bullet_list中删除

    def move_left(self):  # 飞机左移方法
        if self.x < 10:  # X坐标小于10（移动距离）
            pass  # 不做任何事
        else:
            self.x -= 10  # X坐标自减少10

    def move_right(self):  # 飞机右移方法
        if self.x > 480 - 100 - 10:  # X坐标大于（窗口宽度-飞机宽度-移动距离）的值
            pass  # 不做任何事
        else:
            self.x += 10  # 坐标自增加10

    # 存储发射子弹的方法
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))  # 将发射的子弹对象存储到bullet_list中


# 敌机类
class EnemyPlane(object):
    def __init__(self, screen_temp):  # 构造方法 初始化敌机对象的属性
        self.x = 0  # 敌机的起始X坐标
        self.y = 0  # 敌机的起始Y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./images/enemy0.png")  # 创建一个敌机图片
        self.direction = "right"  # 用来存储飞机移动方向，默认向右移动

        # 爆炸效果用的属性
        self.hit = False  # 表示是否要爆炸
        self.bomb_lists = []  # 用来存储爆炸时需要的图片
        self.__crate_images()  # 调用这个方法向bomb_lists中添加图片
        self.image_num = 0  # 用来记录while循环的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号

    def __crate_images(self):  # 将爆炸需要的图片添加到self.bomb_lists中
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down1.png"))
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down2.png"))
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down3.png"))
        self.bomb_lists.append(pygame.image.load("./images/enemy0_down4.png"))

    # 判断爆炸的方法,x1表示子弹最左侧的X坐标，x2表示子弹最右侧的X坐标，y表示子弹当前的Y坐标
    def blast(self, x1, x2, y):
        # 判断子弹能命中敌机的三种情况，满足任意一种即可让敌机爆炸，51是敌机图片的宽度，39是敌机图片的高度
        # 1.子弹横坐标在敌机横坐标的区域中，并且子弹Y坐标小于敌机图片的高度
        # 2.子弹最右侧坐标等于敌机最左侧坐标，并且子弹Y坐标小于敌机图片的高度
        # 3.子弹最左侧坐标等于敌机最右侧坐标，并且子弹Y坐标小于敌机图片的高度
        if ((x1 >= self.x and x2 <= self.x + 51) or x2 == self.x or x1 == self.x + 51) and y < 39:
            self.hit = True

    def display(self):  # 显示敌机的方法
        # 如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:  # 如果满足爆炸条件，就显示爆炸的图片
            self.screen.blit(self.bomb_lists[self.image_index], (self.x, self.y))
            self.image_num += 1  # 这是统计循环次数，为了使玩家看清爆炸效果
            if self.image_num == 7:  # 如果循环次数达到7次
                self.image_num = 0  # 将循环次数改为0次
                self.image_index += 1  # 图片显示序号+1，换为另一张图
            if self.image_index > 3:  # 这里爆炸图片一共是四张，所以是图片序号大于三次
                time.sleep(1)  # 暂停一秒
                exit()  # 调用exit让游戏退出
        else:  # 否则显示正常的敌机图片
            self.screen.blit(self.image, (self.x, self.y))

    def move(self):  # 敌机移动方法
        if self.hit == True:
            pass
        else:
            if self.direction == "right":  # 如果是向右移动
                self.x += 5  # X坐标自增加5
            elif self.direction == "left":  # 如果是向左移动
                self.x -= 5  # X坐标自减少5

            if self.x > 480 - 50:  # 如果X坐标大于窗口减去敌机宽度的值
                self.direction = "left"  # 移动方向改为左
            elif self.x < 0:  # 如果X坐标小于0
                self.direction = "right"  # 移动方向改为右


# 处理鼠标和键盘事件的方法
def key_control(aircraft_temp):
    # 获取当前等待处理的事件,使用for循环来遍历里面的事件
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")  # 输出“exit”
            exit()  # 退出窗口
        # 判断是不是键盘按下事件
        elif event.type == KEYDOWN:
            # 检测按键是不是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')  # 输出“left”
                aircraft_temp.move_left()  # 执行飞机左移方法
            # 检测按键是不是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')  # 输出“right”
                aircraft_temp.move_right()  # 执行飞机右移方法
            # 检测按键是不是空格键
            elif event.key == K_SPACE:
                print('space')  # 输出“space”
                aircraft_temp.fire()  # 执行飞机类中存储子弹的方法


def main():
    # 1. 创建窗口
    pygame.init()
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2. 创建一个背景图片
    background = pygame.image.load("./images/background.png")

    # 3. 创建一个飞机对象
    aircraft = Aircraft_obj(screen)

    # 4. 创建一个敌机对象
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))  # 把背景复制到窗口的0,0处开始贴进去
        aircraft.display()  # 执行飞机类中显示飞机的方法

        for bullet in aircraft.bullet_list:  # 循环飞机对象中存储的子弹信息
            x1 = bullet.x  # 子弹当前X坐标
            x2 = bullet.x + 22  # 子弹当前X坐标+子弹图片的宽
            y1 = bullet.y  # 子弹当前Y坐标
            enemy.blast(x1, x2, y1)  # 判断子弹的坐标区域有没有与敌机相交

        enemy.display()  # 执行敌机类中显示敌机的方法
        enemy.move()  # 调用敌机的移动方法
        pygame.display.update()  # 更新需要显示的内容到窗口
        key_control(aircraft)  # 处理飞机对象的相关事件
        time.sleep(0.01)  # 暂停0.01秒


main()
