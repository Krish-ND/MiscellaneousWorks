import PyPDF2
import os

#List of PDFs to merge
pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf']

merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()