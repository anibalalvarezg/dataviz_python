# Create file
f = open('data/nobel_winners.csv', 'w')

nobel_winners = [{'category': 'Physics', 'name': 'Albert Einstein', 'nationality': 'Swiss', 'sex': 'male', 'year': 1921},
{'category': 'Physics', 'name': 'Paul Dirac', 'nationality': 'British', 'sex': 'male', 'year': 1933},
{'category': 'Chemistry', 'name': 'Marie Curie', 'nationality': 'Polish', 'sex': 'female','year': 1911}]

# Write in file
cols = nobel_winners[0].keys()
cols = sorted(cols)

with open('data/nobel_winners.csv', 'w') as f:
    f.write(','.join(cols) + '\n')
    for o in nobel_winners:
        row = [str(o[col]) for col in cols]
        f.write(','.join(row) + '\n')

# Read file
with open('data/nobel_winners.csv') as f:
    for line in f.readlines():
        print(line),

# Using csv to writing 
import csv
with open('data/nobel_winners_csv_module.csv', 'w') as f:
    fieldnames = nobel_winners[0].keys()
    fieldnames = sorted(fieldnames)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)

# Using csv to reading
with open('data/nobel_winners.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('data/nobel_winners.csv') as f:
    reader = csv.DictReader(f)
    nobel_winners = list(reader)
    
print(nobel_winners)