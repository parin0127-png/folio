import sys
sys.path.append("C:\\Users\\Parin\\OneDrive\\Desktop\\FOLIO")
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import mm
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TITLE_STYLE = ParagraphStyle("title", fontSize = 22, textColor = colors.HexColor("#2C3E50"), fontName = "Helvetica-Bold", alignment = 1)
BODY_STYLE = ParagraphStyle("body", fontSize = 11, leading = 18, textColor = colors.HexColor("#2C3E50"), fontName = "Helvetica")

def border(canvas, doc):
    canvas.setStrokeColor(colors.HexColor("#2980B9"))
    canvas.setLineWidth(2)
    canvas.rect(15*mm, 15*mm, A4[0] - 30*mm, A4[1] - 30*mm)

def generate_pdf(title,text):
    """create and generate a pdf document with any given text or content"""
    path = os.path.join(BASE_DIR, "..", "..", "outputs", "reports.pdf")
    os.makedirs(os.path.dirname(path), exist_ok = True) 

    doc = SimpleDocTemplate(path, pagesize = A4, topMargin = 30*mm, bottomMargin = 30*mm, leftMargin = 35*mm, rightMargin = 35*mm)

    story = [
        Spacer(1, 10*mm),
        Paragraph(title, TITLE_STYLE),
        Spacer(1, 10*mm),
        HRFlowable(width = "100%", thickness = 1, color = colors.HexColor("#2980B9")),
        Spacer(1, 10*mm),
        Paragraph(text.replace("\n", "<br/>"), BODY_STYLE)
    ]

    doc.build(story, onFirstPage = border, onLaterPages = border)
    return f"> Report Saved to {path}"