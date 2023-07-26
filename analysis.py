import time

import pandas as pd


class ResultsAnalysis:

    def __init__(self, data):
        df = pd.DataFrame.from_dict(data)
        df = df[pd.notnull(df['gt_corners'])]
        df = df[pd.notnull(df['rb_corners'])]
        print(f'Total samples: {df.shape[0]}, column count: {df.shape[1]}')
        self.dataframe = df

    def analyze(self):
        values_bar_name = f'plots/{time.time()}_unique_values_bar.png'
        results_bar_name = f'plots/{time.time()}_results_bar.png'

        self.dataframe.rb_corners.value_counts().plot(kind='bar')
        plt.title('Number of unique rb_corners values')
        plt.savefig(values_bar_name)
        plt.cla()
        plt.clf()

        plt.bar(['right predictions', 'wrong predictions'],
                [int(self.dataframe.shape[0]) - len(self.dataframe.loc[(self.dataframe.rb_corners != self.dataframe.gt_corners)]),
                 len(self.dataframe.loc[(self.dataframe.rb_corners != self.dataframe.gt_corners)])])
        plt.title('Right/wrong predictions')
        plt.savefig(results_bar_name)
        return [values_bar_name, results_bar_name]
