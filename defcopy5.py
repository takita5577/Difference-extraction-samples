# -*- coding:utf-8 -*-
"""
差分抽出プログラム　コーディングサンプル５
Difference extraction program coding sample 5

データベースを使う(SQLite on memory)
Use database (SQLite on memory)

Test data:
src_lst1.txt: 10,000 records(lines)
dst_lst1.txt: 20,000 records(lines)
"""
import time
import sqlite3

comp_count = 0
src_only = 0
match_cnt = 0
end_t = 0.0

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute('CREATE TABLE src(no)')
cur.execute('CREATE TABLE dst(no)')

s_ins_str = 'INSERT INTO src (no) VALUES(?)'
d_ins_str = 'INSERT INTO dst (no) VALUES(?)'

start_t = time.time()

print('ソースファイルを読みます')

src_file = open('src_lst1.txt', 'rt')
s_lines = src_file.readlines()
src_line_cont = len(s_lines)
src_file.close()

for s_line in s_lines:
    s_wk = s_line.rstrip('\n')
    cur.execute(s_ins_str,  (s_wk, ))
conn.commit()

dst_file = open('dst_lst1.txt', 'rt')
d_lines = dst_file.readlines()
dst_line_cont = len(d_lines)
dst_file.close()

for d_line in d_lines:
    d_wk = d_line.rstrip('\n')
    cur.execute(d_ins_str,  (d_wk, ))
conn.commit()

cur.execute('SELECT COUNT(*) FROM src INNER JOIN dst ON src.no = dst.no')
result = cur.fetchall()
match_cnt = result[0][0]

cur.close()
conn.close()

end_t = time.time()

print('コピー元のみ存在：', src_line_cont - match_cnt)
print('コピー先のみ存在：', dst_line_cont - match_cnt)
print('両方に存在：', match_cnt)
print('比較回数：', comp_count)
print('処理時間(ms)：', float((end_t - start_t)*1000))
