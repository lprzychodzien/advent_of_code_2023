import numpy as np

def parse_txt_file() -> dict:
    games = {}
    data = open("day2/day2_input.txt","r").read().splitlines()
    
    for game in data:
        game_num = int(game.split(":")[0].split(" ")[1])
        game_data = game.split(":")[1].split(";")
     
        game_iterations = []
        for x in game_data:
            game_results = {}
            for y in x.split(","):
                result = y.strip().split(" ")
                result_num = int(result[0])
                result_color = result[1]
                game_results[result_color] = result_num
            game_iterations.append(game_results)

        games[game_num] = game_iterations
    
    return games

def check_game_possible(game:list) -> bool:
    limits = {
        'red':12,
        'green':13,
        'blue':14,
    }

    for g in game:
        for k,v in g.items():

            if k not in limits:
                return False
            
            if v > limits[k]:
                return False
    return True
            

def check_all_games_possible(games:dict) -> list:
    possible_games = []

    for game_num,game in games.items():
        if check_game_possible(game): #True = possible
            possible_games.append(game_num)

    return possible_games

def get_min_cubes_all_games(games:dict) -> list:
    game_powers = []
    
    for _,game in games.items():
        game_powers.append(get_game_power_of_mins(game))
    return game_powers

def get_game_power_of_mins(game:list) -> int:
    min_values = {}

    for g in game:
        for k,v in g.items():
            if k in min_values:
                if v > min_values[k]:
                    min_values[k] = v
            else:
                min_values[k] = v
    return np.prod(list(min_values.values()))


def part1() -> None:
    games = parse_txt_file()
    game_ids = check_all_games_possible(games)
    print(sum(game_ids))
    
def part2() -> None:
    games = parse_txt_file()
    game_powers = get_min_cubes_all_games(games)
    print(sum(game_powers))

if __name__ == "__main__":
    part1()
    part2()