import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import Data, Block, InitialPedestrian

room_m = Data.ROOM_M
room_n = Data.ROOM_N
exit_width = Data.EXIT_WIGTH
exit_center = 20
people_number = Data.PEOPLE_NUMBER


def draw_main(Peoples):
    plt.clf()
    draw_boundary()
    draw_exit()
    draw_wall()
    # draw_pedestrian()
    draw_exit()

    drawinf()

    drawPeople(Peoples)
    if Data.FLAG == False:
        plt.close()
    else:
        plt.pause(0.01)


def count_exit_axis_horizontal():
    e_x_1 = exit_center - exit_width / 2
    e_x_2 = exit_center + exit_width / 2
    e_y = room_n
    x_list = []
    x_list.append(e_x_1)
    x_list.append(e_x_2)
    y_list = []
    y_list.append(e_y)
    y_list.append(e_y)
    result = []
    result.append(x_list)
    result.append(y_list)
    return result


def draw_wall():
    exit_axis = count_exit_axis_horizontal()
    plt.plot([0, room_m], [0, 0], 'k-')  # bottom,
    plt.plot([0, exit_axis[0][0]], [room_n, room_n], 'k-')  # upper left
    plt.plot([exit_axis[0][1], room_m], [room_n, room_n], 'k-')  # upper right
    plt.plot([0, 0], [0, room_n], 'k-')  # left
    plt.plot([room_m, room_m], [0, room_n], 'k-')  # right

    # plt.plot([exit_center - exit_width / 2, exit_center + exit_width / 2], [room_n, room_n])
    plt.plot([exit_axis[0][0], exit_axis[0][1]], [exit_axis[1][0], exit_axis[1][1]], 'g-', linewidth=6)
    # plt.Rectangle((room_m - exit_width, room_n),exit_width * 2,3)


def draw_boundary():
    '''
    绘制外框，如果不加框，行人从出口出去会造成图像震荡
    框距离墙壁为 3
    :return:
    '''
    plt.plot([-3, room_m + 3], [-3, -3], 'k-')  # bottom
    plt.plot([-3, -3], [-3, room_n + 3], 'k-')  # left
    plt.plot([room_m + 3, room_m + 3], [-3, room_n + 3], 'k-')  # right
    plt.plot([-3, room_m + 3], [room_n + 3, room_n + 3], 'k-')  # upper


def draw_exit():
    pass


def draw_pedestrian():
    pass


def drawPeople(P):
    # plt.clf()  # 清除数据
    P_x_clock = []  # 存放所有行人x坐标
    P_y_clock = []  # 存放所有行人y坐标
    P_x_clock_conter = []
    P_y_clock_conter = []
    BLIND_x = []  # 盲人blind
    BLIND_y = []
    BLIND_x_c = []  # 盲人blind
    BLIND_y_c = []
    DEAF_x = []  # 聋人deaf
    DEAF_y = []
    DEAF_x_c = []  # 聋人deaf
    DEAF_y_c = []
    ZC_x = []  # 正常人
    ZC_y = []
    ZC_x_c = []  # 正常人
    ZC_y_c = []
    for p in P:  # 遍历行人

        if p.type == 1:
            if p.clock_wise:
                BLIND_x.append(p.x)
                BLIND_y.append(p.y)
            else:
                BLIND_x_c.append(p.x)
                BLIND_y_c.append(p.y)
        elif p.type == 2:
            if p.clock_wise:
                DEAF_x.append(p.x)  # 盲人
                DEAF_y.append(p.y)
            else:
                DEAF_x_c.append(p.x)  # 盲人
                DEAF_y_c.append(p.y)
        elif p.type == 3:
            if p.clock_wise:
                ZC_x.append(p.x)
                ZC_y.append(p.y)
            else:
                ZC_x_c.append(p.x)
                ZC_y_c.append(p.y)
        else:
            print('sty')
    '''
    for p in P:  # 遍历行人
        if p.clock_wise:
            P_x_clock.append(p.x)  # 分别添加坐标
            P_y_clock.append(p.y)
        else:
            P_x_clock_conter.append(p.x)
            P_y_clock_conter.append(p.y)
    plt.scatter(P_x_clock, P_y_clock, c='r', marker='o')  # 顺时针行人
    plt.scatter(P_x_clock_conter, P_y_clock_conter, c='b', marker='o') # 逆时针行人
    '''
    plt.scatter(BLIND_x, BLIND_y, c='b', marker='*')  # 盲人blind
    plt.scatter(DEAF_x, DEAF_y, c='b', marker='D')  # 聋人deaf
    plt.scatter(ZC_x, ZC_y, c='b', marker='o')  # 正常人

    plt.scatter(BLIND_x_c, BLIND_y_c, c='r', marker='*')  # 盲人blind
    plt.scatter(DEAF_x_c, DEAF_y_c, c='r', marker='D')  # 聋人deaf
    plt.scatter(ZC_x_c, ZC_y_c, c='r', marker='o')  # 正常人

    '''由于无法右上角关闭 加了个关闭按钮'''
    closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])  # 关闭按钮
    closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')  # 按钮样式
    closeFigbutton.on_clicked(closeFigure)  # 按钮按下去的动作

    # plt.savefig("%d.png" %step) #保存图片用
    # while Data.pause_flag:
    #     plt.pause(1)  # 暂停1s
    # plt.pause(0.3)  # 暂停1s


def closeFigure(event):
    print('onclick')
    plt.close()
    Data.FLAG = False

def drawinf():
    plt.scatter(Data.FX_M,Data.FX_N,c='g', marker='s')

if __name__ == '__main__':
    draw_main()
