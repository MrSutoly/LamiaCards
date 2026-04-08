import pytest
from airflow.models import DagBag
#imports 

@pytest.fixture(scope="session") #cria um fixture do pytest
def dagbag():
    return DagBag() 