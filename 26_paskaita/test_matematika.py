from matematika import sudetis, daugyba


def test_sudetis():
    assert sudetis(1,2) == 3


def test_sudetis_neigiami():
    assert sudetis(-1,-2) == -3

def test_daugyba():
    assert daugyba(2,5) == 10
    assert daugyba(2,5) > 0 # ats su teigiama reisme +
    assert daugyba(-2,5) < 0 # ats Neigiama reiksme -

def test_sudetis_2():
    num1, num2 = 5, 3
    rezultatas = 9
    faktinis_rez = sudetis(num1, num2)
    assert rezultatas == faktinis_rez, f'Sudeties testas neppavyko {num1} + {num2} turetu buti {rezultatas} bet gavome {faktinis_rez}'