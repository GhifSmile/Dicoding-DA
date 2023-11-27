import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

class TableDashboard:
    def __init__(self, df):
        self.df = df

    def start(self):
        df= self.df

        df.drop('instant', axis=1, inplace=True)

        df.rename(columns={'yr':'year', 'mnth': 'month', 'cnt': 'count'}, inplace=True)

        df['year'] = df['year'].replace({0:'2011', 1:'2012'})
        df['dteday'] = df['dteday'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

        column_object = ['season', 'month', 'weekday', 'holiday', 'workingday', 'weathersit']

        for col in column_object:
            df[col] = df[col].astype('object')

        df['temp'] = df['temp'].apply(lambda x: x*41)

        month_rent = df[['year', 'month', 'season', 'weathersit', 'temp','casual', 'registered', 'count']].copy().groupby(['year', 'month', 'season', 'weathersit']).agg({
        'temp': 'mean',
        'casual': 'sum',
        'registered': 'sum',
        'count': 'sum'    
        })

        month_rent_fix = month_rent.reset_index()


        count_month_year = self.count_month_year(month_rent_fix)
        count_year_season = self.count_year_season(month_rent_fix)
        count_year_weathersit = self.count_year_weathersit(month_rent_fix)

        return count_month_year, count_year_season, count_year_weathersit


    def count_month_year(self, df):

        custom_palette = {'2011': '#4EBFD9', '2012': '#F27127'}

        plt.figure(figsize=(15, 10))

        ax = sns.barplot(x='month', y='count', hue='year', data=df, errorbar=None, estimator=sum, palette=custom_palette)

        ax = plt.gca()
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 2, int(p.   get_height()), ha='center', va='bottom', fontsize=10, color='black')

        plt.xlabel('Month')
        plt.ylabel('Count')

        return plt.gcf()
    

    def count_year_season(self, df):
        custom_palette = {1: '#4BA47E', 2: '#F27127', 3: '#A6375F', 4: '#4EBFD9'}    

        plt.figure(figsize=(15, 10))

        ax = sns.barplot(x='year', y='count', hue='season', data=df, errorbar=None, palette=custom_palette, estimator=sum)

        ax = plt.gca()
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 2, int(p.get_height()), ha='center', va='bottom', fontsize=10, color='black')

        legend_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}

        handles, _ = ax.get_legend_handles_labels()

        ax.legend(handles=handles, labels=[legend_labels.get(label, label) for label in df['season'].unique()])

        plt.xlabel('year')
        plt.ylabel('Count')

        return plt.gcf()
    
    def count_year_weathersit(self, df):
        custom_palette = {1: '#4BA47E', 2: '#F27127', 3: '#4EBFD9'}    

        plt.figure(figsize=(15, 10))

        ax = sns.barplot(x='year', y='count', hue='weathersit', data=df, errorbar=None, palette=custom_palette, estimator=sum)

        ax = plt.gca()
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 2, int(p.get_height()), ha='center', va='bottom', fontsize=10, color='black')

        legend_labels = {1: 'Clear', 2: 'Mist', 3: 'Rain'}

        handles, _ = ax.get_legend_handles_labels()

        ax.legend(handles=handles, labels=[legend_labels.get(label, label) for label in df['season'].unique()])

        plt.xlabel('year')
        plt.ylabel('Count')

        return plt.gcf()
    
