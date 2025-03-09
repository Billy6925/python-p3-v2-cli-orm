from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    print("Available departments:")
    list_departments()
    name = input("Enter the department's name: ")
    department_name = Department.find_by_name(name)
    print(department_name) if department_name else print(
        f"{department_name} not found"
    )
    
def find_department_by_id():
    print("Available departments:")
    list_departments()
    id_ = int(input("Enter the department's id: "))
    department = Department.find_by_id(id_)
    print (department) if department else print(
        f"Department {id_} not found"
    )
    
def create_department():
    name = input("Enter the new department's name: ")
    location = input("Enter the new department's location: ")
    try:
        department = Department.create(name,location)
        print(f"Sucess {department}")
    except Exception as exc:
        print(f"Error creating department: ",exc)


def update_department():
    print("Available departments:")
    list_departments()
    dept_id = input("Enter the department's id: ")
    name = input("Enter the department's new name: ")
    location = input("Enter the department's new location: ")
    if department := Department.find_by_id(dept_id):
        try:
            department.name = name
            department.location =location
            department.update()
            print(f"Success {department}")
        except Exception as exc:
            print(f"Error updating department: ",exc)
    else:
        print(f"Department {dept_id} not found")


def delete_department():
    print("Available departments:")
    list_departments()
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            department.delete()
            print(f"Delete {department} success")
        except Exception as exc:
            print(f" Error deleting department: ",exc)
    else:
        print(f"Department {id_} not found")


# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass