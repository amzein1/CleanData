import csv
import re
def main3():
 
    with open("DirtyNames.csv", "r") as file:
        reader = csv.reader(file, quoting=csv.QUOTE_NONE)
        for row in reader:
            for name in row:
                if re.match("[a-zA-Z]", name):
                    # Captlize first letter 
                    name=name.title()
                    with open('CleanNames.csv', "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([name])
                else:
                    with open('InvalidNames.csv', "a", newline="") as file: 
                        writer = csv.writer(file)
                        writer.writerow([name])
                        