import lab2.bmi as bmi


def test_bmi_normal_weight():
    result = []
    result = bmi.calculate_bmi(1.73,57)
    assert(result == 0)


def test_bmi_under_weight(): #Testing for github integration with jira
    result=[]
    result=bmi.calculate_bmi(1.9,45)
    assert(result == -1)


def test_bmi_over_weight():
    result=[]
    result=bmi.calculate_bmi(1.65,90)
    assert(result == 1)


