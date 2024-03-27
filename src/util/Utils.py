import pathlib
import pandas as pd
from datetime import datetime
from pathlib import Path


class Utils:

    @staticmethod
    def get_reports_folder_path():
        return Path.cwd().joinpath('reports').joinpath(datetime.now().strftime('%d-%m-%Y'))

    @staticmethod
    def get_reports_file_path(title):
        return Utils.get_reports_folder_path().joinpath(title+"-"+datetime.now().strftime('%d-%m-%Y-%H%M')+'.xlsx')

    @staticmethod
    def print_list_to_excel(list_to_export, title, columns):
        path = Utils.get_reports_folder_path()
        Utils.create_folder(path)
        string_list = list(map(str, list_to_export))
        formatted_list = [x.split(';') for x in string_list]
        data_frame = pd.DataFrame(formatted_list)
        data_frame.columns = columns
        writer = pd.ExcelWriter(Utils.get_reports_file_path(title), engine='xlsxwriter')
        data_frame.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()

    @staticmethod
    def create_folder(path):
        pathlib.Path(path).mkdir(mode=0o777, parents=True, exist_ok=True)
