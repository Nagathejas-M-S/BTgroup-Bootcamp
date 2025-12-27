-- query 01
-- Get all the predictions.

SELECT
    cardio_id,
    memberinfo_member_id,
    cardioarrestdetected,
    date
FROM cardiodiagnosis;


-- query 02
-- Get all the predictions for the day. 
-- can be = CURRENT_DATE or a specific date like '2019-01-24'

SELECT 
    cardio_id,
    memberinfo_member_id,
    cardioarrestdetected,
    date
FROM cardiodiagnosis
WHERE date::date = '2019-01-24';


-- query 03
-- Get all the predictions for the day and sort them based on the highest probability percentage at 
-- the top. 

SELECT
    cardio_id,
    memberinfo_member_id,
    cardioarrestdetected AS probability_percentage,
    date AS prediction_date
FROM cardiodiagnosis
WHERE date::date = '2019-01-27'
ORDER BY cardioarrestdetected DESC;

-- query 04
-- Get all the unique cities. 

SELECT DISTINCT city
FROM addressinfo
WHERE city IS NOT NULL;

-- query 05
-- Get all the members who are from a city 'Burgos'.

SELECT DISTINCT
    m.member_id,
    m.username,
    m.firstname,
    m.lastname,
    m.age,
    m.gender,
    m.email,
    m.phonenumber
FROM memberinfo m
JOIN addressinfo a
    ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Burgos';

-- query 06
-- Get all the members who are from 'Flora' city.

SELECT DISTINCT
    m.member_id,
    m.username,
    m.firstname,
    m.lastname,
    m.age,
    m.gender,
    m.email,
    m.phonenumber
FROM memberinfo m
JOIN addressinfo a
    ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Flora';


-- query 07
-- Get the total number of blood tests done for Aisha.
-- case insensitive search for firstname.
SELECT
    COUNT(DISTINCT b.blood_id) AS total_blood_tests
FROM memberinfo m
JOIN cardiodiagnosis c
    ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
    ON b.cardiodiagnosis_cardio_id = c.cardio_id
WHERE m.firstname ILIKE 'Aisha' or m.lastname ILIKE 'Aisha';


-- query 08
-- Get the X-ray details of Ajay whose cardio test was done on 26th of Jan 2019. 

SELECT
    x.xray_id,
    x.date AS xray_date,
    x.ca,
    c.cardio_id,
    c.date AS cardio_test_date
FROM memberinfo m
JOIN cardiodiagnosis c
    ON m.member_id = c.memberinfo_member_id
JOIN xray x
    ON x.cardiodiagnosis_cardio_id = c.cardio_id
WHERE m.firstname ILIKE 'Ajay'
  AND c.date::date = '2019-01-26';


-- query 09
-- Get all the members who are from cities 'Burgos' and 'Flora'. 
SELECT DISTINCT
    m.member_id,
    m.username,
    m.firstname,
    m.lastname,
    m.age,
    m.gender,
    m.email,
    m.phonenumber,
	a.city
FROM memberinfo m
JOIN addressinfo a
    ON m.member_id = a.memberinfo_member_id
WHERE a.city IN ('Burgos', 'Flora');


-- query 10
--  Get the total number of blood tests done for Aberson.
SELECT
    COUNT(DISTINCT b.blood_id) AS total_blood_tests
FROM memberinfo m
JOIN cardiodiagnosis c
    ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
    ON b.cardiodiagnosis_cardio_id = c.cardio_id
WHERE m.firstname ILIKE 'Aberson' or m.lastname ILIKE 'Aberson';



