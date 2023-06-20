LECTURE SCHEDULE & TRACKER

This application is created for professors to book lectures and track them conveniently and provides a simple approach to booking a lecture. The main logic of the program is that the day is divided into several slots and time frames respectively, the lecturers themselves can choose the slot they desire which then is accepted by the application. Once the slot is booked the rest of the required information is entered and stored in an Excel file which allows them to keep track of their lectures at any time.


Function 1 - Schedule_lecture

The program starts by inquiring about the length of lectures the user wishes to schedule. Once the length is entered the available slots are presented to the user, they can then choose the slot and add additional information required to schedule their lecture. After the slot is selected they are asked to enter the professor's name, subject, date and time. Following the format given in the options is important here as the application rejects the invalid answers. The lecture is then scheduled successfully once all these details are entered properly.


Function 2 - After_lecture_data

This is the function that allows the user to enter the number of students who attended the scheduled class, i.e. the attendance. The function starts by asking the slot number which is the lecture number. Once the user enters the slot, the function goes to the lecture booked in that slot and allows the user to add the number of students who attended the class. As the name implies this information is added by the user after the lecture is conducted


Function 3 - Display_lecture_history

This is the function responsible for displaying all the lectures scheduled so far. Once a lecture is scheduled the user can select this function and see the scheduled lectures. The serial number, the professor's name, subject, date, time and course. if the user has entered the after-lecture data, that is also displayed along with the previously mentioned information. The information is displayed in a tabular format as dataframe is incorporated into the function. This allows the display to look more organised and readable.


Function 4 - Display_Lectures_by_Professor

this function is very similar to the Display_lecture_history, the only difference is that the lectures displayed will be that of a specific professor. This allows us to keep track of each professor individually. The function returns all the lectures booked by the selected professor so far. The professor themselves can monitor their lectures individually.


Function 5 - Update_lecture

As the name implies this function allows the user to update the details of the scheduled lectures. At the start of the function, the user is asked to enter the number of the slot they desire to delete. once it is entered the user is given the freedom to update all the details existing in the slot such as the professor's name, subject, date, and time. Once the updation of the information is the program updates and stores accordingly. The updation is also done in the display. 


Function 6 - Delete_lecture

This function allows the user to delete a specific slot at a time. The user is asked to enter the slot they wish to delete, once it is entered the schedule is deleted from the program, which means it is also deleted from the CSV file as well as the display it is stored in. 

Data Storage - The storage method chosen here is to save all the schedules to a CSV file, this allows tracking and monitor the schedules. There is also real-time updation of the schedules booked. The details recorded in the CSV file include the slot number, the professor's name, the subject and the course. As there are no complex procedures involving data storage in this program, a CSV file meets our criteria for storage.

This is the Lecture Schedule & Tracking Application in a nutshell.




