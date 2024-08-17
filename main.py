from Roboter.Controller import controller

def TalkAboutRestaurant():
  my_controller = controller.Controller()
  my_controller.SayHello()
  is_recommend_restaurant_exist = my_controller.RecommendRestaurant()
  if not is_recommend_restaurant_exist:
    my_controller.AskUserFavoriteRestaurant()
  my_controller.SayThankYou()

if __name__ == '__main__':
  TalkAboutRestaurant()