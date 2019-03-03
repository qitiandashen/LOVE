import unittest
from module import Calculator

class ModuleTest(unittest.TestCase):
    def setUp(self):
        print('test start')
    def test_add(self):
        j=Calculator(8,4)
        self.assertEquals(j.add(),12)
    def test_sub(self):
        j=Calculator(10,5)
        self.assertEquals(j.sub(),4,msg='you are wrong')
    def test_mul(self):
        j=Calculator(9,9)
        self.assertEquals(j.mul(),81)
    def test_div(self):
        j = Calculator(12,3)
        self.assertEquals(j.div(),4)
    def tearDown(self):
        print('test end')
if __name__=='__main__':
    unittest.main()
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(ModuleTest('test_add'))
    suite.addTest(ModuleTest('test_sub'))
    suite.addTest(ModuleTest('test_mul'))
    suite.addTest(ModuleTest('test_div'))
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)


