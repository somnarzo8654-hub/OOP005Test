import os 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def headerPro():
    print('============== ยินดีต้อนรับสู่ระบบ Mobile Top-Up ===============')
    print('\n')

def line():
    print('\n')
    for i in range(1, 61):
        print('-', end='')
    print('\n')    

def verify_phone(correct_Phone):
    attempt = 0
    max_attempts = 3

    while attempt < max_attempts:
        user_Phone = input(f"กรุณาระบุหมายเลขโทรศัพท์มือถือ 10 หลัก (เหลือโอกาส {max_attempts - attempt} ครั้ง): ")
        if not user_Phone.isdigit() or len(user_Phone) != 10 or not user_Phone.startswith('0'):
            print("หมายเลขโทรศัพท์ต้องเป็นตัวเลข 10 หลัก และขึ้นต้นด้วยเลข 0 กรุณาลองใหม่\n")
            attempt += 1
            continue
        if user_Phone == correct_Phone:
            print("หมายเลขโทรศัพท์ถูกต้อง")
            return True
        else:
            print("หมายเลขโทรศัพท์ไม่ถูกต้อง\n")
            attempt += 1

    print("คุณกรอกหมายเลขโทรศัพท์มือถือผิด 3 ครั้งแล้ว ระบบจะระงับการให้บริการและจบการทำงานของโปรแกรม")
    return False         

def get_topup_amount():
    valid_amounts = [20, 50, 100, 200, 300]
    
    
    while True:
        user_input = input("กรุณาเลือกยอดเงินที่ต้องการเติม (20, 50, 100, 200, 300 บาท) : ")
        
        if not user_input.isdigit():
            print("ป้อนจำนวนเงินไม่ถูกต้อง : กรุณาป้อนหรือกรอกเฉพาะตัวเลขเท่านั้น\n")
            continue
            
        amount = int(user_input)

        if amount not in valid_amounts:
            print("อนุญาตให้เลือกยอดเติมเงินได้เฉพาะ 20, 50, 100, 200, 300 บาท กรุณาลองใหม่\n")
            continue
        
        print("เลือกยอดเงินถูกต้อง")
        return amount

def get_payment(topup_amount):
    while True:
        user_input = input(f"กรุณาหยอดเหรียญ/ธนบัตรเพื่อชำระเงิน (ยอดที่ต้องชำระ {topup_amount} บาท) : ")
        
        if not user_input.isdigit():
            print("ข้อมูลไม่ถูกต้อง : กรุณากรอกเฉพาะตัวเลขจำนวนเต็มเท่านั้น\n")
            continue
            
        cash_paid = int(user_input)

        if cash_paid < topup_amount:
            print(f"จำนวนเงินไม่พอ ชำระเงินเพิ่มอีก {topup_amount - cash_paid} บาท กรุณาลองใหม่\n")
            continue
            
        return cash_paid

def calculate_change(change_amount):
    c100 = change_amount // 100
    change_amount %= 100

    c50 = change_amount // 50
    change_amount %= 50

    c20 = change_amount // 20
    change_amount %= 20

    c10 = change_amount // 10
    change_amount %= 10

    c5 = change_amount // 5
    change_amount %= 5

    c2 = change_amount // 2
    change_amount %= 2

    c1 = change_amount // 1
    
    return c100, c50, c20, c10, c5, c2, c1

def display_receipt(phone_number, topup_amount, cash_paid, change, change_denominations):
    c100, c50, c20, c10, c5, c2, c1 = change_denominations 
    
    clear()
    headerPro()
    line()
    print("\t\tสลิปสรุปการเติมเงินมือถือ")
    line()
    print(f"หมายเลขโทรศัพท์มือถือ : {phone_number}")
    print(f"ยอดเงินที่เติม : {topup_amount} บาท")
    print(f"จำนวนเงินที่จ่าย : {cash_paid} บาท")
    print(f"เงินทอน : {change} บาท")
    line()
    print("\t\tรายละเอียดการทอนเงิน :")
    if change > 0:
        if c100 > 0: print(f"\tธนบัตร 100 บาท : {c100} ใบ")
        if c50 > 0:  print(f"\tธนบัตร 50 บาท : {c50} ใบ")
        if c20 > 0:  print(f"\tธนบัตร 20 บาท : {c20} ใบ")
        if c10 > 0:  print(f"\tเหรียญ 10 บาท : {c10} เหรียญ")
        if c5 > 0:   print(f"\tเหรียญ 5 บาท : {c5} เหรียญ")
        if c2 > 0:   print(f"\tเหรียญ 2 บาท : {c2} เหรียญ")
        if c1 > 0:   print(f"\tเหรียญ 1 บาท : {c1} เหรียญ")
    else:
        print("\tไม่มีเงินทอน")
    line()
    footer = "ขอบคุณที่ใช้บริการ Mobile Top-Up"
    print(f"{footer:^60}")

########### main #########
correct_Phone = "0957781696"

clear()
headerPro()
line()

if verify_phone(correct_Phone):
    line()
    topup_amount = get_topup_amount()
    line()
    
    cash_paid = get_payment(topup_amount)
    
    change = cash_paid - topup_amount
    change_denominations = calculate_change(change)
    
    print("\n=============== ทำรายการเติมเงินมือถือสำเร็จ ==============\n")
    
    display_receipt(correct_Phone, topup_amount, cash_paid, change, change_denominations)
