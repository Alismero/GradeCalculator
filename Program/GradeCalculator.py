##
import pickle

# Opening the file
with open("Data.dat", "rb") as datafile:
    lesson_data = pickle.load(datafile)



def main():

    print("\n" "###" "\n" "Welcome to GRADE CACULATOR !!!")

    # In the first enter the program, it ask for adding new lesson to start
    if not lesson_data:
        print("\n" "Add a lesson to start.")
        AddNewLesson()
        print("")

    while True:

        # When the program runs, it will display the entered notes
        ShowAllLessons()
        print("")
        GeneralAverageV2()
        print("\n")

        print("Choose an action")
        print(" #1 Adding New Lesson" "\n" " #2 Add / Change note" "\n" " #3 Save & Exit")

        # Choose an option
        try:
            option = int(input())
        
        except ValueError:
            print("That is not a valid choice.\n\n")
            continue


        if option == 1:
            AddNewLesson()
            Save()

        elif option == 2:
            AddChangeNote()
            Save()

        elif option == 3:
            print("See you later..." "\n" "###")
            Save()
            break
        else:
            print("\n##That is not a valid choice.\n\n")



def AddNewLesson():

    code = input("Enter the course code: ").upper()
    data = {"midterm": "-", "final": "-"} # Create default values for midterm and final if user doesnt enter a value


    # Getting the weight of the course and ensuring it's a positive integer
    while True:
        try:
            lesson_weight = int(input("Enter the weight of course: "))
            if lesson_weight <= 0:
                print("Invalid input! Please enter an positive integer.")
                continue
            
            break  # Exit the loop, if user enter a valid input   
        
        except ValueError:
            print("Invalid input! Please enter an integer.")

    data["weight"] = lesson_weight
    

    # Getting the values of midterm and final and ensuring they're positive integers
    while True:
        try:
            midterm = input("Enter the midterm grade (p for pass): ")
            if midterm == 'p' or midterm == 'P':
                break

            if int(midterm) <= 0:
                print("Invalid input! Enter a positive integer")
                continue

            mid_per = int(input("Enter the percentage of midterm exam: "))
            
            if mid_per <= 0:
                print("Invalid input!!! Please enter a positive integer.")
                continue

            data["midterm"] = [ali(midterm), mid_per]
            break

            
        except ValueError:
            print("Invalid input! Please enter an integer")
    

    while True:
        try:
            final = input("Enter the final grade (p for pass): ")
            if final == 'p' or final == 'P':
                break

            if int(final) <= 0:
                print("Invalid input! Enter a positive integer")
                continue

            fin_per = int(input("Enter the percentage of final exam: "))
            
            if fin_per <= 0:
                print("Invalid input!!! Please enter a positive integer.")
                continue

            data["final"] = [ali(final), fin_per]
            break
            
        except ValueError:
            print("Invalid input! Please enter an integer")



    # Adding additional assessments if they exists
    ch = input("Enter if grades are done, 'a' for adding value: ")
    queue = 0
    while ch == "a":
        try:
            add_ass = input("Enter the grade for additional assessment: ")
            add_ass_per = int(input("Enter the percentage of additional assessment: "))
            data[queue] = [ali(add_ass), add_ass_per]
            queue += 1
            ch = input("Enter if grades are done. 'a' for adding value: ")
        
        except ValueError:
            print("Invalid input!!! Enter a valid integer")
    

    # Adding another value for easy formatting when we are trying to prints this values
    n = len(data) + 2
    data["columns"] = n

    lesson_data[code] = data    # Adding all data to lesston data. Data type is like "lesson_code":{'exam': [grade, percentange]...,'weight':num 'columns':num"}



