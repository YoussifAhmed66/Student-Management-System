-- Creating the departments table with department no. as id starting from 10 with auto increment and time stamps on creation and updating
-- so the user will only need to insert the name of the department when adding or updating records in this table
CREATE table departments(
	Dno INT PRIMARY key AUTO_INCREMENT,
    Name VARCHAR(20) UNIQUE NOT NULL,
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)AUTO_INCREMENT = 10;

-- Creating the students table with the student details and an id for each each student with auto increment starting from 1000 and timestamps on creation and updating
-- each student must have a department no. as a foreign key from the departments table and it restricts deleting departments found in this table
CREATE TABLE students(
	Sid INT PRIMARY KEY AUTO_INCREMENT,
    Fname VARCHAR(20) NOT NULL,
    Mname VARCHAR(20) NOT NULL,
    Lname VARCHAR(20) NOT NULL,
    Email VARCHAR(30) UNIQUE NOT NULL,
    Phone CHAR(11) UNIQUE NOT NULL,
    Address VARCHAR(100) NOT NULL,
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    Dno INT NOT NULL,

    CONSTRAINT departments_fk
        FOREIGN KEY(Dno) 
        REFERENCES departments(Dno) 
        ON DELETE RESTRICT
        ON UPDATE CASCADE
    
)AUTO_INCREMENT = 1000;


-- Creating the courses table with details of the courses and a course no. as id with auto increment starting from 1 and timestamps on creation and updating
-- each course must have a department no. responsible for it as a foreign key from the departments table and it restricts deleting departments found in this table
CREATE TABLE courses(
	Cno INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(20) NOT NULL,
    Capacity INT NOT NULL,
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    Dno INT NOT NULL,
    FOREIGN KEY (Dno) REFERENCES departments(Dno) 
        ON DELETE RESTRICT 
        ON UPDATE CASCADE
    
);


-- creating the enrollments table which is an intermediate table between students and courses since their relation is M-N that defines which students enrolled in which courses
-- it takes the student id as a foreign key from the students table and department no. as a foreign key from the departments table and when the student was enrolled in this course and the grade has a default value 'Pending' since it is defined at the end of the course
-- the table has a composite key consisting of student id, department id, and erollment date of the student
CREATE TABLE enrollments(
	Sid INT NOT NULL,
    Cno INT NOT NULL,
    Enrolled_at DATE NOT NULL,
    Grade VARCHAR(10) DEFAULT 'Pending',
    
    -- Foreign key to students
    FOREIGN KEY (Sid) REFERENCES students(Sid)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    
    -- foreign key to courses
    FOREIGN KEY (Cno) REFERENCES courses(Cno)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    
    PRIMARY KEY(Sid, Cno, Enrolled_at)
);

-- creating the instructors table cantaining the instructors details and an id for each instructor with auto increment starting from 100 and timstamps for creation and updating
-- each instructor has a department no. foreign key from the department table represnting the department he is workin in
CREATE TABLE instructors(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    Fname VARCHAR(20) NOT NULL,
    Lname VARCHAR(20) NOT NULL,
    Email VARCHAR(30) UNIQUE NOT NULL,
    Phone CHAR(11) UNIQUE NOT NULL,
    Status ENUM('Available', 'Unavailable') NOT NULL,
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    Dno INT NOT NULL,
    
    FOREIGN KEY (Dno) REFERENCES departments(Dno)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
)AUTO_INCREMENT = 100;


-- creating the teaching table which is an intermendiate table between instructors and courses sinse the relation between them is M-N that defines which instructor teaches which courses
-- it takes the instructor id as a foreign kwy from the instrucors table and course no. from the courses table and the assignment date of the instructor with the course
-- the table has a compisite key consisting from instructor id, course no, and the assignment date
CREATE TABLE teaching(
    Instructor_id INT NOT NULL,
    Cno INT NOT NULL,
    assigned_at DATE NOT NULL,
    
    FOREIGN KEY (Instructor_id) REFERENCES instructors(Id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    
    FOREIGN KEY (Cno) REFERENCES courses(Cno)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    
    PRIMARY KEY (Instructor_id, Cno, Term)
);