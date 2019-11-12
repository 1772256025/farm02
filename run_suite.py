"""
    测试套件:
        按照需求组合被执行的测试函数


"""
# 1.导包
import unittest

import app
from case.Test_iHRM_Emp import Test_Emp
from case.Test_iHRM_Login import Test_Login

# 2.实例化套件对象，组织被执行的测试函数
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_Login("test_login_success"))  # 组织登录成功的测试函数
suite.addTest(Test_Emp("test_add"))  # 组织员工新增的测试函数
suite.addTest(Test_Emp("test_update"))  # 组织员工修改的测试函数
suite.addTest(Test_Emp("test_get"))  # 组织员工查看的测试函数
suite.addTest(Test_Emp("test_delete"))

# 3.执行套件，生成测试报告
with open(app.PRO_PATH+"/report/report.html","wb")as f:
    runner = HTMLTestRunner(f,title="人力资源关系系统测试报告",
                            description="测试了员工管理模块")
    runner.run(suite)

# ruuner = unittest.TextTestRunner()
   
