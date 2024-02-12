# from dashboard.models import ApprovalStag
from django.db.models import Sum, Q
from enum import Enum
from django.db import connections

class Query(Enum):
    F_01 =   """
        SELECT * FROM TEST_TABLE
    """
    # -------------------------------------------
