from typing import Optional

from fastapi import FastAPI
from vehicles import get_points_along_path

app = FastAPI()


@app.get("/")
def read_root():
    return {"data": "", "message": "Fareye Transportation app"}


@app.get("/api/trace_route/{path_a}/{path_b}")
def read_item(path_a: str, path_b: str, q: Optional[str] = None):
    return {"data": get_points_along_path('AIzaSyAMRfigkZLcs5qTEHrwHqCP7vfieyAQSHw', path_a, path_b)}
# API Key can be removed to be kept in a better secure place