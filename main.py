# This is the script to create a PDF reader software. The reader can open, extract text from, and edit a pdf.
from tkinter import filedialog as filed

from tkPDFViewer import tkPDFViewer as pdfviewer

from editing_mode_gui import *

root = Tk()
root.geometry("750x450")


#----------------------------------Functionz-------------------------------------------------

# Function to open pdf file
def open_pdf():
    file = filed.askopenfilename(title="Select a PDF", filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))
    if file:
        # Open the PDF File
        # create object like this.
        variable1 = pdfviewer.ShowPdf()
        # Add your pdf location and width and height.
        variable2 = variable1.pdf_view(root, pdf_location=file, width=90, height=100)
        variable2.pack()


# This is the part where I design the GUI
label_frame = LabelFrame(root, text='Toolbar')
label_frame.pack(side="top", fill='x', ipadx=2, ipady=2.3)
# Creating the buttons to perform operations on the pdf file
Button(label_frame, text='Open', command=open_pdf).grid(column=2, row=0, padx=5)
Button(label_frame, text='Edit', command=editing_mode).grid(column=3, row=0, padx=5)

root.mainloop()
