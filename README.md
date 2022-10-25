# Ardor Reward Summary

Ardor Reward Summary script presents daily rewards breakdown for Ardor and NXT nodes.
It takes as parameter wallet address, which was used to register chain nodes.

## Requirements
 - Python 3.8 or newer

## Installation

1. Clone repository and create a Python virtual environment
```bash
$ git clone https://github.com/ChainTools-Tech/ardor_reward_summary
$ cd ardor_reward_summary
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the requirements
```bash
(venv) $ python -m pip install -r requirements.txt
```

3. Install script
```bash
(venv) $ pip install -e .
```

## Usage

```bash
(venv) $ python -m ardor-reward-summary --account ARDOR-XXXX-XXXX-XXXX-XXXXX 
2022-09-29 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-09-30 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-10-01 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-10-02 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-10-03 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-10-04 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-10-05 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-10-06 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
2022-10-07 ARDOR-4PV4-Z2VE-PK78-DUWPX     127.2368
           ARDOR-B3YC-5537-72BN-2TYKS     127.2368
(venv) $
```
**NOTE:** In reward summary list rewards for Ardor nodes and NXT nodes are presented separately as sum of daily rewards 
for following addresses:
 - Ardor nodes reward: ARDOR-4PV4-Z2VE-PK78-DUWPX
 - NXT nodes reward: ARDOR-B3YC-5537-72BN-2TYKS


## Options

RP Checker provides the following options:

- `-a` or `--account` specifies wallet address which receives node rewards.


## Uninstall
```bash
(venv) $ pip uninstall ardor_reward_summary
```

## About the Author

Email: support@chaintools.tech

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this repo for more information.