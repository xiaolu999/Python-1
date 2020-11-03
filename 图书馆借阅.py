#查询，借阅，还书 添加，退出

# 每本书的基本属性都要有四个：书名、作家、推荐语和借阅状态

class Book:

    def __init__(self, name, author, recom, state = 0):

        self.name  = name
        self.author = author
        self.recom = recom
        self.state = state


    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return  '书名《%s》   作者: %s   介绍语:%s\n借阅状态：%s' % (self.name, self.author, self.recom, status)


#总体功能
class BookManger:
    books = []                         #空列表存放书籍，每一个都是Book的实例对象

    #初始化
    def __init__(self):
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。')
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)


    def menu(self):
        print('欢迎来到流浪图书馆')

        while True:
            choice = int(input('请输入数字对应的功能：\n1.查询所有书籍\n2.添加书籍\n3.借出书籍\n4.归还书籍\n5.退出系统\n'))
            if choice == 1:
                self.show_allbook()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break

    def show_allbook(self):
            for book in self.books:
                print(book)
                print('')


    def add_book(self):
        newname = input('请输入要添加的书的名字')
        newauthor = input('请输入要添加的书的作者')
        newrecom = input('请输入书的推荐语')
        new_book = Book(newname, newauthor, newrecom)
        self.books.append(new_book)

    def lend_book(self):
        name = input('请输入想借阅的书籍的名字')
        res = self.check_book(name)
        if res != None:
            if res.state == 1:
                print('抱歉这本书已经被借走了')
            else:
                print('借阅成功')
                res.state = 1
        else:
            print('这本书还没有被收录')




    def return_book(self):
        name = input('请输入要归还的书籍的名字')
        res = self.check_book(name)
        if res == None:
            print('名字打错了吧，这本书还没有')
        else:
            if res.state == 0:
                print('这本书还没有人借阅')
            else:
                print('归还成功')
                res.state = 0

    def check_book(self, name):
        for book in self.books:
            if book.name == name:
                return book

man = BookManger()
man.menu()
