import datetime
import pandas
import sys

from ardor_reward_summary.cli import process_command_line
from ardor_reward_summary.reward_calc import get_epoch_beginning, get_transactions


def main():
    api_dict = {
        "ardor": "https://ardor.jelurida.com/nxt?"
    }

    epoch_beginning = get_epoch_beginning(api_dict['ardor'])
    rewards_account = process_command_line()
    tx_list = get_transactions(api_dict['ardor'], 'IGNIS', rewards_account)

    try:
        txs = tx_list['transactions']
    except KeyError:
        sys.exit("Incorrect account.")

    df_tx_list = pandas.DataFrame(columns=['Date', 'From', 'Amount'])

    for row in txs:
        timestamp = row['timestamp'] + epoch_beginning / 1000
        tx_date_time = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        tx_date = datetime.datetime.strptime(tx_date_time, '%Y-%m-%d').date()
        if 'message' in row['attachment']:
            if 'NodeReward' in row['attachment']['message']:
                df_tx_list.loc[len(df_tx_list), df_tx_list.columns] = tx_date, \
                                                                      row['senderRS'], \
                                                                      float(row['amountNQT']) / 100000000

    df_reward_summary = df_tx_list.groupby(['Date', 'From']).agg(rewards=('Amount', 'sum'))

    with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df_reward_summary)


if __name__ == '__main__':
    main()
