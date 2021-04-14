CREATE TABLE ACME__EMPLOYEES( 
  ID   int ,
  NOT NULL  NAME varchar(250),
  PHONE char(10),
  EMAIL char(20),
  SSN  char(15),

);
CREATE TABLE ACME_EMPLOYEES_ADDRESSES( 
  ADDRESS_ID int ,
  NOT NULL  EMPLOYEE_ID int ,
  STREET char(80),
  ZIP  char(5),
  CITY char(30),

);
