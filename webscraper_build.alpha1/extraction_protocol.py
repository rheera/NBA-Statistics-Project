"""Imported Packages"""
from selenium import webdriver
import scrape_utils
import time
from bs4 import BeautifulSoup
import csv

"""
This file contains all functions need to read and save the scraped data from bball ref to a csv data file
"""

"""Global Variables"""
player_index = {}
adv_stats = []
per100_stats = []
shooting_stats = []

player_file = 'player_index.csv'
adv_file = 'adv_stats.csv'
per100_file = 'per100_stats.csv'
shooting_file = 'shooting_stats.csv'

# initialize webdriver
driver = webdriver.Chrome(
    #executable_path='C:/Users/New/Google Drive/CS4411 - Project/webscraper_build.alpha1/chromedriver.exe'
    executable_path='/usr/local/Cellar/chromedriver/2.37/bin/chromedriver'
)

def export_player_index():
    """
    Takes the player index and writes it to file
    :return: null, it writes to external file
    """

    # initialize field headers
    field_names = ['player_id', 'player_name', 'player_link']

    # initialize file writer
    player_export = open(player_file, 'w')
    writer = csv.writer(player_export)

    # write first line - title headers
    writer.writerow(field_names)

    # using the player keys, iterate through the index and write to file
    ids = player_index.keys()
    for pid in ids:
        writer.writerow([pid, player_index.get(pid)[0], player_index.get(pid)[1]])

""" 
    fetch player list using get_player
    uses initialized chrome driver to access websites
    player_index stores all the player information needed 
    to find their corresponding stats
"""
scrape_utils.get_players(driver, player_index)

# print(player_index)

# save the indexed players to a csv file
export_player_index()


"""
    fetch all stats - advanced, per100, shooting
    uses the player_index to find all the player id, 
    iterates through them to extract the the desired stat table
    each fetch is a separate function, but are done at once per player page
"""


def get_stats(player_id, player_basic):
    """
    This function is used to populate the stat files with all the eligible stats
    of all the players provided in database
    :param player_id: bball-ref generated player id
    :param player_basic: a basic pair holding the player's name and its location link
    :return:
    """
    # generate link to reach player's web page, then wait for it to load
    link = 'https://www.basketball-reference.com' + player_basic[1]
    driver.get(link)
    time.sleep(1)

    # use BeautifulSoup to convert page source to something usable
    html = BeautifulSoup(driver.page_source, "html.parser")

    # extract all the appropriate stats from the web page

    # advanced stats
    scrape_utils.get_adv_stats(html, player_id, adv_stats)

    # per100 stats
    scrape_utils.get_per100(html, player_id, per100_stats)

    # shooting stats
    scrape_utils.get_shooting_stats(html, player_id, shooting_stats)


# Stat Extraction

# extract all player ID's from the index
player_IDs = player_index.keys()

# use ID's to iterate through the players to get their stats into databases
for key in player_IDs:
    get_stats(key, player_index.get(key))


"""Writing the databases to file"""


def export_stat(exporter, fields, stat_db):

    # write stats
    writer = csv.writer(exporter)

    # write first line - title headers
    writer.writerow(fields)

    # write the stats to file
    writer.writerows(stat_db)


# initialize field headers
adv_fields = scrape_utils.get_stat_headings(driver, 'advanced')
per100_fields = scrape_utils.get_stat_headings(driver, 'per_poss')
sh_fields = scrape_utils.get_stat_headings(driver, 'shooting')

# initialize file writers
adv_exporter = open(adv_file, 'w')
per_exporter = open(per100_file, 'w')
sh_exporter = open(shooting_file, 'w')

# write stats to file
export_stat(adv_exporter, adv_fields, adv_stats)
export_stat(per_exporter, per100_fields, per100_stats)
export_stat(sh_exporter, sh_fields, shooting_stats)


driver.close()