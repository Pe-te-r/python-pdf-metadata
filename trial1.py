import PyPDF2 as pdf
import os

file='trial1.pdf'

new_file='new_file.pdf'



def validCheck(path):
    return os.path.exists(path)


# class instant for having an object that can read metadata and write to metadata

class Pdf_file:
    # takes file path for reading metadata from    
    def read_metadata(self,file):
        if validCheck(file):
            data=pdf.PdfReader(file)         
            metadata=data.metadata
            page=len(data.pages)
            for key,value in metadata.items():
                print(f'{key} =>  {value}')
    
    # takes two file path first for the file for writing metadata and where the file path will be saved after a new is created with metadata
    def write_metadata(self,file,new_file):

        self.writer=pdf.PdfWriter()
        if validCheck(file):
            data=pdf.PdfReader(file)
        for page in data.pages:
            self.writer.add_page(page)
    
        self.writer.add_metadata({
        "/Author": "Martin",
        "/Producer": "Libre Writer",
        "/Home":"Nairobi"
    })

        with open(new_file,'wb')as file:
            self.writer.write(file)

    
            

pdf_file=Pdf_file()

pdf_file.read_metadata(file)

pdf_file.write_metadata(file,new_file)