#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:35:47 2024

@author: gloria
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('movie_dataset.csv')

df.columns = df.columns.str.replace(' ', '_')

df.fillna(df.mean(), inplace=True)
df.dropna(inplace=True)
movie_dataset_stats = df.describe()
print(movie_dataset_stats)
#save the cleaned data to csv file (cleaned_dataset.csv)
df.to_csv("cleaned_dataset.csv", index=False)

#QUESTION 1
df = pd.read_csv("cleaned_dataset.csv")
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]
print(highest_rated_movie[['Title', 'Rating']])

#QUESTION 2
df = pd.read_csv("cleaned_dataset.csv")
average_revenue = df['Revenue_(Millions)'].mean()
print(f"Average revenue of all movies: ${average_revenue:.2f} million")


#QUESTION 3
df = pd.read_csv("cleaned_dataset.csv")
# Convert 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
filtered_df = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]
average_revenue_2015_to_2017 = filtered_df['Revenue_(Millions)'].mean()

print(f"Average revenue of movies from 2015 to 2017: ${average_revenue_2015_to_2017:.2f} million")

#QUESTION 4
df = pd.read_csv("cleaned_dataset.csv")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
movies_2016 = df[df['Year'].dt.year == 2016]
num_movies_2016 = movies_2016.shape[0]
print("Number of Movies Released in 2016:", num_movies_2016)

#QUESTION 5
df = pd.read_csv("cleaned_dataset.csv")
movies_nolan = df[df['Director'] == 'Christopher Nolan']
number_of_movies_nolan = len(movies_nolan)
print("Number of Movies Directed by Christopher Nolan:", number_of_movies_nolan)


#QUESTION 6:movies in the dataset have a rating of at least 8.0
df = pd.read_csv("cleaned_dataset.csv")
high_rated_movies = df[df['Rating'] >= 8.0]
num_high_rated_movies = high_rated_movies.shape[0]
print("Number of Movies with a Rating of at Least 8.0:", num_high_rated_movies)


#QUESTION 7
df = pd.read_csv("cleaned_dataset.csv")
movies_nolan = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan = movies_nolan['Rating'].median()
print("The median rating of movies directed by Christopher Nolan:", median_rating_nolan)

#QUESTION 8
df = pd.read_csv("cleaned_dataset.csv")
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df_filtered = df.dropna(subset=['Rating'])
average_rating_by_year = df_filtered.groupby('Year')['Rating'].mean()
# Find the year with the highest average rating
year_highest_avg_rating = average_rating_by_year.idxmax()
print("Year with the highest average rating:", year_highest_avg_rating)


#Question 9
# Load the dataset (loaded earlier but can load again)
df = pd.read_csv("cleaned_dataset.csv")
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]
# Count the number of movies for each year
movies_2006_count = len(movies_2006)
movies_2016_count = len(movies_2016)
percentage_increase = ((movies_2016_count - movies_2006_count) / movies_2006_count) * 100
print("Percentage increase in the number of movies made between 2006 and 2016:", percentage_increase)


#Question 10
df = pd.read_csv("cleaned_dataset.csv")
# After data is loaded, split the 'Actors' column into individual actor names
all_actors = df['Actors'].str.split(', ', expand=True)
flat_actors = all_actors.values.flatten()
actor_counts = pd.Series(flat_actors).value_counts()
most_common_actor = actor_counts.idxmax()
print(f"Most common actor in all the movies: {most_common_actor}")

#Question 11
# Load the dataset
df = pd.read_csv("cleaned_dataset.csv")
all_genres = df['Genre'].str.split(', ', expand=True)
flat_genres = all_genres.values.flatten()
unique_genres = pd.Series(flat_genres).unique()
num_unique_genres = len(unique_genres)
print("Number of unique genres in the dataset is:", num_unique_genres)


#Question 12
df = pd.read_csv("cleaned_dataset.csv")
# Assume and select only numerical columns for correlation analysis
numerical_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_df.corr()
print(correlation_matrix)






