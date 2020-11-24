'''
Porject 5: Web Scraping

Authors: Hongyu Zhang 

Extended Due Date: 10 p.m., Sunday, November 29, 2020

Description: This scrapes infomation form...

'''

'''Notes on what can be meaningful to be done:
What the is contry that is developed the most in the past 'user's choice' years?
Ploting the data using matplotlib
What is the correlation between some data points


'''

from bs4 import BeautifulSoup
import requests
import webbrowser

MENU_OPTIONS = "ABC"
Submenu = 'AB'

'''General functions'''
def parsecode(url):
    source_code = requests.get(url).text
    parsed_code = BeautifulSoup(source_code,'html.parser')
    return parsed_code

'''menu and choices'''
def menu():
    """Displays menu of options and gets user's input."""
    choice = 'none'
    while choice not in MENU_OPTIONS:
        print()
        print("A - select a website")
        print('B - ')
        print('Z - quit')
        choice = input("Please select an option from the menu: ").upper()
        print()
        if choice not in MENU_OPTIONS:
            print("Sorry,", choice, "is not one of the options, please try again.")
    
    return choice



def urlchoice():
    choice = 'none'
    while choice not in Submenu:
        print('Which website do you want to see scrap information from?')
        print('A - Data of Macro & Micro Economics Data from Ceicdata.com')
        print('B - IMBD?')
        print('Z - quit')
        choice = input("Please select an option from the menu: ").upper()
        if choice not in Submenu:
            print("Sorry,", choice, "is not one of the options, please try again.")
        elif choice == 'A':
            url = 'https://www.ceicdata.com/en'
    return url

'''data analysis'''
def econdata(url):
    




'''main'''
def main():
    choice = menu()
    
    while choice != 'Z':
        if choice == 'A':
            url = urlchoice()
            print(url)
        choice = menu

main()