import itertools

player = ['喜羊羊', '沸羊羊', '懒洋洋', '暖洋洋', '灰太狼']

cases = list(itertools.permutations(player, 5))
casess = []
for i in cases:
    casess.append(list(i))


def panduan(case):
    xi_index = case.index('喜羊羊')
    fei_index = case.index('沸羊羊')
    lan_index = case.index('懒洋洋')
    nuan_index = case.index('暖洋洋')
    hui_index = case.index('灰太狼')
    result1 = None
    result2 = None
    result3 = None
    result4 = None
    result5 = None
    for index,item in enumerate(case):
        if(index == 0):
            if(item == "灰太狼"):
                if xi_index > lan_index:
                    result1 = True
            else:
                if xi_index < lan_index:
                    result1 = True
        if(index == 1):
            if(item == "灰太狼"):
                if case.index(item) > nuan_index:
                    result2 = True
            else:
                if case.index(item) < nuan_index:
                    result2 = True
        if(index == 2):
            if(item == "灰太狼"):
                if case.index(item) > hui_index:
                    result3 = True
            else:
                if case.index(item) < hui_index:
                    result3 = True
        if(index == 3):
            if(item == "灰太狼"):
                if xi_index > fei_index:
                    result4 = True
            else:
                if xi_index < fei_index:
                    result4 = True
        if(index == 4):
            if(item == "灰太狼"):
                if nuan_index > hui_index:
                    result5 = True
            else:
                if nuan_index < hui_index:
                    result5 = True
    if (result1 and result2 and result3 and result4 and result5):
        print(case)
        return case


for case in casess:
    panduan(case)
