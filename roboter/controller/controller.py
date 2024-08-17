from Roboter.Model import data_model
from Roboter.Model import file_model
from Roboter.View import view

class Controller(object):
  def __init__(self):
      self.mDataModel = data_model.DataModel('Roboko')
      self.mFileModel = file_model.FileModel()
      self.mDataModel.msRestaurantData = self.mFileModel.PutFileDataIntoDict(self.mDataModel.msRestaurantData)
      self.mView = view.View()

  def SayHello(self):
    while True:
      template_file_content = self.mFileModel.GetTemplateFileContent('hello.txt')
      robot_name = self.mDataModel.GetRobotName()
      user_name = self.mView.PrintHelloMessage(template_file_content, robot_name)
      if user_name:
        self.mDataModel.SetUserName(user_name)
        break

  def RecommendRestaurant(self):
    recommend_restaurant = self.mDataModel.GetMostPupularRestaurant()
    if recommend_restaurant is None:
      return False
    already_recommended_restaurants = [recommend_restaurant]

    while True:
      template_file_content = self.mFileModel.GetTemplateFileContent('greeting.txt')
      is_yes = self.mView.PrintGreetingMessage(template_file_content, recommend_restaurant)

      if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
        return True
      if is_yes.lower() == 'n' or is_yes.lower() == 'no':
        recommend_restaurant = self.mDataModel.GetMostPupularRestaurant(already_recommended_restaurants)
        if recommend_restaurant is None:
          return False
        already_recommended_restaurants.append(recommend_restaurant)

  def AskUserFavoriteRestaurant(self):
    while True:
      template_file_content = self.mFileModel.GetTemplateFileContent('which_restaurant.txt')
      user_name = self.mDataModel.GetUserName()
      user_favorite_restaurant = self.mView.PrintAskMessage(template_file_content, user_name)

      if user_favorite_restaurant:
        restaurant_data = self.mDataModel.IncrementCounter(user_favorite_restaurant)
        self.mFileModel.UpdateFile(restaurant_data)
        break

  def SayThankYou(self):
    template_file_content = self.mFileModel.GetTemplateFileContent('good_by.txt')
    robot_name = self.mDataModel.GetRobotName()
    user_name = self.mDataModel.GetUserName()
    self.mView.PrintThankYouMessage(template_file_content, robot_name, user_name)