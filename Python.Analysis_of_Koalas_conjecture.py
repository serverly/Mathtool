# 角谷猜想的范围计算及智能统计  -Python实现  @3125875442@qq.com  By Mhr
# 我知道我的代码很难看懂，我自己过一会都看不懂

# 即将更新的功能：奇偶数、素数归一步数分析、list可视化、查找经典轨道数字


# Utf-8

main_history = ''  # 全局，ke保存后的历史记录文本
history_dir = {}  # 全局，ke保存后的历史记录字典，保存每档历史记录的详细数据
dir_num = 0  # 全局，当前选中的历史记录字典索引
accuracy = int(7)  # 全局，四舍五入精度，可自由调整为某一整数

allruntimes = 0


# 设置全局变量


def calculation():
    """函数 —— 计算角谷猜想"""
    begin_num = input('起始数字-The begin number:\n')
    last_num = input('结束数字-The last number:\n')

    if begin_num.isdigit() == False or last_num.isdigit() == False:
        print(f'输入的范围 {begin_num}~{last_num} 不是正整数范围，已自动调整为：1~1')
        begin_num, last_num = 1, 1
        # 纠正输入非正整数
    elif int(begin_num) < 1:
        begin_num = 1
        print(f'输入的起始数字 {begin_num} <=1,已自动将输出范围调整为 {begin_num}~{last_num}')
        # 纠正起始小于1
    elif int(begin_num) > int(last_num):
        begin_num = int(last_num) - 1
        print(f'输入的起始数字范围矛盾,已自动将输出范围调整为 {begin_num}~{last_num}')
        # 纠正起始大于末尾

    bothnums = range(int(begin_num), int(last_num) + 1)
    value_2 = 0

    contents_all = []  # 聚合输出
    contents_num = []  # 聚合数字
    contens_max = []  # 最大值列表
    contens_times = []  # 运行次数列表
    contents_placeofmax = []  # 最大值出现位置列表

    # 此四列表分离了解析参数，便于后期进一步生成数据

    times = 0  # 总运次
    _order = ''

    # 以上 设定局部变量
    global allruntimes
    allruntimes = 0
    for runvalue in bothnums:
        allruntimes = allruntimes + 1
        value_2 = value_2 + 1
        loophistory = [runvalue]
        for runnum in loophistory:
            allruntimes = allruntimes + 1
            if runnum != 1:
                if runnum % 2 == 0:
                    runnum = int(runnum / 2)
                    loophistory.append(runnum)
                # 偶数操作
                else:
                    runnum = runnum * 3 + 1
                    loophistory.append(runnum)
        # contents.append(f'{value_2}\t计算数字:{runvalue}\t计算次数:{len(loophistory)}\t最大值:{max(loophistory)}\
        # \t最大值出现位置:{loophistory.index(max(loophistory)) + 1}\n')
        times = times + 1
        contens_times.append(len(loophistory))
        contens_max.append(max(loophistory))
        contents_placeofmax.append(loophistory.index(contens_max[times - 1]))
        contents_num.append(runvalue)
        contents_all.append(f'Number:{runvalue}\tTimes:{contens_times[times - 1]}\tMax:{contens_max[times - 1]}\t\
        MaxnumberPlace:{contents_placeofmax[times - 1]}\n')

    global main_history  # global 可以表明即将在封闭的函数内引用全局变量
    _order = input("您是否想要将本次计算历史保存？\nDo you want to keep the history document later? [Yes/No]\n")
    if _order.lower() == 'yes':
        global dir_num
        dir_num = dir_num + 1
        history_dir[f'History {str(dir_num)}'] = \
            {'number': contents_num, 'max': contens_max, 'maxplace': contents_placeofmax, 'times': contens_times}
        print(f'The History {str(dir_num)} was kept already.')


