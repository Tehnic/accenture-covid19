import snowflake.connector

def connect():
    sfconnection = snowflake.connector.connect(
        account="rn68956.us-east-2.aws",
        user="Tehnic",
        password="Stolik1209!",
        warehouse="COMPUTE_WH",
        database="COVID19_EPIDEMIOLOGICAL_DATA",
        schema="PUBLIC",
    )
    return sfconnection

def disconnect(sfconnection):
    sfconnection.close()

def execute(sfconnection, query):
    cursor = sfconnection.cursor()
    cursor.execute(query)
    return cursor

def execute_async(sfconnection, query):
    cursor = sfconnection.cursor()
    cursor.execute_async(query)
    return cursor
