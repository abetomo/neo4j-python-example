import sys
from neo4j import GraphDatabase

try:
    driver = GraphDatabase.driver(
            'bolt://localhost:7687', auth=('neo4j', 'password'))
except Exception as err:
    print(err)
    sys.exit(1)

with driver.session() as session:
    # create nodes
    session.run('create(:User{name: "user1"})')
    session.run('create(:User{name: "user2"})')

    session.run('create(:Item{name: "item1"})')
    session.run('create(:Item{name: "item2"})')

    # create relationships
    session.run(
        'match(u:User{name: "user1"}),(i:Item{name: "item1"}) '
        'create(u)-[:buy{quantity: 1}]->(i)')
    session.run(
        'match(u:User{name: "user2"}),(i:Item{name: "item1"}) '
        'create(u)-[:sell{quantity: 2}]->(i)')

    # select
    result = session.run(
        'match(nu:User)-[eb:buy]->(ni)<-[es:sell]-(ns) '
        'return nu, eb, ni, es, ns')
    print('Get:')
    for r in result:
        print(r['nu'])
        print(r['eb'])
        print(r['ni'])
        print(r['es'])
        print(r['ns'])

    # update
    session.run(
        'match(nu:User)-[eb:buy]->(ni)<-[es:sell]-(ns) '
        'set es.quantity = 0, eb.quantity = 3')

    # select
    result = session.run(
        'match(nu:User)-[eb:buy]->(ni)<-[es:sell]-(ns) '
        'return nu, eb, ni, es, ns')
    print('\nGet after update:')
    for r in result:
        print(r['nu'])
        print(r['eb'])
        print(r['ni'])
        print(r['es'])
        print(r['ns'])

    # delete nodes with relationships
    session.run('match(u:User) detach delete u')
    session.run('match(i:Item) delete i')

driver.close()
