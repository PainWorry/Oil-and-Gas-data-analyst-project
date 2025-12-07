import pymongo
import random
from datetime import datetime, timedelta

# MongoDB Connection Configuration
# Ensure MongoDB is running locally on default port
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "ptt_logistics_db"
COLLECTION_NAME = "asset_telemetry"

def generate_mock_data(num_records=5000):
    """Generates mock data for pipeline sensors and logistics trucks."""
    data = []
    base_time = datetime.now()
    
    print(f"Generating {num_records} mock records...")
    
    for i in range(num_records):
        # Randomly decide between pipeline sensor or truck data
        if random.random() < 0.5:
            # Pipeline Sensor Data
            record = {
                "timestamp": base_time - timedelta(minutes=random.randint(0, 10000)),
                "type": "pipeline_sensor",
                "pipeline_segment_id": f"SEG-{random.randint(100, 120)}",
                "pressure_psi": round(random.uniform(800, 1200), 2),
                "temperature_c": round(random.uniform(20, 45), 2),
                "vibration_level": round(random.uniform(0, 5), 2),
                "status": random.choice(["NORMAL", "WARNING", "CRITICAL"])
            }
        else:
            # Truck GPS/Logistics Data
            record = {
                "timestamp": base_time - timedelta(minutes=random.randint(0, 10000)),
                "type": "truck_gps",
                "truck_id": f"TRUCK-{random.randint(1001, 1010)}",
                "latitude": round(random.uniform(13.0, 15.0), 6), # Approx Thailand Central/East
                "longitude": round(random.uniform(100.0, 102.0), 6),
                "speed_kmh": round(random.uniform(0, 90), 1),
                "fuel_level_pct": round(random.uniform(10, 100), 1),
                "engine_temp_c": round(random.uniform(80, 110), 1)
            }
        data.append(record)
    
    return data

def ingest_data():
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        
        # Optional: Clear existing data for clean slate in this demo
        # collection.delete_many({}) 
        
        mock_data = generate_mock_data()
        
        result = collection.insert_many(mock_data)
        print(f"Successfully inserted {len(result.inserted_ids)} documents into {DB_NAME}.{COLLECTION_NAME}")
        
    except Exception as e:
        print(f"Error connecting to MongoDB or inserting data: {e}")
        print("Ensure MongoDB is installed and running.")

if __name__ == "__main__":
    ingest_data()
