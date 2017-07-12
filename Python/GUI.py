from tkinter import *
import time
root = Tk()

root.wm_title("SkyGym Workout Tracker")

rep_count = 0
set_count = 0
weight_count = 40


rep_label = Label(root,
                  text=rep_count,
                  padx=50,
                  font=("Century Gothic", 100))
rep_label.grid(row=0,column=0)

rep_text = Label(root,
                 text="Reps",
                 
                 font=("Century Gothic", 32))
rep_text.grid(row=1,column=0)

set_label = Label(root,
                  text=set_count,
                  padx=50,
                  font=("Century Gothic", 100))
set_label.grid(row=0,column=1)

set_text = Label(root,
                 text="Sets",
                 font=("Century Gothic", 32))
set_text.grid(row=1,column=1)

weight_label = Label(root,
                  text=weight_count,
                  padx=50,
                  font=("Century Gothic", 100))
weight_label.grid(row=0,column=2)

weight_text = Label(root,
                 text="Weight (lbs)",
                 font=("Century Gothic", 24))
weight_text.grid(row=1,column=2)



for i in range (0,4):
    for j in range (0,9):
        time.sleep(1)
        rep_count = rep_count + 1
        rep_label.config(text = rep_count)
        root.update()
    rep_count = 0
    rep_label.config(text = rep_count)
    set_count = set_count + 1
    set_label.config(text = set_count)
    root.update()

root.mainloop()


