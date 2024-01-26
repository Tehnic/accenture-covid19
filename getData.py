import snowConnector as sc
import mongoConnector as mc
import pandas as pd

scconn, mcconn = None, None
while scconn is None or mcconn is None:
    scconn = sc.connect()
    mcconn = mc.connect()

def getTotalCasesByCountry():
    table = sc.execute(scconn, ("""SELECT COUNTRY_REGION, SUM(CASES) AS TOTAL_CASES
                                    FROM COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.ECDC_GLOBAL
                                    GROUP BY COUNTRY_REGION
                                    ORDER BY SUM(CASES) DESC"""))
    data = table.fetchall()
    columns = [column[0] for column in table.description]
    df = pd.DataFrame(data, columns=columns)
    return df

def getTotalCasesByDate():
    table = sc.execute(scconn, ("""SELECT DATE, SUM(CASES) AS TOTAL_CASES
                                    FROM COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.ECDC_GLOBAL
                                    GROUP BY DATE
                                    ORDER BY DATE"""))
    data = table.fetchall()
    columns = [column[0] for column in table.description]
    df = pd.DataFrame(data, columns=columns)
    return df

def getCasesByCountry(country):
    try:
        table = sc.execute(scconn, ("""SELECT DATE, CASES
                                    FROM COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.ECDC_GLOBAL
                                    WHERE COUNTRY_REGION = '""" + country + """'
                                    ORDER BY DATE"""))
        data = table.fetchall()
        columns = [column[0] for column in table.description]
        df = pd.DataFrame(data, columns=columns)
        return df
    except:
        return None

def getTotalDeaths():
    table = sc.execute(scconn, ("""SELECT COUNTRY_REGION, SUM(DEATHS) AS TOTAL_DEATHS
                                    FROM COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.ECDC_GLOBAL
                                    GROUP BY COUNTRY_REGION
                                    ORDER BY SUM(DEATHS) DESC"""))
    data = table.fetchall()
    columns = [column[0] for column in table.description]
    df = pd.DataFrame(data, columns=columns)
    return df

def getDeathsByCountry(country):
    try:
        table = sc.execute(scconn, ("""SELECT DATE, DEATHS
                                    FROM COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.ECDC_GLOBAL
                                    WHERE COUNTRY_REGION = '""" + country + """'
                                    ORDER BY DATE"""))
        data = table.fetchall()
        columns = [column[0] for column in table.description]
        df = pd.DataFrame(data, columns=columns)
        return df
    except:
        return None

def getEconomicsDataByCountry(country):
    table = pd.read_csv("data/economicDB.csv")
    return table[19:26]