def AddChangeNote():
    
    key = input("Enter the course code you want to edit/add assessment: ").upper().rstrip()
    while not key in lesson_data:
        if not key:
            key = input("Enter a course code you want to edit/add assessment: ").upper().rstrip()
        
        else:
            print(f"{key} course doesn't exist.")
            key = input("Enter a valid course code you want to edit/add assessment: ").upper().rstrip()

    print("")
    ShowColumns()
    ShowLesson(key)
    print("")
    num = input("1# Edit a note" "\n" "2# Add a new additional assessment" "\n").rstrip()
    

    if num == "1":
        while True:

            print("Choose the note to edit")
            print(" #m Midterm" "\n" " #f Final")
            
            # Adding extra grades if they exist
            try:
                n = 0
                while lesson_data[key][n]:
                    print(f" #{n+1} Ext{n+1}")
                    n += 1

            except KeyError:
                pass

            print(" #q Quit")
            choice = input().rstrip() 

            if choice == "m":
                choice = 'midterm'

            elif choice == "f":
                choice = 'final'

            elif choice == "q":
                break

            else:
                choice = int(choice) - 1
                grade = input(f"Enter the new Ext{choice + 1} grade (p for pass): ")
                if grade != "p":
                    lesson_data[key][choice][0] = ali(grade)
                grade_per = input(f"Enter the new percentage of Ext{choice + 1} exam (p for pass): ")
                if grade_per != "p":
                    lesson_data[key][choice][1] = ali(grade_per)
                
                Save()
                continue

            if lesson_data[key][choice] != "-":
                grade = input(f"Enter the new {choice} grade (p for pass): ")
                if grade != "p":
                    lesson_data[key][choice][0] = ali(float(grade))
                grade_per = input(f"Enter the new percentage of {choice} exam (p for pass): ")
                if grade_per != "p":
                    lesson_data[key][choice][1] = int(grade_per)

            else:
                grade = float(input(f"Enter the {choice} grade: "))
                grade_per = int(input(f"Enter the percentage of {choice} exam: "))
                lesson_data[key][choice] = [ali(grade), grade_per]
            Save()
    

    if num == "2":

        ext_key = 0
        try:
            while lesson_data[key][ext_key]:
                ext_key += 1    
        
        except KeyError:
            pass

        add_ass = ali(input("Enter the grade for additional assessment: "))
        add_ass_per = int(input("Enter the percentage of additional assessment: "))
        lesson_data[key][ext_key] = [add_ass, add_ass_per]
        lesson_data[key]["columns"] += 1



def ShowColumns():
    # Prints the names of columns
    

    ## Print the first line
    # Print the first part
    print(f"{'Codes':<12}{'Mid(%)':<13}{'Fin(%)':<13}", end="")
    
    # Print the middle part (additional assessments) if they exists
    for i in range(0, middle_column_number()):
        print(f"{f'Ext{i+1}(%)':<13}", end="")

    # Print the last part
    print(f"{'AVR':<7}")



def ShowLesson(key):

    # Print the first part
    midterm = lesson_data[key]['midterm'][0]
    midterm_percentage = lesson_data[key]["midterm"][-1]

    final = lesson_data[key]['final'][0]
    final_percentage = lesson_data[key]["final"][-1]    # The reason why I use [-1] for percentages is if the value for final or midterm doesn't exists final[1] will be out of range.

    print(f"{key:<12}{midterm:<4}{f'(%{midterm_percentage})':<9}{final:<4}{f'(%{final_percentage})':<9}",  end="")  # It seems horrible but it'S just a hard formatting :)
    

    # Print the middle part
    for i in range(0, middle_column_number()):
        try:
            etx_grade = lesson_data[key][i][0]
            etx_grade_per = lesson_data[key][i][1]
            print(f"{etx_grade:<4}{f'(%{etx_grade_per})':<9}",  end="")

        except KeyError:    # if the i-th element doesn't exist, just leave the space
            print(f"{'':13}", end="")


    # Print the last part (average)
    print(f"{AverageCalculator(key):<7}")



