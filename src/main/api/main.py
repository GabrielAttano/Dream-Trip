from fastapi import FastAPI
from routes.user_routes import user_router
from routes.package_routes import package_router

app = FastAPI()

app.include_router(user_router)
app.include_router(package_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}