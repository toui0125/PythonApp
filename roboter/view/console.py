from roboter.controller import conversation

class Console(object):
  def __init__(self):
    self.my_controller = conversation.Conversation()

  def SayHello(self):
    while True:
      template_file_content = self.my_controller.GetTemplateFileContentSrv('hello.txt')
      robot_name = self.my_controller.GetRobotNameSrv()
      user_name = input(template_file_content.substitute({
          'robot_name':robot_name
        }))
      if user_name:
        self.my_controller.SetUserNameSrv(user_name)
        break
