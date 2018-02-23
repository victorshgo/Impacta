def dormir(dia_semana, feriado):
    if dia_semana == False or feriado == True:
        return True
    else:
        return False

def test_dormir():
    assert dormir(True, True) == True
    assert dormir(True, False) == False
    assert dormir(False, False) == True
    assert dormir(False, True) == True
    
    