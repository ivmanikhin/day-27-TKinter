import tkinter

window = tkinter.Tk()
window.title('That\'s GUI, boy!')
window.minsize(width=500,
               height=300)

my_label = tkinter.Label(text='That\'s label!',
                         font=('Arial', 24, 'bold'))
my_label.pack(expand=True)

window.mainloop()