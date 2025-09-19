#personal information  

full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
grad_semester = "Spring 2028"
major = "Computer Science"

#academic data organizaton 
current_course = ["COMP 163", "MATH 103", "SPCH 250", "HIS 106","FRST101"]
completed_courses = ["Biology", "Chemisrty", "Calculus", "Spanish II", "World History"]
credit_hours = [3,3,3,3,1]
gpa_history = [3.2, 3.6,3.4,3.7]

#contact information storage 
emergency_contact = ("(Mom)","Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte", "NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", "NC", "28202")
twitter_info = ("Birthday", 5, 22, 2006)

#intrest tracking
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn ={"JavaScript","Data structures", "Git", "Web design","Public speaking"}
career_intrests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life","Incantation", "Memento" }

#organizational mapping
course_credits = {"COMP 163": 3, "MATH 150": 3,"ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105":"Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
#monthly budget
monthly_budget = {"food" : 450, "entertainment":200, "books": 125, "transportation":100}
study_hours = {"programming": 10, "math": 8 , "english": 4, "history": 3}
#calculations
total_credit_hours = sum(credit_hours)
num_courses = len(credit_hours)
cumulative_gpa = sum(gpa_history) / len(gpa_history)
total_studyhours = study_hours["programming"] + study_hours["math"] + study_hours["english"] + study_hours["history"]
academic_load = total_credit_hours + total_studyhours
total_budget = monthly_budget["food"] + monthly_budget["entertainment"] + monthly_budget["books"] + monthly_budget["transportation"]
academic_investment = monthly_budget["books"] / total_studyhours
daily_food = monthly_budget["food"] / 30
annual_budget = total_budget * 12
#line42
courses_completed = len(completed_courses)

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student:", full_name, "|", "Email:", student_email,)
print("From:", hometown,"|", "Graduating:", grad_semester)
print("Major:", major,) 

print("\n=== ACADEMIC PROFILE ===")
print("Current Semester:", total_credit_hours, "credits across", num_courses, "courses")
print(f"Cumulative GPA:{cumulative_gpa: .2f}")
print("Weekly Study Time:", total_studyhours, "hours")
print(f"Academic Investment: ${academic_investment:.1f} per study hour")
print("\nCurrent Courses:")
print(f"COMP 163 - {course_credits['COMP 163']} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"MATH 150 - {course_credits['MATH 150']} credits - {course_professors['MATH 150']} - {course_rooms['MATH 150']}")
print(f"ENG 101 - {course_credits['ENG 101']} credits - {course_professors['ENG 101']} - {course_rooms['ENG 101']}")
print(f"HIS 105 - {course_credits['HIS 105']} credits - {course_professors['HIS 105']} - {course_rooms['HIS 105']}")
print("\n=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_intrests}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}")
print("\n=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${total_budget}")
print(f"Food: ${monthly_budget['food']} (${daily_food:.1f}/day)")
print(f"Entertainment: ${monthly_budget['entertainment']}")
print(f"Books: ${monthly_budget['books']}")
print(f"Transportation: ${monthly_budget['transportation']}")
print(f"Annual Projection: ${annual_budget}")
print("\n=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} {emergency_contact[0]} - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print("Social Media Presence: 439 followers across 2 platforms")
print(f"Key Contacts: {len(emergency_contact)} people in directory")
print("\n=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses)}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f" Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies)} activities")

print("================================================================")
