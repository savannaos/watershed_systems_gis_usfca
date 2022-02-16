import pandas as pd

hours = 24

def daily_average_temp(df, start, end):
  '''
  averages temperature data
  df: pandas dataframe
  '''
  day_sum = 0
  curr_date = df['OBS DATE'][start]
  
  # Sum every hour's precipitation value (inches)
  for i in range(start, end):
    curr_val = df['VALUE'][i]
    day_sum += curr_val

  # Average precipitation for this day
  avg_prec = day_sum/hours
  return (curr_date, avg_prec)

def main(df, rows):
  '''
  go through every row of data, 
  inrementing by 24 (number of hours)
  '''
  data = []
  for i in range(0, rows-1, hours):
    end = i+hours if i+hours < rows else rows
    d = daily_average_temp(df, i, end)
    data.append(d)
  
  df_out = pd.DataFrame(data)
  df_out.to_csv('daily_precip.csv')

if __name__ == '__main__':
  file_name = '~/Downloads/DLT_1.xlsx'
  df = pd.read_excel(file_name)
  #print(df.head())
  main(df, len(df.index))

