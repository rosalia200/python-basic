from payeg import Payroll
# emp1=input('enter name:')
nme = input("name:")
bs= int(input('basic salary:'))
ben = float(input('benefits:'))
# emp_name, emp_salary, emp_benefits = nme, bs,ben
emp1 = Payroll(nme,bs,ben)
print("NAME:               " +emp1.name)
print("GROSS SALARY :      " +str(emp1.find_gross_salary()))
print("NSSF :              "+str(emp1.find_nssf_deductions()))
print("TAXABLE INCOME:     "+str(emp1.find_taxable_income()))
print("PAYE :              "+str(emp1.find_payee()))
print("NHIF :              "+str(emp1.find_nhif_deductions()))
print("TOTAL DEDUCTIONS :  "+str(emp1.find_total_deductions()))
print("NET SALARY :        "+str(emp1.find_net_salary()))