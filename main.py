"""Создает в указанной папке папку с pdf-файлами,
 повернутыми на определенное количество градусов"""

import os
from PyPDF4 import PdfFileReader, PdfFileWriter

def get_file_list(files_path:str) -> list:
    filelist = []
    for element in os.listdir(files_path):
        if element.endswith('.pdf'): filelist.append(element)
    return filelist

def main(inputpath:str, filelist:list, turndegrees:int):
    output_writer = PdfFileWriter()
    os.chdir(inputpath)
    os.mkdir("rotated" + str(turndegrees))

    for filename in filelist:
        with open(inputpath+filename, "rb") as inputf:
            pdfOne = PdfFileReader(inputf)
            numPages = pdfOne.numPages

            for i in range(numPages):
                page = pdfOne.getPage(i).rotateClockwise(turndegrees)
                output_writer.addPage(page)

            with open(inputpath + "rotated" + str(turndegrees) + "//" + filename, "wb") as outfile:
                output_writer.write(outfile)

            print(f"{filename} rotated {turndegrees} degrees!")


if __name__ == "__main__":
    filepath = input('Введите путь:\n')
    if not filepath.endswith('\\'): filepath += '\\'
    turndegrees = int(input('Введите угол поворота по часовой стрелке:\n'))
    # print(get_file_list(filepath))
    main(filepath,get_file_list(filepath),turndegrees)
