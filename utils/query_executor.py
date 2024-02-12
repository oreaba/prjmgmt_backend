# from dashboard.models import ApprovalStag
from django.db.models import Sum, Q
from enum import Enum
from django.db import connections
from utils.query import Query

class QueryExecutor:
    def __init__(self, query:Query, entity_id=None):
        if not isinstance(query, Query): #type(query) is not Query:
            print("can not initialize a Query Executor without a Query object.")
            return None           
        self.query = query
        self.entity_id = entity_id
        self.result = 0

    def to_decimal(self):
        self.result = float(self.result)
        return self.result

    def to_thousand_sep(self):
        self.result = f"{float(self.result):,}"
        return self.result
        
    # def default_query(self):
    #     return None

    def execute_query(self):
        sql_statement = self.query.value
        with connections['default'].cursor() as cursor: # default databse
            cursor.execute(sql_statement)
            result = cursor.fetchone()[0]
            self.result = result
        return result

    def execute_statement(self):
        sql_statement = self.query.value
        with connections['default'].cursor() as cursor: # default databse
            return cursor.execute(sql_statement)
    
    def execute_function(self):
        function_name = self.query.name
        sql_state = f"SELECT {function_name}() FROM DUAL"
        if self.entity_id: 
            sql_state = f"SELECT {function_name}('{self.entity_id}') FROM DUAL"

        with connections['default'].cursor() as cursor: # default databse
            cursor.execute(sql_state)
            result = cursor.fetchone()[0]
            self.result = result
        return result
    # def __format__(self, format_spec) -> str:
    #         first_value = next(iter(self.result.values()), None)
    #         if first_value:
    #             return f"{first_value:,}"
    #             # return first_value
    #         else:
    #             return 0
        # f"{first_value:,.2f}"
