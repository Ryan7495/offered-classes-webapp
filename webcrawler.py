'''
Author: Ryan

Date:	2020-03-09

This script downloads all course information for each school in each region
and saves the content as a csv file.

Ideally id recurse on a tree structure but given the fixed depth of 3 and the
fact that the data (drop downs) are given as lists, its easier to iterate
through each list to expand each branch till you hit the leaf node.
'''

import time 
import os
import sys

from lxml import html
from bs4 import BeautifulSoup

import requests
import csv
import mysql.connector
import sshtunnel


# Help menu
def help():
	print ("\nUsage:\n\ttime python3 webcrawler.py > output_data.csv\n")

def main():
	targetURL = "https://dalonline.dal.ca/PROD/fyskeqiv.P_TransEquiv"
	parameters = {}

	HTTPrequest = requests.post(targetURL, data = parameters)
	HTMLcode = BeautifulSoup(HTTPrequest.content, 'html.parser')

	# Iterativly
	# Use BS4 to select all the select elements with the name and prov attributes and values
	provinceOptions = HTMLcode.find_all('select', attrs = {'name' : 'prov'})
	provinceOptions = BeautifulSoup(str(provinceOptions), 'html.parser')

	skip1 = 0
	for province in provinceOptions.find_all('option'):
		skip1 += 1
		if skip1 <= 3:
			continue

		# Get the first list of provinces
		parameters = {'prov' : province['value']}
		HTTPrequest = requests.post(targetURL, data = parameters)

		if HTTPrequest.status_code is 429:
			time.wait(15)

		HTMLcode = BeautifulSoup(HTTPrequest.content, 'html.parser')

		# Use BS4 to select all the select elements with the name and inst attributes and values
		institutionOptions = HTMLcode.find_all('select', attrs = {'name' : 'inst'})
		institutionOptions = BeautifulSoup(str(institutionOptions), 'html.parser')

		skip2 = 0;
		for institution in institutionOptions.find_all('option'):
			skip2 += 1
			if skip2 <= 1:
				continue

			if len(institution['value']) < 3 or institution['value'] is 'NULL' or institution['value'] is 'DUMMY':
				continue

			# Get a list of all the instituions for each province
			parameters = {'prov' : province['value'], 'inst' : institution['value']}
			HTTPrequest = requests.post(targetURL, data = parameters)

			if HTTPrequest.status_code is 429:
					time.wait(15)

			# Use BS4 to select all the select elements with the name and subj attributes and values
			HTMLcode = BeautifulSoup(HTTPrequest.content, 'html.parser')
			subjectOptions = HTMLcode.find_all('select', attrs = {'name' : 'subj'})
			subjectOptions = BeautifulSoup(str(subjectOptions), 'html.parser')
			
			skip3 = 0;
			for subject in subjectOptions.find_all('option'):
				skip3 += 1
				if skip3 <= 1:
					continue
				if len(subject['value']) < 3 or subject['value'] is 'NULL' or subject['value'] is 'DUMMY':
					continue

				# Get a list of all subjects for each institution in each province
				parameters = {
				'prov' : province['value'], 
				'inst' : institution['value'], 
				'subj' : subject['value']}

				HTTPrequest = requests.post(targetURL, data = parameters)

				if HTTPrequest.status_code is 429:
					time.wait(15)

				HTMLcode = BeautifulSoup(HTTPrequest.content, 'html.parser')

				tableValues = HTMLcode.find_all('td', attrs = {'class':'dedefault'})

				i = 0
				#For all the values in the record, print on the same line
				for cell in tableValues: 
					#You've been spared from formatting the output. 
					#Pat spent way too much time chasing invisible characters.
					#Removes hidden <br> tags as well as \n\r\t elements. 
					output = cell.get_text(strip = True, separator = " ") 
					#print(str(output))

					#Output is currently a Tuple. Convert to String. 
					output = ''.join(output) 

					#Some courses have commas in their titles which ruins our CSV file
					output = output.replace(",", "") 

					#Add a comma for CSV format to separate each piece of data in the record. 
					output += "," 

					try:
                    #Courses offerred in other languages might have unicode characters that could crash your program
						output = output.encode().decode('unicode_escape')
						csvfile.write(output)
						pass

					except UnicodeDecodeError:
						continue
					if (i < 4):
                        #Records are in groups of 4 but we're given the whole table at once.
						i = i + 1
					else:
                        #Record the university's name and subject at the end of the record
						output += institution.get_text() + "," + subject.get_text() + ',\n'
						csvfile.write(output)
						i = 0   

					# sql table into database

	csvfile.close()


if __name__== "__main__":
	main()
