# Objective
The objective of this week is to as following
    - Complete the spill-over from the past week (on priority - as described in the `Tech Debt`
      section towards the end of this document.)
    - Learn sorting with the following objective
        -- Basic Bubble sort using simple array like data
        -- Advanced bubble sort using objects
            --- Download bhav copies for a fixed period like a month or a year (or you can use existing downloaded ones)
            --- Take a company name (as user input)
            --- Find the data for the provided time period for the given company
            --- Compose this data as an array of Python objects
            --- Sort this data based on a key like 'High' or 'Low' field of the data

# Programming Challenge

- Example of bhav copy data sorting
Assume that you have bhav copy for a year (this could be YTD or month or a given quarter like Q1 of 2023 or H1 of 2023.
    - Collect the data for the given symbol for the given time period.
    - Sort this data using the sorting algorithm you have developed.
    - Show the result.
        -- The result could be "What was the data on which the stock gained max. % compared to the previous trading session/date?"
        -- Show the entire object in the output.

## Backgraound of files under consideration

NSE publishes daily bhavcopy of the stocks (also called securities) exchanged (which is bought and sold) for each company. There is 1 bhavcopy published per day but NSE provides URL to download files for historical dates.

## File format specifications

  "symbol": Name of the company (for example INFY stands for INFOSYS)
  "series": Instrument series. For example, "EQ" stands for equities. You can use only "EQ" series.
  "open": The opening price of the stock.
  "high": The high price of the stock that was witnessed on the trading day.
  "low": The low price of the stock that was witnessed on the trading day.
  "close": The closing price of the stock.
  "last": The last traded price price of the stock. (this is also called the last tick-price)
  "previous_close": The previous day closing price of the stock.
  "total_traded_quantity": Volumes or the quantities of the stock traded.
  "total_traded_value": It's the sum of volume traded and price at which the trade took place.
  "timestamp": Represents the trading date.
  "total_trades": Total number of trades that took place. Remeber that 1 trade can involve more than
  1 stock.
  "isin": Unique identification of a stock. This field is not significant now.

## Validations

## Comments on code 

## Parking Lot

## Questions

 1. [ ] Q. For refernce please terms FY, Q1 , H1 . 
          ---
 2. [ ]          

## Tech Debt Items

These are the spillovers from the past week that need to be addressed in the current week.
    - A download url should be tried for maximum 30 seconds
    - 

