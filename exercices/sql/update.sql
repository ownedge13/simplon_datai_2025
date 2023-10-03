USE articles_db;

-- INSERT INTO Famille (famille) VALUES ("titi");
-- INSERT INTO Famille (famille) VALUES ("tata");

INSERT INTO Famille (famille) VALUES ("aaa"),("bbb"),("ccc");

INSERT INTO Conditionnement (conditionnement) VALUES ("aa"),("bb"),("cc");

INSERT INTO Principale (Code_article,Libelle,Famille_ID,Conditionnement_ID,PU_HT)
VALUES 
(1010,"aaaaa",1,1,10.10),
(1010,"bbbbb",2,2,20.10),
(1010,"ccccc",2,3,30.50),
(1010,"ddddd",1,3,50.40);