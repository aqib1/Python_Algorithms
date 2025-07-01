import pandas as pd
from pandas import DataFrame


class PlayTennisProbability:
    DATA_COLUMNS = ['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']

    # Class-level variables
    play_tennis: dict = {}
    tennis_data_frame: DataFrame = None
    cpt_play_tennis_by_outlook: DataFrame = None
    cpt_play_tennis_by_temperature: DataFrame = None
    cpt_play_tennis_by_humidity: DataFrame = None
    cpt_play_tennis_by_wind: DataFrame = None

    def prepare_data(self):
        # Load and clean data
        type(self).tennis_data_frame = self.read_tennis_data_frame()
        # Prepare probabilities
        self.prepare_play_tennis_prior_probability()
        type(self).cpt_play_tennis_by_outlook = self.prepare_cpt_for_play_tennis_by_condition(
            'Outlook',
            'P(Play|Outlook)'
        )
        type(self).cpt_play_tennis_by_temperature = self.prepare_cpt_for_play_tennis_by_condition(
            'Temperature',
            'P(Play|Temperature)'
        )
        type(self).cpt_play_tennis_by_humidity = self.prepare_cpt_for_play_tennis_by_condition(
            'Humidity',
            'P(Play|Humidity)'
        )
        type(self).cpt_play_tennis_by_wind = self.prepare_cpt_for_play_tennis_by_condition(
            'Wind',
            'P(Play|Wind)'
        )
        print(type(self).cpt_play_tennis_by_outlook)
        print(type(self).cpt_play_tennis_by_temperature)
        print(type(self).cpt_play_tennis_by_humidity)
        print(type(self).cpt_play_tennis_by_wind)


    def read_tennis_data_frame(self) -> DataFrame:
        df = pd.read_csv('tennis_data.txt', sep=',', names=list(self.DATA_COLUMNS))
        return df.drop(columns='Day')

    def prepare_play_tennis_prior_probability(self):
        counts = type(self).tennis_data_frame['PlayTennis'].value_counts()

        total = counts.sum()
        type(self).play_tennis = {
            "Yes": counts.get("Yes", 0),
            "No": counts.get("No", 0),
            "Total": total,
            "P(Y)": round(counts.get("Yes", 0) / total, 2),
            "P(N)": round(counts.get("No", 0) / total, 2),
        }

    ## CPT - Conditional probability table
    def prepare_cpt_for_play_tennis_by_condition(
            self,
            condition_column,
            probability_column
    ) -> DataFrame:
        df = type(self).tennis_data_frame
        cpt = (df.groupby([condition_column, 'PlayTennis'])
                                                 .size()
                                                 .reset_index(name="Count"))
        cpt[probability_column] = cpt.apply(
            lambda row: round(row['Count'] / type(self).play_tennis['Yes'], 2) if row['PlayTennis'] == 'Yes' else round(
                row['Count'] / type(self).play_tennis['No'], 2), axis=1)
        return cpt


if __name__ == '__main__':
    play = PlayTennisProbability()
    play.prepare_data()
