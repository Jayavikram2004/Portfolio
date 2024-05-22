create table emp(
    emp_no char(8) 
    primary key,
    emp_name varchar(30),
    sex char(1),
    location VARCHAR(20),
    basic NUMBER(8),
    hra NUMBER(8),
    desgn VARCHAR(20),
    dept varchar(15),
    salary NUMBER(10,2),
    addr1 VARCHAR(20),
    addr2 VARCHAR(20),
    addr3 VARCHAR(20),
    pin NUMBER(8),
    ph_no NUMBER(10),
    rep_officer_no CHAR(8),
    rep_officer_name VARCHAR(30) 
);





INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(101, 'Alice Johnson', 'F', 'New York', 50000, 10000, 'Manager', 'HR', 60000.00, '123 Main St', 'Apt 4', 'Floor 2', 10001, 1234567890, 102, 'Bob Smith');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(102, 'Bob Smith', 'M', 'Chicago', 48000, 9000, 'Assistant Manager', 'HR', 57000.00, '456 Oak St', 'Apt 12B', 'Floor 3', 60616, 2345678901, 103, 'Carol White');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(103, 'Carol White', 'F', 'Los Angeles', 52000, 11000, 'Manager', 'Finance', 63000.00, '789 Pine St', 'Suite 5', 'Building B', 90001, 3456789012, 104, 'David Green');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(104, 'David Green', 'M', 'Houston', 46000, 8500, 'Analyst', 'Finance', 54500.00, '101 Maple St', 'Suite 1A', 'Building A', 77001, 4567890123, 103, 'Carol White');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(105, 'Eve Black', 'F', 'San Francisco', 55000, 12000, 'Senior Analyst', 'IT', 67000.00, '202 Birch St', 'Apt 8', 'Floor 4', 94101, 5678901234, 106, 'Frank Blue');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(106, 'Frank Blue', 'M', 'Boston', 53000, 10500, 'Manager', 'IT', 63500.00, '303 Cedar St', 'Suite 7C', 'Building C', 02101, 6789012345, 107, 'Grace Grey');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(107, 'Grace Grey', 'F', 'Seattle', 49000, 9500, 'Senior Analyst', 'IT', 58500.00, '404 Elm St', 'Apt 9', 'Floor 5', 98101, 7890123456, 106, 'Frank Blue');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(108, 'Hank Brown', 'M', 'Denver', 47000, 9000, 'Analyst', 'Sales', 56000.00, '505 Fir St', 'Suite 6A', 'Building D', 80201, 8901234567, 109, 'Ivy Pink');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(109, 'Ivy Pink', 'F', 'Miami', 51000, 10000, 'Manager', 'Sales', 61000.00, '606 Gum St', 'Apt 3B', 'Floor 6', 33101, 9012345678, 110, 'Jake Lime');

INSERT INTO emp (emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name) VALUES 
(110, 'Jake Lime', 'M', 'Dallas', 48000, 9200, 'Assistant Manager', 'Sales', 57200.00, '707 Hazel St', 'Suite 2D', 'Building E', 75201, 1230984567, 109, 'Ivy Pink');
