import random
import time
from fastapi import FastAPI
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary, make_asgi_app
from starlette.middleware.wsgi import WSGIMiddleware



app = FastAPI()
app.handler = FastAPIHandler()


instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted prices',
    buckets=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
)
request_counter = Counter('prediction_requests_total', 'Total number of prediction requests')
data_shift_metric = Gauge('model_data_shift', 'Current data shift value')
latency_summary = Summary('prediction_request_latency_seconds', 'Latency of prediction requests')


@app.get("/", tags=['home'])
def home():
    return {"Hello": "World"}

@app.post('/api/prediction')
def make_prediction(car_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)[0]

    prediction_metric.observe(prediction)

    start_time = time.time()

    request_counter.inc()
    data_shift_metric.set(random.uniform(0.1, 0.5))

    prediction = app.handler.predict(item_features.dict())

    prediction_metric.observe(prediction)


    latency_summary.observe(time.time() - start_time)
    
    return ({
             'Present_Price': float(prediction),
             'car_id': car_id
            })