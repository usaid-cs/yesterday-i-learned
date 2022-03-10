"""https://mdtax.ca/blog/physicians/personal-income-tax-brackets-ontario-2021/"""


tax_brackets = [
    [0, 13807, 0.00],
    [13808, 45142, 20.05],
    [45143, 49020, 24.15],
    [49021, 79500, 29.65],
    [79501, 90287, 31.48],
    [90288, 93656, 33.89],
    [93657, 98040, 37.91],
    [98041, 150000, 43.41],
    [150001, 151978, 44.97],
    [151979, 216511, 48.29],
    [216512, 220000, 51.97],
    [220001, 1000000, 53.53],
]


def get_net_income(gross_income):
    remainder = gross_income
    taxes = 0
    for bracket_from, bracket_to, tax_rate in tax_brackets:
        if remainder <= 0:
            continue
        whole_bracket = bracket_to - bracket_from
        taxable = min(whole_bracket, remainder)
        taxes += taxable * tax_rate / 100
        remainder -= taxable
    return int(gross_income - taxes)


for gross_income in range(0, 1000001, 1000):
    print(gross_income, get_net_income(gross_income))
