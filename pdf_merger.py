from PyPDF2 import PdfMerger

all_pdf = ["1.pdf", "2.pdf"]

our_merger = PdfMerger()

for new_pdf in all_pdf:
    our_merger.append(new_pdf)

our_merger.write("3.pdf")
our_merger.close()

