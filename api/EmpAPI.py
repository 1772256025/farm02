"""
    设计员工模块的增删改查请求
"""
import app


class EmpCRUD:
    # 初始化函数 --- 封装资源路径
    def __init__(self):
        self.emp_url = app.BASE_URL + "/api/sys/user"

    # 请求函数:增
    def add(self, session, username=None, mobile=None, timeOfEntry=None, formOfEmployment=None, workNumber=None,
            departmentName=None, departmentId=None, correctionTime=None):
        my_add = {"username": username,
                  "mobile": mobile,
                  "timeOfEntry": timeOfEntry,
                  "formOfEmployment": formOfEmployment,
                  "workNumber": workNumber,
                  "departmentName": departmentName,
                  "departmentId": departmentId,
                  "correctionTime": correctionTime}
        return session.post(self.emp_url, json=my_add,
                            headers={"Authorization": "Bearer " + app.TOKEN})

    # 请求函数:改
    def update(self, session, id, username):
        return session.put(self.emp_url + "/" + id,
                           json={"username": username},
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 请求函数:查
    def get(self, session, id):
        return session.get(self.emp_url + "/" + id,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 请求函数:删
    def delete(self, session, id):
        return session.delete(self.emp_url + "/" + id,
                              headers={"Authorization": "Bearer " + app.TOKEN})