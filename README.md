# CSCI 3172 Lab 6


## Web Crawler

For my web crawler I choose to scrape all the information in one pass and to not store any unnecessary data. The request package automaticly reuses the TCP connection to avoid redoing the TCP handshake each time. My webcrawler ran on Timberlea in ~21 mins while taking ~35 mins at home on my laptop scraping 49890 rows.


## Database Design

For my database I created a table with appropriate names given the data in the CSV file through the use of SQL queries. I then uploaded my CSV file into the table. Ideally id just write the data into the database using SQL queries in my web crawler, but I was unable to figure out how to open an SSH connection for my DB connection to run over. I might be able to avoid the SSH connection by skipping a hop just openning a DB connection while running the web crawler on Timberlea.


## Web Site

I wrote my two main files in php, the first, index.php is the landing page for my website where a user can search by institution, host course, dal course, credit hours and date. The second file takes the entered form field values and builds a SQL query to search by the parameters specified by the user.
