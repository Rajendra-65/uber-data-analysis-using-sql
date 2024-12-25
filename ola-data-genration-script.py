import pandas as pd
import random
import faker
from datetime import datetime, timedelta

# Initialize the Faker object and set random seed for reproducibility
fake = faker.Faker()
random.seed(42)

# Define possible values for the fields
booking_status = ['Success', 'Cancelled', 'Incomplete']
vehicle_types = ['Auto', 'Prime Plus', 'Prime Sedan', 'Mini', 'Bike', 'eBike', 'Prime SUV']
pickup_locations = [
    "Koramangala", "Indiranagar", "MG Road", "Whitefield", "Jayanagar", "Banaswadi", "Sadashivanagar",
    "Bellandur", "Marathahalli", "Hebbal", "HSR Layout", "Ulsoor", "Kalyan Nagar", "Banashankari", 
    "Rajajinagar", "Malleswaram", "Malleshwaram", "Brigade Road", "Vasanth Nagar", "Shivajinagar",
    "Cunningham Road", "Yelahanka", "Kengeri", "Basavanagudi", "Domlur", "Bangalore East", "Bangalore West",
    "JP Nagar", "RT Nagar", "BTM Layout", "Chamrajpet", "Vikram Sarabhai Marg", "Chandapura", "Hoskote", 
    "Attibele", "Sarjapur", "Devanahalli", "Anandapura", "Srinivaspura", "Jigani", "Nelamangala", "Koratagere",
    "Anekal", "Hulimavu", "Peenya", "Kudlu", "Yelahanka New Town", "KR Puram", "Varthur", "Vijayanagar",
    "Gandhinagar", "Richmond Town"
]

drop_locations = pickup_locations  # Drop locations can be similar to pickup locations

cancellation_reasons_customer = [
    "Driver is not moving towards pickup location", "Driver asked to cancel", "AC is not working", 
    "Change of plans", "Wrong Address"
]

cancellation_reasons_driver = [
    "Personal & Car related issues", "Customer related issue", "The customer was coughing/sick", 
    "More than permitted people in there"
]

incomplete_ride_reasons = [
    "Customer Demand", "Vehicle Breakdown", "Other Issue"
]

def generate_random_datetime():
    """Generates random date and time within the past month"""
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()
    random_datetime = fake.date_time_between(start_date=start_date, end_date=end_date)
    return random_datetime.strftime('%Y-%m-%d'), random_datetime.strftime('%H:%M:%S')

def generate_row():
    """Generates a random row of data"""
    date, time = generate_random_datetime()
    booking_id = fake.uuid4()
    booking_status_value = random.choices(booking_status, weights=[62, 18, 20], k=1)[0]  # 62% success
    customer_id = fake.uuid4()
    vehicle_type = random.choice(vehicle_types)
    
    pickup_location = random.choice(pickup_locations)
    drop_location = random.choice(drop_locations)
    
    avg_vtat = round(random.uniform(5, 20), 2) if booking_status_value == 'Success' else None
    avg_ctat = round(random.uniform(5, 20), 2) if booking_status_value == 'Success' else None
    
    cancelled_rides_customer = random.choice([0, 1]) if booking_status_value == 'Cancelled' else 0
    cancelled_reason_customer = random.choice(cancellation_reasons_customer) if cancelled_rides_customer == 1 else None
    
    cancelled_rides_driver = random.choice([0, 1]) if booking_status_value == 'Cancelled' else 0
    cancelled_reason_driver = random.choice(cancellation_reasons_driver) if cancelled_rides_driver == 1 else None
    
    incomplete_ride = random.choice([0, 1]) if booking_status_value != 'Success' else 0
    incomplete_reason = random.choice(incomplete_ride_reasons) if incomplete_ride == 1 else None
    
    booking_value = round(random.uniform(50, 300), 2) if booking_status_value == 'Success' else None
    ride_distance = round(random.uniform(1, 30), 2) if booking_status_value == 'Success' else None
    
    driver_rating = round(random.uniform(3, 5), 2) if booking_status_value == 'Success' else None
    customer_rating = round(random.uniform(3, 5), 2) if booking_status_value == 'Success' else None
    
    return {
        "Date": date,
        "Time": time,
        "Booking ID": booking_id,
        "Booking Status": booking_status_value,
        "Customer ID": customer_id,
        "Vehicle Type": vehicle_type,
        "Pickup Location": pickup_location,
        "Drop Location": drop_location,
        "Avg VTAT": avg_vtat,
        "Avg CTAT": avg_ctat,
        "Cancelled Rides by Customer": cancelled_rides_customer,
        "Reason for cancelling by Customer": cancelled_reason_customer,
        "Cancelled Rides by Driver": cancelled_rides_driver,
        "Reason for cancelling by Driver": cancelled_reason_driver,
        "Incomplete Rides": incomplete_ride,
        "Incomplete Rides Reason": incomplete_reason,
        "Booking Value": booking_value,
        "Ride Distance": ride_distance,
        "Driver Ratings": driver_rating,
        "Customer Rating": customer_rating
    }

# Generate 50,000 rows
data = [generate_row() for _ in range(100000)]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("bengaluru_ride_data.csv", index=False)
