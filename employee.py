def employee_details(name, emp_id, department, salary):
    result = (
        f"name:{name}\n"
        f"Employee:{emp_id}\n"
        f"Department:{department}\n"
        f"Salary:{salary}"
    )
    return result


if __name__ == "__main__":
    # Sample input (you can change)
    name="Alice"
    emp_id="E1001"
    department="IT"
    salary=55000

    print(employee_details(name,emp_id,department,salary))
