import csv
answ={'привет':'И тебе привет!','как дела?':'Лучше всех','пока':'Увидимся'}
with open('2.csv', 'w') as f:
    spamwriter = csv.writer(f, lineterminator='\n')
    for a in answ:
        b=answ[a]
        spamwriter.writerow([a]+[b])
