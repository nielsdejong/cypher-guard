

import csv

from guard.guard import CypherGuard

file_path = 'data/examples.csv'

# Loop over the example queries
with open(file_path) as file:
    csv_reader = csv.reader(file, delimiter=',')

    # Skip header
    next(csv_reader)

    # Keep track of how many queries we can successfully fix...
    correct_count = 0
    incorrect_count = 0

    for row in csv_reader:
        input_query = row[0].replace('""','"')
        schema = row[1]
        correct_query = row[2]

        cypher_guard = CypherGuard(schema)
        result = cypher_guard.run(input_query)
        success: bool = (result == correct_query)

        if not success:
            print("original: ", input_query.replace('\n', ' '))
            print("result:   ", result.replace('\n', ' '))
            print("correct:  ", correct_query.replace('\n', ' '))
            print("=====================")
            break

        if success:
            correct_count += 1
        else:
            incorrect_count += 1

print("Completed. " + str(correct_count) + "/" + str(correct_count + incorrect_count) + " queries succesfully corrected." )