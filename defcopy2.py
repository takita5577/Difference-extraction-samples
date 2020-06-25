# -*- coding:utf-8 -*-
"""
差分抽出プログラム　コーディングサンプル２
Difference extraction program coding sample 2

ファイルIOを抑える（バッファリング）
Suppress file IO (buffering)

Test data:
src_lst1.txt: 10,000 records(lines)
dst_lst1.txt: 20,000 records(lines)
"""
import time

comp_count = 0
src_only = 0
match_cnt = 0
start_t = 0.0
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

for s_line in s_lines:
    wk_s_line = s_line.rstrip('\n')
    for d_line in d_lines:
        wk_d_line = d_line.rstrip('\n')
        comp_count += 1
        if wk_s_line == wk_d_line:
            match_cnt += 1
            break

end_t = time.time()

print('コピー元のみ存在：', src_line_cont - match_cnt)
print('コピー先のみ存在：', dst_line_cont - match_cnt)
print('両方に存在：', match_cnt)
print('比較回数：', comp_count)
print('処理時間(ms)：', float((end_t - start_t)*1000))
