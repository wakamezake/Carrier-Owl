import pickle
from pathlib import Path

import pytest

from src.carrier_owl import get_text_from_page_source

current_dir = Path(__file__).parent.absolute()


def get_arxiv_articles():
    with open(current_dir / 'test.pkl', 'rb') as f:
        articles = pickle.load(f)
    return articles


@pytest.mark.parametrize('html', [''])
def test_get_text_from_page_source(html):
    text = get_text_from_page_source(html)
