# -*- coding:utf-8 -*-
"""

"""
# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import time, pathlib, datetime, glob, shutil, sys

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("JPGファイル", "*.JPG")]

copy_root_dir = 'E:/その他の写真/'
copy_root_fil = '/**/*.JPG'

files = tkinter.filedialog.askopenfilenames(filetypes = fTyp, title='コピー元のファイル（複数）を選択してくだい。')

#キャンセルが押された
if 0 == len(files):
    print('キャンセルしました')
    sys.exit()

start_t = time.time()

#コピー元pathの保存
f_org_path = os.path.dirname(files[0])

# 選択されたファイルを集合として登録
wk_src_f = []
wk_src_yyyy = []
for f_name in files:
    dt = datetime.datetime.fromtimestamp(os.path.getmtime(f_name))
    f_b_name = os.path.basename(f_name)
    yyyy_str = dt.strftime('%Y')
    wk_src_yyyy.append(yyyy_str)
    mm_str = dt.strftime('%m')
    wk_src_f_n = yyyy_str + '/' + mm_str + '01/' + f_b_name
    wk_src_f.append(wk_src_f_n)
src_set = set(wk_src_f)
yyyy_set = set(wk_src_yyyy)

# 検索されたファイルを集合として登録
wk_dst_f = []
for d_yyyy in yyyy_set:
    copy_dst_path = copy_root_dir + d_yyyy + copy_root_fil
    dst_files = glob.glob(copy_dst_path, recursive=True)
    for dst_file in dst_files:
        wk_dst_file = dst_file.replace('\\', '/')
        path = wk_dst_file.split('/')
        spt_p = wk_dst_file.split(copy_root_dir)
        wk_dst_f.append(spt_p[1])
dst_set = set(wk_dst_f)

w_set = src_set - dst_set

# 差分のファイルをコピー
for w in w_set:
    w_b_name = os.path.basename(w)
    copy_dst = copy_root_dir + w
    copy_src = f_org_path + '/' + w_b_name
    c_p = os.path.dirname(copy_dst)
    if not os.path.exists(c_p):
        os.mkdir(c_p)
    shutil.copy2(copy_src, copy_dst)

end_t = time.time()

msgstr = 'コピーファイル数：{0:d}\n処理時間(ms)：{1:f}' .format( len(w_set), float((end_t - start_t)*1000))
tkinter.messagebox.showinfo('確認', msgstr)
