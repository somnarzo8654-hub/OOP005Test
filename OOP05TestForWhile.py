import os

def clrscr():
    os.system('cls')

def line1():
    print('-'*60)

def line2():
    print('='*60)   

def header():
    print('\t=============== ระบบคำนวณตารางผ่อนชำระสินค้า===============')

def inputdata():
    price = float(input('กรอกราคาสินค้า (บาท) : '))
    down_payment = float(input('กรอกเงินดาวน์ (บาท) :'))
    principal = price - down_payment
    return principal

def get_months():
    while True:
        month = int(input('เลือกผ่อนชำระ (3ม 6 หรือ 12 เดือน)'))
        if month == 3  or month == 12 or month == 6 :
            return month
        else:
            print('!! จำนวนเงินไม่ถูกต้อง กรุณาระบุเฉพาะ 3 , 6 หรือ 12 เดือน เท่านั้น')
def calculate_loan(p,m):
    if m == 3:
        interest_rate = 0.00
    elif m == 6:
        interest_rate = 0.03
    else:
        interest_rate = 0.06

    interrest_amount = p*interest_rate    
    total_debt = p + interrest_amount
    monthly_pay = total_debt/m
    return interest_rate, interrest_amount,total_debt,monthly_pay 
        
def schedule_table(months, monthly_pay , total_debt):
#งวดที่ 14 + 3 | +20 ยอด +3
    print(f"{'งวดที่' :<14} | {'ยอดชำระ (บาท)':<20} | {'ตงเหลือ (บาท)':<20}")
    line1()
    balance = total_debt
    for mt in range(1, months+1):
        balance -= monthly_pay
        if balance < 0:
            balance = 0.0
        print(f"งวดที่ {mt:<8} | {monthly_pay:>20,.2f} | {balance:>20,.2f}")  
        line2()      

#################     
clrscr()
line2()
header()
principal = inputdata()
months = get_months()

interest_rate, interrest_amount,total_debt,monthly_pay = calculate_loan(principal, months)
print('\n')
line2()
print(f"ยอดจัดไฟแนนซ์  : {principal:,.2f}บาท")
print(f"ดอกเบี้ย ({interest_rate*100:.0f}%) : {interrest_amount:,.2f}บาท")
print(f"ยอดผ่อนรวมสุทธิ  : {total_debt:,.2f} บาท (งวดละ {monthly_pay:,.2f} บาท )")
line2()
#ตาราง
schedule_table(months, monthly_pay , total_debt)


