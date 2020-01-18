import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

pd.options.display.max_columns = None #Display all columns




poke_url = 'https://pokemondb.net/pokedex/all'

pokeresp = requests.get(poke_url)
pokerespsoup = BeautifulSoup(pokeresp.text, 'html.parser')

# print(pokerespsoup.prettify())

table_tag = pokerespsoup.find('table', attrs={'class' : 'data-table block-wide'})
# print(table_tag.prettify())

rows_tags = table_tag.findAll('tr')
headers = []
h_row = rows_tags[0]
h_col = h_row.findAll('th')
for hc in h_col:
    headers.append(hc.text.strip())
# print(headers)

poke_list = []
for poke_row_tag in rows_tags[1:]:
    # Find all td tags
    poke_td_tags = poke_row_tag.findAll('td')

    # Iterate through the td tags and store them in a list
    p_stats = []
    for pk in poke_td_tags[1:]:
        p_stats.append(pk.text.strip())

    # Iterate the list of headers and values and store them accordingly
    # in a dictionary
    p_stats_dict = dict()
    for k in range(0,len(headers)-1):
        p_stats_dict[headers[k+1]] = p_stats[k]
    poke_list.append(p_stats_dict)

df = pd.DataFrame(poke_list)
df_ordered =df[headers[1:]]
print(df_ordered)

df_ordered.to_json(orient='table')

# special = random.randint(0,len(df_ordered))
# print(df_ordered.iloc[[special], :])
