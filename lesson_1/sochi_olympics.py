from pandas import DataFrame, Series
import numpy


countries = [
    'Russian Federation',
    'Norway',
    'Canada',
    'United States',
    'Netherlands',
    'Germany',
    'Switzerland',
    'Belarus',
    'Austria',
    'France',
    'Poland',
    'China',
    'Korea',
    'Sweden',
    'Czech Republic',
    'Slovenia',
    'Japan',
    'Finland',
    'Great Britain',
    'Ukraine',
    'Slovakia',
    'Italy',
    'Latvia',
    'Austria',
    'Croatia',
    'Kazakhstan'
]

gold_medals = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0 ,0]
silver_medals = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze_medals = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]


data_frame_src = {
    'country_name': Series(countries),
    'gold': Series(gold_medals),
    'silver': Series(silver_medals),
    'bronze': Series(bronze_medals)
}

sochi_olympics_frame = DataFrame(data_frame_src)


def get_avg_bronze_for_countries_with_a_gold_medal():
    countries_with_one_gold = sochi_olympics_frame[sochi_olympics_frame['gold'] >= 1]
    # bronze = sochi_olympics_frame['bronze'][sochi_olympics_frame['gold'] >=1] - listen in the solution
    avg_bronze_at_least_one_gold = numpy.mean(countries_with_one_gold['bronze'])
    return avg_bronze_at_least_one_gold


def get_avg_medal_count():
    countries_with_one_medal = sochi_olympics_frame[(sochi_olympics_frame.gold > 0) | (sochi_olympics_frame.silver > 0) | (sochi_olympics_frame.bronze > 0)]
    avg_medal_count = sochi_olympics_frame[['gold', 'silver', 'bronze']].apply(numpy.mean)
    print avg_medal_count


def get_score():
    GOLD_MEDAL = 4
    SILVER_MEDAL = 2
    BRONZE_MEDAL = 1

    sochi_olympics_frame['total'] = numpy.dot(sochi_olympics_frame[['gold', 'silver', 'bronze']], [4, 2, 1])
    print sochi_olympics_frame


if __name__ == '__main__':
    get_score()

    # print(sochi_olympics_frame.dtypes)
    # print ""
    # print(sochi_olympics_frame.describe())
    # print ""
    # print(sochi_olympics_frame[(sochi_olympics_frame['gold'] > 10) & (sochi_olympics_frame.country_name == 'Norway')])
    # print ""
    # print(sochi_olympics_frame)
