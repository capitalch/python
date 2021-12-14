from fpdf import FPDF, HTMLMixin
from datetime import datetime, date
from invoice import invoice


class FPDF(FPDF, HTMLMixin):
    def header(self):
        self.cell(150)
        self.cell(0, 5, 'Sushant Agrawal', ln=1)
        self.cell(150)
        self.cell(0, 5, '12 J. L. Nehru Road', ln=1)
        self.cell(150)
        self.cell(0, 5, 'Kolkata 700013', ln=1)
        self.ln(20)
        self.cell(0,5,'jkjjk', ln=1)

def get_long_html():
        ht = []
        for i in range(2000):
            ht.append(f'''<div style="color:red">This is a test line {i}</div><br/>''')
        return(''.join(ht))

pdf = FPDF()
pdf.set_font('Helvetica', '', 12)
pdf.add_page()

pdf.set_font('Helvetica', 'B', 16)
pdf.write_html(get_long_html())
# pdf.cell(0, 10, 'Hello world')
pdf.output('example1.pdf', 'F')
