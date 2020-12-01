# chat-api


## 1. Creating the api

This was easy to do with Flask.

## 2. Creating the tables in SQL

At first I decided to create 3 tables: Chats, Users and Messages. But in order to simplify the requests I deleted the chat table and keep only two tables as follows:
<p><img src="images\Table_1.png" width="40%"></p> <p><img src="images\Table_2.png" width="20%"></p>

## 3. Connecting the api with SQL

This was the biggest challange just because I didn't know the steps to follow, nonetheless was very simple (once I could understand how it works). 

I created 4 endpoints and 3 functions:

1. The first enpoint for welcoming.
2. The second one to get the tables. This was linked with the function get_table.
3. The third one to introduce users. This was linked with the function users.
4. The fourth one to introduce messages. This was linked with the function messages.

## 4. Creating data

I created some fake names, lasnames and departments trhough Postman that I stored in the Users table. 

<p><img src="images\Postman.png" width="60%"></p>

After that I defined some functions for different tasks: to introduce messages manually, to introduce fake messages using a predefined fuction called faker(), to introduce messages by department.

Also I web scrapped 3 sites of lyrics where I got two love songs and one hate love.


## 5. Analyse data

I defined some functions to get data, to clean and organise data and to analyse the hapiness by department or the global happiness.



