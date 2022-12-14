import os

import json
import time
import uuid

import redis
import settings

from typing import Dict, Tuple

# Connect to Redis and assign to variable `db``
# Load Redis settings from settings.py module
db = redis.Redis(
    host=os.getenv("REDIS_IP", "redis"),
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB_ID
)

def model_predict(data: Dict) -> Tuple:
    """
    Receives an dictionary and queues the job into Redis.
    Will loop until getting the answer from our ML service.

    Parameters
    ----------
    data : dict
        Name for the image uploaded by the user.

    Returns
    -------
    prediction, probability : tuple(str, float)
        Model predicted result as a string and the corresponding probabilty
        as a number.
    """
    job_id = str(uuid.uuid4())
    
    job_data = {
        "id": job_id,
        "data": data
    }    

    db.lpush(settings.REDIS_QUEUE, json.dumps(job_data))

    while True:
        output = db.get(job_id)

        if output:
            db.delete(job_id)
            break
        
        time.sleep(settings.API_SLEEP)

    output = json.loads(output)
    prediction = output["prediction"]
    probability = output["probability"]

    return prediction, probability