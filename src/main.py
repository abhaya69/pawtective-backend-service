import time
import json

from fastapi import FastAPI,Request,Header,Response
import uvicorn

from routers import routes
from config import logger,API_KEY

app = FastAPI()

# @app.middleware("http")
# async def check_authentication(request : Request, call_next):
#     start=time.time()
#     if 'api-key' not in request.headers:
#         return Response(content=json.dumps({"error":"Authentication not provided","success":False}),media_type="application/json")
#     if request.headers['api-key']!=API_KEY:
#         return Response(content=json.dumps({"error":"Invalid Key","success":False}),media_type="application/json")
#     response = await call_next(request)
#     process_time=round(time.time()-start,4)
#     logger.debug("Processing Time : {}".format(str(process_time)))
#     response.headers["X-Process-Time"] = str(process_time)
#     return response

@app.on_event("startup")
async def startup_event():
    logger.info({"message":"Started Pawtective service"})

@app.on_event("shutdown")
def shutdown_event():
    logger.info({"message":"Shutting down Pawtective service"})

@app.get("/")
async def read_root():
    return {"message":"ok"}


app.include_router(
    routes.router,
    prefix="/api"
)

if __name__=='__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=8000,workers=1)

    # BUYidAjRUV7eO9D8AovlU6rzBdKe0NRn3CQ4pdKjGUnZH1BcU0Aa79reZ5MMIPGqpdQS55Tclkl9tb2$zx0UUi8vS9jEbeHhstmN$2DC$vmpn18VeDb4Z3mfRKWkpZ$8Db4GgetdkfxbMP1IC8FCEv4pgpUT6dU5