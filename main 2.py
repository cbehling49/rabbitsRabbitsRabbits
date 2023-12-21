"""
Project Name: Rabbits, Rabbits, Rabbits
Author: Cody Behling
Due Date: 10/17/2020
Course: CS1400-X01

Calculate how many months of rabbit reproduction it will take before they run out of 500 cages.
Each week, a pair of adult rabbits will reproduce a pair of baby rabbits.
It takes one month for baby rabbits to mature before reproducing.
Each pair of rabbits will use one cage.
While writing this program, I learned how to use a dictionary in my code.
No user inputs were needed, but a new CSV file is generated with teh correctly-calculated data.
"""


import csv


def main():

    # starting values
    rabbitDict = {
          'month': 1,
          'adults': 1,
          'babies': 0,
          'total': 1
          }
    totalCages = 500

    # total rabbit pairs subtract from remaining cages
    availableCages = totalCages - rabbitDict['total']

    try:
        # create non-existent CSV file
        with open('rabbits.csv', 'w') as rabbitsRabbitsRabbits:
            writer = csv.writer(rabbitsRabbitsRabbits, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # write rows to CSV file
            writer.writerow(['# Table of rabbit pairs'])
            writer.writerow(['Month', 'Adults', 'Babies', 'Total'])
            writer.writerow([rabbitDict['month'], rabbitDict['adults'], rabbitDict['babies'], rabbitDict['total']])

            # iterate through loop to calculate values with each passing month
            while availableCages > 0:
                if rabbitDict['babies'] > 0:
                    rabbitDict['month'] += 1
                    newBabies = rabbitDict['adults']
                    rabbitDict['adults'] = rabbitDict['adults'] + rabbitDict['babies']
                    rabbitDict['babies'] = newBabies
                    rabbitDict['total'] = rabbitDict['adults'] + rabbitDict['babies']
                else:
                    rabbitDict['month'] += 1
                    rabbitDict['babies'] = rabbitDict['adults']
                    rabbitDict['total'] = rabbitDict['adults'] + rabbitDict['babies']
                writer.writerow([rabbitDict['month'], rabbitDict['adults'], rabbitDict['babies'], rabbitDict['total']])
                availableCages = totalCages - rabbitDict['total']

            # write final row
            writer.writerow([f"# Cages will run out in month {rabbitDict['month']}"])

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
