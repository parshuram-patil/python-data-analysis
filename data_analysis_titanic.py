import os

import pandas as pd

from config import Config

root_path = os.path.dirname(os.path.abspath(__file__))


def main():
    print("******    Start   ******")

    df = pd.read_csv(r'' + Config.TITANIC_CSV_DATA_FILE)
    # titanic_df = pd.read_excel(root_path + './datasets/titanic/titanic.xlsx', sheet_name='titanic')
    # print("\nInput file Information ----> \n")
    # df.info()
    # print(titanic_df.head())

    print("\nTop 10 Elders ----> \n")
    print(df[['Name', 'Age']].sort_values('Age', ascending=False).head(10).to_string(index=False))
    # print(df.filter(['Name', 'Age'])[(df.Age >= 50)].count())

    print("\nCount of People whose Age is greater than 50  ----> \n")
    print(len(df[(df.Age > 50)]))

    print("\nCount of people whose Age is 24 ----> \n")
    print(pd.value_counts(df[(df.Age == 24)]['Age']).to_string(index=False))

    print("\nSex wise Average Fair ----> \n")
    print(df[['Sex', 'Fare']].groupby(['Sex']).mean())

    print("\nAverage of people survived by Sex and Class ----> \n")
    print(df[['Sex', 'Survived', 'Pclass']].groupby(['Sex', 'Pclass']).mean())

    print("\nNumber of Females survived in 3rd Class ----> \n")
    print(df[(df.Sex == 'female') & (df.Pclass == 3)][['Sex', 'Survived', 'Pclass']].groupby(['Sex', 'Pclass']).count().to_string(index=False))

    print("\n\nWriting data to File ----> \n")
    # out_dir = Config.OUTPUT_PATH.rsplit('/', 1)[0]
    # if not os.path.exists(Config.OUTPUT_PATH):
    #     os.mkdir(Config.OUTPUT_PATH)
    os.makedirs(Config.OUTPUT_PATH, exist_ok=True)
    csv_data = pd.DataFrame()
    csv_data = csv_data.append([df.head(5), df.tail(5)])
    csv_data.to_csv(Config.OUTPUT_PATH + "result.csv", index=False)


if __name__ == '__main__':
    main()




