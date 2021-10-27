import importlib
import sys
from datetime import timedelta
from datetime import datetime
import re

# from temporal import roman
import temporal
from sanctoral import roman

# sys.path.append(".")
# import temporal.roman


def full_year(year):
    year_list = []
    yearstart = datetime(year=year, month=1, day=1)
    while yearstart.strftime("%Y") != str(year + 1):
        year_list.append(yearstart.strftime("%m/%d"))
        yearstart += timedelta(days=1)
    return year_list


def occur(one, two):
    '''
    If one occurs on two...
    '''
    occur_table = [
        [0, 1, 3, 1, 3, 3, 3, 3, 3, 3, 6, 5, 8, 6, 3, 3, 6],
        [0, 3, 3, 1, 3, 6, 3, 3, 3, 3, 6, 8, 6, 6, 3, 6, 6],
        [0, 3, 3, 3, 3, 4, 3, 3, 3, 7, 4, 4, 4, 0, 4, 4, 4],
        [0, 3, 3, 3, 3, 4, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 3, 3, 3, 3, 4, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 3, 3, 3, 3, 4, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 4, 4, 4],
        [0, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 0, 0],
        [0, 7, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 2, 0, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4],
    ]
    comparison = occur_table[one][-(two+1)]
    if comparison == 1: result = 1
    elif comparison == 2: result = 2
    elif comparison == 3: result = 3
    elif comparison == 4: result = 4
    elif comparison == 5: result = 5
    elif comparison == 6: result = 6
    elif comparison == 7: result = 7
    else: result = 8
    return result

def concur(one, two):
    '''
    If one concurs with two...
    '''
    concur_table = [
        [4, 0, 4, 4, 4, 4, 4, 4, 3, 3, 0],
        [2, 2, 2, 4, 4, 4, 4, 4, 5, 2, 4],
        [2, 2, 2, 4, 4, 4, 4, 4, 3, 3, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4],
        [4, 4, 4, 4, 4, 4, 4, 5, 3, 1, 3],
        [4, 4, 4, 4, 4, 4, 5, 3, 3, 1, 3],
        [4, 4, 4, 4, 4, 5, 3, 3, 3, 1, 3],
        [4, 4, 4, 4, 5, 3, 3, 3, 1, 1, 3],
        [4, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3],
        [4, 0, 0, 0, 3, 3, 3, 3, 1, 1, 3],
    ]
    comparison = concur_table[one][-(two+1)]
    if comparison == 1: result = 1   # all of the following, nothing of the preceding
    elif comparison == 2: result = 2 # all of the preceding, nothing of the following
    elif comparison == 3: result = 3 # all of the following, commemoration of the preceding
    elif comparison == 4: result = 4 # all of the preceding, commemoration of the following
    else: result = 5                 # all  of the more noble, commemoration of the other; in equality, a cap the following, commemoration of the preceding
    return result


def dict_clean(direct, dict):
    mdl = importlib.import_module(direct + str(dict))
    i = 0
    try:
        dic = mdl.temporal
    except AttributeError:
        dic = mdl.calen
    x = sorted(dic)
    for second in x:
        try: 
            first = x[i+1]
            if first[0:5] == second and len(first) == 6:
                #todo add a "nobility meter" to the feasts
                print(second)
                ranker = occur(dic[first]['rank'][0], dic[second]['rank'][1])
                if ranker == 1:
                    # office of the first
                    dic.update({first.strip('.'): dic[first]})
                    del dic[second], dic[first]
                elif ranker == 2:
                    # office of the second
                    dic.update({first.strip('.'): dic[second]})
                    del dic[second], dic[first]
                elif ranker == 3:
                    # commemoration of the second
                    dic[second].update({'feast': dic[first]['feast'], 'rank': dic[first]['rank'], 'target': dic[first]['target'], 'com1': dic[second]['feast']})
                    del dic[first]
                elif ranker == 4:
                    # commemoration of the first
                    dic.update({first.strip('.'): {'feast': dic[second]['feast'], 'rank': dic[second]['rank'], 'target': dic[second]['target'], 'com1': dic[first]['feast']}})
                    del dic[first]
                elif ranker == 5:
                    # translation of the second
                    dic.update({'trans' + second.strip('.'): dic[second]})
                    del dic[second]
                elif ranker == 6:
                    # translation of the first
                    dic.update({'trans_' + first.strip('.'): dic[first]})
                    del dic[first]
                elif ranker == 7:
                    # office of more noble, commemoration of the less noble
                    continue
                elif ranker == 8:
                    # office of the more noble, translation of the less noble
                    continue                        
                else: pass
            else: pass
            i += 1
        except IndexError:
            break
    gen_file = re.sub(r"\.", r'/', direct) + str(dict)
    with open(gen_file + ".py", "a") as f:        
        f.truncate(0)
        i = 0
        for line in sorted(dic):
            if i == 0: f.write(re.sub(r"/(temporal|calendar)", '', gen_file) + ' = {\n\'' + line + '\' : ' + str(dic[line]) + ',\n')
            else: f.write('\'' + line + '\' : ' + str(dic[line]) + ',\n')
            i += 1
        f.write('}')
        f.close()

def stitch(t, s):
    mdltemporal = importlib.import_module('temporal.temporal_' + str(t)).temporal
    mdlsanctoral = importlib.import_module('sanctoral.' + s).sanctoral
    mdlt, mdls = sorted(mdltemporal), sorted(mdlsanctoral)
    calen = {}
    for feast in mdls:
        if feast in mdlt:
            calen.update({feast+'.': mdlsanctoral[feast]})
        else:
            calen.update({feast: mdlsanctoral[feast]})
    for feast in mdlt:
        calen.update({feast: mdltemporal[feast]})
    with open("calen/calendar_" + str(t) + ".py", "w") as f:
        f.truncate(0)
        i = 0
        for line in sorted(calen):
            if i == 0: f.write('calen = {\n\'' + line + '\' : ' + str(calen[line]) + ',\n')
            else: f.write('\'' + line + '\' : ' + str(calen[line]) + ',\n')
            i += 1
        f.write('}')
    f.close()
    print('calendar stitched and written.')

    return 0
