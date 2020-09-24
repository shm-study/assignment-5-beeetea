from ex04.fibonacci import fibo

class Test_Ex03:
    def testcase_1(self):
        assert fibo(1) == 1
    
    def testcase_2(self):
        assert fibo(10) == 55

    def testcase_3(self):
        assert fibo(15) == 610

    def testcase_4(self):
        assert fibo(20) == 6765

    def testcase_5(self):
        assert fibo(25) == 75025