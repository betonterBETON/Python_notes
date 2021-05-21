# source: 1
import openpyxl
import os


if __name__ == '__main__':
    # check which version of openpyxl we have installed
    print(openpyxl.__version__)

    # assuming excel sample file and this script are in the same directory,
    # go to that directory
    this_script_path = os.path.realpath(__file__)
    excel_file_name = "file_example_XLSX_100.xlsx"
    excel_file_path = os.path.join(os.path.dirname(this_script_path), excel_file_name)
    os. chdir(os.path.dirname(excel_file_path))

    # making sure which directory we're in
    print(os.getcwd())

    # create instance of workbook class
    wb = openpyxl.load_workbook(excel_file_name)
    # check what type that is
    print(type(wb))



