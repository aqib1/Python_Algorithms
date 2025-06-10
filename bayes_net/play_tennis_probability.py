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

    def answer_query(self, query: dict, given: dict) -> float:
        """
            Supports:
            - query={'PlayTennis': 'Yes'}, given={condition_name: value, ...}
            - query={condition_name: '?'}, given={'PlayTennis': 'Yes'}
        """
        answer: float = 0.0
        if 'PlayTennis' in query:
            ## Apply naive bayes classification
            answer = self.naive_bayes_classification(query, given)
        return round(answer,4)

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

if __name__ == '__main__':
    play = PlayTennisProbability()
    play.prepare_data()
    print(
        play.answer_query(
            {'PlayTennis': 'Yes'},
            {'Outlook': 'Sunny', 'Wind': 'Strong', 'Temperature': 'Cool', 'Humidity': 'High'}
        )
    )
