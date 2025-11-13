class PDFPrinter:
    def print_file(self,name):
        print("Printing",name,"as PDF")
class Inkjet():
    def print_file(self,name):
        print("Printing",name,'using inkjet')
def perform(printer,file):
    printer.print_file(file)
    
    
perform(PDFPrinter(), "form.pdf")
perform(Inkjet(),"invoice.docx")