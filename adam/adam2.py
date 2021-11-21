
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import cm, inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, BaseDocTemplate
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from reportlab.platypus.doctemplate import FrameBreak, PageTemplate
from reportlab.platypus.frames import Frame
from invoice import invoice


def draw_invoice():
    def draw_company_info(c):
        pass

    # c = canvas.Canvas('i1.pdf')
    styles = getSampleStyleSheet()
    styleH1 = styles['Heading1']
    styleH2 = styles['Heading2']
    styleN = styles['Normal']

    ci = invoice['companyInfo']
    # doc = BaseDocTemplate('invoice1.pdf')
    doc = SimpleDocTemplate('invoice1.pdf', pagesize=A4, leftMargin=1*cm,
                            rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm)
    
    name = f"<b><font size=14>{ci['name']}</font></b><br/>{ci['address1']} {ci['address2']}"
    ciNamePara = Paragraph(name, styleN)
    # ciNamePara.wrap(10,10)
    taxInvoicePara = Paragraph('Tax invoice', styleH2)
    ciAddressPara = Paragraph(ci['address1'] + ci['address2'], styleN)
    story = [ciNamePara, FrameBreak(), ciAddressPara]
    frameLeft = Frame(cm,24*cm, 10*cm, 5*cm, showBoundary=1)
    frameRight = Frame(11.5*cm, 24*cm, 9*cm, 5*cm, showBoundary=1)
    # frameLeft
    # frameLeft.addFromList(story)
    page = PageTemplate(frames=[frameLeft, frameRight])
    doc.addPageTemplates(page)

    doc.build(story)


draw_invoice()


def canvas_ex():
    c = canvas.Canvas('hello.pdf')  # creates a file hello.pdf
    c.translate(10 * mm, 10 * mm)  # moves the origin as x= 10mm, y = 10 mm
    width, height = A4
    print('Width:', width, ' height:', height)
    c.setFont('Helvetica', 14)
    # draws line starting from new origin which is 10mm, 10mm
    c.line(0, 0, 0, 1.7*inch)
    c.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch, fill=0)  # draw a rectangle
    # at point 10,10 draw string. There are drawRightString, drawCenterString
    c.drawString(10, 10, 'Hello world')
    c.showPage()  # ends the page and resets font, colors etc.
    c.save()


