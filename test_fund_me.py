# create this file under brownie_fund_me/tests
# refer video 2.solidity time 1:19:39


from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    account=get_account()
    fund_me=deploy_fund_me()
    entrance_fee=fund_me.getEntranceFee()
    tx=fund_me.fund({"from":account,"value":entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==entrance_fee
    tx2=fund_me.withdraw({"from":account})
    tx2.wait(1)
    
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
       pytest.skip("only for local testing")
    fund_me=deploy_fund_me()
    bad_actor=accounts.add()
    fund_me.withdraw({"from":bad_actor})
    
    
    
    


