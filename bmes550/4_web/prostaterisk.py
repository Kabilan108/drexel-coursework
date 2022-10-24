"""
Compute the risk of prostate cancer using factors identified in "Decision 
Tree-Based Modeling of Androgen Pathway Genes and Prostate Cancer Risk", 
Cancer Epidemiol Biomarkers Prev. 2011 Jun; 20(6): 1146-1155
"""


def getprostaterisk(
    history: bool, 
    euro_ances: float, 
    repeat: int, 
    haplotype: str
) -> float:
    
    # Check for invalid inputs
    assert isinstance(history, bool), "history must either be True or False"
    assert 0 <= euro_ances <= 1, "euro_ances must be between 0 and 1"
    assert isinstance(repeat, int), "repeat must be an integer"
    assert isinstance(haplotype, str), \
        "haplotype must be one of 'AA', 'AG', 'GG', or 'GG'"
    haplotype = haplotype.upper()

    # Compute risk
    if history:
        if euro_ances >= 0.204:
            if haplotype in ['GA', 'AG', 'GG']:
                risk = 14 / (7 + 14)
            else:
                risk = 3 / (10 + 3)
        else:
            if repeat < 16:
                risk = 7 / (4 + 7)
            else:
                risk = 19 / (38 + 19)
    else:
        risk = 110 / (343 + 110)

    return round(risk, 4)


def test_getprostaterisk():
    # Test for invalid inputs
    try:
        getprostaterisk(1, 0.5, 10, 'GG')
    except AssertionError:
        pass
    else:
        raise AssertionError("getprostaterisk did not raise an AssertionError "
                             "when given invalid inputs")

    # Test for valid inputs
    assert getprostaterisk(False, 0.8, 12, 'GG') == 0.2428
    assert getprostaterisk(True, 0.1, 16, 'AA') == 0.3333
    assert getprostaterisk(True, 0.1, 10, 'AA') == 0.6364
    assert getprostaterisk(True, 0.8, 12, 'AA') == 0.2308
    assert getprostaterisk(True, 0.5, 16, 'GA') == 0.6667

    print("All tests passed!")


if __name__ == '__main__':
    test_getprostaterisk()
