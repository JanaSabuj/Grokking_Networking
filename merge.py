import os
from PyPDF2 import PdfFileMerger

path_to_files = '/home/sabuj/projects/Grokking_Networking' # place root directory ?
lo = 1 # place first file id ? eg lo_fname.pdf
hi = 115 # place last file id ? eg hi_fname.pdf
final_pdf_name = "0_GCN.pdf" # final pdf name ?

files_arr = []

# traverse files
for root, dirs, file_names in os.walk(path_to_files):
    for file in file_names:
        if (file == final_pdf_name or file.split('.')[-1] != "pdf"):
            print("Excluding from merging....", file) 
            continue
        files_arr.append(file)

# sort the files_arr
files_arr.sort(key= lambda x: int(x.split('_')[0]))

#Create an instance of PdfFileMerger() class
merger = PdfFileMerger()

# merge files in order
for file in files_arr:
    print("Merging", file, ".............")
    merger.append(file)

#Write out the merged PDF file
merger.write(final_pdf_name)
print("FINAL PDF GENERATED: ", final_pdf_name)
merger.close()