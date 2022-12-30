import pandas as pd


class UserItemData:
    def __init__(self, path, from_date=None, to_date=None, min_ratings=None):
        self.path = path
        self.df = pd.read_table(path, encoding_errors="ignore")
        self.format_data = "%d.%m.%Y"
        self.df.rename(columns={"date_year": "year", "date_month": "month", "date_day": "day"}, inplace=True)

        if from_date is not None:
            self.df["date"] = pd.to_datetime(self.df[["day", "month", "year"]])
            self.df = self.df[self.df["date"] >= pd.to_datetime(from_date, format=self.format_data)]
            self.df.drop("date", axis=1)

        if to_date is not None:
            self.df["date"] = pd.to_datetime(self.df[["day", "month", "year"]])
            self.df = self.df[self.df["date"] < pd.to_datetime(to_date, format=self.format_data)]
            self.df.drop("date", axis=1)

        if min_ratings is not None:
            cnt = self.df["movieID"].value_counts()
            self.df = self.df[self.df["movieID"].isin(cnt[cnt >= min_ratings].index)]


    def no_of_ratings(self):
        return self.df.shape[0]
