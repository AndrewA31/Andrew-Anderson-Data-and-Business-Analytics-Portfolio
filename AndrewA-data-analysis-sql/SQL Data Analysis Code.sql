1. Create a SQL statement to list all managers and their titles.


SELECT mdn.emp_no, t.title, e.first_name, e.last_name
	FROM
		(SELECT dm.emp_no, dm.dept_no, d.dept_name FROM dept_manager dm
		  JOIN departments d ON dm.dept_no = d.dept_no) AS mdn
 LEFT JOIN employees e ON mdn.emp_no = e.emp_no
 LEFT JOIN titles t ON e.emp_no = t.emp_no ;
 
 2. Create a SQL statement to show the salary of all employees and their department 
name.

--First Attempt (WRONG)
SELECT e.emp_no, e.first_name, e.last_name, rs.salary, de.dept_no, d.dept_name FROM employees e
LEFT JOIN 
		(SELECT emp_no, salary, RANK() OVER(PARTITION BY emp_no ORDER BY from_date DESC) AS recent_salary
		FROM salaries) 
			AS rs ON e.emp_no = rs.emp_no
LEFT JOIN dept_emp de ON e.emp_no = de.emp_no
LEFT JOIN departments d ON de.dept_no = d.dept_no
WHERE rs.recent_salary = 1 OR rs.recent_salary IS NULL ;


--Second attempt(FINAL SUBMISSION)
CREATE TEMPORARY TABLE emp_dept_sal
(
WITH cte AS

(SELECT dm.emp_no, dm.dept_no, d.dept_name, dm.from_date, dm.to_date  FROM dept_manager dm
LEFT JOIN departments d ON dm.dept_no = d.dept_no
UNION
SELECT de.emp_no, de.dept_no, d.dept_name, de.from_date, de.to_date FROM dept_emp de
LEFT JOIN departments d ON de.dept_no = d.dept_no)

SELECT cte.dept_name, e.emp_no, e.first_name, e.last_name, s.salary, s.from_date AS sal_from, s.to_date AS sal_to,
	ROW_NUMBER() OVER(PARTITION BY e.emp_no, cte.dept_name ORDER BY s.salary DESC) AS row_num
FROM cte
RIGHT JOIN employees e ON cte.emp_no = e.emp_no
LEFT JOIN salaries s ON e.emp_no = s.emp_no 
AND s.from_date >= cte.from_date
)

SELECT * FROM emp_dept_sal
EXCEPT 
	SELECT * FROM emp_dept_sal 
	WHERE row_num != 1 AND salary IS NULL

3. Create a SQL statement to show the hire date and birth date of employees who belong to HR 
department.


SELECT e.hire_date, e.birth_date FROM employees e
LEFT JOIN dept_emp de ON e.emp_no = de.emp_no
LEFT JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Human Resources'
UNION
SELECT e.hire_date, e.birth_date FROM employees e
LEFT JOIN dept_manager dm ON e.emp_no = dm.emp_no
LEFT JOIN departments d ON dm.dept_no = d.dept_no
WHERE d.dept_name = 'Human Resources'


4. Create a SQL statement to show all departments and their department’s managers

SELECT d.dept_no, d.dept_name, e.first_name, e.last_name, dm.emp_no
FROM departments d
LEFT JOIN dept_manager dm ON d.dept_no = dm.dept_no
LEFT JOIN employees e ON dm.emp_no = e.emp_no;


5. Create a SQL statement to show a list of HR’s employees who were hired after 1986.

SELECT e.emp_no, e.first_name, e.last_name, e.hire_date FROM employees e
LEFT JOIN dept_emp de ON e.emp_no = de.emp_no
LEFT JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Human Resources' AND YEAR(e.hire_date) > 1986
UNION
SELECT e.emp_no, e.first_name, e.last_name, e.hire_date FROM employees e
LEFT JOIN dept_manager dm ON e.emp_no = dm.emp_no
LEFT JOIN departments d ON dm.dept_no = d.dept_no
WHERE d.dept_name = 'Human Resources' AND YEAR(e.hire_date) > 1986;


