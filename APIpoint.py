from fastapi import FastAPI
import caching
import plotly.express as px
import getData as gd

app = FastAPI()
cache = {}
for COUNTRY in caching.trigger().Country:
    cache[COUNTRY] = caching.trigger().loc[caching.trigger().Country == COUNTRY]

@app.get("/")
async def hello():
    return {"message": "Hello there! API is working!"}
@app.get("/author")
async def author():
    return {"message": "Marks Dvojeglazovs"}
@app.get("/help")
async def help():
    return {"message": "This is a help page. You can find all the information about this API here."}
@app.get("/data/{country}")
async def data(country):
    if cache:
        return {"message": cache[country].to_json()}
    else:
        return gd.getCasesByCountry(country).to_json()
@app.get("/visual/{country}")
async def visual(country):
    if cache:
        return {"message": px.line(cache[country], x="Date", y="Cases", color="Country", title="Cases per country").to_json()}
    else:
        return gd.getCasesByCountry(country).any().plot(kind='line', x='DATE', y='CASES', title='Cases by date in ' + country)
@app.get("/economy/{country}")
async def economy(country):
    return {"message": gd.getEconomicsDataByCountry(country).to_json()}
