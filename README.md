# MySQL-FSE-EngStore-

[Assignment2-fa23.pdf](https://github.com/ATacoDev/MySQL-FSE-EngStore-/files/13629502/Assignment2-fa23.pdf)

README

Jaden Johnson
ID: 2405823
Email: Jadjohnson@chapman.edu
CPSC-408 Section 1
Programming Assignment 2

Submission of main.py, menu.py, options.py, runProgram.py, README

Compilation/Run command: python runProgram.py

## Current Errors/Bugs
 - N/A

## Notes:
 - If the user picks option 6, I am assuming that they will pick a customer to make the order,
 as well as whatever that customer will order + the quantity.
 - I am also assuming that when it says "UnitPrice" in the OrderDetails table, that it's a reference to
 the price of one single unit from that order
 - Assuming the user makes an order, they will only be able to order 1 thing at a time.
 ie. They can order multiple things however they will go under different order IDs.
 - Otherwise, should work as intended by the requirements :).

## References:
- N/A


## Normalization Process:
- Given that we were allowed to assume the tables were already in 3NF, I Just took precaution
to make sure the tables stayed in 3NF when adding the new entries. This meant making sure
there were no transitive dependencies and making sure everything was independent on the tables.


Stored Procedures:
Since they were written in DataGrip, I'll post the txt versions of them both here.

# ADD NEW ORDER PROCEDURE
'''create
    definer = root@`%` procedure AddNewOrder(IN customer_id int, IN product_id int, IN quantity int)
BEGIN
    DECLARE order_id INT;

    INSERT INTO Orders (CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity, ShipPostalCode, ShipCountry)
SELECT
    c.CustomerID,
    NOW(),
    DATE_ADD(NOW(), INTERVAL 2 DAY),
    c.Address,
    c.City,
    c.PostalCode,
    c.Country
FROM
    Customers c
WHERE
    c.CustomerID = customer_id;

    SET order_id = LAST_INSERT_ID();
    -- Insert into OrderDetails table
    INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice)
    SELECT
           order_id,
           o.ProductID,
           quantity,
           o.UnitPrice
    FROM OrderDetails o
    WHERE
        o.ProductID = product_id;
     VALUES (order_id, product_id, quantity);

    -- Update stock quantity
    CALL UpdateStockQuantity(product_id, quantity);
END;'''


# UPDATE STOCK QUANTITY PROCEDURE
'''create
    definer = root@`%` procedure UpdateStockQuantity(IN product_id int, IN quantity int)
BEGIN
    -- Update stock quantity in the Products table
    UPDATE Products
    SET UnitsInStock = UnitsInStock - quantity
    WHERE ProductID = product_id;
END;'''
