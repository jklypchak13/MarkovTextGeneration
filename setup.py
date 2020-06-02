import requests
import os
import sys
from bs4 import BeautifulSoup

# The Office scripts are pulled from https://transcripts.foreverdreaming.org/
# These are the corresponding IDs for the office scripts at the site.
seasons = {
    '1': [25301, 25306],
    '2': [25308, 25329],
    '3': [25332, 25354],
    '4': [25356, 25369],
    '5': [25372, 25397],
    '6': [25402, 25425],
    '7': [25427, 25450],
    '8': [25451, 25474],
    '9': [25476, 25498]
}


def get_episode(e_id: str, e_number: int, e_season: str, output_dir: str):
    """writes the specified episode to the specified file

    Arguments:
        e_id {str} -- the id of the string at the site to scrape.
        e_number {int} -- the episode number (for naming purposes)
        e_season {str} -- the season number (for naming purposes)
        output_dir {str} -- the path to write the file to
    """

    page = requests.get(
        f'https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t={e_id}')

    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('div', class_='postbody')
    lines = content[0].find_all('p')
    with open(f'{output_dir}{os.sep}episode_{e_season}x{e_number}.txt', 'w') as fp:
        for line in lines:
            # encode and decode to remove unsupported unicode characters.
            fp.write(line.text.encode('ascii', 'ignore').decode("utf-8"))
            fp.write('\n')


if __name__ == "__main__":
    # Create Parent Directory
    if not os.path.isdir('office_scripts'):
        os.mkdir('office_scripts')
    for season_num, ids in seasons.items():
        # Create Season Directory
        if not os.path.isdir(f'office_scripts{os.sep}season_{season_num}'):
            os.mkdir(f'office_scripts{os.sep}season_{season_num}')

        for episode_count, id_num in enumerate(range(ids[0], ids[1] + 1)):
            get_episode(id_num, episode_count + 1, season_num,
                        f'office_scripts{os.sep}season_{season_num}')
