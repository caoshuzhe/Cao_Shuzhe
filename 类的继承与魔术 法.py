class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}")

# 2. 定义Student类，继承Person类
class Student(Person):
    def __init__(self, name, age, gender, college, class_info):
        super().__init__(name, age, gender)
        self.college = college
        self.class_info = class_info

    def personInfo(self):
        super().personInfo()
        print(f"学院：{self.college}，班级：{self.class_info}")

    # 3. 重写__str__方法
    def __str__(self):
        return f"学生{self.name}，{self.age}岁，{self.gender}，来自{self.college}的{self.class_info}班"

# 测试代码
if __name__ == "__main__":
    stu = Student("张三", 20, "男", "计算机学院", "软件工程1班")
    stu.personInfo()
    print(stu)