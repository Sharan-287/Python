print("SAASC-College")
print("Students 2025 Pass-Out")

students={
    "Final Year":[
        {
            "Students List":[
                {"AddNo":1,"Name":"Abimanyu","CGPA":9.0,"Grade":"A+","Percentage":86},
                {"AddNo":2,"Name":"Akash","CGPA":8.5,"Grade":"A","Percentage":75},
                {"AddNo":3,"Name":"Bharath","CGPA":7.5,"Grade":"B+","Percentage":65},
                {"AddNo":4,"Name":"Dharan","CGPA":6.5,"Grade":"B","Percentage":66},
                {"AddNo":5,"Name":"Dhinesh","CGPA":9.5,"Grade":"A+","Percentage":94},
                {"AddNo":6,"Name":"Ghanesh","CGPA":8.7,"Grade":"A","Percentage":80},
                {"AddNo":7,"Name":"Hari","CGPA":7.7,"Grade":"B+","Percentage":70},
                {"AddNo":8,"Name":"Hariram","CGPA":6.7,"Grade":"B","Percentage":69},
                {"AddNo":9,"Name":"Jeeva","CGPA":9.3,"Grade":"A+","Percentage":87},
                {"AddNo":10,"Name":"Manoj","CGPA":8.9,"Grade":"A","Percentage":83},
                {"AddNo":11,"Name":"Naresh","CGPA":7.9,"Grade":"B+","Percentage":68},
                {"AddNo":12,"Name":"Praveen","CGPA":6.9,"Grade":"B","Percentage":73},
                {"AddNo":13,"Name":"Radhakrishnan","CGPA":9.1,"Grade":"A+","Percentage":91},
                {"AddNo":14,"Name":"Sanjay","CGPA":8.3,"Grade":"A","Percentage":77},
                {"AddNo":15,"Name":"Saran","CGPA":7.3,"Grade":"B+","Percentage":74},
                {"AddNo":16,"Name":"Sharan","CGPA":6.3,"Grade":"B","Percentage":72},
                {"AddNo":17,"Name":"Vijay","CGPA":9.9,"Grade":"A+","Percentage":90},
                {"AddNo":18,"Name":"Vikram","CGPA":8.2,"Grade":"A","Percentage":76},
                {"AddNo":19,"Name":"Vivek","CGPA":7.2,"Grade":"B+","Percentage":66},
                {"AddNo":20,"Name":"Vinoth","CGPA":6.2,"Grade":"B","Percentage":74}
            ]
        }
    ]
}

try:
    addno=input("Enter a AddNo= ")
    if not addno.isdigit():
        raise ValueError("AddNo must be in Digits")
    
    addno=int(addno)

    if addno == 1:
        num1 = students["Final Year"][0]["Students List"][0]
        print("Details of Student:", num1)

    elif addno == 2:
        num2 = students["Final Year"][0]["Students List"][1]
        print("Details of Student:", num2)

    elif addno == 3:
        num3 = students["Final Year"][0]["Students List"][2]
        print("Details of Student:", num3)

    elif addno == 4:
        num4 = students["Final Year"][0]["Students List"][3]
        print("Details of Student:", num4)  

    elif addno == 5:
        num5 = students["Final Year"][0]["Students List"][4]
        print("Details of Student:", num5)

    elif addno == 6:
        num6 = students["Final Year"][0]["Students List"][5]
        print("Details of Student:", num6)

    elif addno == 7:
        num7 = students["Final Year"][0]["Students List"][6]
        print("Details of Student:", num7)

    elif addno == 8:
        num8 = students["Final Year"][0]["Students List"][7]
        print("Details of Student:", num8)

    elif addno == 9:
        num9 = students["Final Year"][0]["Students List"][8]
        print("Details of Student:", num9)

    elif addno == 10:
        num10 = students["Final Year"][0]["Students List"][9]
        print("Details of Student:", num10)

    elif addno == 11:
        num11 = students["Final Year"][0]["Students List"][10]
        print("Details of Student:", num11)

    elif addno == 12:
        num12 = students["Final Year"][0]["Students List"][11]
        print("Details of Student:", num12)

    elif addno == 13:
        num13 = students["Final Year"][0]["Students List"][12]
        print("Details of Student:", num13)

    elif addno == 14:
        num14 = students["Final Year"][0]["Students List"][13]
        print("Details of Student:", num14)

    elif addno == 15:
        num15 = students["Final Year"][0]["Students List"][14]
        print("Details of Student:", num15)

    elif addno == 16:
        num16 = students["Final Year"][0]["Students List"][15]
        print("Details of Student:", num16)

    elif addno == 17:
        num17 = students["Final Year"][0]["Students List"][16]
        print("Details of Student:", num17)

    elif addno == 18:
        num18 = students["Final Year"][0]["Students List"][17]
        print("Details of Student:", num18)

    elif addno == 19:
        num19 = students["Final Year"][0]["Students List"][18]
        print("Details of Student:", num19)

    elif addno == 20:
        num20 = students["Final Year"][0]["Students List"][19]
        print("Details of Student:", num20)
    
    else:
        print("AddNo out of range!")

except ValueError:
    print("AddNo must be in Digits")

finally:
    print("Grade Tracker Was Done")



"""try:
    addno = input("Enter AddNo: ")
    if not addno.isdigit():
        raise ValueError("AddNo must be in digits")
    
    addno = int(addno)
    student_list = students["Final Year"][0]["Students List"]

    if 1 <= addno <= len(student_list):
        student = student_list[addno - 1]
        print("\n--- Student Details ---")
        print(f"AddNo      : {student['AddNo']}")
        print(f"Name       : {student['Name']}")
        print(f"CGPA       : {student['CGPA']}")
        print(f"Grade      : {student['Grade']}")
        print(f"Percentage : {student['Percentage']}%")
    else:
        print("AddNo out of range!")

except ValueError as e:
    print("Error:", e)

finally:
    print("\nGrade Tracker Finished")"""