"""
Compute the risk of prostate cancer using factors identified in "Decision 
Tree-Based Modeling of Androgen Pathway Genes and Prostate Cancer Risk", 
Cancer Epidemiol Biomarkers Prev. 2011 Jun; 20(6): 1146-1155
"""

def getprostaterisk(
    history: str, 
    euro_ances: float, 
    repeat: float, 
    haplotype: str
) -> float:
    
    # Fix input variabels
    euro_ances = euro_ances / 100
    haplotype = haplotype.upper()
    history = True if history == 'Yes' else False

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


if __name__ == '__main__':
    import sys

    risk = getprostaterisk(
        sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    )
    print(f"{risk*100:.2f}%")
