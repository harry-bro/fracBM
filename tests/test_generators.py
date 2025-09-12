import fracbm

def test_cholesky_length():
    B = fracbm.cholesky(0.9, 100)
    assert len(B) == 100

def test_daviesharte_length():
    B = fracbm.daviesharte(0.9, 100)
    assert len(B) == 100
