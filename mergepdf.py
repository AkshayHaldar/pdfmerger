from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs=[]
n=int(input("enter your number of pdf you want to merge?:"))
for i in range(0,n):
    name=input(f"enter your pdf name {i+1}:")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()