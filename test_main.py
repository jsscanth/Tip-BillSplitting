from main import calculate_tip, calculate_bill, split_bill

def test_main():
    assert calculate_tip(85.50, 15)
    assert calculate_bill(85.50, calculate_tip(85.50, 15))
    assert split_bill(calculate_bill(85.50, calculate_tip(85.50, 15)), 4)
    
    assert calculate_tip(100, 10)
    assert calculate_bill(100, calculate_tip(100, 10))
    assert split_bill(calculate_bill(100, calculate_tip(100, 10)), 5)
    
    assert calculate_tip(76.52, 11)
    assert calculate_bill(76.52, calculate_tip(76.51, 11))
    assert split_bill(calculate_bill(76.52, calculate_tip(76.52, 11)), 3)
    