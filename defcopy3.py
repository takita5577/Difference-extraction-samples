# -*- coding:utf-8 -*-
"""
差分抽出プログラム　コーディングサンプル３
Difference extraction program coding sample 3

比較にif in 構文を使う
Use 'if in' syntax for comparison

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
src_line_cont = len(s_lines)
src_file.close()

dst_file = open('dst_lst1.txt', 'rt')
d_lines = dst_file.readlines()
dst_line_cont = len(d_lines)
dst_file.close()

wk_d_lines = []
for d_line in d_lines:
    wk_d_lines.append(d_line.rstrip('\n'))

for s_line in s_lines:
    wk_s_line = s_line.rstrip('\n')
    if wk_s_line in wk_d_lines:
        match_cnt += 1

end_t = time.time()

print('コピー元のみ存在：', src_line_cont - match_cnt)
print('コピー先のみ存在：', dst_line_cont - match_cnt)
print('両方に存在：', match_cnt)
print('比較回数：', comp_count)
print('処理時間(ms)：', float((end_t - start_t)*1000))
