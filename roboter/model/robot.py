import os
import string

class NoTemplateFileError(Exception):
  pass

class Robot(object):
  def __init__(self, name, user_name=None):
    self.name = name
    self.user_name = user_name

  def GetTemplateDirPath(self):
      template_dir_path = None

      # setting.pyにパスの記載がある場合はそれを読み込む
      try:
        import setting
        if setting.TEMPLATE_DIR_PATH:
          template_dir_path = setting.TEMPLATE_DIR_PATH
      except ImportError:
        pass
      
      # 記載がなかった場合
      if not template_dir_path:
        roboter_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(roboter_dir_path, 'template')

      return template_dir_path

  """テンプレートファイルのパスを返す"""
  # model
  def GetTemplateFilePath(self, template_file_name):
    # テンプレートファイルのパス
    template_dir_path = self.GetTemplateDirPath()
    template_file_path = os.path.join(template_dir_path, template_file_name)

    # 存在確認
    if not os.path.exists(template_file_path):
      raise NoTemplateFileError(f'cannot find {template_file_name}')

    return template_file_path

  """テンプレートファイルの中身を編集可能状態にして返す"""
  # model
  def GetTemplateFileContent(self, template_file_name):
    # テンプレートファイルのパス
    template_file_path = self.GetTemplateFilePath(template_file_name)

    with open(template_file_path, 'r', encoding='utf-8') as template_file:
      template_file_content = template_file.read()
      template_file_content = template_file_content.rstrip(os.linesep)

      splitter = '=' * 60
      sep = os.linesep

      template_file_content = f'{splitter}{sep}{template_file_content}{sep}{splitter}{sep}'

      return string.Template(template_file_content)

  def GetRobotName(self):
    return self.name

  def SetUserName(self, user_name):
    self.user_name = user_name.title()