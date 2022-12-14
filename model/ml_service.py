import os, json, time
import redis
import settings

# Connect to Redis and assign to variable `db``
# Load Redis settings from settings.py module
db = redis.Redis(
    host=os.getenv("REDIS_IP", "redis"),
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB_ID
)

# Load your model

def classify_process():
    """
    Loop indefinitely asking Redis for new jobs.
    When a new job arrives, takes it from the Redis queue, uses the loaded ML
    model to get predictions and stores the results back in Redis using
    the original job ID so other services can see it was processed and access
    the results.

    Loads data recieved from Redis, then pass it to the ML model to get predictions.
    """    
    while True:
        _, message = db.brpop(settings.REDIS_QUEUE)
        data_dict = json.loads(message)


        # TODO
        # 
        # Hardcoded prediction and probability
        # Replace by the prediction of your model.
        prediction = "deny" # Should be 'deny' or 'accept'
        probability = "0.2"


        prediction_data = {
            "prediction": prediction,
            "probability": probability
        }
        db.set(data_dict["id"], json.dumps(prediction_data))

        time.sleep(settings.SERVER_SLEEP)

if __name__ == "__main__":
    print("Launching ML service...")
    classify_process()