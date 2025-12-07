-- Table for Pipeline Inspection Logs
CREATE TABLE IF NOT EXISTS pipeline_inspection_logs (
    inspection_id SERIAL PRIMARY KEY,
    pipeline_segment_id VARCHAR(50) NOT NULL,
    inspection_date DATE NOT NULL,
    inspector_id VARCHAR(50),
    crack_detected BOOLEAN,
    corrosion_level FLOAT, -- Percentage or scale
    maintenance_required BOOLEAN,
    notes TEXT
);

-- Table for Tanker/Truck Master Data
CREATE TABLE IF NOT EXISTS tanker_master_data (
    truck_id VARCHAR(50) PRIMARY KEY,
    driver_name VARCHAR(100),
    capacity_liters INT,
    license_plate VARCHAR(20),
    fleet_base_location VARCHAR(100)
);
