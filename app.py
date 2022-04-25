from flask import Flask, request, jsonify
import csv
from datetime import date, datetime
from calculateage import calculate_age

app = Flask(__name__)


MONTH = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
         "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}


@app.route('/')
def hello_world():
    return "hello flask is running"


@app.route('/players_birth_year', methods=['GET'])
def player_birth_year():
    """
    This api is used to find the percentage of the players above the birth year mentioned.

    request :-> {"Year":"1995"}

    """
    input_json = request.get_json(force=True)
    birth_year = input_json["Year"]
    try:
        with open('Players.csv', 'r', ) as file:
            reader = csv.DictReader(file)
            total_player = []
            players = []
            no_dob = []
            for row in reader:
                if row['DOB'] != '':
                    date_birth = row['DOB']
                    date_birth = date_birth.split("-")
                    if date_birth[2] >= birth_year[2:]:
                        players.append(row['ï»¿Player_Name'])
                else:
                    no_dob.append(row['ï»¿Player_Name'])

                total_player.append(row['ï»¿Player_Name'])
            average_player = round((len(players) / len(total_player)) * 100, 2)
            no_dob_player = round((len(no_dob) / len(total_player)) * 100, 2)
            players_result = {f"Percentage of player born above {birth_year}": f"{average_player}%",
                              "Percentage of player with no date of birth": f"{no_dob_player}%"}
            return jsonify(players_result)
    except:
        return "something went wrong"


@app.route('/average_age', methods=['GET'])
def average_ages():
    """
    This api is used to find the average age of players in a team.

    Request:-> {"Country":"India"}
    """
    try:
        input_json = request.get_json(force=True)
        country_req = input_json["Country"]
        with open('Players.csv', 'r', ) as file:
            players_obj = csv.DictReader(file)
            total_of_age = {"total_players": 0, "age_dob": 0}
            for row in players_obj:
                if row['Country'] == country_req:
                    total_of_age["total_players"] = total_of_age["total_players"] + 1
                    if row["DOB"] != "":
                        date_of_birth = row["DOB"]
                        date_of_birth = date_of_birth.split("-")
                        org_date_of_birth = f"{date_of_birth[0]} {MONTH[date_of_birth[1]]} 19{date_of_birth[2]}"
                        org_date_of_birth = datetime.strptime(org_date_of_birth, "%d %m %Y")
                        age = calculate_age(org_date_of_birth)
                        total_of_age["age_dob"] = total_of_age["age_dob"] + age
            if total_of_age["total_players"] != 0:
                average_age = round(total_of_age["age_dob"] / total_of_age["total_players"], 2)
                team_age = {f"{country_req} team average age": f"{average_age}%"}
                return jsonify(team_age)
            else:
                return f"Players does not exits in {country_req}"
    except:
        return "something went wrong"


@app.route('/batsmen_position_left', methods=['GET'])
def batsmen_position():
    """
    This api is used to find the team which have most number of left hands batsmen.

    Request:-> Not required
    """
    batsmen_country = {}
    with open('Players.csv', 'r', ) as file:
        players_obj = csv.DictReader(file)
        try:
            for row in players_obj:
                position = row["Batting_Hand"].split("_")
                if position[0] == "Left":
                    if row["Country"] not in batsmen_country:
                        country = row["Country"]
                        batsmen_country[f"{country}"] = 0
                    else:
                        batsmen_country[f"{country}"] = batsmen_country[f"{country}"] + 1
            max_player_country = max(batsmen_country, key=batsmen_country.get)
            batsmen_left_country = {f"The country with maximum left hand batsmen is": f"{max_player_country}"}
            return jsonify(batsmen_left_country)
        except:
            return "something went Wrong"


@app.route('/no_country', methods=['GET'])
def no_country():

    """
    This is api is used to find the players whose country is not mentioned

    Request:-> Not required
    """
    try:
        no_country_player = []
        with open('Players.csv', 'r', ) as file:
            player_obj = csv.DictReader(file)
            for row in player_obj:
                if row["Country"] == "":
                    no_country_player.append(row['ï»¿Player_Name'])
            no_country = {"Player with no country defined": f"{no_country_player}"}
            return jsonify(no_country)
    except:
        return "something went wrong"


@app.route('/player_country', methods=['GET'])
def country_player():

    """
    This is api is used to get the list of players on the bases of the team name.

    Request:-> {"Country":"India"}

    """
    try:
        input_json = request.get_json(force=True)
        country = input_json["Country"]
        country_player = []
        with open('Players.csv', 'r', ) as file:
            player_obj = csv.DictReader(file)
            for row in player_obj:
                if row["Country"] == country:
                    country_player.append(row["ï»¿Player_Name"])

        if len(country_player) != 0:
            result = {f"Players of {country}": f"{country_player}"}
            return jsonify(result)
        else:
            return f"No player exists in {country}"
    except:
        return "something went wrong"
