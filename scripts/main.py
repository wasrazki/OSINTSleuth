import tkinter as tk 
from PIL import ImageTk, Image
from fpdf import FPDF 
#main frame
root = tk.Tk() 
root.title("Information Gathering")
root.geometry("1200x450")
root.resizable(False, False)
root.configure(bg="#1b1b22")
#image
img = ImageTk.PhotoImage(Image.open("./assets/bg.jpg"))
imagelabel= tk.Label(root, image=img, border=0)
imagelabel.pack()

# entry 
text="DOMAIN: example.com"
def on_entry_click(event):
    if entry.get() == text:
        entry.delete(0, tk.END)
        
def on_entry_leave(event):
    if not entry.get():
        entry.insert(0, text)
          
entry= tk.Entry(root, background="#1b1b22", font = ('courier', 15, 'bold'), border=0.5, fg="white", width=43)
entry.insert(0,text)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_entry_leave)
entry.place(x=265, y=250)


# button
import portscan
import opersys
import subdomainenumeration 
import dnsenumeration
import hiddendirectory
import emailgathering


class MyPDF(FPDF):
    def header(self):
        self.set_fill_color(255, 153, 153)  # Set text color to red
        self.set_font('Arial', 'B', 25)  # Set font and size
        self.cell(0, 10, 'OSINT REPORT ', 0, 1, 'C', 1)  # Create a cell with title text and a border
        self.ln(10)  # Move down to create space for text

    def chapter_title(self, title):
        self.set_fill_color(153, 204, 255)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_fill_color(255, 255, 255)  # Set background color to white
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate():
    domain= entry.get()
    portscanningoutput= portscan.portscanning(domain)
    osoutput= opersys.os_fingerprint(domain) 
    dnsoutput= dnsenumeration.enumerate_record_types(domain)  
    #subdomainoutput = subdomainenumeration.subdomain(domain)  
    #diroutput= hiddendirectory.hidden_directory(domain)
    emailoutput = emailgathering.get_email(domain)

    # Create a PDF instance
    pdf = MyPDF()
    pdf.add_page()

    #add the information to the pdf file 
    pdf.chapter_title("DNS INFORMATION")
    pdf.chapter_body(dnsoutput)
    pdf.chapter_title("OS FINGERPRINTING")
    pdf.chapter_body(osoutput)
    pdf.chapter_title("PORT SCANNING")
    pdf.chapter_body(portscanningoutput) 
    pdf.chapter_title("SUBDOMAIN ENUMERATION")
    #pdf.chapter_body(subdomainoutput)
    pdf.chapter_title("DIRECTORY ENUMERATION")
    #pdf.chapter_body(diroutput) 
    pdf.chapter_title("EMAIL GATHERING")
    pdf.chapter_body(emailoutput)
    
    # save the report  
    pdf_file = "./reports/my_report.pdf"
    pdf.output(pdf_file)


report_button = tk.Button(root, text="Generate report", font = ('courier', 11, 'bold'), command=generate)
report_button.place(x=800,y=250)

#credits
developer_label = tk.Label(root,text="DEVELOPED BY Razki Wassim", font = ('courier', 9, 'bold'), bg="#1b1b22", fg="white")
developer_label.place(x=1000, y=420)




root.mainloop()  


