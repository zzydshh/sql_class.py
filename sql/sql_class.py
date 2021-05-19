#python数据库,函数class形式
#姓名:章宗扬
#日期:2021.5.17
import pymysql
import pandas as pd

class MySQLServer(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    def create_conn(self):
        self.connect = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                       password=self.password, database=self.database
                                       )
        if self.connect:
            print('数据库连接成功')
            self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)
        else:
            print('数据库连接失败')

    def server_close(self):
            self.cursor.close()
            self.connect.cursor()

    def add_Employee(self, EmployeeID, EmployeeName, Sex, Age,
                      DepartmentId, EmploymentYear, Telephone,IdentityID,Duty):
            """添加员工信息"""
            result = self.cursor.execute('insert into Employee values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                         (EmployeeID, EmployeeName, Sex, Age,
                                          DepartmentId, EmploymentYear, Telephone, IdentityID, Duty))
            if result == 1:
                print('添加信息成功')
            self.connect.commit()

    def delete_Employee(self, EmployeeID):
            """删除员工信息"""
            result = self.cursor.execute('delete from Employee where EmployeeID=%s', (EmployeeID,))
            if result == 1:
                print('删除员工成功')
            self.connect.commit()

    def update_Employee(self, EmployeeName,Age, DepartmentId, Duty, EmployeeID):
            """更新员工信息"""
            result = self.cursor.execute(
                'update Employee set EmployeeName=%s,Age=%s, DepartmentId=%s, Duty=%s where EmployeeID=%s',
                (EmployeeName,Age, DepartmentId,Duty, EmployeeID))
            if result == 1:
                print('更新员工信息成功')
            self.connect.commit()
    def select_allEmployee(self):
        """查询所有员工信息"""
        self.cursor.execute('select * from Employee')
        for row in self.cursor.fetchall():
            print(row)
    def select_Employee(self,EmployeeName):
        """查询指定员工的信息"""
        self.cursor.execute('select * from Employee where EmployeeName=%s',(EmployeeName,))
        for row in self.cursor.fetchall():
            print(row)
    def add_CheckStat(self, CheckID, EmployeeID, EmployeeName, OvertimeDay,
                      AbsentDay, LateDay,CheckDate):
            """添加员工考勤信息"""
            result = self.cursor.execute('insert into CheckStat values (%s,%s,%s,%s,%s,%s,%s)',
                                         (CheckID, EmployeeID, EmployeeName, OvertimeDay,
                                        AbsentDay, LateDay,CheckDate))
            if result == 1:
                print('添加信息成功')
            self.connect.commit()
    def delete_CheckStat(self, CheckID):
            """删除员工考勤信息"""
            result = self.cursor.execute('delete from CheckStat where CheckID=%s', (CheckID,))
            if result == 1:
                print('删除员工成功')
            self.connect.commit()
    def update_CheckStat(self, EmployeeName,OvertimeDay,AbsentDay, LateDay, CheckDate,CheckID):
            """更新员工考勤信息"""
            result = self.cursor.execute(
                'update CheckStat set EmployeeName=%s,OvertimeDay=%s, AbsentDay=%s, LateDay=%s, CheckDate=%swhere CheckID=%s',
                (EmployeeName,OvertimeDay,AbsentDay, LateDay, CheckDate,CheckID))
            if result == 1:
                print('更新员工信息成功')
            self.connect.commit()
    def select_allCheckStat(self):
        """查询所有员工考勤信息"""
        self.cursor.execute('select * from CheckStat')
        for row in self.cursor.fetchall():
            print(row)
    def select_CheckStat(self,EmployeeName):
        """查询指定员工的信息"""
        self.cursor.execute('select * from CheckStat where EmployeeName=%s',(EmployeeName,))
        for row in self.cursor.fetchall():
            print(row)
    def prepare_wage(self):
        """准备计算wage"""
        self.cursor.execute('select * from wageconfig')
        result=self.cursor.fetchall()
        config_df=pd.DataFrame(list(result),columns=["Duty","BaseWage","OvertimeStandard",
                                                     "AbsentStandard","TaxRate","LateStandard","Bonus"])
        self.cursor.execute('select * from checkstat')
        result = self.cursor.fetchall()
        checkstat_df = pd.DataFrame(list(result), columns=["CheckID", "EmployeeID","EmployeeName","OvertimeDay",
                                                           "AbsentDay","LateDay","CheckDate"])
        self.cursor.execute('select * from department')
        result = self.cursor.fetchall()
        department_df = pd.DataFrame(list(result), columns=["DepartmentID", "DepartmentName", "DepartmentCount"])

        self.cursor.execute('select * from employee')
        result = self.cursor.fetchall()
        employee_df = pd.DataFrame(list(result), columns=["EmployeeID", "EmployeeName", "Sex", "Age",
                                         " DepartmentId", "EmploymentYear", "Telephone", "IdentityID", "Duty"])
        return config_df,checkstat_df,department_df,employee_df
    def add_wage(self, WageID, EmployeeID, EmployeeName, WageDate,BaseWage,OvertimeWage,
                      AbsentWage, LateWage,TaxWage,BonusWage,Totalwage):
            """添加员工考勤信息"""
            result = self.cursor.execute('insert into wage values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                         (WageID, EmployeeID, EmployeeName, WageDate,BaseWage,OvertimeWage,
                      AbsentWage, LateWage,TaxWage,BonusWage,Totalwage))
            self.connect.commit()
    def count_wage(self,config_df,checkstat_df,department_df,employee_df):
        i = int(input('请输入从第几位员工开始计算薪资：'))
        len = employee_df.shape[0]
        while i <= len:
            WageID = i
            EmployeeID = i
            EmployeeName = employee_df.loc[i - 1, 'EmployeeName']
            WageDate = "2021-1-1"
            Baselist = ["销售类","服务类","财务类","管理类"]
            Base_index = Baselist.index(employee_df.loc[i - 1, 'Duty'])
            BaseWage = config_df.loc[Base_index, 'BaseWage']
            OvertimeWage = config_df.loc[Base_index, 'OvertimeStandard'] * checkstat_df.loc[i - 1, 'OvertimeDay']
            AbsentWage = config_df.loc[Base_index, 'AbsentStandard'] * checkstat_df.loc[i - 1, 'AbsentDay']
            LateWage = config_df.loc[Base_index, 'LateStandard'] * checkstat_df.loc[i - 1, 'LateDay']
            BonusWage = config_df.loc[Base_index, 'Bonus']
            Totalwage_before = BaseWage + OvertimeWage - AbsentWage - LateWage + BonusWage
            TaxWage = config_df.loc[Base_index, 'TaxRate'] * Totalwage_before
            Totalwage = Totalwage_before - TaxWage
            self.add_wage(WageID, EmployeeID, EmployeeName, WageDate, BaseWage, OvertimeWage,
                         AbsentWage, LateWage, TaxWage, BonusWage, Totalwage)
            i += 1

    def select_allwage(self):
        """查询所有员工薪资信息"""
        self.cursor.execute('select * from wage')
        for row in self.cursor.fetchall():
            print(row)
    def select_wage(self,EmployeeName):
        """查询指定员工薪资信息"""
        self.cursor.execute('select * from wage where EmployeeName=%s',(EmployeeName,))
        for row in self.cursor.fetchall():
            print(row)
