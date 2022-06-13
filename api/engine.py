import logging

from pymongo import MongoClient

from exceptions import DataAccessError

logger = logging.getLogger(__name__)

class MongoEngine(object):
    """Class for MongoDB database manipulation"""

    def __init__(self, uri: str, timeout: int = 60000, readPreference: str = 'secondaryPreferred') -> None:
        self.client = MongoClient(
            uri, connectTimeoutMS=timeout, socketTimeoutMS=timeout, readPreference=readPreference)
        self.database = None
        self.cursor = None

    
    def _get_database(self, database: str) -> None:
        self.database = self.client.get_database(database)

    
    def insert_data(self, database: str, collection_name: str, data: dict) -> str:
        try:
            logger.info(f'Getting {collection_name} data...')
            self._get_database(database)
            self.cursor = self.database.get_collection(collection_name)
            _id = self.cursor.insert_one(data).inserted_id
            logger.info(f'Data inserted...')
            return str(_id)
        except Exception as ex:
            raise DataAccessError(f"Cannot insert data because: {ex}")


    def get_data(self, database: str, collection_name: str, query: dict = {}):
        try:
            logger.info(f'Getting {collection_name} data...')
            self._get_database(database)
            self.cursor = self.database.get_collection(collection_name).find(query)
            logger.info(f'Connect cursor ok.')
            return self.cursor
        except Exception as ex:
            raise DataAccessError(f"Cannot access data because: {ex}")
