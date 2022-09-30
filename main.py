import os
from PyPDF4 import PdfFileReader, PdfFileWriter

def get_file_list(files_path:str):
    filelist = []
    for root, dirs, files in os.walk(files_path):
        for filename in files:
            filelist.append(filename)
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
    # filepath = "R:\\Лаборатория ЭТЛ\\СДС ИНТЕРГАЗСЕРТ\\! ИК №1\ООО Томсккабель\\20.1103.12141.027-ТУ 041-монтажные\\" \
    #            "9.1.5.5 Доп. материалы\\9. Прием. контроль и период. исп\\Протоколы ПИ\\2021\\"
    filepath = input('Введите путь:\n')
    if not filepath.endswith('\\'): filepath += '\\'
    turndegrees = int(input('Введите угол поворота по часовой стрелке:\n'))
    main(filepath,get_file_list(filepath),turndegrees)
