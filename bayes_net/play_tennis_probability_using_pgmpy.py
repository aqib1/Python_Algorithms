import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination

TENNIS_DATA_FILE_PATH = 'tennis_data.txt'
DATA_COLUMNS = ['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']
MODEL_STRUCTURE = [
        ('Outlook', 'PlayTennis'),
        ('Temperature', 'PlayTennis'),
        ('Humidity', 'PlayTennis'),
        ('Wind', 'PlayTennis')
    ]

class PlayTennisProbability:
    inference: VariableElimination = None

    def __init__(self):
        data = self.load_play_tennis_data_frame()
        type(self).inference = self.load_variable_elimination_inference(data)

    def query(self, variables: list, evidence: dict):
        return type(self).inference.query(variables=variables, evidence=evidence)

    def load_play_tennis_data_frame(self):
        df = pd.read_csv(TENNIS_DATA_FILE_PATH, sep=',', names=list(DATA_COLUMNS))
        return df.drop(columns = 'Day')

    def load_variable_elimination_inference(self, data):
        model = DiscreteBayesianNetwork(MODEL_STRUCTURE)
        estimator = BayesianEstimator(model, data)
        ## As total rows in tennis_data are 14,
        ## and we want our model to produce smooth predictions based on a prior value
        ## rather than relying only on data, we will put
        ## equivalent_sample_size with value >= 5
        ## get_parameters return CPDs
        model.add_cpds(*estimator.get_parameters(equivalent_sample_size=10))
        return VariableElimination(model)


if __name__ == '__main__':
    playTennisProbability = PlayTennisProbability()

    print("\nQ1: PlayTennis = Yes with a sunny outlook, strong wind, cool temperature, and high humidity.\n")
    print(playTennisProbability.query(
        ['PlayTennis'],
        {
            'Outlook' : 'Sunny',
            'Wind': 'Strong',
            'Temperature': 'Cool',
            'Humidity': 'High'
        }
    ))

    print("\nQ2: Given the wind is strong, is it more likely that PlayTennis is yes or no?.\n")
    print(playTennisProbability.query(
        ['PlayTennis'],
        {
            'Wind': 'Strong'
        }
    ))

    print("\nQ3: Given the wind is weak, is it more likely that PlayTennis is yes or no?.\n")
    print(playTennisProbability.query(
        ['PlayTennis'],
        {
            'Wind': 'Weak'
        }
    ))

    print("\nQ4: Assuming we PlayTennis and the temperature is hot, what wind strength is most likely?.\n")
    print(playTennisProbability.query(
        ['Wind'],
        {
            'PlayTennis': 'Yes',
            'Temperature': 'Hot'
        }
    ))

    print("\nQ5: If PlayTennis is no, what are the most likely values for outlook, wind, humidity and temperature?.\n")
    print(playTennisProbability.query(
        ['Outlook', 'Wind', 'Humidity', 'Temperature'],
        {
            'PlayTennis': 'No'
        }
    ))
