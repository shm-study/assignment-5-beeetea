from ex03.convert_temp import ctof

class Test_Ex03:
    def testcase_1(self):
        assert ctof(0) == 32.0
    
    def testcase_2(self):
        assert ctof(32) == 89.6

    def testcase_3(self):
        assert ctof(100) == 212.0
