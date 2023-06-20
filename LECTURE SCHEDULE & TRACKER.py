import pandas as pd
import csv

class LectureTracker:
    def __init__(self):
        self.lecture_tracker = []
        self.available_lectures = {}
#-------------------------------------------------------------------------------------------------------------------------
        
    def csvfile(self):
        with open('lecture_schedule.csv', 'w+', newline='') as file:
            myFile = csv.writer(file)
            myFile.writerow(['Slot', 'Date', 'Professor', 'Subject', 'Course','Time'])
            for lecture in self.lecture_tracker:
                slot = lecture['Slot']
                date = lecture['Date']
                professor = lecture['Professor']
                subject = lecture['Subject']
                course = lecture['Course']
                times = lecture['Time']
                myFile.writerow([slot, date, professor, subject, course, times])
#------------------------------------------------------------------------------------------------------------------------------
                
    def schedule_lecture(self):
        if not self.available_lectures:
            print("All Lectures have been filled")
            return

        print("\nAvailable Lecture Slots:")
        for slot in self.available_lectures.keys():
            print('Lecture --',{slot})

        slot = int(input("\nEnter the lecture number to schedule the lecture:\n"))

        if slot not in self.available_lectures:
            print("Invalid Lecture number. Please select another.")
            return

        profs = ['Ayana Shaji', 'Balagangadhar Reddy', 'Lekha Jeyabal', 'Lian Mathew', 'Vijayalakshmi S']
        subjcts = ['Inferential Statistics', 'Data Analytics', 'Database Management Systems', 'Multivariate Calculus', 'Operating Systems & Software Engineering']
        time = ['9:00 am - 9:50 am', '10:00 am - 10:50 am', '11:00 am - 11:50 am', '12:00 pm - 12:50 pm', '2:00 pm - 2:50 pm', '3:00 pm - 3:50 pm']

        print("\nEnter Professor name:")
        for i in profs:
            print("--->", i)
        professor = input("\n- ")
        if professor not in profs:
            print("\nInvalid Professor name. Please enter a valid name.")
            return

        course = "BSC DATA SCIENCE"

        print("\nEnter Subject:")
        for i in subjcts:
            print("--->", i)
        subject = input("\n- ")
        if subject not in subjcts:
            print("Invalid Subject. Please enter a valid subject.")
            return

        print('\nSelect Time:')
        for i in time:
            print("--->", i)
        times = input("- ")
        if times not in time:
            print("Invalid Time slot. Please enter a valid Time frame.")
            return

        date = input("\nEnter Date:")

        lecture = {
            "Slot": slot,
            "Date": date,
            "Professor": professor,
            "Course": course,
            "Subject": subject,
            "Time": times
        }

        self.lecture_tracker.append(lecture)
        del self.available_lectures[slot]
        time.remove(times)
        print("\nLecture scheduled successfully")
#-----------------------------------------------------------------------------------------------------------------------------
        
    def after_lecture_data(self):
        if not self.lecture_tracker:
            print("No lectures scheduled.")
            return

        slot = int(input("Enter the slot number to add after-lecture data: "))

        for lecture in self.lecture_tracker:
            if lecture["Slot"] == slot:
                students = int(input("Enter Number of Students Attended: "))
                lecture["Students"] = students
                print("\nLecture details added successfully.")
                return

        print("No schedule found for the given slot.")

#---------------------------------------------------------------------------------------------------------------------------------
        
    def display_lectures(self):
        print("\nLecture Details:")
        if not self.lecture_tracker:
            print("No lectures found.")
        else:
            df = pd.DataFrame(self.lecture_tracker)
            print(df)
