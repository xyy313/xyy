import pandas as pd

import matplotlib.pyplot as plt
from collections import Counter
def generate_img2(image_address):
    data = pd.read_excel(image_address,keep_default_na=False)



    a_list = data['单穴主治病证']
    # b_list = data[u'配穴2']
    # c_list = data[u'配穴3']
    # d_list = data[u'配穴4']
    # e_list = data[u'配穴5']
    # f_list = data[u'配穴6']
    # g_list = data[u'配穴7']
    # h_list = data[u'配穴8']
    # i_list = data[u'配穴9']
    # j_list = data[u'配穴10']
    # k_list = data[u'配穴11']
    # l_list = data[u'配穴12']
    # m_list = data[u'配穴13']
    # n_list = data[u'配穴14']
    # o_list = data[u'配穴15']
    # p_list = data[u'配穴16']
    # q_list = data[u'配穴17']
    # r_list = data[u'配穴18']
    # s_list = data[u'配穴19']
    # t_list = data[u'配穴20']
    # u_list = data[u'配穴21']

    global list
    list = list(a_list)
    # list(b_list)+list(c_list)+list(d_list)+list(e_list)+list(f_list)+list(g_list)+list(h_list)+list(i_list)\
    #        +list(j_list)+list(k_list)+list(l_list)+list(m_list)+list(n_list)+list(o_list)+list(p_list)+list(q_list)+list(r_list)+list(s_list)+list(t_list)+list(u_list)
    while '' in list:
     list.remove('')
    print(list)


    c = Counter(list)

    print(c)
    print([i for i in c.keys()])#取出键
    print([i for i in c.values()])


    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')  # 垂直和水平的布局
            # rect.get_x(),1.03*height,'%s' % int(height))
            plt.xticks(range(len(num_list)), name_list, rotation=80)  # rotation=80是横坐标的倾斜度


    name_list = [i for i in c.keys()]
    num_list = [i for i in c.values()]
    plt.figure(figsize=(10, 5))  # 画布大小
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('Category statistics of entities', fontsize=13)  # 设置标题，footsize是设置字体大小
    plt.xlabel(u'category', fontsize=11)  # 设置x轴的标题，以及它的字号大小
    plt.ylabel(u'quantity', fontsize=13)  # 设置y轴的标题，以及它的字号
    autolabel(plt.bar(range(len(num_list)), num_list, width=0.8, edgecolor='darkblue', lw=1))  # edgecolor：柱子轮廓色；lw：柱子轮廓的宽度；
    fig = plt.gcf()
    # plt.legend(loc=2)
    image_address_fin = image_address + '.jpg'
    fig.savefig(fname=image_address_fin)
# generate_img2()
# # plt.rcParams['font.sans-serif']=['SimHei']
# # plt.rcParams['axes.unicode_minus'] = False
# # data['单穴主治病证'].value_counts().plot.bar()
# # plt.show()
# word_counts = c
# counter_list = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
#
# label = list(map(lambda x: x[0], counter_list[:20]))
# value = list(map(lambda y: y[1], counter_list[:20]))
#
# plt.bar(range(len(value)), value, tick_label=label)
# plt.show()
