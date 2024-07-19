from ordotools.tools.feast import Feast

def sort_criterion(e):
    return e.rank_n

def sorted(one: Feast, two: Feast) -> list:
    feasts = [one, two]
    feasts.sort(key=sort_criterion)
    return feasts

def commemorate(feast: Feast, commemoration: Feast) -> Feast:
    # print(f"commemorating {commemoration.code}.")
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
        "fasting": commemoration.fasting,
    }
    return feast

translated_feasts = []

def translate(feast: Feast, translated: Feast) -> Feast:
    # print(f"commemorating {translated.code}.")
    translated_feasts.append(translated)
    return feast

def nobility(one: Feast, two: Feast, handler: int) -> Feast:
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
        # print("Warning! Nobility checker failed.")
        return commemorate(one, two)

            

def rank(dynamic: Feast, static: Feast) -> Feast | None | list:

    group_one = ( 2, 5, 6, 7, 10, 13, 11, 14, 15, 16, 18, 19, 20, 22, )
    group_two = (1, 8, 12, 3, 2, 5, 6, 7, 10, 4, 13, 11, 14, 15, 16, 9, 17, 18, 19, 20, 21, )
    # NOTE: if 19 is a vigil, it must go in 1

    if dynamic.rank_n == 23:
        return static
    if static.rank_n == 23:
        return dynamic

    # distinguish between a major feria and vigil
    if dynamic.rank_n == 19 or static.rank_n == 19:
        if dynamic.rank_n == 19:
            if "v" in dynamic.rank_v.lower():
                one, two = dynamic, static
            else:
                one, two = static, dynamic
        elif static.rank_n == 19:
            if "v" in static.rank_v.lower():
                one, two = static, dynamic
            else:
                one, two = dynamic, static

    elif dynamic.rank_n == 21:  # Our Lady's Saturday
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


    # print("-"*50)
    # print(f"{one.date.strftime('%b %d')}")
    # print(f"ONE = {one.code}, row {position_one()}")
    # print(f"TWO = {two.code}, col {position_two()}")

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

    # print(f"ranking result = {ranking_result}")

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
        return sorted(one, two)

    if not translated_feasts:
        # print(f"typeof result = {type(ranked)}")
        return ranked
    else:
        if ranked is not None and ranked.rank_n > 16:
            for translated in translated_feasts:
                translated_feasts.remove(translated)
                return rank(ranked, translated)
        else:
            # print(f"typeof result = {type(ranked)}")
            return ranked
