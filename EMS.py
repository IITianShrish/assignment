Emp_storage={'emp_id':
             {101:{'Name':"Shrish",'Age':19,"Department":"HR","Salary":100000.00}}

             }


user_info=Emp_storage.values()



def main_menu():
    print("Menu:\n 1.Add employee \n 2.View All Employees \n 3.Search for Employees \n 4.Exit")
    
    global user_input
    user_input=input("Please Enter digits corresponding to Options in Menu :")
    print(50*"-")





def add_employee():

    list_of_emp_id=[]
    
    print("Processing to Add Employees...")
    emp_id=input("Enter Employee ID:(Numeruic only):")

    for keys in user_info:
        for user_data_keys,user_data_values in keys.items():
            list_of_emp_id+=[user_data_keys]
        

    if emp_id in str(list_of_emp_id):
        print(f'Emp_id:{emp_id} already Exist')
    
        
    else:
        new_emp_name=input("Enter Name:")
        new_emp_age=input("Enter Age:")
        new_emp_department=input("Enter Department Name:")
        new_emp_salary=input("Enter Salary:")
        add_emp={int(emp_id):{'Name':new_emp_name,'Age':int(new_emp_age),"Department":new_emp_department,"Salary":float(new_emp_salary)}}

        print("Adding details Of New Employee....")
        Emp_storage['emp_id'].update(add_emp)
        print('Sucessfully Added New Employee')

        for keys in user_info:
            for user_data_keys,user_data_values in keys.items():

                if emp_id in str(user_data_keys):
                    print("\n Emp_id:",user_data_keys,"\n")

                    for headings,heading_values in user_data_values.items():
                        print(f'{headings} : {heading_values}')



    
def view_employees():
    print("Processing to View All Employees")
    
    for keys in user_info:
        for user_data_keys,user_data_values in keys.items():
            print("\n Emp_id:",user_data_keys,"\n")

            for headings,heading_values in user_data_values.items():
                print(f'{headings} : {heading_values}')

            print(30*"-")

def search_employee():
    print("Processing to Search for Employees:")

    try:
        user_search=input("Please Enter Employee ID:")
        list_empid=[]   
        for keys in user_info:
            for user_data_keys,user_data_values in keys.items():
                list_empid+=[str(user_data_keys)]

            if str(user_search) in list_empid:
                print("\n Emp_id:",user_data_keys,"\n")

                for headings,heading_values in user_data_values.items():
                    print(f'{headings} : {heading_values}')

            else:
                print(f'Employee with Emp ID:{user_search} is not found')
                    
    except Exception as error:
        print('something went wrong')


n=True

while n:
    try:
        main_menu()

        if int(user_input)==1:#To Add employee as per Menu
            add_employee()
            print(50*"-")


        elif int(user_input)==2:#To View all employees as per menu
            view_employees()
            print(50*"-")

        elif int(user_input)==3:#To Search all employees
            search_employee()
            print(50*"-")
        
        elif int(user_input)==4:#to exit
            print("Thank You for Using The program")
            print("Exiting")
            print(50*"-")
            n=False
        else:
            print("Wrong Input")
            print(50*"-")
    except Exception as ex:
        print("Something Went Wrong!")
        print(ex,50*"-")
        