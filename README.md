# CSCI 3172 Lab 6


## Web Crawler

For my web crawler I choose to scrape all the information in one pass and to not store any unnecessary data. The request package automaticly reuses the TCP connection to avoid redoing the TCP handshake each time. My webcrawler ran on Timberlea in ~21 mins while taking ~35 mins at home on my laptop scraping 49890 rows.


## Database Design

For my database I created a table with appropriate attributes given the data in the CSV file through the use of SQL queries. I used SQL queries to insert the scraped data into the database.


## Web Site

I wrote my two main files in php, the first, index.php is the landing page for my website where a user can search by institution, host course, dal course, credit hours and date. The second file takes the entered form field values and builds a SQL query to search by the parameters specified by the user.
