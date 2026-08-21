with open('Index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# line 8979 is <script>, line 8980 is code, line 9278 is </script> (0-indexed: 8979:9277)
script2 = ''.join(lines[8979:9277])
with open('test_script2.js', 'w', encoding='utf-8') as f:
    f.write(script2)

# line 9279 is <script>, line 9280 is code, line 9384 is </script> (0-indexed: 9279:9383)
script3 = ''.join(lines[9279:9383])
with open('test_script3.js', 'w', encoding='utf-8') as f:
    f.write(script3)

# line 9385 is <script>, line 9386 is code, line 10227 is </script> (0-indexed: 9385:10226)
script4 = ''.join(lines[9385:10226])
with open('test_script4.js', 'w', encoding='utf-8') as f:
    f.write(script4)

print("Wrote scripts 2, 3, 4 properly")
