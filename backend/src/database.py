from typing import List, Optional, Dict
from neo4j import GraphDatabase
from logger import logger


class Neo4jDatabase:
    def __init__(self, host: str = "neo4j://localhost:7687",
                 user: str = "neo4j",
                 password: str = "aowang"):
        """Initialize the movie database"""
        self.driver = GraphDatabase.driver(host, auth=(user, password))
        print('driver sucess'+host)

    def query(
        self,
        cypher_query: str,
        params: Optional[Dict] = {}
    ) -> List[Dict[str, str]]:
        logger.debug(cypher_query)
        with self.driver.session() as session:
            result = session.run(cypher_query, params)
            # Limit to at most 50 results
            return [r.values()[0] for r in result][:50]


if __name__ == "__main__":
    database = Neo4jDatabase(host="neo4j://localhost:7687",
                             user="neo4j", password="aowang")

    a = database.query("""
    MATCH (n) RETURN {count: count(*)} AS count
    """)

    print(a)
