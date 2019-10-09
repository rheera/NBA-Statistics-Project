"""
scrape utilities
This file holds all the functions needed to scrape the necessary sections
from Basketball Reference.
"""

# Imported Packages
from bs4 import BeautifulSoup
import time
import csv
import selenium



def get_players(driver, player_db):
    """
    This method reads from bball ref's player index to extract name, id, and link data for all players that match the criteria
    :param driver: this is the selenium drive to be used for browser interaction
    :param player_db: a dictionary of all the players extracted
    """
    # Set up url and alphabet for index population
    base_url = "https://www.basketball-reference.com/players/"
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
    # test_sample = ['a', 'b', 'c']

    # loop through a-z (no x) to find all applicable players
    for letter in alphabet:
        # setup current url and retrieve with webdriver
        target_url = base_url + letter
        driver.get(target_url)

        # wait for website contents to load fully (timeout = 1 sec)
        time.sleep(1)

        # export source of webpage for scraping with BeautifulSoup
        html = BeautifulSoup(driver.page_source, "html.parser")

        # find the table of players
        table = html.find('table', attrs={'id': 'players'})
        player_list = table.find('tbody')

        for details in player_list.find_all('tr'):
            # find each line for a player and parse into array for reading
            identifier = details.a
            full_details = details.find_all('td')
            parsed_detail = tuple([attr.text for attr in full_details])

            # restrict player base to be playing after 2000
            if int(parsed_detail[1]) > 2016:
                # extract player's page link and name
                link = identifier.get('href')
                name = identifier.string

                # extract player id from player name
                player_page = link.split("/")[3]
                id = player_page.split(".")[0]

                # save basic info as a pair and add to db with player id as its key
                basic_info = [name, link]
                player_db[id] = basic_info


def get_adv_stats(player_url, player_id, stat_db):
    """
    This function receives a webdriver and a player index database and
    fetches all the advanced statistics
    :param player_url: a BeautifulSoup object of the player web page. can directly extract data from here
    :param player_id: the bball-ref's generated id for the player
    :param stat_db: the dictionary of all the players' advanced stats. each entry is identified
    :return:
    """

    # identify the stat table
    table = player_url.find('table', attrs={'id': 'advanced'})
    all_stats = table.find('tbody')
    if (all_stats)
    for stat_line in all_stats.find_all('tr'):
        # extract the playing season of the current stat line, convert start year to integer to compare
        season = stat_line.th.a.text
        season_start = int(season.split('-')[0])

        # extract only stat lines that are from after 2000 & with more than 20 games
        if season_start > 1999:
            # extract all stat values
            per_season = stat_line.find_all('td')

            # initialize from of interest with its identifiers: player_id, playing_season
            row = [player_id, season]

            # checks for season with more than 20 games
            if (int(stat_line.find('td', attrs={'data-stat': 'g'}).text)) > 19:
                # adds all stat values to row, in read order to store in stat_db
                for value in per_season:
                    row.append(value.text)

                # add newly generated stat line to db
                stat_db.append(row)


def get_per100(player_url, player_id, stat_db):
    """
    Works as with the advanced stat extractor
    :param player_url: BeautifulSoup web page of specified player
    :param player_id: id of the specified player
    :param stat_db: the database holding the stat of interest
    :return: null, all processed data is passed to the stat_db provided
    """
    # identify the stat table
    table = player_url.find('table', attrs={'id': 'per_poss'})
    all_stats = table.find('tbody')

    for stat_line in all_stats.find_all('tr'):
        # extract the playing season of the current stat line, convert start year to integer to compare
        season = stat_line.th.a.text
        season_start = int(season.split('-')[0])

        # extract only stat lines that are from after 2000 & with more than 20 games
        if season_start > 1999:
            # extract all stat values
            per_season = stat_line.find_all('td')

            # initialize from of interest with its identifiers: player_id, playing_season
            row = [player_id, season]

            # checks for season with more than 20 games
            if (int(stat_line.find('td', attrs={'data-stat': 'g'}).text)) > 19:
                # adds all stat values to row, in read order to store in stat_db
                for value in per_season:
                    row.append(value.text)

                # add newly generated stat line to db
                stat_db.append(row)


def get_shooting_stats(player_url, player_id, stat_db):
    """
    Works as with the advanced stat extractor, but it does not test for season year as all shooting stats are from after 2000
    :param player_url: BeautifulSoup web page of specified player
    :param player_id: id of the specified player
    :param stat_db: the database holding the stat of interest
    :return: null, all processed data is passed to the stat_db provided
    """
    # identify the stat table
    table = player_url.find('table', attrs={'id': 'shooting'})
    all_stats = table.find('tbody')

    for stat_line in all_stats.find_all('tr'):
        # extract the playing season of the current stat line, convert start year to integer to compare
        season = stat_line.th.a.text

        # extract all stat values
        per_season = stat_line.find_all('td')

        # initialize from of interest with its identifiers: player_id, playing_season
        row = [player_id, season]

        # checks for season with more than 20 games
        if (int(stat_line.find('td', attrs={'data-stat': 'g'}).text)) > 19:
            # adds all stat values to row, in read order to store in stat_db
            for value in per_season:
                row.append(value.text)

            # add newly generated stat line to db
            stat_db.append(row)


def get_stat_headings(driver, stat_type):
    """
    This function is used to find the table headings of stats.
    The function extracts the table headings of the specified stat needed.
    all headings extracted from a reference player page: Vince Carter - cartevi01
    :param driver: the selenium webdriver
    :param stat_type: string indicating which stat headings to extract
    :return: an array of the headings, in the extracted order.
    """

    # initialize field name container, adding player_id in the beginning
    field_names = ["player_id"]

    # set reference website and access through webdriver to get raw source page
    url = "https://www.basketball-reference.com/players/c/cartevi01.html"
    driver.get(url)
    time.sleep(1)
    raw = BeautifulSoup(driver.page_source, "html.parser")

    # find the right table to extract headings
    table = raw.find('table', attrs={'id': stat_type});
    headers = table.find('thead')

    fields = headers.find_all('th')

    if stat_type == 'shooting':
        temp = headers.find('tr')
        for row in temp:
            if row.tag['class'].text == 'over_header':
                continue
            else:
                fields = headers.find_all('th')

    for field in fields:
        field_names.append(field.text)

    return field_names

