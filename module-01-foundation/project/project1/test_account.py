from bank import AccountFactory
from observer import SMSAlert, AuditLog
from registry import AccountRegistry


def test_account_functionality():

    registry = AccountRegistry()

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

    registry.add(account1)
    registry.add(savings)
    registry.add(current)

    registry.list_all()

    account1.deposit(2000)
    savings.add_interest()
    current.withdraw(2500)

    print()

    account = registry.find("1000224080786")

    if account:
        account.statement()

    print()

    registry.undo_last("1000224080786")

    account.statement()


test_account_functionality()