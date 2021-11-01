# create this file under brownie_fund_me/scripts
# refer video 2.solidity time 1:15:11

from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
  fund_me=FundMe[-1]
  account=get_account()
