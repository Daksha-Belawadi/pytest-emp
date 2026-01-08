from employee import employee_details

def test_employee_details():
    expected_output = (
        "name:Alice\n"
        "emp_id:E1001\n"
        "department:IT\n"
        "salary:55000"
    )

    assert employee_details("Alice","E1001","IT",55000) == expected_output
