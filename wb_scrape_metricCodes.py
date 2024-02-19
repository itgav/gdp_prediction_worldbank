import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# go to Worldbank and scrape a (what I think is) complete list of metrics and their associated codes that are used for API calls


def wb_scrape_metricCodes(output_path):
    url = 'https://data.worldbank.org/indicator?tab=all'
    response = requests.get(url=url)
    result_html = BeautifulSoup(response.content, 'html.parser')

    ### GET SECTION NAMES FOR THE METRICS ###
    # syntax: {data-reactid: name, ...}
    section_dict = {}
    for x_section in result_html.find_all('h3'):  # finding 'h3' tags
        try:
            section_id = x_section['data-reactid']
            section_name = x_section.a.text  # retrieve 'a' tag's text
            section_dict[section_id] = section_name
        except Exception:
            pass
    # print(section_dict)

    ### GET LIST OF METRICS AND THEIR NAMES ###
    indicator_list = []
    for x_link in result_html.find_all('a'):  # finding 'a' tags
        try:
            # where 'href' attribute starts with 'x'
            if x_link['href'].startswith('/indicator/'):
                # this id is enumerated from top to bottom on page, can use this to later determine the section title of the metrics
                x_dataReactId = int(x_link['data-reactid'])
                x_href = x_link['href']
                # remove non-indicator code text
                x_href = x_href.replace(
                    '/indicator/', '').replace('?view=chart', '')
                indicator_list.append([x_dataReactId, x_href, x_link.text])
            else:
                pass
        except Exception:
            pass
    # print(indicator_list)

    ### ADD CATEGORY NAME TO METRICS ###
    section_keys = list(section_dict.keys())
    section_keys = [int(x) for x in section_keys]  # convert to integers
    # sorted descending. Occurs in-place don't need to assign to variable
    section_keys.sort(reverse=True)
    # print(section_keys)

    df = pd.DataFrame(indicator_list, columns=['dataReactId', 'code', 'name'])
    df.loc[:, 'category'] = np.nan  # create NaN column to later fill

    for x_key in section_keys:
        section_name = section_dict[str(x_key)]
        df.loc[((df['dataReactId'] > x_key) & (df['category'].isna())),
               'category'] = section_name  # from bottom up apply category names

    df = df.drop(columns=['dataReactId'])  # remove
    # df['code'].isna().sum() # confirmed that no NaN codes

    ### EXPORT AS CSV ###
    df.to_csv(output_path, index=False)

    return (print("Worldbank metric codes have been exported to csv file."))
