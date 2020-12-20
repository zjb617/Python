import os
os.mkdir('poems')
os.listdir('poems')
os.mkdir('poems/mcintyre')
os.listdir('poems')
fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write('''Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')
fout.close()
os.listdir('poems/mcintyre')