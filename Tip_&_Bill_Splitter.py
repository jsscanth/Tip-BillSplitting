bill_amount = 0.00 
tip_percentage = 0.00
number_of_people = 0
total_tip = 0.00
total_bill = 0.00
total_bill_person = 0.00 # Total bill per person

def main ():
    bill_amount = float(input("Subtotal: "))
    tip_percentage = float(input("Tip percentage: ").strip("%"))
    number_of_people = int(input("Number of people: "))
    
    total_tip = calculate_tip(bill_amount, tip_percentage)
    total_bill = calculate_bill(bill_amount, total_tip)    
    total_bill_person = split_bill(total_bill, number_of_people)
    
    print("---------BILL SUMMARY---------")
    print(f"{'Subtotal':<20}: ${bill_amount:,.2f}")
    print(f"{f'Tip({tip_percentage:.0f}%)':<20}: %{total_tip:,.2f}")
    print(f"{'Total':<20}: ${total_bill:,.2f}")
    print(f"{'People':<20}: {number_of_people}")
    print(f"{'Each person pays':<20}: ${total_bill_person:,.2f}")
    print("------------------------------")
    
#Calculate the tip based on tip percentage on amount
def calculate_tip(amount, tip):
    total = amount * (tip/100)
    return total

# Calculate the bill after adding the tip
def calculate_bill(amount, tip):
    total_bill = amount + tip
    return total_bill
    
# Divide the bill per people
def split_bill(bill, people):
    total_bill = bill / people
    return total_bill
    
main()