import requests
from config.constants_dev import API_KEY


# プレイヤーのpuuidを取得する関数
def get_player_puuid(api_key, game_name, tag_line):
    url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'
    print(f"url: {url}")

    headers = {
        'X-Riot-Token': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['puuid']
    else:
        print(f"Failed to get puuid. Status code: {response.status_code}, Response: {response.text}")
        return None


def main():
    puuid = get_player_puuid(API_KEY, "nodoame", "27181")
    print(f"puuid: {puuid}")


if __name__ == "__main__":
    main()
