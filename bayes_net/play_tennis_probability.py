import pandas as pd
from pandas import DataFrame


class PlayTennisProbability:
    DATA_COLUMNS = ['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']

    # Class-level variables
    play_tennis: dict = {}
    tennis_data_frame: DataFrame = None
    conditional_prob_tables: dict = {}

    def prepare_data(self):
        # Load and clean data
        type(self).tennis_data_frame = self.read_tennis_data_frame()
        # Prepare probabilities
        self.prepare_play_tennis_prior_probability()
        for column in type(self).DATA_COLUMNS[1:-1]:
            probability_column = f'P({column}|Play)'
            type(self).conditional_prob_tables[column] = self.prepare_cpt_for_play_tennis_by_condition(
                column,
                probability_column
            )

    def query(self, query: dict, given: dict):
        """
        Generic query method for:

        1) P(PlayTennis = Yes/No | conditions)
        2) Given PlayTennis = Yes/No, find most likely condition value
        3) Probability distribution over PlayTennis given conditions
        4) Given PlayTennis = Yes/No, find most likely values of conditions

        Parameters:
        - query: dict, e.g. {'PlayTennis': 'Yes'} or {'Wind': '?'}
        - given: dict of conditions, e.g. {'Outlook': 'Sunny'}

        Returns:
        - float (probability) or dict (distribution or most likely values)
        """
        if 'PlayTennis' in query and query['PlayTennis'] in ['Yes', 'No']:
            ## Apply naive bayes classification
            answer = self.naive_bayes_classification(query, given)
            return round(answer, 4)
        if 'PlayTennis' in given:
            return self.most_likely_value_from_conditions(query, given)
        if 'PlayTennis' in query and query['PlayTennis'] == '?':
            return self.normalisation_naive_bayes_classification(given)
        raise Exception("Invalid Format of query")

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

    def naive_bayes_classification(self, query, given):
        pt_value = query['PlayTennis']
        answer = self.play_tennis[f'P({pt_value[0]})']
        for condition_name, condition_value in given.items():
            cpt = type(self).conditional_prob_tables[condition_name]
            prob_row: DataFrame = cpt[
                (cpt[condition_name] == condition_value) & (cpt['PlayTennis'] == pt_value)
                ]
            if not prob_row.empty:
                answer *= prob_row.iloc[0][f"P({condition_name}|Play)"]
        return answer

    def most_likely_value_from_conditions(self, query, given):
        pt_value = given['PlayTennis']
        most_likely_value_from_conditions = {}
        conditions = (query.items()) if query else type(self).DATA_COLUMNS[1:-1]
        for condition, _ in conditions:
            cpt = type(self).conditional_prob_tables[condition]
            filtered: DataFrame = cpt[cpt['PlayTennis'] == pt_value]
            if filtered.empty:
                most_likely_value_from_conditions[condition] = None
            else:
                max_row = filtered.loc[filtered[f'P({condition}|Play)'].idxmax()]
                most_likely_value_from_conditions[condition] = max_row[condition]
        return most_likely_value_from_conditions

    def normalisation_naive_bayes_classification(self, given):
        pt_yes = self.naive_bayes_classification({'PlayTennis': 'Yes'}, given)
        pt_no = self.naive_bayes_classification({'PlayTennis': 'No'}, given)
        pt_total = pt_yes + pt_no
        return {
            'Yes': round(pt_yes / pt_total, 5),
            'No': round(pt_no / pt_total, 5)
        }


if __name__ == '__main__':
    play = PlayTennisProbability()
    play.prepare_data()
    ## 1. PlayTennis = Yes with a sunny outlook, strong wind, cool temperature, and high humidity.
    print(
        play.query(
            {'PlayTennis': 'Yes'},
            {'Outlook': 'Sunny', 'Wind': 'Strong', 'Temperature': 'Cool', 'Humidity': 'High'}
        )
    )
    ## 2. Given the wind is strong, is it more likely that PlayTennis is yes or no?
    print(
        play.query(
            {'PlayTennis': '?'},
            {'Wind': 'Strong'}
        )
    )

    # 4. With Outlook=Overcast, Wind=Weak, Temperature=Mild, Humidity=Normal, probability distribution over PlayTennis
    print(
        play.query(
            {'PlayTennis': '?'},
            {'Outlook': 'Overcast', 'Wind': 'Weak', 'Temperature': 'Mild', 'Humidity': 'Normal'}
        )
    )

    ## 5. If PlayTennis is no, what are the most likely values for outlook, wind, humidity and temperature?
    print(
        play.query(
            {'Outlook': '?', 'Wind': '?', 'Humidity': '?', 'Temperature': '?'},
            {'PlayTennis': 'No'}
        )
    )
