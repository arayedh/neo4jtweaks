from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "ra5la"))
session = driver.session()

CyphQuery = 'LOAD CSV WITH HEADERS FROM "file:///Automatisation_GPIN_2.csv" AS row CREATE(:NewCase{testName:row.Test,Auto:row.Automatisation,Etat:row.Etat,Charge:row.charge});'

session.run(CyphQuery)

# result = session.run("MATCH (a:Person) WHERE a.name = {name} "
#                        "RETURN a.name AS name, a.title AS title",
#                        {"name": "Arthur"})
# for record in result:
#     print("%s %s" % (record["title"], record["name"]))

session.close()