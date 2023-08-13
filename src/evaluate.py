import csv
import time
from guard.guard import CypherGuard

file_path = 'data/examples.csv'

# Loop over the example queries, attempt to fix each of them and record the results.
with open(file_path) as file:
    csv_reader = csv.reader(file, delimiter=',')

    # Skip header
    next(csv_reader)

    # Keep track of how many queries we can successfully fix.
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()

    for row in csv_reader:
        input_query = row[0].replace('""', '"')
        schema = row[1]
        correct_query = row[2].replace('""', '"')

        cypher_guard = CypherGuard(schema)
        result = cypher_guard.run(input_query)
        success: bool = (result == correct_query)

        if not success:
            print("original: ", input_query.replace('\n', ' '))
            print("result:   ", result.replace('\n', ' '))
            print("correct:  ", correct_query.replace('\n', ' '))
            print("=====================")

        if success:
            correct_count += 1
        else:
            incorrect_count += 1

print("Completed in " + str(time.time()-start_time) + ' seconds.')
print(str(correct_count) + "/" + str(correct_count +
      incorrect_count) + " queries succesfully corrected.")
