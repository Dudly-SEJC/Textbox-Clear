from tkinter import *
def clear_textbox():
    text_box.delete(1.0, 2.0)  # 'end', means lines get deleted from row 1 to the very end, you may also specify a certain line such as 5.0 instead of 'end'
 # "1.0" mean Line 1 , first char.
 #  Similarly END is the string end including the line break.

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#84BF04')
message = '''
Dear Reader,
Don't let this situation
blind your future. We at
PythonGuides write tutorials
with real life examples to
make you understand the concept
in best possible way.
Thanks & Regards,
Team PythonGuides '''

text_box = Text(ws, height=13, width=40) # width can set number of columns in text box
text_box.pack(expand=True)
text_box.insert('end', message)
Button(ws, text='Clear Button', width=15, height=2, command=clear_textbox).pack(expand=True)
ws.mainloop()
