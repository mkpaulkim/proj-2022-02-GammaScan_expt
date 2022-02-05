
import os

import numpy as np

import pycubelib.hardware as hw
import pycubelib.files_functions as ff
import pycubelib.general_functions as gf
import pycubelib.plotting_functions as pf
import pycubelib.tkclasses as tkc

pi = np.pi
pi2 = pi*2
pilim = (-pi, pi)
cwd = os.path.dirname(__file__)
txtpath_0 = "E:\{{SeaGate}}\Dropbox\[DATA FOLDER]\[DATA 2022-02] GammaScan\data 0202"

print(f'\n>> initialize devices and front panel ...')
uno = hw.Arduino()
qcam = hw.Quantalux()
pzt = hw.MDT694B()
ddr = hw.DDR25()

print(f'\n>> set up front panel ...')
tkw = tkc.tkwindow('A_gammaexpt.py', window=(20, 20, 955, 390))
y_row = 35
x_ent = 100
w_ent = 12

fr_cam = tkc.tkframe(tkw, window=(10, 10, 230, 370))
ent_tcam = tkc.ParamEntry(fr_cam, (x_ent, 10+y_row*0, w_ent), 'T_cam, ms', 300)
ent_texp = tkc.ParamEntry(fr_cam, (x_ent, 10+y_row*1, w_ent), 'T_exp, ms', 5.0)
btn_cset = tkc.CmdButton(fr_cam, (x_ent, 10+y_row*2, w_ent), 'cam set')
btn_cam = tkc.CmdButton(fr_cam, (x_ent, 10+y_row*3, w_ent), 'camera', 'dark orange')
prg_level = tkc.ProgressBar(fr_cam, (x_ent, 10+y_row*4, w_ent), (90, 130), 'level')
ent_nxy = tkc.ParamEntry(fr_cam, (x_ent, 10+y_row*6, w_ent), 'nxy', '1920, 1080')
ent_roi = tkc.ParamEntry(fr_cam, (x_ent, 10+y_row*7, w_ent), 'roi', '960, 540, 10, 10')
ent_ax = tkc.ParamEntry(fr_cam, (x_ent, 10+y_row*8, w_ent), 'ax, mm', 9.5)
ent_lam0 = tkc.ParamEntry(fr_cam, (x_ent, 10+y_row*9, w_ent), 'lam0, um', 0.6328)

fr_pzt = tkc.tkframe(tkw, window=(245, 10, 230, 370))
ent_vpz = tkc.ParamEntry(fr_pzt, (x_ent, 10+y_row*0, w_ent), 'Vpz', 0)
btn_vset = tkc.CmdButton(fr_pzt, (x_ent, 10+y_row*1, w_ent), 'set Vpz')
ent_v2pi = tkc.ParamEntry(fr_pzt, (x_ent, 10+y_row*2, w_ent), 'V2pi', 5.30)
btn_calib = tkc.CmdButton(fr_pzt, (x_ent, 10+y_row*3, w_ent), 'calib V2pi')
btn_getvv = tkc.CmdButton(fr_pzt, (x_ent, 10+y_row*4, w_ent), 'get vv')
ent_v1 = tkc.ParamEntry(fr_pzt, (x_ent, 10+y_row*5, w_ent), 'V1', 20.00)
ent_nv = tkc.ParamEntry(fr_pzt, (x_ent, 10+y_row*6, w_ent), 'nV', 10)
ent_n2pi = tkc.ParamEntry(fr_pzt, (x_ent, 10+y_row*7, w_ent), 'N2pi', 2)
ent_v2 = tkc.ParamEntry(fr_pzt, (x_ent, 10+y_row*8, w_ent), 'V2', 0)
btn_hh = tkc.CmdButton(fr_pzt, (x_ent, 10+y_row*9, w_ent), 'acq HH', 'dark orange')

