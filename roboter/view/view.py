class View(object):

  def PrintHelloMessage(self, template_file_content, robot_name):
    return input(template_file_content.substitute({
      'robot_name':robot_name
    }))

  def PrintGreetingMessage(self, template_file_content, recommend_restaurant):
    return input(template_file_content.substitute({
      'restaurant':recommend_restaurant
    }))

  def PrintAskMessage(self, template_file_content, user_name):
    return input(template_file_content.substitute({
      'user_name':user_name
    }))

  def PrintThankYouMessage(self, template_file_content, robot_name, user_name):
    print(template_file_content.substitute({
      'robot_name':robot_name,
      'user_name':user_name
    }))