def write_txt(_place, _data, _num):
    """写出计算过程 _place:写出目录 _data:写出数据 _num:当前序数"""
    odvuce = open(f"{_place}\\calculation {_num}.txt", 'w', encoding='utf-8')
    odvuce.write(_data)


def longest_txt(list_):
    len_group = []
    for txt in list_:
        len_group.append(len(txt))
    return list_[len_group.index(max(len_group))]


def strtobool(str_):
    if str_.lower() == 'true':
        return True
    else:
        return False


def is_prime(nx, mode_def):
    """判断奇数偶数或素数合数，mode= True则判断素数合数，mode= False则判断奇数偶数。奇数，素数为True"""
    if mode_def:
        import math

        if nx <= 1:
            return False
        if nx == 2:
            return True
        if nx > 2 and nx % 2 == 0:
            return False

        max_div = math.floor(math.sqrt(nx))
        for i in range(3, 1 + max_div, 2):
            if nx % i == 0:
                return False
        return True
    else:
        if nx % 2 == 0:
            return False
        else:
            return True


def ask_averaging(list_):
    num_c = 0
    for value_def in list_:
        num_c = num_c + value_def
    return round(num_c / len(list_), accuracy)  # 四舍五入到浮点数5位


print(
    '欢迎使用此Python程序进行角谷猜想的分析计算\n'
    'Welcome to use this Python program to analyze and calculate the corner Valley conjecture.\n'
)
# 启动欢迎

# 以下为继服务循环支
continue_ = True
helptxt = 'ke \t —— 将已进行的算法记录保存为txt，后续需提供保存目录及索引位置\nca \t —— 进行角谷猜想范围计算\n' \
          'ch \t —— 在控制台输出运算历史记录\nse \t —— 从历史记录筛选数据\ntime\t —— 输出当前总运次\n' \
          'chetypenum\t —— 解析指定数字范围内角谷猜想与素数、合数的关系\ndraw \t —— 绘画数据统计图\n\n''......\n\nhelp ' \
          '\t —— 获取帮助\nexit \t —— 退出计算程序'
