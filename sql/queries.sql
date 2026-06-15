-- Total Members

SELECT COUNT(*) AS total_members
FROM members;

-- Total Trainers

SELECT COUNT(*) AS total_trainers
FROM trainers;

-- Active Memberships

SELECT *
FROM subscriptions
WHERE status='Active';

-- Expired Memberships

SELECT *
FROM subscriptions
WHERE status='Expired';

-- Members Per Trainer

SELECT
trainer_id,
COUNT(*) AS total_members
FROM members
GROUP BY trainer_id;

-- Membership Revenue

SELECT
SUM(amount) AS total_revenue
FROM subscriptions;

-- Trainer Ranking

SELECT
trainer_id,
COUNT(*) AS members_count,
RANK() OVER(
ORDER BY COUNT(*) DESC
) AS rank_no
FROM members
GROUP BY trainer_id;
