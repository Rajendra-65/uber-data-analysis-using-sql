create database ola;

use ola;

show tables;

#count the total number of records

select count(*) as row_num from bookings;

#select the 5 element from bookings

select * from bookings limit 5;

#create the successful_bookings

create view successful_bookings As
select * from bookings
where `Booking Status` = 'Success';

#select 20 successful_bookings

select `Booking Status` from successful_bookings limit 20;

#Retrive all Succeful Bookings

select * from successful_bookings;

#Avg ride distance by the vehicle..

create view ride_distance_for_each_vehicle as
select 
	`Vehicle Type`,
    avg(`Ride Distance`) as avg_ride_distance
from
	bookings
group by
	`Vehicle Type`;


select * from ride_distance_for_each_vehicle;

# count the number of cancellation due to the reason of customer

create view reason_for_cancelling_by_customer as
select 
	count(`Reason for cancelling by Customer`) as reason_for_cancelling_by_customer
from bookings
where `Reason for cancelling by Customer` != '';

select * from reason_for_cancelling_by_customer;

#top five customer for rides

create view top_five_customer_for_rides as
select 
	`Customer ID`,
    count(`Booking ID`) as booking_count
from
	bookings
group by 
	`Customer ID`
order by
	count(`Booking ID`) desc
limit 5;

select * from top_five_customer_for_rides;

create view cancelation_reason_due_to_personal_and_car_related_issues as
select
	count(*) as cancelation_reason_due_to_personal_and_car_related_issues
from 
	bookings
where 
	`Reason for cancelling by Driver` = 'Personal & Car related issues';

create view max_min_rating_of_prime_sedan as
SELECT 
	`Vehicle Type`,
	MAX(`Driver Ratings`) AS max_driver_ratings,
	MIN(`Driver Ratings`) AS min_driver_ratings
FROM
	bookings
WHERE 
	`Vehicle Type` = 'Prime Sedan'
    and `Driver Ratings` is not null
    and `Driver Ratings` != '';
    
select * from max_min_rating_of_prime_sedan;

#Avg customer rating per vehicle type

create view  avg_customer_rating_per_vehicle_type as
select 
	`Vehicle Type`,
    avg(`Customer Rating`) as avg_customer_ratings
from
	bookings
where 
	`Driver Ratings` is not null and `Driver Ratings` != ''
group by
	`Vehicle Type`;

select * from avg_customer_rating_per_vehicle_type;

create view total_booking_value as 
select 
	sum(`Booking Value`) as total_booking_value
from
	bookings
where 
	`Booking Status` = 'Success';
    
select * from total_booking_value;

SELECT
    *
FROM 
    bookings
WHERE 
    (`Booking Status` = 'Incomplete' OR `Booking Status` = 'Cancelled')
    AND
    (`Reason for cancelling by Customer` IS NOT NULL AND `Reason for cancelling by Driver` IS NOT NULL)
    AND
    (`Reason for cancelling by Customer` != '' AND `Reason for cancelling by Driver` != '');
