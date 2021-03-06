from bs4 import BeautifulSoup
import requests
# from urlparse import urljoin # python 2
from urllib.parse import urljoin

from django.conf import settings
from .youtube_one_page import extract_one_page
import logging

logger = logging.getLogger(__name__)


ytlink = 'https://www.youtube.com/channel/UCUvoulvwzCnUVk7yoduI_Gw/videos'


def get_links(url=ytlink):
    # cretate all css selectors
    ajax_css = "button[data-uix-load-more-href]"
    summ = list()

    s = requests.Session()

    r = s.get(url, proxies=settings.PROXY).content
    soup = BeautifulSoup(r, 'html.parser')

    # yield first visible links
    extract_one_page(soup, summ)

    # Load more button
    ajaxs = soup.select(ajax_css)
    if not ajaxs:
        return summ
    ajax = ajaxs[0]["data-uix-load-more-href"]

    while True:
        print(ajax)
        r = s.get(urljoin('https://www.youtube.com/', ajax), proxies=settings.PROXY)

        # next html is stored in the json.values()
        # soup = BeautifulSoup(r.content, "html.parser")
        soup = BeautifulSoup("".join(r.json().values()), "html.parser")
        extract_one_page(soup, summ)
        ajax = soup.select(ajax_css)
        # if empty "Load more" button would be gone
        if not ajax:
            break
        ajax = ajax[0]["data-uix-load-more-href"]
    return summ
