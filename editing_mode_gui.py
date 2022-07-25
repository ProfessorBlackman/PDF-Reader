# This is the script to create the editing mode window
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from PyPDF2 import *
from pyperclip3 import *


def editing_mode():
    # Create an instance of tkinter frame
    win = Tk()
    # Set the Geometry
    win.geometry("750x450")

    # Opening active file in editing window

    # ---------------------------------------Functionz---------------------------------------------
    def open_edit_pdf():
        # Opening the pdf file and displaying it with PyPDF2
        file = fd.askopenfilename(title="Select a PDF", filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))
        if file:
            # Open the PDF File
            pdf_file = PdfFileReader(file)
            # Select a Page to read
            page = pdf_file.getPage(0)
            # Get the content of the Page
            content = page.extractText()
            # Add the content to TextBox
            text.insert(1.0, content)

    def copy_pdf():
        copy(text.get())

    def cut_pdf():
        copy(text.get())
        text.delete()

    def paste_pdf():
        print("hello")

    def mark_pdf():
        print("hello")

    def save_as():
        print("hello")

    def save_pdf():
        print("hello")

    # This is the part where I design the GUI
    label_frame = LabelFrame(win, text='Toolbar')
    label_frame.pack(side="top", fill='x', ipadx=2, ipady=2.3)

    # Create a Text Box
    text = Text(win, width=80, height=30)
    text.pack(side='bottom', pady=20)

    # Creating the button to be pressed to open the pdf file
    Button(label_frame, text='Open', command=open_edit_pdf).grid(column=0, row=0, padx=5)
    Button(label_frame, text='Copy', command=copy_pdf).grid(column=1, row=0, padx=5)
    Button(label_frame, text='Cut', command=cut_pdf).grid(column=2, row=0, padx=5)
    Button(label_frame, text='Paste', command=paste_pdf).grid(column=3, row=0, padx=5)
    Button(label_frame, text='Mark', command=mark_pdf).grid(column=4, row=0, padx=5)
    Button(label_frame, text='Save As', command=save_as).grid(column=5, row=0, padx=5)
    Button(label_frame, text='Save', command=save_pdf).grid(column=6, row=0, padx=5)

    win.mainloop()
