import pandas as pd
import matplotlib.pyplot as plt


def clean():
    df = pd.read_csv('predict_auction_price/data/Train.csv')

    df = df[['SalePrice', 'YearMade', 'saledate', 
            'Enclosure','Turbocharged', 'ProductGroup', ]]

    #Eliminate rows with YearMade = 1000 and calculate age column
    df = df[df.YearMade >= 1930]
    df['saleyear'] = df['saledate'].str[-9:-4].astype('int32')
    df['age'] = df['saleyear'] - df['YearMade']

    # Create binary turbo column
    df['Turbo_binary'] = df['Turbocharged'].map(lambda x: 1.0 if x == "Yes" else 0.0)

    #product group dummies
    prod_group_dummies = pd.get_dummies(df['ProductGroup'], prefix='PrGrp')
    df = pd.concat([df, prod_group_dummies], axis = 1)

    # will leave us with three options: OROPS, EROPS, EROPS w AC
    df['Enclosure'] = df['Enclosure'].map(lambda x: 'EROPS w AC' if x == 'EROPS AC' else x)
    df['Enclosure'] = df['Enclosure'].map(lambda x: 'OROPS' if x == 'NO ROPS' else x)
    df = df[df.Enclosure != 'None or Unspecified']

    #enclosure group dummies
    enc_dummies = pd.get_dummies(df['Enclosure'], prefix='Enc')
    df = pd.concat([df, enc_dummies], axis = 1)

    return df

if __name__ == '__main__':
    df = clean()
    df.to_csv('predict_auction_price/data/CleanTrainData.csv')