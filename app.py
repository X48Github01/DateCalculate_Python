import datetime
from datetime import datetime, timedelta
import tkinter as tk
from tkcalendar import DateEntry
import babel.numbers
from babel.numbers import *

def calculate_date_diff():
    date_format = "%Y-%m-%d"

    # Get the date strings from the input fields
    date_x = entry_date_x.get_date().strftime(date_format)
    date_y = entry_date_y.get_date().strftime(date_format)

    # Convert the date strings to datetime objects
    datetime_x = datetime.datetime.strptime(date_x, date_format)
    datetime_y = datetime.datetime.strptime(date_y, date_format)

    # Calculate the difference between the dates in days
    delta = datetime_y - datetime_x
    days = delta.days

    # Calculate the number of years and months in the delta
    years = days // 365
    days -= years * 365

    months = days // 30.44
    days -= months * 30.44

    # Round months and days to nearest integer
    months = int(round(months))
    days = int(round(days))

    # If months equals 12, increment years and set months to 0
    if months == 12:
        years += 1
        months = 0

    # Format the result as "x years y months z days"
    result = f"ระยะเวลาในการปฏิบัติงานของท่านคือ\n{years} ปี / {months} เดือน / {days} วัน"

    # Update the label with the result
    label_result.config(text=result)
    label_result.config(bg="lightgray", fg="blue", font=("Arial", 16, "bold"))

# Create the GUI
root = tk.Tk()
root.geometry("800x600")
root.title("Date Difference Calculator by X4815162342")

# Create the title label
label_title = tk.Label(root, text="โปรแกรมคำนวณระยะเวลาในการทำงาน\nBy X4815162342", font=("Arial", 24, "bold"))
label_title.pack(side="top", pady=20)

# Create the input fields
frame_inputs = tk.Frame(root)
frame_inputs.pack(expand=True)

#default_date_x = datetime.datetime.strptime('2561-04-02', '%Y-%m-%d')
#default_date_x = datetime.datetime.strptime('2561-04-02', '%Y-%m-%d')
label_date_x = tk.Label(frame_inputs, text="วันที่เริ่มปฏิบัติงาน : ", font=("Arial", 20, "bold"))
label_date_x.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_date_x = DateEntry(frame_inputs, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-MM-dd', font=("Arial", 16, "bold"))
entry_date_x.grid(row=0, column=1, padx=10, pady=10)


label_date_y = tk.Label(frame_inputs, text="วันสุดท้ายของเดือนที่ปฏิบัติงาน : ", font=("Arial", 20, "bold"))
label_date_y.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_date_y = DateEntry(frame_inputs, width=12,background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-MM-dd', font=("Arial", 16, "bold"))
entry_date_y.grid(row=1, column=1, padx=10, pady=10)

label_explain = tk.Label(root,text="สามารถพิมพ์ ปี/เดือน/วัน เป็น พ.ศ. ได้เลยครับ เช่น\n\n2537 - 05 - 31\nพ.ศ. / เดือน / วัน", font=("Arial", 14, "bold"))
label_explain.pack(pady=20)

#Create the calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_date_diff, bg="green", fg="white", font=("Arial", 16, "bold"))
button_calculate.pack(pady=20)

#Create the exit button
button_exit = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Arial", 14, "bold"))
button_exit.pack(pady=10)

#Create the result label
label_result = tk.Label(root, text="", font=("Arial", 16, "bold"))
label_result.pack(pady=20)

#Run the GUI
root.mainloop()
