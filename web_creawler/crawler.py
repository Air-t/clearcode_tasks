import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint


def site_map(url):
    """Return dictionary for all internal links in a given domain.

    :param url: domain string to be inspected. Trailing slash to be omitted
    """
    searched_links = []
    searched_links.append(url)
    final_map = {}

    def entry(url):
        """Return dictionary for all internal links in a given subdomain.

        :param url: domain string to be inspected.
        """
        final_map = {}
        # todo handle exceptions
        # download requested page
        page = requests.get(url).text

        # parse requested page
        soup = BeautifulSoup(page, 'html.parser')

        # todo add regex to not grab any "http" anchors. DONE
        links = soup.find_all('a', attrs={'href': re.compile("^(?!.*http(s)?://).*")})

        # todo how to set base url to be CONSTANT. DONE
        links_to_search = [f"{searched_links[0]}{tag.get('href')}" for tag in links]

        final_map = {'title': soup.title.text, 'links': set(links_to_search)}
        return final_map, links_to_search

    # creates base domain, first entry in dictionary
    final_map[url], links = entry(url)
    links_to_search = links

    # loop through found resources
    while links_to_search:
        link = links_to_search.pop()
        if link in searched_links:
            continue
        else:
            searched_links.append(link)
            final_map[link], links = entry(link)
            links_to_search.extend(links)

    # print returned object
    pprint(final_map)
    return final_map


# check if function works
if __name__ == '__main__':
    site_map("https://hackaday.com")


























