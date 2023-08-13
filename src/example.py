
from guard.guard import CypherGuard

schema_string = '(Person, KNOWS, Person), (Person, WORKS_AT, Organization)'
input_query =  'MATCH (p:Person {id:"Foo"})<-[:WORKS_AT]-(o:Organization) RETURN o.name AS name'
correct_query = 'MATCH (p:Person {id:"Foo"})-[:WORKS_AT]->(o:Organization) RETURN o.name AS name'

guard = CypherGuard(schema_string=schema_string)
output = guard.run(input_query)

# Print the output, and whether it is equal to the correct query.
print(output)
print(output == correct_query)
