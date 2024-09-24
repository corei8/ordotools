from ordotools.tools.feast import Feast
import logging


def sort_criterion(e):
    return e.rank_n


def sorted(one: Feast, two: Feast) -> list:
    feasts = [one, two]
    feasts.sort(key=sort_criterion)
    return feasts


def commemorate(feast: Feast, commemoration: Feast) -> Feast:
    feast.com_1 = {
        "code": commemoration.code,
        "rank": [commemoration.rank_n, commemoration.rank_v],
        "infra_octave_name": commemoration.infra_octave_name,
        "day_in_octave": commemoration.day_in_octave,
        "color": commemoration.color,
        "mass": commemoration.mass,
        "matins": {},
        "lauds": {},
        "vespers": commemoration.vespers,
        "nobility": commemoration.nobility,
        "office_type": commemoration.office_type,
    }
    # FIX: first commemorations being bumped to second commemoration
    #      this assumes that there is never a third commemoration... which is not true?
    if "code" in commemoration.com_1.keys():
        feast.com_2 = commemoration.com_1
    return feast


translated_feasts = []


def translate(feast: Feast, translated: Feast) -> Feast:
    # NOTE: do we really have to be returing anything here?
    logging.debug(f"Tranlsating {translated.code}")
    translated_feasts.append(translated)
    return feast


def nobility(one: Feast, two: Feast, handler: int) -> Feast:
    logging.debug(f"Ranking by nobility between {one.code} and {two.code}")
    for parameter in range(6):
        if one.nobility[parameter] < two.nobility[parameter]:
            if handler == 7:
                return commemorate(one, two)
            else:
                return translate(one, two)
        elif one.nobility[parameter] > two.nobility[parameter]:
            if handler == 7:
                return commemorate(two, one)
            else:
                return translate(two, one)
    else:
        return commemorate(one, two)


def rank(dynamic: Feast, static: Feast):

    group_one = (2, 5, 6, 7, 10, 13, 11, 14, 15, 16, 18, 19, 20, 22, )
    group_two = (1, 8, 12, 3, 2, 5, 6, 7, 10, 4, 13, 11, 14, 15, 16, 9, 17, 18, 19, 20, 21, )

    if dynamic.rank_n == 23:
        return static
    if static.rank_n == 23:
        return dynamic

    # distinguish between a major feria and vigil
    if dynamic.rank_n == 19 or static.rank_n == 19:
        if dynamic.rank_n == 19:
            if "v" in dynamic.rank_v.lower():
                # TODO: take care of the edge case where a vigil is anticipated
                if static.rank_n == 22:
                    one, two = static, dynamic
                else:
                    one, two = dynamic, static
            else:
                one, two = static, dynamic
        elif static.rank_n == 19:
            if "v" in static.rank_v.lower():
                one, two = static, dynamic
            else:
                one, two = dynamic, static

    # override our Lady's Saturday
    elif dynamic.rank_n == 21:
        if static.rank_n < 22:
            return static


    elif dynamic.rank_n in group_one and static.rank_n in group_two:
        one, two = dynamic, static
    else:
        one, two = static, dynamic

    def position_one() -> int:
        group_one_grouped = (
            (2, 5, 6, 7,), # Duplex I classis
            (10,),         # Duplex II classis
            (13,),         # Dies Octava Communis
            (11, 14,),     # Duplex majus
            (15,),         # Duplex minus
            (16,),         # Semiduplex
            (18,),         # Dies infra Oct. communem.
            (19,),         # Vigilia
            (20,),         # Dies Octava Simplex
            (22,),         # Simplex
        )
        for count, group in enumerate(group_one_grouped):
            if one.rank_n in group:
                return count
        else:
            return 0

    def position_two() -> int:
        group_two_grouped = (
            (1,),          # Dominica I classis
            (8,),          # Dominica II classis
            (12,),         # Dominica minor vel Vigilia Epiphaniæ
            (3,),          # Feria privileg., Vigilia I cl., vel dies infra Oct. I ord.
            (2, 5, 6, 7,), # Duplex I classis
            (10,),         # Duplex II classis
            (4,),          # Dies Octava II ordinis
            (13,),         # Dies Oct. Communis vel III ordinis
            (11, 14,),     # Duplex majus
            (15,),         # Duplex minus
            (16,),         # Semiduplex
            (9,),          # Dies infra Octavam II ordinis
            (17,),         # Dies infra Octavam III ordinis
            (18,),         # Dies infra Octavam communem
            (19,),         # Feria major non privilegiata
            (20,),         # Dies Octava simplex
            (21,),          # S. Maria in Sabbato
        )
        for count, group in enumerate(group_two_grouped):
            if two.rank_n in group:
                return 16 - count
        else:
            return 0

    ranking_table = (
        (0, 1, 3, 1, 3, 3, 3, 3, 3, 3, 6, 5, 8, 6, 3, 3, 6,),
        (0, 3, 3, 1, 3, 6, 3, 3, 3, 3, 6, 8, 6, 6, 3, 6, 6,),
        (0, 3, 3, 3, 3, 4, 3, 3, 3, 7, 4, 4, 4, 0, 4, 4, 4,),
        (0, 3, 3, 3, 3, 4, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4,),
        (0, 3, 3, 3, 3, 4, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4,),
        (0, 3, 3, 3, 3, 4, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,),
        (0, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 4, 4, 4,),
        (0, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 0, 0,),
        (0, 7, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 2, 0, 4, 4, 4,),
        (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4,),
    )

    ranking_result = ranking_table[position_one()][position_two()]

    if ranking_result == 1:
        ranked = one
    elif ranking_result == 2:
        ranked = two
    elif ranking_result == 3:
        ranked = commemorate(one, two)
    elif ranking_result == 4:
        ranked = commemorate(two, one)
    elif ranking_result == 5:
        ranked = translate(one, two)
    elif ranking_result == 6:
        ranked = translate(two, one)
    elif ranking_result == 7:
        ranked = nobility(one, two, ranking_result)
    elif ranking_result == 8:
        ranked = nobility(one, two, ranking_result)
    else:
        print(f"WARNING!! We have a problem with {one.code} occuring on {two.code}")
        return sorted(one, two)

    if not translated_feasts:
        return ranked
    else:
        if ranked is not None and ranked.rank_n > 16:
            for translated in translated_feasts:
                # NOTE: what is the limit for translating a feast?
                # We have to do something about the date of the feast as well.
                translated.date = ranked.date
                translated_feasts.remove(translated)
                return rank(ranked, translated)
        else:
            return ranked
