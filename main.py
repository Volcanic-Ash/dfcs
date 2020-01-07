import pandas as pd
import pdb
from tabulate import tabulate
import colorama

colorama.init()

class DFCS:

    def __init__(self, data):

        self.data = data
        self.result_df = pd.DataFrame(index=data.index)

        background_index = list(range(40, 48))
        background_index.extend(list(range(100, 108)))

        self.background_dict = dict(
            list(zip([
                'Black',
                'Red',
                'Green',
                'Yellow',
                'Blue',
                'Magenta',
                'Cyan',
                'Lightgray',
                'Darkgray',
                'Lightred',
                'Lightgreen',
                'Lightyellow',
                'Lightblue',
                'Lightmagenta',
                'Lightcyan',
                'White'
            ],
                background_index
            )
            )
        )

        font_color_index = list(range(30, 38))
        font_color_index.extend(list(range(90, 98)))

        self.font_color_dict = dict(
            list(zip([
                'Black',
                'Red',
                'Green',
                'Yellow',
                'Blue',
                'Magenta',
                'Cyan',
                'Lightgray',
                'Darkgray',
                'Lightred',
                'Lightgreen',
                'Lightyellow',
                'Lightblue',
                'Lightmagenta',
                'Lightcyan',
                'White'
            ],
                font_color_index
            ))
        )

        self.color_range_dict = {
            'Green-Red': {
                1: 'Green',
                2: 'Lightgreen',
                3: 'Yellow',
                4: 'Lightmagenta',
                5: 'Lightred'
#                 4: 'Lightred',
#                 5: 'Red'
            },

            'Blue-Red': {
                1: 'Lightblue',
                2: 'Lightcyan',
                3: 'Yellow',
                4: 'Lightmagenta',
                5: 'Lightred'
#                 4: 'Lightred',
#                 5: 'Red'
            }
        }

        self.prefix = '\033['

    def outputdf(self,color_target='font', color_theme='Blue-Red', tablefmt='grid',each_column=True):

        try:
            self.data = self.data.astype(float)

        except:
            return print("Error")

        if color_target=='font':
            color_set = self.font_color_dict
            infix = 'm'

        elif color_target=='background':
            color_set = self.background_dict
            infix = ';30m'

        suffix = '\x1b[0m'

        if each_column==False:
            target_range = self.data.max().max() - self.data.min().min()

            step = target_range*0.2
            target_base = self.data.min().min()

        for target_column in self.data.columns:

            target_sr = self.data[target_column]

            if each_column:
                target_range = target_sr.max() - target_sr.min()

                step = target_range*0.2
                target_base = target_sr.min()

            result_sr = pd.Series()

            for x in range(1, 6):

                lower = x-1
                upper = x

                if x == 1:
                    threshold_lower = target_base + step * (lower-1)
                    threshold_upper = target_base + step * upper
                elif x == 5:
                    threshold_lower = target_base + step * lower
                    threshold_upper = target_base + step * (upper+1)
                else:
                    threshold_lower = target_base + step * lower
                    threshold_upper = target_base + step * upper

                target_color_theme = \
                    color_set[self.color_range_dict[color_theme][x]]

                result_part_sr = target_sr[(target_sr >= threshold_lower) &
                                           (target_sr <= threshold_upper)]

                result_part_sr = self.prefix + \
                    str(target_color_theme) + \
                    infix + result_part_sr.astype(str) + suffix

                result_sr = pd.concat(
                    [result_sr, result_part_sr], sort=False)

            self.result_df = pd.concat(
                [self.result_df, result_sr], sort=False, axis=1)

        print(tabulate(self.result_df,
                       headers=self.data.columns, tablefmt=tablefmt))

        return