# C:\Users\86152\Desktop
while continue_:
    command = input("你待会想要进行什么操作？\nwhat do you want to order next?\n")
    command = command.lower()
    if command == 'exit':
        continue_ = False
    elif command == 'help':
        print(helptxt)
    elif command == 'ca':
        calculation()
    elif command == 'draw':
        print('这些是您已经保存了的历史记录文档\nThese are the history documents you have.\n')
        for value in history_dir.keys():
            print(f'\t{value}')
        place = input(
            '请输入您想要展示的历史文档的序号\nPlease input the ordinal number of history document which you want to check.\n'
        )
        draw_history_dir = history_dir.get(f'History {place}', '参数错误\nWrong parameter')
        if draw_history_dir != '参数错误\nWrong parameter':
            draw_dir_number = draw_history_dir.get('number')
            # data_numbers = data_dir.get('number')
            # data_max = data_dir.get('max')
            # data_maxplace = data_dir.get('maxplace')
            # data_times = data_dir.get('times')
            mode = input('请输入您想查看的数据类型\n\tmax\t最大值\n\tmaxplace\t最大值位置\n\ttimes\t计算次数\n')
            mode_datalist = draw_history_dir.get(mode, '参数错误\nWrong parameter')

            if mode_datalist != '参数错误\nWrong parameter':
                mode_datalist.insert(0, 0)
                import matplotlib.pyplot as drawplot

                from matplotlib.pyplot import MultipleLocator

                drawplot.rcParams['savefig.dpi'] = 480
                drawplot.rcParams['figure.dpi'] = 480
                # 设定统计图api
                x_str = ['0']

                for value in draw_dir_number:
                    x_str.append(str(value))
                drawplot.xlim(0, len(x_str))
                # 设置统计图x轴宽
                drawplot.plot(
                    x_str, mode_datalist, linewidth=0.25, label=r"$\mathregular{\xi_a}$=0", color='k',
                    linestyle='solid'
                )
                # 设置统计图属性

                drawplot.title(f'{mode.title()} line graph', fontsize=8)
                drawplot.xlabel('Numbers', fontsize=8)
                drawplot.ylabel(mode.title(), fontsize=8)
                #  drawplot.tick_params(axis='both', which='major', labelsize=5)
                import math
                if len(mode_datalist) > 10 ** len(str(len(mode_datalist))) / 4:

                    lenth_gra = 10 ** (len(str(len(mode_datalist))) - 1)
                else:
                    lenth_gra = 10 ** (len(str(len(mode_datalist))) - 2)
                x_major_locator = MultipleLocator(lenth_gra)
                #  把x轴的刻度间隔设置为1，并存在变量里
                ax = drawplot.gca()
                ax.xaxis.set_major_locator(x_major_locator)
                #  把x轴的主刻度设置为10的倍数
                drawplot.xticks(fontsize=5)
                drawplot.yticks(fontsize=5)
                drawplot.xticks(rotation=90)

                # drawplot.savefig('C:\\Users\\86152\\Desktop\\1.png')

                drawplot.show()
    elif command == 'ke':
        place = input(
            '请输入正确的保存地址\nPlease input the correct save address.\n')
        print('\n')
        for key, value in history_dir.items():
            print(f'{key}')

        num = input(
            '\n这些是已经保存的计算历史，请输入您想要保存的历史文档序号'
            'These are the cal history,please input the ordinal number of document which you want to keep.\n'
        )
        data_dir = history_dir.get(f'History {num}', 'None')
        if data_dir != 'None':
            # noinspection PyRedeclaration
            data_numbers = data_dir.get('number')
            data_max = data_dir.get('max')
            data_maxplace = data_dir.get('maxplace')
            data_times = data_dir.get('times')
            data_last = []
            value = 0
            for _num_ in data_numbers:
                data_last.append(f'num= \t{data_numbers[value]}\t'
                                 f'max= \t{data_max[value]}\t'
                                 f'maxplace= \t{data_maxplace[value]}\t'
                                 f'runtimes= \t{data_times[value]}\t\n'
                                 )
                value = value + 1
            # {'number':contents_num, 'max':contens_max, 'maxplace':contents_placeofmax, 'times':contens_times}
            txtlast = ''
            txtlast = txtlast.join(data_last)
            write_txt(place, str(txtlast), num)
            print('可能已经保存成功了，您可以亲自查看\nMaybe it has been successed, you can check it self.\n')
    elif command == 'ch':
        place = input(
            '请输入您想要检查的历史文档的序号\nPlease input the ordinal number of history document which you want to check.\n'
        )
        print(
            history_dir.get(f'History {place}', '参数错误\nWrong parameter')
        )
    elif command == 'se':
        print('这些是您已经保存了的历史记录文档\nThese are the history documents you have.\n')
        for value in history_dir.keys():
            print(f'\t{value}')
        document = input('\n请输入历史文档的序号\nPlease input the number of history document.\n')
        _now_history = history_dir.get(f'History {document}', '参数错误-Wrong parameter')
        if _now_history != '参数错误-Wrong parameter':
            lastback = ''  # 最后返回文本
            nowgroup = history_dir
            print('1\t查看该历史文件中拥有相同最大值的数\n'
                  '2\t查看该历史文件中拥有相同计算次数的数\n'
                  '3\t查看该历史文件中拥有相同最大值位置的数\n\n'
                  '......\n\n 若范围过大，可能导致超长时间运算.建议范围始末区间大小小于5000.')

            select = input(
                f'请输入您想操作的历史文档的序号\n'
                'Please input the ordinal number of command which will effect the History {document}\n'
            )
            if select.isdigit():  # 检查命令合法
                if select == '1':  # 1方法
                    max_group = _now_history.get('max')
                    nonesecond = sorted(list(set(max_group)))
                    been_indiff = {}
                    numgroup = _now_history.get('number')
                    n = 0
                    for second in nonesecond:
                        n = n + 1

                        _just_maxgroup = []
                        for _max in max_group:
                            if _max == second:
                                max_group_2 = max_group[:]
                                # _just_timegroup.append(numgroup[times_group.index(_time)])

                                while _max in max_group_2:
                                    _just_maxgroup.append(numgroup[max_group_2.index(_max)])
                                    max_group_2[max_group_2.index(_max)] = 0
                        been_indiff[f'{n}.max= {second}\tnumber:'] = sorted(list(set(_just_maxgroup)))

                    # 1方法完成建设，been_indiff储存当前历史记录下的所有相同max值num。
                    # 以下为输出代码

                    _group_ke = []
                    for key, information in been_indiff.items():
                        _group_ke.append(f'{key} {str(information)}\n\n')
                    maxonlen = longest_txt(_group_ke)
                    _group_ke.append(maxonlen)
                    lastback = lastback.join(_group_ke)

                    print(lastback)

                elif select == '2':
                    # 2方法
                    times_group = _now_history.get('times')
                    nonetimes = sorted(list(set(times_group)))
                    been_indiff = {}
                    numgroup = _now_history.get('number')
                    n = 0
                    for time in nonetimes:
                        n = n + 1

                        _just_timegroup = []
                        for _time in times_group:
                            if _time == time:
                                times_group_2 = times_group[:]
                                # _just_timegroup.append(numgroup[times_group.index(_time)])

                                while _time in times_group_2:
                                    _just_timegroup.append(numgroup[times_group_2.index(_time)])
                                    times_group_2[times_group_2.index(_time)] = 0
                        been_indiff[f'{n}.time= {time}\tnumber:'] = sorted(list(set(_just_timegroup)))

                    # 2方法完成建设，been_indiff储存当前历史记录下的所有相同time值num。
                    # 以下为输出代码

                    _group_ke = []
                    for key, information in been_indiff.items():
                        _group_ke.append(f'{key} {str(information)}\n\n')
                    maxonlen = longest_txt(_group_ke)
                    _group_ke.append(maxonlen)
                    lastback = lastback.join(_group_ke)

                    print(lastback)

                elif select == '3':
                    maxplace_group = _now_history.get('maxplace')
                    nonemaxplace = sorted(list(set(maxplace_group)))
                    been_indiff = {}
                    numgroup = _now_history.get('number')
                    n = 0
                    for maxplace in nonemaxplace:
                        n = n + 1

                        _just_maxplacegroup = []
                        for _maxplace in maxplace_group:
                            if _maxplace == maxplace:
                                maxplace_group_2 = maxplace_group[:]
                                while _maxplace in maxplace_group_2:
                                    _just_maxplacegroup.append(numgroup[maxplace_group_2.index(_maxplace)])
                                    maxplace_group_2[maxplace_group_2.index(_maxplace)] = 0
                        been_indiff[f'{n}.max= {maxplace}\tnumber:'] = sorted(list(set(_just_maxplacegroup)))
                    # 3方法完成建设，been_indiff储存当前历史记录下的所有相同max值num。
                    # 以下为输出代码
                    _group_ke = []
                    for key, information in been_indiff.items():
                        _group_ke.append(f'{key} \t{str(information)}\n\n')
                    maxonlen = longest_txt(_group_ke)
                    _group_ke.append(maxonlen)
                    lastback = lastback.join(_group_ke)

                    print(lastback)

            command_ke = input('您想要保存这个返回文本吗？\nDo you want to keep the return text? [Yes/No]\n')
            if command_ke.lower() == 'yes':
                keplace = input('那么请输入正确的保存地址\nThen input correct save address.\n')
                write_txt(keplace, lastback, document)
                print('也许已经保存成功了，您可以亲自查看\nMaybe it has been successed, you can check it self.\n')
        else:  # 自此条件筛选代码块结束
            print('参数错误-Wrong parameter')
    elif command == 'time':
        print(f'for runtimes={allruntimes}')
    elif command == 'chetypenum':
        beginnum = input('起始数字是什么?\nwhat is first number?\n')
        lastnum = input('\n结束数字是什么?\nwhat is last number?\n')
        mode = input('操作模式是什么?\nwhat is the mode?\n\tTrue\t素数和合数-Prime numbers and total numbers'
                     '\n\tFalse(Or any others)'
                     '\t偶数和奇数-Odd numbers and even numbers\n'
                     )
        if beginnum.isdigit() == True and lastnum.isdigit() == True:
            beginnum = int(beginnum)
            lastnum = int(lastnum)
            if mode:
                mode_str = ['', 'prime numbers', 'total numbers']
                mode_str_z = ['', '素数', '合数']
            else:
                mode_str = ['', 'odd numbers', 'even numbers']
                mode_str_z = ['', '奇数', '偶数']

            result_list_max = {mode_str[1]: [], mode_str[2]: []}
            result_list_max_multiple = {mode_str[1]: [], mode_str[2]: []}
            result_list_time = {mode_str[1]: [], mode_str[2]: []}

            for num in range(beginnum, lastnum + 1):
                number_all = [num]
                for runvalue2 in number_all:
                    if runvalue2 != 1:
                        if runvalue2 % 2 == 0:
                            number_all.append(runvalue2 / 2)
                        else:
                            number_all.append(runvalue2 * 3 + 1)

                if is_prime(num, mode):
                    maxnum = max(number_all)
                    result_list_max[mode_str[1]].append(maxnum)
                    result_list_max_multiple[mode_str[1]].append(maxnum / num)
                    result_list_time[mode_str[1]].append(len(number_all))

                else:
                    maxnum = max(number_all)
                    result_list_max[mode_str[2]].append(maxnum)
                    result_list_max_multiple[mode_str[2]].append(maxnum / num)
                    result_list_time[mode_str[2]].append(len(number_all))

            p_list_max_averaging = ask_averaging(result_list_max[mode_str[1]])
            p_list_time_averaging = ask_averaging(result_list_time[mode_str[1]])
            p_list_maxmultiple_averaging = ask_averaging(result_list_max_multiple[mode_str[1]])

            t_list_max_averaging = ask_averaging(result_list_max[mode_str[2]])
            t_list_time_averaging = ask_averaging(result_list_time[mode_str[2]])
            t_list_maxmultiple_averaging = ask_averaging(result_list_max_multiple[mode_str[2]])

            print(f"\n对于指定的{beginnum}~{lastnum}进行的角谷猜想与{mode_str_z[1]}、{mode_str_z[2]}关系的解析如下(四舍五入精度:"
                  f"小数点后{accuracy}位):"
                  f"\n\n{mode_str_z[1]}:\n\t平均最大值:\t"
                  f"{p_list_max_averaging}\n\t平均运行次数:\t"
                  f"{p_list_time_averaging}\n\t平均最大值与原数的倍数:\t"
                  f"{p_list_maxmultiple_averaging}\n{mode_str_z[2]}:\n\t平均最大值:\t"
                  f"{t_list_max_averaging}\n\t平均运行次数:\t"
                  f"{t_list_time_averaging}\n\t平均最大值与原数的倍数:\t"
                  f"{t_list_maxmultiple_averaging}\n"
                  f"\n差值({mode_str_z[1]} - {mode_str_z[2]}):\n\t平均最大值:"
                  f"\t{round(p_list_max_averaging - t_list_max_averaging, accuracy)}"
                  f"\n\t平均运行次数:\t{round(p_list_time_averaging - t_list_time_averaging, accuracy)}"
                  f"\n\t平均最大值与原数的倍数:\t"
                  f"{round(p_list_maxmultiple_averaging - t_list_maxmultiple_averaging, accuracy)}"
                  "\n"
                  )

    else:
        print(helptxt)
