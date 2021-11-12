from tkinter import *

FONT = ('Arial', 16)


# button action
def button_click():
    kilometers.config(text=round(float(miles.get()) * 1.609344, 2))


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=10, pady=10)

# label
is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=0)
is_equal_to.config(padx=3, pady=3)

kilometers = Label(text="0", font=FONT)
kilometers.grid(column=1, row=1)
kilometers.config(padx=3, pady=3)

km = Label(text="km", font=FONT)
km.grid(column=2, row=1)
km.config(padx=3, pady=3)

ml = Label(text="miles", font=FONT)
ml.grid(column=2, row=0)
ml.config(padx=3, pady=3)

# button itself
calc = Button(text='Calculate', font=FONT, command=button_click)
calc.grid(column=1, row=2)
calc.config(padx=3, pady=3)

# 1 string text input
miles = Entry(font=FONT, width=5)
miles.insert(END, string="0")
miles.grid(column=1, row=0)

# # multi-string text input
# text_box = Text(height=3,
#                 font=('Arial', 16),
#                 width=10)
# text_box.insert(END, "Some text")
# text_box.focus()
# text_box.pack()
#
#
# # spinbox action
# def spinbox_act():
#     my_label.config(text=spinbox.get())
#
#
# # spinbox itself
# spinbox = Spinbox(from_=0,
#                   to=10,
#                   width=3,
#                   font=('Arial', 16),
#                   command=spinbox_act)
# spinbox.pack()
#
#
# # scale action
# def scale_act(value):
#     my_label.config(text=value)
#
#
# # scale itself
# scale = Scale(from_=0,
#               to=100,
#               font=('Arial', 16),
#               command=scale_act)
# scale.pack()

window.mainloop()
