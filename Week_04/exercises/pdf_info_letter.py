'''Python code starts here'''

from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Document format
doc = SimpleDocTemplate("pdf_info_letter.pdf", pagesize=letter,
						 rightMargin=72, leftMargin=72,
						 topMargin=72, bottomMargin=18)

# Story, logo & style
Story=[]

# Image
logo = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Lanz_Bulldog_1928-crop.jpg"

# Variables
var01 = 'Lanz Bulldog'
var02 = 'Heinrich Lanz AG in Mannheim'
var03 = 1921
var04 = 1956
var05 = '220,000'

formatted_time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
full_name = "busy-ZHAW-student"
address_parts = ["Theaterstrasse 17", "Winterthur, 8400"]
img = Image(logo, 3*inch, 2.5*inch)
Story.append(img)
Story.append(Spacer(1, 48))
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '%s' % formatted_time
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 24))

# Create return address
ptext = '%s' % full_name
Story.append(Paragraph(ptext, styles["Normal"]))       
for part in address_parts:
	ptext = '%s' % part.strip()
	Story.append(Paragraph(ptext, styles["Normal"]))   
Story.append(Spacer(1, 24))

# Content
ptext = 'Dear %s' % full_name.split()[0].strip() + ','
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
ptext = f'''Did you know, that the <b><font color="blue">{var01}</font></b> was a series 
         of tractors manufactured by <b><font color="blue">{var01}</font></b>, Baden-Württemberg,
         Germany. Production started in <b><font color="blue">{var03}</font></b> with
         the Lanz HL, and various versions of the Bulldog were produced up to 1960,
         one of them being the Lanz Bulldog D 9506. John Deere purchased Lanz in
        <b><font color="blue">{var04}</font></b> and started using the name "John Deere Lanz"
         for the Lanz product line. A few years after the Bulldog was discontinued
         the Lanz name fell into disuse. The Lanz Bulldog was one of the most popular
         German tractors, with over <b><font color="blue">{var05}</font></b> of them produced
         in its long production life. The name "Bulldog" is widely used in Germany as
         a synonym for tractors even today, especially in Bavaria.'''

Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = 'Thank you very much!'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 24))
ptext = 'Sincerely,'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 24))
ptext = 'Your lecturer'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
doc.build(Story)

'''Python code ends here'''