from ex02.insert_underbar import insert_underbar

class Test_Ex02:
    def testcase_1(self):
        assert insert_underbar("py", "thon") == "py_thon"
    
    def testcase_2(self):
        assert insert_underbar("to", "mok") == "to_mok"

    def testcase_3(self):
        assert insert_underbar("ice", "americano") == "ice_americano"