def ShowAllLessons():

    # Print the names of columns
    ShowColumns()
    
    ## Print the other lines
    # Taking lesson codes (They are keys for lesson_data)
    keys_list = list(lesson_data.keys())
    for key in keys_list: 
       ShowLesson(key)




def AverageCalculator(key):
    # Find the key lesson's average
    
    average_sum = 0
    average_per = 0

    try:
        midterm = lesson_data[key]["midterm"][0]
        midterm_percentage = lesson_data[key]["midterm"][1]
        
        average_sum += midterm * midterm_percentage
        average_per += midterm_percentage
    
    except:
        pass    # If there is no midterm grade, midterm is "-" as default 


    try:
        final = lesson_data[key]["final"][0]
        final_percentage = lesson_data[key]["final"][1]

        average_sum += final * final_percentage
        average_per += final_percentage
    
    except:
        pass    # If there is no final grade, final is "-" as default 

    
    # Add extra grades
    for i in range(0, middle_column_number()):
        try:
            ext_grade = lesson_data[key][i][0]
            ext_grade_per = lesson_data[key][i][1]
            
            average_sum += ext_grade * ext_grade_per
            average_per += ext_grade_per
        
        except KeyError:
            break   # Continue until the extra grades are finished.
    
    
    if average_per == 0:    # If there is no grades in this course, there is just name of course
        return "-"
    
    else:   # If there is any grade
        
        result = ali(average_sum / average_per)
        return round(result)



def GeneralAverageV1():
    # Arithmetic average

    keys_list = list(lesson_data.keys())
    
    avg_sum = 0
    avg_weights = 0

    for key in keys_list:
        avg_sum += AverageCalculator(key) * (lesson_data[key]["weight"])
        avg_weights += lesson_data[key]["weight"]
    

    if avg_weights != 0:
        result = avg_sum / avg_weights
    
    else:
        result = "-"
    

    try:
        print(f"GENERAL AVERAGE: {result:.2f} (Out of 100), {result/25:.2f} (Out of 4)")
    
    except ValueError:
        print("GENERAL AVERAGE: -")



def GeneralAverageV2():
    # Average by letter grades. (These are used in transkripts)

    keys_list = list(lesson_data.keys())

    avg_sum = 0 
    avg_weights = 0 

    notes = []

    for key in keys_list:
        lesson_avr = AverageCalculator(key)

        if 90 <= lesson_avr <= 100:
            lesson_avr = 4.00
        
        elif 85 <= lesson_avr < 90:       
            lesson_avr = 3.50
        
        elif 80 <= lesson_avr < 85:
            lesson_avr = 3.25
        
        elif 75 <= lesson_avr < 80:
            lesson_avr = 3.00
        
        elif 70 <= lesson_avr < 75:
            lesson_avr = 2.75
        
        elif 65 <= lesson_avr < 70:
            lesson_avr = 2.50
        
        elif 60 <= lesson_avr < 65:
            lesson_avr = 2.00
        
        elif 50 <= lesson_avr < 60:
            lesson_avr = 1.50
        
        else:
            lesson_avr = 0
        
        avg_sum += lesson_avr * (lesson_data[key]["weight"])
        avg_weights += lesson_data[key]["weight"]


    if avg_weights != 0:    
        result = avg_sum / avg_weights
    
    else:
        result = "-"
    
    
    try:
        print(f"GENERAL AVERAGE: {result:.2f} (Out of 4)")

    except ValueError:
        print("GENERAL AVERAGE: -")



def middle_column_number():
    middle_column_number = max(lesson_data.values(), key=lambda x: x["columns"])["columns"] - 5
    return middle_column_number



def Save():
    with open("Data.dat", "wb") as datafile:
            pickle.dump(lesson_data, datafile)



def ali(num):   # I couldn't find an build-in function, so I made it
    # Configurated eval function
    
    try:
        num = float(num)
    
    except ValueError:
        return num
    

    if num.is_integer():
        result = int(num)
        return result
    
    else:
        result = round(num, 2)
        return result




main()

