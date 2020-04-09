#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> data.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/9 19:08
@Desc    :
================================================="""

basic_salary = float(input("请输入月基本薪资："))
day = basic_salary/21.75
print("每天：", end="")
print(day)
hour = day/8
print("每小时：", end="")
print(hour)
hour_night = hour * 1.5
print("晚上加班一小时：", end="")
print(hour_night)
hour_week = hour * 2
print("周末加班一小时：", end="")
print(hour_week)
print("")

hour_night_num = float(input("请输入晚上加班时数："))
print("晚上加班工资为：", end="")
print(hour_night * hour_night_num)
print("")

hour_week_num = float(input("请输入周末加班时数："))
print("周末加班工资为：", end="")
print(hour_week * hour_week_num)
print("")

total_salary = hour_night * hour_night_num + hour_week * hour_week_num + basic_salary
print("税前工资为：", end="")
print(total_salary)
print("")

tax_basic_salary = float(input("扣税的薪资基数："))
# 公积金缴纳工资的10%，个人和公司各承担50%
HousingProvidentFund = tax_basic_salary * 0.05
print("公积金缴纳：", end="")
print(HousingProvidentFund)

# 养老保险缴纳工资的24%，公司承担66.7%，个人承担33.3%
EndowmentInsurance = tax_basic_salary * 0.08

# 工伤保险缴纳工资的0.35%，个人不缴纳
EmploymentInjuryInsurance = 0

# 生育保险缴纳工资的0.7%，个人不缴纳
MaternityInsurance = 0

# 失业保险缴纳工资的1%，公司承担70%，个人承担30%
UnemploymentInsurance = tax_basic_salary * 0.003

# 基本医疗保险缴纳工资的10%，公司承担80%，个人承担20%
MedicalInsurance = tax_basic_salary * 0.02

# 大额医疗保险每个月7元
CompanyMedical = 7

# 五险扣除总数
totalSocialInsurance = EndowmentInsurance + UnemploymentInsurance + MedicalInsurance + CompanyMedical
print("五险缴纳为：", end="")
print(totalSocialInsurance)
print("")

# 武汉工资扣除标准
tax_standard_salary = float(input("工资扣除标准："))
tax_salary = total_salary - totalSocialInsurance - HousingProvidentFund - tax_standard_salary
print(tax_salary)

tax_money = tax_salary * 0.03
print(tax_money)





