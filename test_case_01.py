from selenium import webdriver

class Test_Credence_01:
    def test_sum_01(self):
        a=9
        b=6
        sum=a+b
        print(sum)
        if sum==15:
            assert True
        else:
            assert False

    def test_mul_01(self):
        a=4
        b=8
        mul=a*b
        print(mul)
        if mul==32:
            assert True
        else:
            assert False

