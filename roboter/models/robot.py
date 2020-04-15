from termcolor import colored
from termcolor import cprint
from roboter.models import ranking


class Robot(object):
    """Base model for Robot."""

    def __init__(self, user_name=''
                 ):
        self.user_name = user_name

    def hello(self):
        while True:
            cprint('=' * 40, 'green')
            user_name = input(colored('Hello, I am Roboko. What is your name?\n' + '=' * 40 + '\n', 'green'))
            if user_name:
                self.user_name = user_name.title()
                break
            cprint('Please enter your name!', 'red')

class RestaurantRobot(Robot):
    """Handle data model on restaurant."""

    def __init__(self):
        super().__init__()
        self.ranking_model = ranking.RankingModel()



    def recommend_restaurant(self):
        new_recommend_restaurant = self.ranking_model.get_most_popular()
        if not new_recommend_restaurant:
            return None

        will_recommend_restaurants = [new_recommend_restaurant]
        while True:
            recommend = colored('I recommend {} restaurant.\nDo you like it? [Yes/No]\n' + '=' * 40 + '\n', 'green')
            cprint('=' * 40, 'green')
            answer = input(recommend.format(new_recommend_restaurant)).upper()
            if answer == 'YES' or answer == 'Y':
                break
            if answer == 'NO' or answer == 'N':
                new_recommend_restaurant = self.ranking_model.get_most_popular(
                    not_list=will_recommend_restaurants)
                if not new_recommend_restaurant:
                    break
                will_recommend_restaurants.append(new_recommend_restaurant)

    def ask_user_favorite(self):
        """Collect favorite restaurant information from users."""
        while True:
            cprint('=' * 40, 'green')
            restaurant = input(colored(self.user_name + ', which restaurants do you like?\n' + '=' * 40 + '\n', 'green')).title()
            cprint('=' * 40, 'green')

            fin = colored('Roboko: Thank you so much, {}!\nHave a good day!\n' + '=' * 40 + '\n', 'green')
            print(fin.format(self.user_name))
            if restaurant:
                self.ranking_model.increment(restaurant)
                break

