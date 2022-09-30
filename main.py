"""Создает в указанной папке папку с pdf-файлами,
 повернутыми на определенное количество градусов"""

import os
from PyPDF4 import PdfFileReader, PdfFileWriter

def get_file_list() -> (list, str):
    filepath = ''
    while not os.path.isdir(filepath):
        filepath = input('Введите путь:\n')
    if not filepath.endswith('\\'): filepath += '\\'
    filelist = []
    for element in os.listdir(filepath):
        if element.endswith('.pdf'): filelist.append(element)
    return (filelist, filepath)

def get_degree_turn() -> int:
    turndegrees = ''
    while not turndegrees.isdecimal():
        turndegrees = input('Введите угол поворота по часовой стрелке (90, 180, 270):\n')
    return int(turndegrees)

def main():
    filelist, filepath = get_file_list()
    turndegrees = get_degree_turn()
    os.chdir(filepath)
    os.mkdir("rotated" + str(turndegrees))

    for filename in filelist:
        output_writer = PdfFileWriter()
        with open(filepath+filename, "rb") as inputf:
            pdfOne = PdfFileReader(inputf)
            numPages = pdfOne.numPages

            for i in range(numPages):
                page = pdfOne.getPage(i).rotateClockwise(turndegrees)
                output_writer.addPage(page)

            with open(filepath + "rotated" + str(turndegrees) + "//" + filename, "wb") as outfile:
                output_writer.write(outfile)

            print(f"{filename} rotated {turndegrees} degrees!")


if __name__ == "__main__":
    main()