def main():
    # host_i = input('请输入主机IP地址:')
    # port_i = int(input('请输入连接端口：'))
    # user_i = input('请输入用户名：')
    # password_i = input('请输入密码:')
    # database_i = input('请输入数据库的名称:')
    # charset_i = input('请输入字符集编码：')
    emp = MySQLServer(host="127.0.0.1",port=3306,user="root",password="zzy123456",database="company")
    emp.create_conn()
    while 1:
        select = int(input('请输入想要进行的操作：\n'
                           '1、添加员工信息         '
                           '2、删除员工信息       \n'
                           '3、修改员工信息         '
                           '4、查询所有员工信息    \n'
                           '5、查询指定员工信息      '
                           '6、添加员工考勤信息    \n'
                           '7、删除员工考勤信息      '
                           '8、修改员工考勤信息    \n'
                           '9、查询所有员工考勤信息   '
                           '10、查询指定员工考勤信息\n'
                           '11、计算所有员工的薪资表  '
                           '12、查询所有员工的薪资表\n'
                           '13、查询指定员工的薪资表  '
                           '14、退出：\n'))
        if select == 1:
            EmployeeID = input('请输入员工的编号：')
            EmployeeName = input('请输入员工的姓名：')
            Sex = input('请输入员工的性别：')
            Age = input('请输入员工的年龄：')
            DepartmentId = input('请输入员工的部门编号：')
            EmploymentYear = input('请输入员工的入职年份：')
            Telephone = input('请输入员工的电话：')
            IdentityID = input('请输入员工的身份证号：')
            Duty = input('请输入员工的职务：')
            emp.add_Employee(EmployeeID, EmployeeName, Sex, Age,
                             DepartmentId, EmploymentYear, Telephone, IdentityID, Duty)
        elif select == 2:
            EmployeeID = input('请输入需要删除的员工的编号:')
            emp.delete_Employee(EmployeeID)
        elif select == 3:
            EmployeeID = input('请输入员工的编号：')
            EmployeeName = input('请输入员工的姓名：')
            Age = input('请输入员工的年龄：')
            DepartmentId = input('请输入员工的部门编号：')
            Duty = input('请输入员工的职务：')
            emp.update_Employee(EmployeeName,Age, DepartmentId, Duty,EmployeeID)
        elif select == 4:
            emp.select_allEmployee()
        elif select == 5:
            EmployeeName = input('请输入员工的姓名：')
            emp.select_Employee(EmployeeName)
        elif select == 6:
            CheckID=input("请输入考勤编号：")
            EmployeeID = input('请输入员工的编号：')
            EmployeeName = input('请输入员工的姓名：')
            OvertimeDay = input('请输入员工的加班天数：')
            AbsentDay = input('请输入员工的旷工天数：')
            LateDay = input('请输入员工的迟到天数：')
            CheckDate = input('请输入员工的考勤日期：')
            emp.add_CheckStat(CheckID, EmployeeID, EmployeeName, OvertimeDay,
                                        AbsentDay, LateDay,CheckDate)
        elif select == 7:
            EmployeeID = input('请输入需要删除的员工的编号:')
            emp.delete_CheckStat(EmployeeID)
        elif select == 8:
            CheckID = input("请输入考勤编号：")
            EmployeeName = input('请输入员工的姓名：')
            OvertimeDay = input('请输入员工的加班天数：')
            AbsentDay = input('请输入员工的旷工天数：')
            LateDay = input('请输入员工的迟到天数：')
            CheckDate = input('请输入员工的考勤日期：')
            emp.update_CheckStat(EmployeeName,OvertimeDay,AbsentDay, LateDay, CheckDate,CheckID)
        elif select == 9:
            emp.select_allCheckStat()
        elif select == 10:
            EmployeeName = input('请输入员工的姓名：')
            emp.select_CheckStat(EmployeeName)
        elif select == 11:
            config_df,checkstat_df,department_df,employee_df=emp.prepare_wage()
            emp.count_wage(config_df,checkstat_df,department_df,employee_df)
        elif select == 12:
            emp.select_allwage()
        elif select == 13:
            EmployeeName = input('请输入员工的姓名：')
            emp.select_wage(EmployeeName)
        else:
            print('成功退出')
            emp.server_close()
            break
if __name__ == "__main__":
    main()
    # emp.add_Employee("1", "zhang", "男", 18, "001", "2010", "133+", "33032+", "销售类")