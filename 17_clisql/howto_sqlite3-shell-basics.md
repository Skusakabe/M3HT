SJS: Shinji, Jeffery, Sebastian

SoftDev

K13 -- Egoless + CSS

2022-18-10

time spent: 2hrs

# how-to :: SQLite3 Shell Basics
---
## Overview


### Estimated Time Cost: x.x hrs (round to nearest 0.1)

### Prerequisites:

- Install SQLite3


1. Create a file for data
2. Create a table 
NOTE: Semicolon (;) required after each statement
```
CREATE TABLE <name> (<column name> <data type>, ...);
```
a. Can put in different data types (TEXT, INTEGER, REAL, NUMERIC, BLOB)

b. Column can be PRIMARY KEY  (every entry is unique & != NULL) or NOT NULL (No entry == NULL)

3. Insert data into table
```
INSERT INTO <tbl_name> VALUES ( <field 1>, <field 2> ...)
```

4. Get values from entries using ```SELECT```
```
SELECT * FROM <tbl_name>;
SELECT <field_name> FROM <tbl_name>;
```

a. Use * to get all fields from that table
b. Use <field_name> to get a single field


1. Step, with [hyperlink](https://xkcd.com)s...


### Resources
* thing1
* thing2

---

Accurate as of (last update): 2022-mm-dd

#### Contributors:  
Clyde "Thluffy" Sinclair  
Thundercleese, pd2  
Buttercup, pd7  
Blossom, pd7  
Bubbles, pd7  
Fake Grimlock, pd8  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
