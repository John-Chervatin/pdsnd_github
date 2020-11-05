import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':'chicago.csv',
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
    print('Please select a city: Chicago, New York City, Washington. ')
    global city
    city= input().lower()

    while True:
        if city in CITY_DATA:
            print('\n')
            break
        else:
            print('City not in list, please enter city')
            city = input().lower()

    print('Please select a month: All, January, February, March, ..., June.')
    global month
    month = input().lower()
    print('\n')

    print('Please select a day of the week: All, Monday, Tuesday, ..., Sunday.')
    global day
    day = input().lower()
    print('\n')

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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month)+1

        df = df[df['month']==month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
    return city,month,day


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print('The most popular month to hire a bike in {} is {}'.format(city.title(),popular_month))

    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week to hire a bike in {} is {}'.format(city,popular_day))

    popular_hour = df['hour'].mode()[0]
    print('The most popular hour to hire a bike in{} is {}'.format(city,popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_pickup = df['Start Station'].mode()[0]
    print('The most popular pick up location in {} is {}'.format(city,popular_pickup))

    popular_dropoff = df['End Station'].mode()[0]
    print('The most popular drop off location in {} is {}'.format(city, popular_dropoff))

    df['trip'] = df['Start Station']+' '+df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('The most popular combination of start and end locations in {} is {}'.format(city,popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    print('the total travel time taken over your month in {} is {} minutes'.format(city,total_travel))

    mean_travel = df['Trip Duration'].mean(axis=0)
    print('the average(mean) travel time taken in {} is {} minutes'.format(city,mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_types = df['User Type'].value_counts()
    print('Here is the breakdown of users types from {}:'.format(city))
    print(user_types)

    try:
        gender_types = df['Gender'].value_counts()
    except:
        print('\nGender information not recorded for users in {}.'.format(city))
    else:
        df['Gender'].fillna('Unknown')
        print("\nHere is the breakdown of users' gender across {}:".format(city))
        print(gender_types)

    try:
        birth_count =df['Birth Year'].value_counts()
    except:
        print('\nBirth year information not recorded for users in {}.'.format(city))
    else:
        recent_birth = int(df['Birth Year'].max())
        earlierst_birth = int(df['Birth Year'].min())
        print('\nThe earliest birth year for a user in {} was {},'.format(city,earlierst_birth))
        print('\nThe most recent birth year for a user in {} was {},'.format(city,recent_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Allows user to request to see raw data for n rows"""
    start_time = time.time()

    print('Would you like to see the raw data? Enter yes or no.\n')
    raw_data = input()
    if raw_data.lower() == 'yes':
        print('Enter the number of rows you would like to see 1-30000?')
        rows = input()

        while True:
           rows != None
           try:
            int(rows)
           except:
            print('Plese enter a number?')
            rows = int(input())
           else:
            int(rows)
            break

        print(df.head(rows))

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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
