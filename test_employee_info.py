import employee_info


def test_get_employees_by_age_range():
    # Define the expected result based on the employee data in the specified age range

    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]

    # Call the get_employees_by_age_range function with the specified age range
    result = employee_info.get_employees_by_age_range(22, 36)

    # Assert that the result matches the expected result
    assert result == expected_result


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    expected = 60166.67

    assert(result == expected)


def test_get_employees_by_dept():
    expected_result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]
    result=[]
    result=employee_info.get_employees_by_dept("Marketing")
    assert result==expected_result




