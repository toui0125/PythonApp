import os
import csv
import string
import pathlib

class NoTemplateFileError(Exception):
  pass

class FileModel(object):
  def __init__(self, csv_file_path = None):
    if not csv_file_path:
      self.mCsvFilePath = self.GetCsvFilePath()
    pathlib.Path(self.mCsvFilePath).touch()
    self.mCsvFileColumn = ['RESTAURANT_NAME', 'POPULAR_COUNT']

  def GetCsvFilePath(self):
    csv_file_path = None

    try:
      import setting
      if setting.CSV_FILE_PATH:
        csv_file_path = setting.CSV_FILE_PATH
    except ImportError:
      pass

    if not csv_file_path:
      csv_file_path = 'restaurant_ranking.csv'

    return csv_file_path


  def GetTemplateDirPath(self):
      template_dir_path = None

      try:
        import setting
        if setting.TEMPLATE_DIR_PATH:
          template_dir_path = setting.TEMPLATE_DIR_PATH
      except ImportError:
        pass
      
      if not template_dir_path:
        model_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(model_dir_path, 'template')

      return template_dir_path

  def GetTemplateFilePath(self, template_file_name):
    template_dir_path = self.GetTemplateDirPath()
    template_file_path = os.path.join(template_dir_path, template_file_name)

    if not os.path.exists(template_file_path):
      raise NoTemplateFileError(f'cannot find {template_file_name}')

    return template_file_path

  """テンプレートファイルの中身を編集可能状態にして返す"""
  def GetTemplateFileContent(self, template_file_name):
    template_file_path = self.GetTemplateFilePath(template_file_name)

    with open(template_file_path, 'r', encoding='utf-8') as template_file:
      template_file_content = template_file.read()
      splitter = '=' * 60
      sep = os.linesep
      template_file_content = f'{splitter}{sep}{template_file_content}{sep}{splitter}{sep}'

      return string.Template(template_file_content)

  def PutFileDataIntoDict(self, restaurant_data):
    with open(self.mCsvFilePath, 'r+') as csv_file:
      csv_file_rows = csv.DictReader(csv_file)

      for csv_file_row in csv_file_rows:
        restaurant_data[csv_file_row[self.mCsvFileColumn[0]]] = int(csv_file_row[self.mCsvFileColumn[1]])
    
    return restaurant_data

  def UpdateFile(self, restaurant_data):
    with open(self.mCsvFilePath, 'w+') as csv_file:
      file_update_writer = csv.DictWriter(csv_file, fieldnames = self.mCsvFileColumn)
      file_update_writer.writeheader()

      for restaurant_name, popular_count in restaurant_data.items():
        file_update_writer.writerow({
          self.mCsvFileColumn[0] : restaurant_name,
          self.mCsvFileColumn[1] : popular_count
        })