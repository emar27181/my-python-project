import requests
from config.constants_dev import API_KEY


# プレイヤーのpuuidを取得する関数
def get_player_puuid(api_key, game_name, tag_line):
    url = f'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'
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


# マッチリストを取得する関数
# マッチまでアクセス可能なAPIは個人利用で取得できない？(2024/08/03)
def get_recent_matches(api_key, puuid, count=10):
    url = f'https://ap.api.riotgames.com/val/match/v1/matchlists/by-puuid/{puuid}'
    print(f"url: {url}")
    params = {
        'start': 0,
        'count': count
    }
    headers = {
        'X-Riot-Token': api_key
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get match list. Status code: {response.status_code}, Response: {response.text}")
        return None


def main():
    puuid = get_player_puuid(API_KEY, "nodoame", "27181")
    print(f"puuid: {puuid}")
    get_recent_matches(API_KEY, puuid)


if __name__ == "__main__":
    main()
