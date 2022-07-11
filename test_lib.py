from lib import Average

def test_average():
    input1 = [10, 11, 12]
    expected_result = 11
    actual_result = Average(input1)
    assert expected_result == actual_result , "C kc"
     
test_average()