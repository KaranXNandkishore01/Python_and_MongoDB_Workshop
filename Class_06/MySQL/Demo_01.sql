
-- Create database
-- CREATE DATABASE IF NOT EXISTS company;
-- USA company;

-- Drop table if it already exists (for testing/reruns)
-- DROP TABLE IF EXISTS employee;

-- Create employee table
CREATE TABLE employee (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(30),
    salary DECIMAL(10,2),
    city VARCHAR(40)
);

-- Insert sample data
INSERT INTO employee (emp_name, department, salary, city) VALUES
('Karan Prajapati', 'IT', 65000, 'Bhopal'),
('Palak Sharma', 'HR', 48000, 'Indore'),
('Sourabh Rajput', 'Finance', 72000, 'Bhopal'),
('Riya Mehta', 'IT', 55000, 'Indore'),
('Rohit Patel', 'Sales', 40000, 'Jabalpur'),
('Anjali Verma', 'Finance', 68000, 'Bhopal'),
('Tushar Singh', 'Sales', 43000, 'Indore');

-- ===============================
-- 📊 Aggregation Queries
-- ===============================

-- 1️⃣ Total Salary of all Employees
SELECT SUM(salary) AS Total_Salary FROM employee;

-- 2️⃣ Average Salary
SELECT AVG(salary) AS Average_Salary FROM employee;

-- 3️⃣ Highest Salary
SELECT MAX(salary) AS Highest_Salary FROM employee;

-- 4️⃣ Lowest Salary
SELECT MIN(salary) AS Lowest_Salary FROM employee;

-- 5️⃣ Total Number of Employees
SELECT COUNT(emp_id) AS Total_Employees FROM employee;

-- ===============================
-- 📈 Aggregation by Department
-- ===============================
SELECT department,
       COUNT(emp_id) AS No_of_Employees,
       SUM(salary) AS Total_Salary,
       AVG(salary) AS Average_Salary,
       MAX(salary) AS Highest_Salary,
       MIN(salary) AS Lowest_Salary
FROM employee
GROUP BY department;

-- ===============================
-- 📉 Sort by Average Salary (Descending)
-- ===============================
SELECT department, AVG(salary) AS Average_Salary
FROM employee
GROUP BY department
ORDER BY Average_Salary DESC;

-- End of Script
