import time
import calendar
import pandas as pd
import numpy as np
from datetime import timedelta


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in CITY_DATA:
        city = input("What is the name of the city to analyze data?: ").lower()
        if city not in CITY_DATA:
            print(">>> {} is not in CITY_DATA".format(city))
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = calendar.month_name[1:7] + ['All']
    month = ""
    while month not in months:
        month = input("Please enter the month to analyze data: ").capitalize()
        if month not in months:
            print(">>> Month name is not correct")
    if month == 'All': month = 'all'   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = calendar.day_name[:] + ['All']
    day = ""
    while day not in days:
        day = input("Please enter the day of week to analyze data: ").capitalize()
        if day not in days:
            print("Day of week is not correct: ")
    if day == 'All': day = 'all'

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time','End Time'])
    
    dfilter = df

    if month != 'all':
        monthNumber = calendar.month_name[1:7].index(month)+1
        dfilter = dfilter[df['Start Time'].dt.month == monthNumber]
        dfilter = dfilter[df['End Time'].dt.month == monthNumber]
        
    # else dfilter = df
    # """Display data based on user input"""
    paginate(df, 5)

    if day != 'all':        
        dayNumber = calendar.day_name[:].index(day)+1
        dfilter = dfilter[df['Start Time'].dt.day == dayNumber]
        dfilter = dfilter[df['End Time'].dt.day == dayNumber]
    # else dfilter = df
    
    return dfilter

def paginate(frame, skip=5):
    start_loc = 0
    stop_loc = frame.shape[0]
    while start_loc < stop_loc:

        ask_to_paginate = input("\n Do you want to paginate {} data? yes/no: ".format(skip)).lower()

        if ask_to_paginate == 'yes':
            print(frame.iloc[start_loc:start_loc + skip])
            start_loc += skip
        else:
            break

    # print reminder data
    print(frame.iloc[start_loc:stop_loc])


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_number = df['Start Time'].dt.month.mode()[0]
    print("Most common month is: ", calendar.month_name[month_number])

    # TO DO: display the most common day of week
    day_week = df['Start Time'].dt.dayofweek.mode()[0]
    print("Most common day of the week is: ", calendar.day_name[day_week])

    # TO DO: display the most common start hour
    start_hour = df['Start Time'].dt.hour.mode()[0]
    print("Most common hour is: ", start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("Most common start station is: ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("Most common end station is: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end_station = (df['Start Station'] + " - " + df['End Station']).mode()[0]
    print("Most frequent combination of start and end station is: ", most_frequent_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    tdelta = timedelta(seconds=int(total_travel_time))
    print("Total travel time is: {} years {} days {} hours {} minutes {} seconds".format(
        tdelta.days // 365, tdelta.days % 365, tdelta.seconds // 3600, tdelta.seconds % 3600 // 60, tdelta.seconds % 60))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    tdelta = timedelta(seconds=mean_travel_time)
    print("Mean travel duration is: {} minutes {} seconds {} miliseconds".format(
        tdelta.seconds // 60, tdelta.seconds % 60, tdelta.microseconds // 1000))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("User types count:\n", user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_distribution = df['Gender'].value_counts()
        print("\nDistribution for each gender:\n", gender_distribution)
    else:
        print("\nThere is no data available for city: {}".format(city.title()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print("\nBirth dates by Year")
        print("\tEarliest Birth:", earliest_birth)
        print("\tRecent Birth:", recent_birth)
        print("\tCommon Birth:", common_birth)
    else:
        print("\nThere is no data available for city: {}".format(city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        # asking using for input
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
