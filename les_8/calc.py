class Calc():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def addition(self):
        print('Answer :', self.num_1 + self.num_2)

    def subtraction(self):
        print('Answer :', self.num_1 - self.num_2)

    def multiplication(self):
        print('Answer :', self.num_1 * self.num_2)

    def division(self):
        print('Answer :', self.num_1 / self.num_2)
