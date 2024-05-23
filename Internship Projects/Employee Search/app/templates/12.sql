-- Correct syntax and check for any Oracle-specific clauses
INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000001', 'John Smith', 'M', 'New York', 50000, 10000, 'Manager', 'Sales', 60000.00, '123 Main St', 'Apt 4B', 'NY', 10001, 1234567890, 'E0000005', 'Jane Doe'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000002', 'Alice Johnson', 'F', 'Los Angeles', 45000, 9000, 'Analyst', 'Marketing', 54000.00, '456 Elm St', 'Suite 500', 'CA', 90001, 2345678901, 'E0000006', 'Robert Brown'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000003', 'Michael Williams', 'M', 'Chicago', 47000, 9500, 'Developer', 'IT', 56500.00, '789 Oak St', 'Floor 3', 'IL', 60601, 3456789012, 'E0000005', 'Jane Doe'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000004', 'Emily Davis', 'F', 'Houston', 42000, 8500, 'Designer', 'Creative', 50500.00, '101 Pine St', 'Building A', 'TX', 77001, 4567890123, 'E0000007', 'Richard Roe'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000005', 'Jane Doe', 'F', 'New York', 55000, 11000, 'Director', 'Sales', 66000.00, '123 Main St', 'Apt 5A', 'NY', 10001, 5678901234, 'E0000008', 'Laura White'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000006', 'Robert Brown', 'M', 'Los Angeles', 48000, 9600, 'Manager', 'Marketing', 57600.00, '456 Elm St', 'Suite 600', 'CA', 90001, 6789012345, 'E0000008', 'Laura White'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000007', 'Richard Roe', 'M', 'Houston', 46000, 9200, 'Consultant', 'Finance', 55200.00, '102 Maple St', 'Building B', 'TX', 77002, 7890123456, 'E0000008', 'Laura White'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000008', 'Laura White', 'F', 'Chicago', 53000, 10600, 'VP', 'HR', 63600.00, '103 Cedar St', 'Building C', 'IL', 60602, 8901234567, 'E0000009', 'Nancy Green'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000009', 'Nancy Green', 'F', 'Boston', 51000, 10200, 'Executive', 'Admin', 61200.00, '104 Birch St', 'Suite 200', 'MA', 02101, 9012345678, 'E0000010', 'Edward Black'
);

INSERT INTO emp (
    emp_no, emp_name, sex, location, basic, hra, desgn, dept, salary, addr1, addr2, addr3, pin, ph_no, rep_officer_no, rep_officer_name
) VALUES (
    'E0000010', 'Edward Black', 'M', 'Miami', 54000, 10800, 'Senior Manager', 'Operations', 64800.00, '105 Redwood St', 'Apt 3C', 'FL', 33101, 9123456789, 'E0000008', 'Laura White'
);

commit;