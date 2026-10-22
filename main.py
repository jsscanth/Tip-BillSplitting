from decimal import Decimal, ROUND_HALF_UP

def main ():
    while True:
        try:
            bill_amount = float(input("Subtotal: "))
            
            if bill_amount <= 0:
                print("Input the proper amount of bill")
                continue
            else:
                break
        except ValueError:
            print("Input the proper amount of bill.")
            
    while True:
        try:
            tip_percentage = float(input("Tip percentage: ").strip("%"))
            
            if tip_percentage < 0:
                print("Input the proper amount of tip")
                continue
            else:
                break
        except ValueError:
            print("Input the proper amount of tip.")

    while True:
        try:
            number_of_people = int(input("Number of people: "))
            
            if number_of_people <= 0:
                print("Input the proper amount of people")
                continue
            else:
                break
        except ValueError:
            print("Input the proper amount of people.")    
    
    total_tip = calculate_tip(bill_amount, tip_percentage)
    total_bill = calculate_bill(bill_amount, total_tip)    
    total_bill_person = split_bill(total_bill, number_of_people)
    
    print("---------BILL SUMMARY---------")
    print(f"{'Subtotal':<20}: ${bill_amount:,.2f}")
    print(f"{f'Tip({tip_percentage:.0f})%':<20}: ${total_tip:,.2f}")
    print(f"{'Total':<20}: ${total_bill:,.2f}")
    print(f"{'People':<20}: {number_of_people}")
    print(f"{'Each person pays':<20}: ${total_bill_person:,.2f}")
    print("------------------------------")
         
#Calculate the tip based on tip percentage on amount
def calculate_tip(amount, tip):
    total = amount * (tip/100)
    total = Decimal(str(total))
    total = total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return float(total)

# Calculate the bill after adding the tip
def calculate_bill(amount, tip):
    total_bill = amount + tip
    total_bill = Decimal(str(total_bill))
    total_bill = total_bill.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return float(total_bill)
    
# Divide the bill per people
def split_bill(bill, people):
    total_bill = bill / people
    total_bill = Decimal(str(total_bill))
    total_bill = total_bill.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return float(total_bill)

if __name__ == "__main__":
    main()