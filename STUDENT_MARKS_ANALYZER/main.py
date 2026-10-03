"""
Build Student Marks Analyzer v1 
Create a Python CLI program that:
Asks for a student's name.
Accepts marks for multiple subjects.
Calculates total and average marks.
Displays a result.
Determines pass/fail using a clearly defined rule.
Suggested rule: for this prototype, define the passing mark as 40 in each subject. State that rule in your program.

Your program should calculate:

Total marks for each student
Average
Pass/fail
Highest scorer
Lowest scorer
Class average
Subject-wise average
Number of passed students
Number of failed students
"""


# Global dictionary to store all student data
# main_dict = {}

# def get_student_info():
#     # We ask how many students to input so the program can handle multiple people
#     num_students = int(input("How many students do you want to enter? "))
    
#     for _ in range(num_students):
#         name = input("\nEnter student's Full name: ")
#         no_of_subjects = int(input(f"How many subjects did {name} take? "))
        
#         # Create a FRESH sub-dictionary for EACH individual student
#         subdict = {}
        
#         for i in range(no_of_subjects):
#             name_of_subject = input(f"  Enter the name of subject {i+1}: ")
#             marks = float(input(f"  Enter the marks for {name_of_subject}: "))
            
#             # Save subject and marks to the student's personal dictionary
#             subdict[name_of_subject] = marks
            
#         # Link the student's name to their subjects dictionary in the main dictionary
#         main_dict[name] = subdict
        
#     print("\nCollected Data Structure:", main_dict)


# def analyze_and_report():
#     print("\n================ REPORT CARD ================")
    
#     # Variables to track the overall class metrics
#     total_class_marks = 0
#     total_subjects_count = 0
#     passed_students = 0
#     failed_students = 0
    
#     highest_score = -1
#     lowest_score = 9999
#     highest_scorer = ""
#     lowest_scorer = ""
    
#     # Dictionary to keep track of total marks for subject-wise averages
#     subject_totals = {}
#     subject_counts = {}

#     # Loop through each student in our main dictionary
#     for name, subjects in main_dict.items():
#         print(f"\nStudent Name: {name}")
        
#         student_total = 0
#         student_subject_count = len(subjects)
        
#         # Loop through this specific student's subjects and scores
#         for subject, score in subjects.items():
#             print(f"  - {subject}: {score}")
#             student_total += score
            
#             # Accumulate data for subject-wise averages
#             if subject not in subject_totals:
#                 subject_totals[subject] = 0
#                 subject_counts[subject] = 0
#             subject_totals[subject] += score
#             subject_counts[subject] += 1
            
#         # Calculate individual average / percentage
#         student_average = student_total / student_subject_count
        
#         # Check Pass/Fail status
#         if student_average < 40:
#             status = "Failed"
#             failed_students += 1
#         else:
#             status = "Passed"
#             passed_students += 1
            
#         print(f"  Total Marks: {student_total}")
#         print(f"  Average/Percentage: {student_average:.2f}%")
#         print(f"  Result: {status}")
        
#         # Update metrics for class average
#         total_class_marks += student_total
#         total_subjects_count += student_subject_count
        
#         # Check for highest and lowest scorers
#         if student_total > highest_score:
#             highest_score = student_total
#             highest_scorer = name
            
#         if student_total < lowest_score:
#             lowest_score = student_total
#             lowest_scorer = name

#     # Print overall class metrics if data was entered
#     if main_dict:
#         class_average = total_class_marks / total_subjects_count
#         print("\n================ CLASS SUMMARY ================")
#         print(f"Class Average: {class_average:.2f}%")
#         print(f"Highest Scorer: {highest_scorer} ({highest_score} marks)")
#         print(f"Lowest Scorer: {lowest_scorer} ({lowest_score} marks)")
#         print(f"Number of Passed Students: {passed_students}")
#         print(f"Number of Failed Students: {failed_students}")
        
#         print("\nSubject-Wise Averages:")
#         for subject in subject_totals:
#             sub_avg = subject_totals[subject] / subject_counts[subject]
#             print(f"  - {subject}: {sub_avg:.2f}")
#     print("=============================================")

# # --- Execution ---
# # 1. Gather info from the user
# get_student_info()
# # 2. Run calculations and print all outputs
# analyze_and_report()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ==========================================
# GLOBAL DATA
# ==========================================
main_dict = {}

# ==========================================
# CORE FUNCTIONS
# ==========================================