fr_qscan = tkc.tkframe(tkw, window=(480, 10, 230, 370))
ent_qddr = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*0, w_ent), 'Qddr', 237.600)
btn_qset = tkc.CmdButton(fr_qscan, (x_ent, 10+y_row*1, w_ent), 'set Q')
ent_psi = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*2, w_ent), 'psi', 237.600)
ent_q0 = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*3, w_ent), 'Q0', 237.600)
ent_q1 = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*4, w_ent), 'Q1', 237.600)
btn_qns = tkc.CmdButton(fr_qscan, (x_ent, 10+y_row*5, w_ent), 'get Qns')
ent_lam12 = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*6, w_ent), 'lam_12, um', 237.600)
ent_lam1nh = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*7, w_ent), 'lam_1nh, um', 237.600)
ent_nh = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*8, w_ent), 'Nh', 237.600)
ent_gamma = tkc.ParamEntry(fr_qscan, (x_ent, 10+y_row*9, w_ent), 'gamma', 237.600)

fr_proc = tkc.tkframe(tkw, window=(715, 10, 230, 370))
btn_madh = tkc.CmdButton(fr_proc, (x_ent, 10+y_row*0, w_ent), 'MADH')
prg_qscan = tkc.ProgressBar(fr_proc, (x_ent, 10+y_row*1, w_ent), (20, 200), 'Qscan')
prg_vscan = tkc.ProgressBar(fr_proc, (x_ent, 10+y_row*3, w_ent), (20, 200), 'Vscan')
btn_txt = tkc.CmdButton(fr_proc, (x_ent, 10+y_row*5, w_ent), 'txt path')
ent_txtpath = tkc.ParamEntry(fr_proc, (40, 10+y_row*6, 20), 'txt', '')
ent_phpath = tkc.ParamEntry(fr_proc, (40, 10+y_row*7, 20), 'phs', '')
btn_laser = tkc.CmdButton(fr_proc, (x_ent, 10+y_row*8, w_ent), 'laser', 'gray')
btn_adios = tkc.CmdButton(fr_proc, (x_ent, 10+y_row*9, w_ent), 'adios', 'indian red')


def main_loop():

    if btn_cam.is_on():
        cc = show_cam()
       
    tkw.after(tloop, main_loop)


def set_camera():
    t_cam = ent_tcam.get_val()
    t_exp = ent_texp.get_val(typ=float)
    uno.set_Tcam(t_cam)
    qcam.setup(t_exp=t_exp)
    

def show_cam():
    qcam.acquire_cc()
    capA = f'qcam.cc: iframe = {qcam.iframe}'
    cc = qcam.cc * 1.0
    pf.plotAAB(cc, figname='qcam.cc', capA=capA, ulimit=(0, 2**16-1), pause=0.1)
    level = int(100 * np.sum(cc) / (np.prod(np.shape(cc)) * (65536.)))
    prg_level.setval(level)


def set_vpz():
    pass


def calib_v2pi():
    pass


def get_vv():
    pass


def acq_hh(iq=1):
    pass


def set_ddr_q():
    pass


def get_qns():
    pass


def madh():
    pass


def set_txtpath():
    pass


def make_notes():
    pass


def laser():
    if not btn_laser.is_on():
        btn_laser.on()
        uno.set_LED(3)
    else:
        btn_laser.off()
        uno.set_LED(0)


def adios():
    qcam.dispose()
    tkw.destroy()
    print(f'> adios amigos ...')
    quit()


btn_cset.command(set_camera)
btn_cam.command(btn_cam.switch)
btn_vset.command(set_vpz)
btn_calib.command(calib_v2pi)
btn_getvv.command(get_vv)
btn_hh.command(acq_hh)
btn_qset.command(set_ddr_q)
btn_qns.command(get_qns)
btn_madh.command(madh)
btn_txt.command(set_txtpath)
btn_laser.command(laser)
btn_adios.command(adios)

set_camera()
set_vpz()
get_vv()
set_ddr_q()
get_qns()

tloop = 10
tkw.after(tloop, main_loop)
tkw.mainloop()
