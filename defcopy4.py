# -*- coding:utf-8 -*-
"""
差分抽出プログラム　コーディングサンプル４
Difference extraction program coding sample 4

集合を使う
Use a set

Test data:
src_lst1.txt: 10,000 records(lines)
dst_lst1.txt: 20,000 records(lines)
"""
import time

comp_count = 0
src_only = 0
match_cnt = 0
end_t = 0.0
start_t = time.time()

print('ソースファイルを読みます')

src_file = open('src_lst1.txt', 'rt')
s_lines = src_file.readlines()
src_file.close()
wk_s_lines = []
for s_line in s_lines:
    wk_s_lines.append(s_line.rstrip('\n'))
s_lines_set = set(wk_s_lines)
src_line_cont = len(wk_s_lines)

dst_file = open('dst_lst1.txt', 'rt')
d_lines = dst_file.readlines()
dst_file.close()
wk_d_lines = []
for d_line in d_lines:
    wk_d_lines.append(d_line.rstrip('\n'))
d_lines_set = set(wk_d_lines)
dst_line_cont = len(wk_d_lines)

w_lines_set = d_lines_set & s_lines_set
match_cnt = len(w_lines_set)

end_t = time.time()

print('コピー元のみ存在：', src_line_cont - match_cnt)
print('コピー先のみ存在：', dst_line_cont - match_cnt)
print('両方に存在：', match_cnt)
print('比較回数：', comp_count)
print('処理時間(ms)：', float((end_t - start_t)*1000))

