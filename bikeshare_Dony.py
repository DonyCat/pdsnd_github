import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
      city = input('Which city would you like to explore? chicago, new york city, washington? \n> ').lower()
                  
      if city not in CITIES:
            print("Please check your input, it doesn\'t appear to be conforming to any of the accepted input formats")
            continue
      else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input('\nWhich month do you prefer? all, january, february, march, april, may, june? \n> ').lower()

      if month not in('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Try Again") 
            continue
      else:
            break
               
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhat day do you prefer? all, monday, tuesday, wednesday, thursday, friday, saturday, sunday? \n> ').lower() 

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

    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
        
    return df
  
def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month :', most_common_month)
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('most common day of week :', most_common_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df ['hour'].mode()[0]
    print('most common start hour :', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station 
    start_station = df ['Start Station'].value_counts().idxmax()
    print('most commonly used start station :', start_station)
    # TO DO: display most commonly used end station
    end_station = df ['End Station'].value_counts().idxmax()
    print('most commonly used end station :', end_station)
    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination station :', start_station, " & ", end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df ['Trip Duration'].sum()
    print('total travel time :', total_travel_time)
    # TO DO: display mean travel time
    total_mean_travel_time = df ['Trip Duration'].mean()
    print('total mean travel time :', total_mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df ['User Type'].value_counts()
    usertype_count=df['User Type'].value_counts()
    print('\nCount of User types:{}\n'.format(usertype_count))
    # TO DO: Display counts of gender
    if'Gender' in df.columns:
        gender_count=df['Gender'].value_counts()
        print('\nCount of Gender:{}\n'.format(gender_count))
    else:
        print ('Gender stats cannot be calculated because Gender cannot be located in the dataframe')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_birth_year = df ['Birth Year'].max()
        print('Earliest Birth Year:', Earliest_birth_year)
        Most_Recent_Birth_Year = df ['Birth Year'].min()
        print('Most Recent Birth Year:', Most_Recent_Birth_Year)
        Most_Common_Year = df ['Birth Year'].value_counts().idxmax()
        print('Most Common Year:', Most_Common_Year)  
    except:
        print("There are no birth year details in this file.")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
       
def raw_data (df, city):
        i = 0
        display_data=input("Would you like to view 5 rows of individual trip data? Enter yes or no?")  
        while True:
            if display_data.lower() != "yes":
                break
            else:
                print("Now printing five lines from the {} raw data...".format(city.title()))
                print(df.iloc[i:i + 5])
                i += 5
                display_data=input("Do you wish to view more raw data? yes or no").lower()
                               
def main():
        while True:
      
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            raw_data(df, city)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                print("Thank you for participating.")
            break

if __name__ == "__main__":
        main()
                