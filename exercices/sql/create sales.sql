-- on jette on créé
DROP DATABASE IF EXISTS sales;
CREATE DATABASE sales;

-- on utilise 
USE sales;

-- on va créer nos tables 

-- table Country
CREATE TABLE Country
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Country VARCHAR(80) UNIQUE,
    PRIMARY KEY (ID)
);

-- table Product_Category
CREATE TABLE Product_Category
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Product_Category VARCHAR(80) UNIQUE,
    PRIMARY KEY (ID)
);

-- table Age_Group
CREATE TABLE Age_Group
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Age_Group VARCHAR(80) UNIQUE,
    PRIMARY KEY (ID)
);

-- table Customer_Gender
CREATE TABLE Customer_Gender
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Customer_Gender VARCHAR(80) UNIQUE,
    PRIMARY KEY (ID)
);

-- table State
CREATE TABLE State
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    State VARCHAR(80) UNIQUE,
    ID2 SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID2) REFERENCES Country(ID) ON DELETE CASCADE
);

-- table Sub_Category
CREATE TABLE Sub_Category
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Sub_Category VARCHAR(80) UNIQUE,
    ID2 SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID2) REFERENCES Product_Category(ID) ON DELETE CASCADE
);

-- table Product
CREATE TABLE Product
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Product VARCHAR(80) UNIQUE,
    ID2 SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID2) REFERENCES Sub_Category(ID) ON DELETE CASCADE
);

-- table Principale 
CREATE TABLE Principale
(
	ID INT NOT NULL AUTO_INCREMENT,
    Date_ date,
    Customer_Age INT,
    Age_Group SMALLINT UNSIGNED NOT NULL,
	Customer_Gender SMALLINT UNSIGNED NOT NULL,
	Country SMALLINT UNSIGNED NOT NULL,
    State SMALLINT UNSIGNED NOT NULL,
    Product_Category SMALLINT UNSIGNED NOT NULL,
    Sub_Category SMALLINT UNSIGNED NOT NULL,
    Product SMALLINT UNSIGNED NOT NULL,
	Order_Quantity INT,
    Unit_Cost INT,
    Unit_Price INT,
    Profit INT,
    Cost INT,
    Revenue INT,
    PRIMARY KEY (ID),
    FOREIGN KEY (Age_Group) REFERENCES Age_Group(ID) ON DELETE CASCADE,
    FOREIGN KEY (Customer_Gender) REFERENCES Customer_Gender(ID) ON DELETE CASCADE,
    FOREIGN KEY (Country) REFERENCES Country(ID) ON DELETE CASCADE,
    FOREIGN KEY (State) REFERENCES State(ID) ON DELETE CASCADE,
    FOREIGN KEY (Product_Category) REFERENCES Product_Category(ID) ON DELETE CASCADE,
    FOREIGN KEY (Sub_Category) REFERENCES Sub_Category(ID) ON DELETE CASCADE,
    FOREIGN KEY (Product) REFERENCES Product(ID)
);