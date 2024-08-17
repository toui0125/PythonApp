import collections

class DataModel(object):
  def __init__(self, name, user_name=None):
    self.mName = name
    self.mUserName = user_name
    self.msRestaurantData = collections.defaultdict(int)

  def GetRobotName(self):
    return self.mName

  def SetUserName(self, user_name):
    self.mUserName = user_name.title()

  def GetMostPupularRestaurant(self, already_recomennded_restaurants = None):
    if already_recomennded_restaurants is None:
      already_recomennded_restaurants = []

    if not self.msRestaurantData:
      return None

    sorted_restaurant_data = sorted(self.msRestaurantData, key = self.msRestaurantData.get, reverse = True)
    for restaurant in sorted_restaurant_data:
      if restaurant in already_recomennded_restaurants:
        continue
      return restaurant

    return None

  def GetUserName(self):
    return self.mUserName

  def IncrementCounter(self, restaurant):
    self.msRestaurantData[restaurant.title()] += 1
    return self.msRestaurantData
