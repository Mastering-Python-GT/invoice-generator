from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from datetime import date

class SalesInvoice():
    def __init__(self,company,email,phone,companyAddress,table,logo,total,discount,payment,rest,client,clientAddress,invoiceNumber) -> None:
        d_ate = date.today()
        today = d_ate.strftime("%d-%m-%Y")
        file = invoiceNumber+"_"+client+".pdf"
        my_canvas = canvas.Canvas(file, pagesize=A4)
        mystyle = ParagraphStyle('my style',fontName='Helvetica',fontSize=10,leading=15)
        my_canvas.setLineWidth(.5)
        my_canvas.setFont('Helvetica-Bold', 18)
        my_canvas.drawString(24, 817, company)
        my_canvas.setFont('Helvetica', 12)
        my_canvas.drawString(24, 800, companyAddress)
        my_canvas.drawString(24, 783, phone)
        my_canvas.drawString(24, 766, email)
        my_canvas.drawImage(logo, 460, 760, width=60, height=60)
        my_canvas.setFont('Helvetica-Bold', 15)
        my_canvas.drawCentredString(297.5, 735, 'Sales Invoice')
        my_canvas.setFont('Helvetica', 10)
        my_canvas.line(24, 740, 230, 740)
        my_canvas.line(360, 740, 571, 740)
        my_canvas.drawString(24, 720, 'Client :')
        my_canvas.drawString(75, 720, client)
        my_canvas.drawString(473, 720, 'N° Invoice :')
        my_canvas.drawRightString(571, 720, invoiceNumber)
        my_canvas.drawString(24, 703, 'Address :')
        my_canvas.drawString(474, 703, 'Date :')
        my_canvas.drawRightString(571, 703, today)

        p1 = Paragraph(clientAddress, mystyle)

        p1.wrapOn(my_canvas, 200, 100)
        p1.drawOn(my_canvas, 75, 684)

        my_canvas.line(24, 670, 571, 670)

        my_canvas.setFont('Helvetica-Bold', 9)

        my_canvas.drawCentredString(49 , 657, 'N°Product')
        my_canvas.drawCentredString(144, 657, 'Product')
        my_canvas.drawCentredString(250, 657, 'Quantity')
        my_canvas.drawCentredString(350, 657, 'Price')
        my_canvas.drawCentredString(490, 657, 'Amount')


        my_canvas.line(24, 650, 571, 650)
        my_canvas.setFont('Helvetica', 9)

        line_y = 650

        row = table.rowCount()

        for i in range(row):
            if line_y <= 30 and line_y >= 0:

                my_canvas.showPage()
                my_canvas.setFont('Helvetica', 9)
                line_y = 817

                my_canvas.line(24, line_y, 571, line_y)

                line_y = line_y - 13

                my_canvas.drawCentredString(49 , line_y, table.item(i,0).text())
                my_canvas.drawCentredString(144, line_y, table.item(i,1).text())
                my_canvas.drawCentredString(250, line_y, table.item(i,2).text())
                my_canvas.drawCentredString(350, line_y, table.item(i,3).text())
                my_canvas.drawCentredString(490, line_y, table.item(i,4).text())

                line_y = line_y - 7

                my_canvas.line(24, line_y, 571, line_y)

            else:
                line_y = line_y - 13

                my_canvas.drawCentredString(49, line_y, table.item(i,0).text())
                my_canvas.drawCentredString(144, line_y, table.item(i,1).text())
                my_canvas.drawCentredString(250, line_y, table.item(i,2).text())
                my_canvas.drawCentredString(350, line_y, table.item(i,3).text())
                my_canvas.drawCentredString(490, line_y, table.item(i,4).text())

                line_y = line_y - 7

                my_canvas.line(24, line_y, 571, line_y)

        if line_y >= 30 and line_y <= 70:
            line_y = line_y = 817
            my_canvas.showPage()
            my_canvas.setFont('Helvetica', 9)

        my_canvas.setFont('Helvetica-Bold', 10)
        my_canvas.drawRightString(500, line_y-20, 'Total :')
        my_canvas.drawRightString(500, line_y-35, 'Discount :')
        my_canvas.drawRightString(500, line_y-50, 'Payment :')
        my_canvas.drawRightString(500, line_y-65, 'Rest :')

        my_canvas.setFont('Helvetica', 10)
        my_canvas.drawRightString(571, line_y-20, total)
        my_canvas.drawRightString(571, line_y-35, discount)
        my_canvas.drawRightString(571, line_y-50, payment)
        my_canvas.drawRightString(571, line_y-65, rest)

        my_canvas.save()