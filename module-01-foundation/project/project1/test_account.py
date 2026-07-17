from bank import AccountFactory
from observer import SMSAlert, AuditLog


def test_account_functionality():

    account1 = AccountFactory.create("account", "Kidus", "1000224080786", 3000)
    savings = AccountFactory.create("savings", "Almaz", "1000224080787", 5000)
    current = AccountFactory.create("current", "Sara", "1000224080788", 2000)

    sms = SMSAlert()
    log = AuditLog()

    account1.subscribe(sms)
    account1.subscribe(log)

    savings.subscribe(sms)
    savings.subscribe(log)

    current.subscribe(sms)
    current.subscribe(log)

    account1.deposit(2000)
    savings.add_interest()
    current.withdraw(2500)

    accounts = [account1, savings, current]

    for account in accounts:
        account.statement()
        print()


test_account_functionality()