6. Create a SQL statement to increase any employee’s salary up to 2%. Assume the 
employee has just phoned in with his/her last name.

CREATE TEMPORARY TABLE emp_sal AS
SELECT e.*, s.salary, s.from_date, s.to_date FROM employees e 
LEFT JOIN salaries s On e.emp_no = s.emp_no;


UPDATE emp_sal
	SET salary = 
		CASE last_name WHEN ~insert_last_name~ THEN salary * 1.02
		END
		
		
7. Create a SQL statement to delete employee’s record who belongs to marketing 
department and name start with A

CREATE TEMPORARY TABLE emp_dept_full AS
SELECT e.emp_no, e.first_name, e.last_name, d.dept_name FROM employees e
LEFT JOIN dept_emp de ON e.emp_no = de.emp_no
LEFT JOIN departments d ON de.dept_no = d.dept_no
WHERE dept_name IS NOT NULL
UNION
SELECT e.emp_no, e.first_name, e.last_name, d.dept_name FROM employees e
LEFT JOIN dept_manager dm ON e.emp_no = dm.emp_no
LEFT JOIN departments d ON dm.dept_no = d.dept_no
WHERE dept_name IS NOT NULL;


INSERT INTO emp_dept_full VALUES 
(99999, 'Andrew', 'Anderson', 'Marketing');


DELETE FROM emp_dept_full 
WHERE
	dept_name = 'marketing' AND first_name LIKE 'a%';
	
	
8. Create a database view to list the full names of all departments’ managers, and their 
salaries.

CREATE VIEW full_dept_man_sal AS
SELECT dm.emp_no, e.first_name, e.last_name, d.dept_name, d.dept_no, s.salary FROM employees e 
LEFT JOIN dept_manager dm ON e.emp_no = dm.emp_no
RIGHT JOIN departments d ON dm.dept_no = d.dept_no
LEFT JOIN salaries s ON e.emp_no = s.emp_no;

9. Create a database view to list all departments and their department’s managers, who 
were hired between 1980 and 1990.

CREATE VIEW dept_man_hired_between_1980_1990 AS
SELECT dm.emp_no, e.first_name, e.last_name, d.dept_name, d.dept_no, e.hire_date FROM employees e 
LEFT JOIN dept_manager dm ON e.emp_no = dm.emp_no
RIGHT JOIN departments d ON dm.dept_no = d.dept_no
WHERE YEAR(e.hire_date) BETWEEN 1980 AND 1990;

10. Create a SQL statement to increase salaries of all department’s managers up to 10% 
who are working since 1990.

--First Attempt

CREATE TEMPORARY TABLE dept_man_sal AS(

SELECT dm.emp_no, e.first_name, e.last_name, d.dept_name, d.dept_no, s.salary, e.hire_date FROM employees e 
LEFT JOIN dept_manager dm ON e.emp_no = dm.emp_no
RIGHT JOIN departments d ON dm.dept_no = d.dept_no
LEFT JOIN salaries s ON e.emp_no = s.emp_no
);

UPDATE dept_man_sal
    SET salary = 
        CASE YEAR(hire_date) WHEN <=1990 THEN salary * 1.10
        END ;

--Second Attempt

CREATE TEMPORARY TABLE man_sal AS(

SELECT * FROM salaries s
LEFT JOIN employees e ON s.emp_no = e.emp_no
LEFT JOIN dept_manager dm ON e.emp_no = dm.emp_no
WHERE s.emp_no IN (SELECT emp_no FROM dept_manager)
) ;

UPDATE dept_man_sal
    SET salary = 
        CASE YEAR(hire_date) WHEN <=1990 THEN salary * 1.10
        END ;
