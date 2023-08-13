# test stuff
# input = 'MATCH (p:Person {id:"Foo"})<-[:WORKS_AT]-(o:Organization) RETURN o.name AS name'
# input =  'MATCH (p:Person {id:"Foo"})<-[:WORKS_AT]-(o:Organization) RETURN o.name AS name'
# schema_string = '(Person, KNOWS, Person), (Person, WORKS_AT, Organization)'
# correct = 'MATCH (p:Person {id:"Foo"})-[:WORKS_AT]->(o:Organization) RETURN o.name AS name'

# guard = CypherGuard(schema_string=schema_string)
# output = guard.run(input)
# print(output)

# print(output == correct)
