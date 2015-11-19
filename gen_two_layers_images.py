#!/bin/env python2
# -*- coding: utf-8 -*-

for m in ['c', 'g']:
    for d in ['x', 'y', 'z']:
        print('\\begin{figure}[ht]')
        for c in ['drpr', 'hashin', 'puck', 'tsaiwu', 'tsaihill']:
            for t in ['-', '+']:
                print('\\begin{minipage}[h]{0.50\\textwidth}')
                print('\\centering')
                print('\\includegraphics[width=0.91\\textwidth]{png/destruction/2l%(mat)s-%(cri)s-%(dir)s.png}' % {
                    'mat': m,
                    'cri': c,
                    'dir': d+t
                })
                print('\\end{minipage}')
            print('\\\\')
        print(('\\caption{Область разрушения для столкновения с %(mat)s, вид против направления оси %(dir)s (слева)' +
               ' и по направлению оси %(dir)s (справа). Критерии, сверху вниз: Друкер-Прагер, Хашин, Пак, Цай-Хилл, Цай-Ву}') % {
                'mat': 'CFRP' if m == 'c' else 'GFRP',
                'dir': d.upper()
        })
        print('\\label{рис:столкновение-с-%s-%s}' % ('cfrp' if m == 'c' else 'gfrp', d))
        print('\\end{figure}')

print('\\begin{figure}[ht]')
for c in ['drpr', 'hashin', 'puck', 'tsaiwu', 'tsaihill']:
    for m in ['c', 'g']:
        print('\\begin{minipage}[h]{0.50\\textwidth}')
        print('\\centering')
        print('\\includegraphics[width=0.91\\textwidth]{png/destruction/2l%(mat)s-%(cri)s-delam.png}' % {
            'mat': m,
            'cri': c,
        })
        print('\\end{minipage}')
    print('\\\\')
print('\\caption{Область расслоения для столкновения с GFRP(слева) и с CFRP (справа).' +
      ' Критерии, сверху вниз: Друкер-Прагер, Хашин, Пак, Цай-Хилл, Цай-Ву}')
print('\\label{рис:расслоение-cfrp-gfrp}')
print('\\end{figure}')