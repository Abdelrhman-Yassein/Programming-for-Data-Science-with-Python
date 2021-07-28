import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def check_input(input_str, input_type):
    """
    check the validity of user input.
    input_str: is the input of the user
    input_type: is the type of input: 1 = city, 2 = month, 3 = day
    """
    while True:
        input_read = input(input_str)
        try:
            if input_read in ['chicago', 'new york city', 'washington'] and input_type == 1:
                break
            elif input_read in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and input_type == 2:
                break
            elif input_read in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print(
                        "Sorry, your input should be: chicago new york city or washington")
                if input_type == 2:
                    print(
                        "Sorry, your input should be: january, february, march, april, may, june or all")
                if input_type == 3:
                    print(
                        "Sorry, your input should be: sunday, ... friday, saturday or all")
        except ValueError:
            print("Sorry, your input is wrong")
    return input_read


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

    city = check_input(
        "Would you like to see the data for chicago, new york city or washington?", 1)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = check_input("Which Month (all, january, ... june)?", 2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_input("Which day? (all, monday, tuesday, ... sunday)", 3)

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('the most common month : ', most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('the most common day of week : ', most_common_day)
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('he most common start hour : ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print('most commonly used start station : ', Start_Station)
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('most commonly used end station : ', end_station)
    # TO DO: display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station', 'End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n',
          popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel = df['Trip Duration'].sum()
    print('total travel time : ', total_travel)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('total travel mean : ', mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_typs = df['User Type'].value_counts()
    print('counts of user types : ', user_typs)
    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('counts of user gender : ', gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('earliest year : ', earliest_year)
        earliest_year = df['Birth Year'].max()
        print('most recent year : ', earliest_year)
        most_common_year = df['Birth Year'].mode()[0]
        print('most common year : ', most_common_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df, row_number):
    user_input = input('do you want to see raw data?(yes or no)')
    while user_input == 'yes':
        five_rows = df.iloc[:row_number]
        row_number += 5
        print(five_rows)
        display_data(df,row_number)
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df,5)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