def get_student_data():
    """Gathers data from the user and populates the main dictionary."""
    num_students = int(input("How many students do you want to enter? "))
    
    for _ in range(num_students):
        name = input("\nEnter student's Full name: ")
        no_of_subjects = int(input(f"How many subjects did {name} take? "))
        
        # Fresh dictionary for each student
        subdict = {}
        for i in range(no_of_subjects):
            name_of_subject = input(f"  Enter the name of subject {i+1}: ")
            marks = float(input(f"  Enter the marks for {name_of_subject}: "))
            subdict[name_of_subject] = marks
            
        # Store in global dictionary
        main_dict[name] = subdict
    print("\nData collection complete!")


def calculate_total(subject_dict):
    """Calculates the total marks from a student's subject dictionary."""
    total = 0
    for score in subject_dict.values():
        total += score
    return total


def calculate_average(total_marks, total_subjects):
    """Calculates the average based on total marks and total subjects."""
    if total_subjects == 0:
        return 0
    return total_marks / total_subjects


def check_result(average_score):
    """Determines if a student passed or failed based on a 40% threshold."""
    if average_score < 40:
        return "Failed"
    else:
        return "Passed"


def find_topper_and_lowest():
    """Finds the highest and lowest scorers in the class based on total marks."""
    highest_score = -1
    lowest_score = 99999
    topper = ""
    lowest_scorer = ""
    
    for name, subjects in main_dict.items():
        student_total = calculate_total(subjects)
        
        # Check for topper
        if student_total > highest_score:
            highest_score = student_total
            topper = name
            
        # Check for lowest scorer
        if student_total < lowest_score:
            lowest_score = student_total
            lowest_scorer = name
            
    return topper, highest_score, lowest_scorer, lowest_score


def calculate_class_and_subject_averages():
    """Calculates the overall class average and individual subject averages."""
    total_class_marks = 0
    total_class_subjects = 0
    
    subject_totals = {}
    subject_counts = {}
    
    for name, subjects in main_dict.items():
        total_class_marks += calculate_total(subjects)
        total_class_subjects += len(subjects)
        
        for subject, score in subjects.items():
            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0
            subject_totals[subject] += score
            subject_counts[subject] += 1
            
    # Calculate overall class average
    class_average = calculate_average(total_class_marks, total_class_subjects)
    
    # Calculate subject-wise averages
    subject_averages = {}
    for subject in subject_totals:
        subject_averages[subject] = subject_totals[subject] / subject_counts[subject]
        
    return class_average, subject_averages


# ==========================================
# REPORT DISPLAY FUNCTION
# ==========================================

def display_report():
    """Combines all functions to generate and display the final report card."""
    if not main_dict:
        print("No student data available.")
        return
        
    print("\n================ INDIVIDUAL REPORT CARD ================")
    passed_count = 0
    failed_count = 0
    
    # 1. Process and print individual student metrics
    for name, subjects in main_dict.items():
        print(f"\nStudent Name: {name}")
        
        # Print individual marks
        for subject, score in subjects.items():
            print(f"  - {subject}: {score}")
            
        # Core metric calculations using our functions
        s_total = calculate_total(subjects)
        s_average = calculate_average(s_total, len(subjects))
        s_result = check_result(s_average)
        
        # Track pass/fail tallies
        if s_result == "Passed":
            passed_count += 1
        else:
            failed_count += 1
            
        print(f"  Total Marks : {s_total}")
        print(f"  Average     : {s_average:.2f}%")
        print(f"  Result      : {s_result}")

    # 2. Process and print class-wide metrics
    topper, top_score, lowest_student, low_score = find_topper_and_lowest()
    class_avg, sub_averages = calculate_class_and_subject_averages()
    
    print("\n================ FINAL CLASS SUMMARY ================")
    print(f"Overall Class Average : {class_avg:.2f}%")
    print(f"Highest Scorer (Topper): {topper} ({top_score} marks)")
    print(f"Lowest Scorer          : {lowest_student} ({low_score} marks)")
    print(f"Total Students Passed  : {passed_count}")
    print(f"Total Students Failed  : {failed_count}")
    
    print("\n--- Subject-Wise Averages ---")
    for subject, avg in sub_averages.items():
        print(f"  - {subject}: {avg:.2f}")
    print("=====================================================")

# ==========================================
# PROGRAM EXECUTION
# ==========================================
# Step 1: Get the data
get_student_data()

# Step 2: Display the comprehensive report
display_report()
