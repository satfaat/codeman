import pandas
realty_df = pandas.read_csv('yandex_realty_data.csv')

realty_df['expenses'] = realty_df['price'] + 2 * 50000 * 1.43
realty_df['incomes_normal'] = realty_df['traffic'] * 18 * 1/225 * 0.1 * 21000 * 0.2 * 30
realty_df['incomes_pessimistic'] = realty_df['traffic'] * 18 * 1/300 * 0.05 * 20000 * 0.2 * 30
realty_df['profits_normal'] = realty_df['incomes_normal'] - realty_df['expenses']
realty_df['profits_pessimistic'] = realty_df['incomes_pessimistic'] - realty_df['expenses']

realty_df_filtered = realty_df[(realty_df['floor'] == 1) &
                               (realty_df['area'] >= 40) &
                               (realty_df['price'] <= 190000) & 
                               realty_df['commercial_type'].isin(['FREE_PURPOSE', 'RETAIL']) &
                               (realty_df['distance'] <= 6.7) &
                               (realty_df['already_taken'] == 0) &
                               (realty_df['competitors'] <= 1) &
                               (realty_df['profits_normal'] > 500000) &
                               (realty_df['profits_pessimistic'] > 0)]

print(realty_df_filtered)