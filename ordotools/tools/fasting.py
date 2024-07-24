from ordotools.tools.feast import Feast


def friday_abstinence(feast: Feast):
    if feast.date.strftime("%w") == '5':
        feast.abstinence = True
