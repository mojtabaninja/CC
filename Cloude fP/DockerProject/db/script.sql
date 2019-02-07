
create table users(user_id INT NOT NULL AUTO_INCReMENT PRIMARY KEY, fname TEXT, lname TEXT, nationcode TEXT, password TEXT);
insert into users(fname, lname,  nationcode, password) values ('mojtaba', 'hatami', '1', '123');

create table Onlineuser(user_id INT, token TEXT);

create table ElectionH(ElH_id INT NOT NULL AUTO_INCReMENT PRIMARY KEY, title TEXT);

create table ElectionD(ElD_id INT NOT NULL AUTO_INCReMENT PRIMARY KEY, ElH_id INT, Cndidate TEXT);

create table User_Election(user_id INT , ElH_id INT, ElD_id INT);


insert into ElectionD(ElD_id, ElH_id, Cndidate) values (1, 1, 'Hatami Mojtaba');
insert into ElectionD(ElD_id, ElH_id, Cndidate) values (2, 1, 'Reza Ahmadi');
insert into ElectionD(ElD_id, ElH_id, Cndidate) values (3, 1, 'Hatami Hassan');
insert into ElectionD(ElD_id, ElH_id, Cndidate) values (4, 1, 'Ali Mojtaba');
insert into ElectionD(ElD_id, ElH_id, Cndidate) values (5, 1, 'Mohsen Mojtaba');
insert into ElectionD(ElD_id, ElH_id, Cndidate) values (6, 1, 'Hatami Akbar');
insert into ElectionD(ElD_id, ElH_id, Cndidate) values (7, 1, 'Ahmadiyan sss');

