/* 1.For each different laptop speed, find the average price of the laptops in that group. Display (a) the speed and (b) the average price as 'avg price'. */

SELECT speed, AVG(price) AS 'avg price'
FROM laptop
ORDER BY speed;

/*
2. Find the average price of the PCs made by manufacturer A.

Hint: A natural join is helpful here. */
--product and pc give me the tables that have price and manufacturer
SELECT AVG(price) FROM PC NATURAL JOIN Product
            WHERE maker='A';

/*
3. For each manufacturer, find the average screen size of its laptops.
Hint: A natural join is helpful here. */
--getting maker in the same table as average screen
--all of the different options of maker finding average of all screens that apply to it
SELECT AVG(screen), maker FROM Laptop NATURAL JOIN Product 
            GROUP BY maker;
--tells me what I want the different groups to be, all avg screens grouped to specific group they belong to.

/*
 4.Which laptops are faster than at least one PC that has a smaller hard drive than the laptop? Display the model, speed, and hard drive size of these laptops.

Hint: A correlated subquery is helpful here. The shape of the solution is similar to that for Problem 6 on Homework 5.
*/
SELECT model, speed, hd AS HDLAPTOP FROM Laptop
WHERE speed > (SELECT MIN(SPEED) FROM PC WHERE HDLAPTOP > hd);
--hd in pc and sub query HDLAPTOP is the outside query related to the outside.

/*
Which manufacturer makes the color printer with the lowest price? Remember: the color attribute is a boolean value.

Hint: Correlated subqueries are helpful here, too. Try breaking the problem down into steps:

    find the price of the cheapest color printer
    find the model for that printer
    find the maker of that model

Use these small pieces as subqueries to build your solution. 
*/

--Will find model from inner query
--making it equal to the models we pull from those two subqueries 
SELECT maker FROM Product WHERE model =
(SELECT model FROM
(SELECT model, min(price) FROM Printer
WHERE color));
--subquery 



 
 
