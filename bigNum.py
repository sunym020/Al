def bigNum(L1, L2):
        max_len = max(len(L1), len(L2))
        l1 = list(L1.zfill(max_len))
        l2 = list(L2.zfill(max_len))
        l3 = [0]*(max_len+1)
        for i in range(max_len-1, -1, -1):
                i_sum = int(l3[i+1]) + int(l2[i]) + int(l1[i])
                less = i_sum -10
                l3[i+1] = i_sum%10
                l3[i] = 1 if less>=0 else 0
        if l3[0] == 0:
                l3.pop(0)  
        result = [str(i) for i in l3]
        return ''.join(result)




#  单元测试
import unittest

class bigNumTest(unittest.TestCase):
        @classmethod
        def setUpClass(self):
                print("开始运行测试")
        
        @classmethod
        def tearDownClass(self):
                print("测试用例运行结束")
        
        def test_01(self):
                L1 = "13345"
                L2 = "345"
                self.assertEqual(bigNum("13345", "345"), str(int(L1)+int(L2)))
        
        def test_02(self):
                L1 = "abc"
                L2 = "345"
                self.assertTrue(isinstance(L1[i], int) for i in range(len(L1)))
                self.assertTrue(isinstance(L2[i], int) for i in range(len(L2)))
                with self.assertRaises(TypeError):
                        print("请输入整型组成的字符串")


def suite():
        suite = unittest.TestSuite()
        suite.addTest(bigNumTest("test_01"))
        suite.addTest(bigNumTest("test_02"))
        return suite

if __name__ == "__main__":
        runner = unittest.TextTestRunner()
        runner.run(suite())