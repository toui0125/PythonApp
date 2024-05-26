from roboter.model import robot

class Conversation(object):
  def __init__(self):
      self.my_robot = robot.Robot('Roboko')

  def GetTemplateFileContentSrv(self, template_file_name):
    return self.my_robot.GetTemplateFileContent(template_file_name)

  def GetRobotNameSrv(self):
    return self.my_robot.GetRobotName()

  def SetUserNameSrv(self, user_name):
    self.my_robot.SetUserName(user_name)