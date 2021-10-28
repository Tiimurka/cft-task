#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import mysql.connector

conn = mysql.connector.connect(
         user='tiimurka',
         password='***',
         host='127.0.0.1',
         database='cft')
		 
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS cft.records;')
cur.execute('DROP TABLE IF EXISTS cft.accounts;')
cur.execute('DROP TABLE IF EXISTS cft.products;')
cur.execute('DROP TABLE IF EXISTS cft.product_type;')
cur.execute('DROP TABLE IF EXISTS cft.tarifs;')
cur.execute('DROP TABLE IF EXISTS cft.clients;')

cur.execute('CREATE TABLE IF NOT EXISTS cft.clients ('\
    'ID DECIMAL(10) PRIMARY KEY, NAME VARCHAR(1000), PLACE_OF_BIRTH VARCHAR(1000), DATE_OF_BIRTH DATE, ADDRESS VARCHAR(1000), PASSPORT VARCHAR(100));')

cur.execute('CREATE TABLE IF NOT EXISTS cft.tarifs ('\
    'ID DECIMAL(10) PRIMARY KEY, NAME VARCHAR(100), COST DECIMAL(10,2));')

cur.execute('CREATE TABLE IF NOT EXISTS cft.product_type ('\
    'ID DECIMAL(10) PRIMARY KEY, NAME VARCHAR(100), BEGIN_DATE DATE, END_DATE DATE, TARIF_REF DECIMAL(10), '\
    'FOREIGN KEY (TARIF_REF) REFERENCES tarifs(ID));')

cur.execute('CREATE TABLE IF NOT EXISTS cft.products ('\
    'ID DECIMAL(10) PRIMARY KEY, PRODUCT_TYPE_ID DECIMAL(10), NAME VARCHAR(100), CLIENT_REF DECIMAL(10), OPEN_DATE DATE, CLOSE_DATE DATE, '\
    'FOREIGN KEY (CLIENT_REF) REFERENCES clients(ID), FOREIGN KEY (PRODUCT_TYPE_ID) REFERENCES product_type(ID));')

cur.execute('CREATE TABLE IF NOT EXISTS cft.accounts ('\
    'ID DECIMAL(10) PRIMARY KEY, NAME VARCHAR(100), SALDO DECIMAL(10,2), CLIENT_REF DECIMAL(10), OPEN_DATE DATE, CLOSE_DATE DATE, PRODUCT_REF DECIMAL(10), '\
    'ACC_NUM VARCHAR(25), FOREIGN KEY (CLIENT_REF) REFERENCES clients(ID), FOREIGN KEY (PRODUCT_REF) REFERENCES products(ID));')

cur.execute('CREATE TABLE IF NOT EXISTS cft.records ('\
    'ID DECIMAL(10) PRIMARY KEY, DT DECIMAL(1), SUM DECIMAL(10,2), ACC_REF DECIMAL(10), OPER_DATE DATE, '\
    'FOREIGN KEY (ACC_REF) REFERENCES accounts(ID));')

cur.execute('INSERT tarifs VALUES (1, \'Тариф за выдачу кредита\', 10);')
cur.execute('INSERT tarifs VALUES (2,\'Тариф за открытие счета\', 10);')
cur.execute('INSERT tarifs VALUES (3,\'Тариф за обслуживание карты\', 10);')

cur.execute('INSERT product_type VALUES (1, \'КРЕДИТ\', str_to_date(\'01 01 2018\',\'%d %m %Y\'), null, 1);')
cur.execute('INSERT product_type VALUES (2, \'ДЕПОЗИТ\', str_to_date(\'01 01 2018\',\'%d %m %Y\'), null, 2);')
cur.execute('INSERT product_type VALUES (3, \'КАРТА\', str_to_date(\'01 01 2018\',\'%d %m %Y\'), null, 3);')

cur.execute('INSERT clients VALUES (1, \'Сидоров Иван Петрович\', \'Россия, Московская облать, г. Пушкин\', str_to_date(\'01 01 2001\',\'%d %m %Y\'), \'Россия, Московская облать, г. Пушкин, ул. Грибоедова, д. 5\', \'2222 555555, выдан ОВД г. Пушкин, 10.01.2015\');')
cur.execute('INSERT clients VALUES (2, \'Иванов Петр Сидорович\', \'Россия, Московская облать, г. Клин\', str_to_date(\'01 01 2001\',\'%d %m %Y\'), \'Россия, Московская облать, г. Клин, ул. Мясникова, д. 3\', \'4444 666666, выдан ОВД г. Клин, 10.01.2015\');')
cur.execute('INSERT clients VALUES (3, \'Петров Сиодр Иванович\', \'Россия, Московская облать, г. Балашиха\', str_to_date(\'01 01 2001\',\'%d %m %Y\'), \'Россия, Московская облать, г. Балашиха, ул. Пушкина, д. 7\', \'4444 666666, выдан ОВД г. Клин, 10.01.2015\');')

cur.execute('INSERT products VALUES (1, 1, \'Кредитный договор с Сидоровым И.П.\', 1, str_to_date(\'01 06 2015\',\'%d %m %Y\'), null);')
cur.execute('INSERT products VALUES (2, 2, \'Депозитный договор с Ивановым П.С.\', 2, str_to_date(\'01 08 2017\',\'%d %m %Y\'), null);')
cur.execute('INSERT products VALUES (3, 3, \'Карточный договор с Петровым С.И.\', 3, str_to_date(\'01 08 2017\',\'%d %m %Y\'), null);')

cur.execute('INSERT accounts VALUES (1, \'Кредитный счет для Сидорова И.П.\', -2000, 1, str_to_date(\'01 06 2015\',\'%d %m %Y\'), null, 1, \'45502810401020000022\');')
cur.execute('INSERT accounts VALUES (2, \'Депозитный счет для Иванова П.С.\', 6000, 2, str_to_date(\'01 08 2017\',\'%d %m %Y\'), null, 2, \'42301810400000000001\');')
cur.execute('INSERT accounts VALUES (3, \'Карточный счет для Петрова С.И.\', 8000, 3, str_to_date(\'01 08 2017\',\'%d %m %Y\'), null, 3, \'40817810700000000001\');')

cur.execute('INSERT records VALUES (1, 1, 5000, 1, str_to_date(\'01 06 2015\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (2, 0, 1000, 1, str_to_date(\'01 07 2015\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (3, 0, 2000, 1, str_to_date(\'01 08 2015\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (4, 0, 3000, 1, str_to_date(\'01 09 2015\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (5, 1, 5000, 1, str_to_date(\'01 10 2015\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (6, 0, 3000, 1, str_to_date(\'01 10 2015\',\'%d %m %Y\'));')

cur.execute('INSERT records VALUES (7, 0, 10000, 2, str_to_date(\'01 08 2017\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (8, 1, 1000, 2, str_to_date(\'05 08 2017\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (9, 1, 2000, 2, str_to_date(\'21 09 2017\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (10, 1, 5000, 2, str_to_date(\'24 10 2017\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (11, 0, 6000, 2, str_to_date(\'26 11 2017\',\'%d %m %Y\'));')

cur.execute('INSERT records VALUES (12, 0, 120000, 3, str_to_date(\'08 09 2017\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (13, 1, 1000, 3, str_to_date(\'05 10 2017\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (14, 1, 2000, 3, str_to_date(\'21 10 2017\',\'%d %m %Y\'));')
cur.execute('INSERT records VALUES (15, 1, 5000, 3, str_to_date(\'24 10 2017\',\'%d %m %Y\'));')

conn.commit()
cur.close()
conn.close()





