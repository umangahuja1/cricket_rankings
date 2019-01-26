from bs4 import BeautifulSoup
import requests


def Menu():
    print('\n1. Men \n2. Women\n')
    gen = Gender()
    print('\n1. Team Rankings \n2. Player Ranking\n')
    tp = TeamOrPlayer()

    mode = ''
    val = ''

    if gen == 'mens':
        print('\n1. Test\n2. ODI\n3. T20\n')
        mode = Mode()

    if tp == 'player-rankings':
        if mode == '':
            print('\n1. ODI\n2. T20\n')
            mode = Mode2()
        print('\n1. Batting\n2. Bowling\n3. All-Rounder\n')
        val = Value()

    return gen, tp, mode, val


def Gender():
    gender = input('Enter your choice:')
    code = {'1': 'mens', '2': 'womens'}

    if gender in code:
        return code[gender]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Gender();


def TeamOrPlayer():
    choice = input('Enter your choice:')
    tp = {'1': 'team-rankings', '2': 'player-rankings'}

    if choice in tp:
        return tp[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return TeamOrPlayer();


def Mode():
    choice = input('Enter your choice:')
    word = {'1': '/test', '2': '/odi', '3': '/t20i'}

    if choice in word:
        return word[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Mode();


def Mode2():
    choice = input('Enter your choice:')
    word = {'1': '/odi', '2': '/t20i'}

    if choice in word:
        return word[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Mode2();


def Value():
    choice = input('Enter your choice:')
    val = {'1': 'batting', '2': 'bowling', '3': 'all-rounder'}

    if choice in val:
        return val[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Value()


def URL():
    gen, tp, mode, val = Menu()
    url = 'https://www.icc-cricket.com/rankings/' + gen + '/' + tp + mode + '/' + val
    header = gen.upper() + ' ' + mode[1:].upper() + ' ' + val.upper()
    print('\n{:<15}  {:<30}\n{:<15}  {:<30}'.format('', tp.upper(), '', header))
    print()
    return url, tp


def SOUP(url, tp):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        a = soup.find_all('tr', {'class': 'table-body'})
        
        data = []

        for i in a:
            rank = None
            player = None
            team = None
            rating = None
            
            try:
                rank = int(i.find('td', {'class':'table-body__cell--position'}).text)

                if tp == 'player-rankings':
                    try:
                        player = i.find('div', {'class':'name'}).text.strip()
                        team_name = i.find('div', {'class':'nationality-logo'}).text.strip()
                    except:
                        try:
                            player = i.find('td', {'class':'name'}).text.strip()
                            team_name = i.find('td', {'class':'nationality-logo'}).text.strip()
                        except:
                            pass
                else:
                    team_name = i.find('td', {'class':'rankings-table__team'}).text.strip()

                rating = i.find('td', {'class':'rating'}).text.strip()
            
            except:
                pass


            if tp == 'player-rankings':
                row = {
                'rank' : rank, 
                'name' : player,
                'team' : team_name,
                'rating' : rating
            }

            else:
                row = {
                'rank' : rank, 
                'team' : team_name,
                'rating' : rating
                }


            data.append(row)

        return data

    except:
        print("Sorry couldn't find the data right now")


def Print(data, tp):
    if tp == 'player-rankings':
        print('{:<25}{:<25}{:<25}{:<25}'.format('RANKING', 'Name', 'TEAM', 'RATING'))    
    else:
        print('{:<25}{:<25}{:<25}'.format('RANKING', 'TEAM', 'RATING'))   

    for row in data[:10]:
        for key in row.keys():
            print('{:<25}'.format(row[key]), end='')
        print()


def rankings():
    """
    Diplays cricket rankings based on the input given by users

    Args : None (No arguements are passed into this function)

    Returns : None (No value is returned by this function)

    """

    url, tp = URL()
    data = SOUP(url, tp)
    Print(data,tp)


if __name__ == '__main__':
    rankings()
