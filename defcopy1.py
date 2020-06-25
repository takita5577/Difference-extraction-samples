# -*- coding:utf-8 -*-
"""
差分抽出プログラム　コーディングサンプル１
Difference extraction program coding sample 1

素朴なコード（何の工夫もなし）
Simple code (no ingenuity)

Test data:
src_lst1.txt: 10,000 records(lines)
dst_lst1.txt: 20,000 records(lines)
"""
import time

comp_count = 0
src_only = 0
dst_line_cont = 0
match_cnt = 0
save_dst_line_cont = 0
start_t = 0.0
end_t =0.0
start_t = time.time()

src_file = open('src_lst1.txt', 'rt')

print('ソースファイルを読みます')
while True:
    s_line = src_file.readline()
    if not s_line:
        break
    wk_s_line = s_line.rstrip('\n')
    dst_file = open('dst_lst1.txt', 'rt')
    dst_line_cont = 0
    while True:
        d_line = dst_file.readline()
        wk_d_line = d_line.rstrip('\n')
        if not d_line:
            save_dst_line_cont = dst_line_cont
            src_only += 1
            break
        comp_count += 1
        if wk_s_line == wk_d_line:
            match_cnt += 1
#            print('match!', s_line, d_line)
            break
        dst_line_cont += 1
    dst_file.close()
src_file.close()

end_t = time.time()

print('コピー元のみ存在：', src_only)
print('コピー先のみ存在：', save_dst_line_cont - match_cnt)
print('両方に存在：', match_cnt)
print('比較回数：', comp_count)
print('処理時間(ms)：', float((end_t - start_t)*1000))
