import pandas as pd
import numpy as np

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    data = [1, 2, 3]
    arr = np.array(data)
    d = {'a': 11, 'b': 12, 'c': 13}

    series = pd.Series(data)
    print(series)

    series_labels = pd.Series(data, index=labels)
    print(series_labels)

    ## series from dictionary
    series_from_dic = pd.Series(d)
    print(series_from_dic)

    ## Pandas series can hold functions too
    function_series = pd.Series(data = [sum, print, len])
    print(function_series)

    s1 = pd.Series(
        [1, 2, 3, 4],
        ['UK', 'Netherlands', 'Germany', 'Hungary']
    )

    s2 = pd.Series(
        [5, 1, 6, 10],
        ['UK', 'Netherlands', 'China', 'Hungary']
    )

    ## China and Germany will have NaN
    print(s1 + s2)

    ## Clean way to avoid NaN
    print(s1.add(s2, fill_value=0))