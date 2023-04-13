class TestExample:
    def test_check_math(selfs): #test_check_math - name of a test
        a = 5
        b = 9
        expected_sum = 14
        assert a+b == expected_sum, f"Sum of variables a and b is  equal t {expected_sum}" # assert - проверка`

    def test_check_math2(selfs): #test_check_math - name of test
        a = 5
        b = 2
        expected_sum = 14
        assert a+b == expected_sum, f"Sum of variables a and b is NOT equal t {expected_sum}"