import csv
fil='test.csv'
with open(fil,'rt') as f:
  data = csv.reader(f)
  for row in data:
      for ele in row:
          if len(ele)>5:
              if ele[0]=="+" or ele.isnumeric():
                  print(ele)