#-----------------------------------------------------------------------------------------------------------------------------------------------
            
    def display_lectures_professor(self):
        profs = ['Ayana Shaji', 'Balagangadhar Reddy', 'Lekha Jeyabal', 'Lian Mathew', 'Vijayalakshmi S']
        professor = input("Enter the name of professor: ")
        print("Lectures by", professor, ":")

        lectures_found = False

        for lecture in self.lecture_tracker:
            if lecture["Professor"] == professor:
                print("Course:", lecture["Course"])
                print("Subject:", lecture["Subject"])
                print("Date:", lecture["Date"])
                print("Slot:", lecture["Slot"])
                print("Time:", lecture["Time"])
                lectures_found = True

        if not lectures_found:
            print("No lectures found for", professor)
#------------------------------------------------------------------------------------------------------------------------------------------
            
    def update_schedule(self):
        if not self.lecture_tracker:
            print("No lectures scheduled.")
            return

        slot = int(input("Enter the slot number to update the schedule: "))

        for lecture in self.lecture_tracker:
            if lecture["Slot"] == slot:
                print("Current Schedule:")
                print("Professor:", lecture["Professor"])
                print("Subject:", lecture["Subject"])
                print("Date:", lecture["Date"])
                print("Time:", lecture["Time"])

                profs = ['Ayana Shaji', 'Balagangadhar Reddy', 'Lekha Jeyabal', 'Lian Mathew', 'Vijayalakshmi S']
                subjcts = ['Inferential Statistics', 'Data Analytics', 'Database Management Systems', 'Multivariate Calculus', 'Operating Systems & Software Engineering']
                time = ['9:00 am - 9:50 am', '10:00 am - 10:50 am', '11:00 am - 11:50 am', '12:00 pm - 12:50 pm', '2:00 pm - 2:50 pm', '3:00 pm - 3:50 pm']

                print("\nUpdate Professor name:")
                for i in profs:
                    print("--->", i)
                new_professor = input("- ")
                if new_professor:
                    lecture["Professor"] = new_professor

                print("\nUpdate Subject: ")
                for i in subjcts:
                    print("--->", i)
                new_subject = input("- ")
                if new_subject:
                    lecture["Subject"] = new_subject

                print("\nUpdate Date: ")
                new_date = input("- ")
                if new_date:
                    lecture["Date"] = new_date

                print('\nUpdate Time:')
                for i in time:
                    print("--->", i)
                new_time = input("- ")
                if new_time:
                    lecture["Time"] = new_time

                print("\nSchedule updated successfully.")
                return

        print("No schedule found for the given slot.")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    def delete_schedule(self):
        if not self.lecture_tracker:
            print("No lectures scheduled.")
            return

        slot = int(input("Enter the slot number to delete the schedule: "))

        for lecture in self.lecture_tracker:
            if lecture["Slot"] == slot:
                self.available_lectures[slot] = True
                self.lecture_tracker.remove(lecture)
                print("Schedule deleted successfully.")
                return

        print("No schedule found for the given slot.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    def main(self, length):
        self.available_lectures = {slot: True for slot in range(1, length + 1)}
        print("\n----->------>------>----- WELCOME TO LECTURE TRACKER ---<------<------<-----")
        print("\nPlease Proceed,\n ")
        while True:
            print("\n1. Schedule Lecture")
            print("--------------------------------")
            print("2. After Lecture Data")
            print("--------------------------------")
            print("3. Display Lecture History")
            print("--------------------------------")
            print("4. Display Lectures by Professor")
            print("--------------------------------")
            print("5. Update Lecture")
            print("--------------------------------")
            print("6. Delete Lecture")
            print("--------------------------------")
            print("0. Quit")
            print("--------------------------------")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.schedule_lecture()
            elif choice == "2":
                self.after_lecture_data()
            elif choice == "3":
                self.display_lectures()
            elif choice == "4":
                self.display_lectures_professor()
            elif choice == "5":
                self.update_schedule()
            elif choice == "6":
                self.delete_schedule()
            elif choice == "0":
                self.csvfile()
                print("Thank you for using the lecture tracker!")
                break
            else:
                print("Invalid choice. Please try again.")


# Creating an instance of the LectureTracker class.
tracker = LectureTracker()

# Starting the program
length = int(input('Enter the length of Lectures : '))
tracker.main(length)
