#display all records from the table
SELECT * FROM Customers;

SELECT City FROM Customers

#Select all the different values from the table.
SELECT DISTINCT Country FROM Customers;

#Select all records where the column has the value specific.
SELECT * FROM Customers
WHERE City = 'Berlin';

#NOT keyword to select all records where condition is NOT.
SELECT * FROM Customers
WHERE NOT City = 'Berlin';

#Select all records where the column has the value specific.
SELECT * FROM Customers
WHERE Customer ID = 32;

#Select all records where columnd habe specifiec values.
SELECT * FROM Customers
 WHERE City = 'Berlin' AND PostalCode = 12209;

#Select all records where columns satisfy either one of the conditions.
SELECT * FROM Customers City = 'Berlin' OR City  = 'London';