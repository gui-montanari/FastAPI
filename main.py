from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)




if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")



"""token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzI3MzgxMzM5LCJpYXQiOjE3MjY3NzY1MzksInN1YiI6IjcifQ.wCCYAUJR3X0Xe_2ludJD8aOXJrVOwjc3XkoU4hrQRzo"""
"""tipo: bearer"""
"""token2: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzI3Mzg0OTg3LCJpYXQiOjE3MjY3ODAxODcsInN1YiI6IjgifQ.KfRMoQeajIILTAYBVl_Hj6LIC1vGvCKXKlUjykAMFPs"""