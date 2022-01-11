import time
import pandas as pd
import numpy as np
import calendar

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
  while True:
    city = input("enter city name from 'new york city' 'washington' 'chicago': ").lower()
    if city not in CITY_DATA:
        print("city not within coverage")

    else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
  while True:
    month = input("enter month name 'January to June' or type 'all' to show all months: ").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month != "all" and month not in months:
        print("month not within coverage")
    else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
  while True:
    day = input("enter week day or type 'all' to show all days: ").lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    if day != "all" and day not in days:
        print("enter a correct day name, e.g 'sunday', 'monday' etc")
    else:
        break

    print('-'*40)
    return city, month, day

# 1 Popular times of travel (i.e., occurs most often in the start time)
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
def load_data(city, month, day):
# data file loading to workspace
   df = pd.read_csv(CITY_DATA[city])
# conversion of start time to date time
   df['Start Time'] = pd.to_datetime(df['Start Time'])
# setting a separate column for month
   df['month'] = df['Start Time'].dt.month
# setting a separate column for day of the week
   df['day_of_week'] = df['Start Time'].dt.day_name()

   if month != "all":

       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1

       df = df[df['month'] == month]

   if day != "all":

       df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):

    i=0
    reply = input("do you want to see the first 5 rows? ").lower()
    pd.set_option("display.max_columns", None)

    while True:
        if reply == "no":
            break
    	print(df[i:i+5])
    	reply = input('do you want to see another five 5 rows? ').lower()
    	i += 5

# 2 Popular stations and trip
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month: ', calendar.month_name[common_month])


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("most common day of week: ", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]

    print("most common start hour: ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('most common start station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('most common end station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_and_end_stations = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print("most frequent combination of start and end stations: ", common_start_and_end_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#3 Trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: ", total_travel_time/360, "in minutes")

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_time/360, "in minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# 4 User info
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n", df['User Type'].value_counts());

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\n Counts of gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = float(df['Birth Year'].min())
        print("\n Earliest year of birth:\n", earliest_birth_year)
        recent_birth_year = float(df['Birth Year'].max())
        print("\n Most recent birth year:\n", recent_birth_year)
        common_birth_year = float(df['Birth Year'].mode()[0])
        print("\n common birth year:\n", common_birth_year)

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
