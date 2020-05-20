import os
import openpyxl as opx


class read_excel:
    """This class will be responsible to
    provide cell Value"""
    def __init__(self, sheetName, path):
        """
        :param sheetName: sheet name is a string value
        :param path: it should be absolute path from the project Root
        """
        global Path
        if r':/' not in str(path):
            Path = os.path.dirname(os.path.abspath(__file__))
        self.filePath = Path+path
        self.workbook = opx.load_workbook(self.filePath)
        self.worksheet = self.workbook.get_sheet_by_name(sheetName)

    def cell_value(self, column, Row):
        """This method will return cell value"""

        cellValue = self.worksheet.cell(row=Row, column=column)
        return cellValue


