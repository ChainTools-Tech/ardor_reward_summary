import json
import sys

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def get_epoch_beginning(api_url, api_headers=None, api_params=None):
    """
    https://ardor.qf3l3k.tech/nxt?requestType=getConstants
    :return:
    """
    if api_params is None:
        api_params = {}

    if api_headers is None:
        api_headers = {}

    api_session = Session()
    api_session.headers.update(api_headers)

    try:
        api_response = api_session.get(api_url + 'requestType=getConstants', params=api_params)
        api_json_data = json.loads(api_response.text)
    except (ConnectionError, Timeout, TooManyRedirects):
        sys.exit("Connection error.")

    return api_json_data['epochBeginning']


def get_transactions(api_url, chain_id, account, api_headers=None, api_params=None):
    """Fetch list of transactions for specific account.

    Args:
        :param api_url:
        :param chain_id:
        :param account:
        :param api_headers:
        :param api_params:

    Returns:
        :return:
    """
    if api_params is None:
        api_params = {}

    if api_headers is None:
        api_headers = {}

    api_session = Session()
    api_session.headers.update(api_headers)

    try:
        api_request = 'requestType=getBlockchainTransactions&chain=' + chain_id + '&account=' + account
        api_response = api_session.get(api_url + api_request, params=api_params)
        api_json_data = json.loads(api_response.text)
    except (ConnectionError, Timeout, TooManyRedirects):
        sys.exit("API connection error.")

    return api_json_data