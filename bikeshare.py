import time
import calendar
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
            print(">>> {} nu este in CITY_DATA".format(city))
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = calendar.month_name[1:7] + ['All']
    month = ""
    while month not in months:
        month = input("Please enter the month to analize data: ").capitalize()
        if month not in months:
            print(">>> Month name is incorect")
    if month == 'All': month = 'all'   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = calendar.day_name[:] + ['All']
    day = ""
    while day not in days:
        day = input("Please enter the day of week to analize data: ").capitalize()
        if day not in days:
            print("Day of week is incorect: ")
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
        monthNumer = calendar.month_name[1:7].index(month)+1
        dfilter = dfilter[ df['Start Time'].dt.month == monthNumber and df['End Time'].dt.month == monthNumber ]
        
    # else dfilter = df
    
    print(df['Start Time'].dt.date)
    
    if day != 'all':        
        dayNumber = calendar.day_name[:].index(day)+1
        dfilter = dfilter[ df['Start Time'].dt.date and df['End Time'].dt.date ]
    # else dfilter = df
    
    return dfilter


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #df['momnth"] = df['Start Time'].dt.month
    #common_month = df['month'].mode()[0]
    #print common_month

    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
