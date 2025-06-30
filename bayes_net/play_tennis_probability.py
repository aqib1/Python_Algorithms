import pandas as pd

class PlayTennisProbability:
    def probability(self):
        columns = ['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']
        tennis_data_frame = pd.read_csv('tennis_data.txt', sep=',', names = columns)
        ## Dropping column Day as its not needed
        tennis_data_frame = tennis_data_frame.drop('Day', axis=1)
        print(tennis_data_frame)


if __name__ == '__main__':
    play = PlayTennisProbability()
    play.probability()