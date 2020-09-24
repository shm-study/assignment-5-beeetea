from ex01.my_first_function import print_hello

def test_ex01(capfd):
    print_hello()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"