def flowable_ex():
    doc = SimpleDocTemplate("example_flowable.pdf", pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    my_text1 = "Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
    my_text2 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
    para1 = Paragraph(my_text1, getSampleStyleSheet()['Normal'])
    para1.beginText(1*inch, 1*inch)
    doc.build([
        # Paragraph(my_text1.replace("\n", "<br />"), getSampleStyleSheet()['Normal']),
        para1,
        Paragraph(my_text2, getSampleStyleSheet()['Normal'])
    ])
    print('ok')


def canvas_paragraph():
    c = canvas.Canvas('hello.pdf')
    my_text1 = 'Lorem Ipsum has been the industry standard dummy text ever since the 1500s,'
    styleN = getSampleStyleSheet()['Normal']
    style1 = ParagraphStyle({
        'alignment': 0,
        'borderColor': '#000000',
        'borderWidth': 1,
        'backColor': '#FFFF00'
    })
    p1 = Paragraph(my_text1, style1)
    p1.wrap(200, 150)

    p2 = Paragraph(my_text1, styleN)
    p2.wrap(2*cm, 200*cm)

    p1.drawOn(c, 20, 100)
    p2.drawOn(c, 300, 100)
    c.showPage()
    c.save()


def frame_canvas_paragraph():
    c = canvas.Canvas('hello.pdf')
    c.translate(0, 300)
    my_text1 = 'Lorem Ipsum has been the industry standard dummy text ever since the 1500s,'
    styleN = getSampleStyleSheet()['Normal']
    p1 = Paragraph(my_text1, styleN)
    # p1.wrap(100, 100)

    p2 = Paragraph(my_text1, styleN)
    # p2.wrap(2*cm, 200*cm)
    story = [p1, p2]
    f = Frame(inch, inch, 2*inch, 3*inch, showBoundary=1)
    f.addFromList(story, c)
    c.save()


def simple_doc_template():
    styleN = getSampleStyleSheet()['Normal']
    styleH = getSampleStyleSheet()['Heading6']
    my_text1 = 'Lorem Ipsum has been the industry standard dummy text ever since the 1500s,'
    my_text2 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,"
    para1 = Paragraph(my_text1, styleN)
    para2 = Paragraph(my_text2, styleH)
    story = [para1, para2]
    doc = SimpleDocTemplate('myDoc.pdf')
    doc.build(story)


def docTemplate_page_frame_para():
    c = canvas.Canvas('hello.pdf')
    styleN = getSampleStyleSheet()['Normal']
    styleH = getSampleStyleSheet()['Heading6']
    my_text1 = 'Lorem Ipsum has been the industry standard dummy text ever since the 1500s,'
    my_text2 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,"

    style1 = ParagraphStyle({
        'alignment': 0,
        'borderColor': 'black',
        'borderWidth': 1
    })

    para1 = Paragraph(my_text1, style1)
    para2 = Paragraph(my_text2, styleH)

    frame1 = Frame(inch, inch, 2*inch, 3*inch, showBoundary=1)
    frame2 = Frame(4*inch, inch, 2*inch, 3*inch, showBoundary=1)
    frame1.addFromList([para1], c)
    frame2.addFromList([para2], c)
    page = PageTemplate(frames=[frame1, frame2])
    doc = SimpleDocTemplate('myDoc.pdf')
    doc.addPageTemplates(page)
    doc.build([para1, para2])


# canvas_paragraph()
# docTemplate_page_frame_para()

# import simplejson as json
# import pandas as pd
# import numpy as np

# jDataString = '''[
# {
#     "country": "India",
#     "capital":"New Delhi",
#     "population":"130CR"
# },
# {
#     "country": "Usa",
#     "capital":"Wash",
#     "population":"50CR"
# }]

#     '''
# # df = pd.read_excel('sales-funnel.xlsx')
# # df["Status"] = df["Status"].astype("category")
# # df["Status"].cat.set_categories(
# #     ["won", "pending", "presented", "declined"], inplace=True)
# # df1 = pd.pivot_table(df, index=["Manager", "Rep"], values=[
# #                      "Price", "Quantity"], aggfunc=np.sum, columns="Product")
# # print(df)
# # print(df1)
# d1 = [
#     {
#         "accName": "Conveyance",
#         "amount": 100,
#         "dc": "D",
#         "remarks": "shop to office"
#     },
#     {
#         "accName": "Cash A/c",
#         "amount": 700,
#         "dc": "C",
#         "remarks": "shop to office"
#     },
#     {
#         "accName": "Showroom Exp",
#         "amount": 500,
#         "dc": "D",
#         "remarks": "Repairs of items"
#     },
#     {
#         "accName": "Office exp",
#         "amount": 100,
#         "dc": "C",
#         "remarks": "Furniture repairs"
#     },
#     {
#         "accName": "Office exp",
#         "amount": 200,
#         "dc": "D",
#         "remarks": "Mix repairs"
#     },
#     {
#         "accName": "Cash A/c",
#         "amount": 200,
#         "dc": "C",
#         "remarks": "paid"
#     },
#     {
#         "accName": "Cash A/c",
#         "amount": -1200.23,
#         "dc": "O",
#         "remarks": "paid"
#     }
# ]
# df = pd.DataFrame(d1)
# pivot = pd.pivot_table(df, index=["accName"], columns="dc",
#                        values="amount", aggfunc=np.sum, fill_value=0).reindex(columns=['O', 'D', 'C'])
# pivot.rename(
#     columns={
#         'D': 'Debit',
#         'C': 'Credit',
#         'O': 'Opening'
#     },
#     inplace=True
# )

# pivot['Closing'] = pivot['Opening'] + pivot['Debit'] - pivot['Credit']


# pivot.loc['total'] = pivot.select_dtypes(pd.np.number).sum() # for summary
# pivot['op_dc'] = pivot['Opening'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
# pivot['clos_dc'] = pivot['Closing'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
# pivot = pivot.reindex(
#     columns=['Opening','op_dc', 'Debit', 'Credit','Closing', 'clos_dc']
# )
# pivot['Opening'] = pivot['Opening'].apply(lambda x: x if x>=0 else -x)
# pivot['Closing'] = pivot['Closing'].apply(lambda x: x if x>=0 else -x)

# json = pivot.to_json(orient='table')
# print(pivot)
# print(json)
