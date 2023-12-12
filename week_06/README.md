# Objective
- To get an hands-on experience about Pandas library
- Ideas about pandas DataFrame methods
- Usage of pandas DF manipulations methods.
# Programming Challenge
## Definitions
- What is a week?
    - Monday to Friday is considered as a week.
- Current Week
    - If the most recent week beginning + 5 days results in a date in future
      then we should consider the Monday that is in the past week.
    - A user will provide a date and based on the date input the following needs
      to be accomplished.
    1. Proceed to next step if it is a valid trading date.Verify if it is a
       valid trading date or not. If it is not a valid trading date (either
       weekend or holiday of NSE), find the nearest trading date of the past.
    2. Once the lastest trading date is inferred, find the beginning of the
       trading week. Let's call this date (which is the beginning of the
       trading week as X)
    3. For the week starting on X, gather all the bhav copies for the entire
       week. (Remember that max days in a week is 5 and min is 0 which is least
       likely because an entire week cannot be a holiday)
    4. Merge the bhav copies for the entire week.
    5. Filter the data inside the bhav copies that are ONLY in 'EQ' series. Extract
       data pertaining to each unique symbol into it's own file. For example,
       data related to INFY will need to extracted into INFY.csv file.
    6. Now, for each symbol calculate gain or loss % as the case may be. Idea is
       to see if a stock has gained or lost for the entire week.
    7. For calculating gain or loss treat beginning of week's data (OPEN price)
       as the starting price and end of week's data (CLOSE price) as the ending
       price.
    8. Show the top 5 stocks that have gained maximum %.
    9. Show the top 5 stocks that have lost maximum %.

## Validations
1. [ ] User input date cannot be in future.
2. [ ] Ensure that the date entered by the user is correct
    - Only valid date format is accepts. And the date format should be DD/MMM/YYYY
3. [ ] Ensure that you do not fetch data for weekends
    - Bhavcopy files are available only for weekdays.
4. [ ] It may so happen that for a given input the bhav copy may not exist for
   the period under consideration. In that case you should be able to download
   the required files on-the-fly. (re-use existing code)
5. [ ] This analytics cannot be performed for the current/running week since you
   need data for the entire week and current week may not have ended.

## Comments on code 

## Parking Lot

## Questions


