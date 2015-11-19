#!/bin/env python2
# -*- coding: utf-8 -*-

for a in ['x', 'z']:
    for d in ['x', 'y', 'z']:
        print('\\begin{figure}[ht]')
        for c in ['drpr', 'hashin', 'puck', 'tsaiwu', 'tsaihill']:
            for t in ['-', '+']:
                print('\\begin{minipage}[h]{0.50\\linewidth}')
                print('\\centering')
                print('\\includegraphics[width=0.92\\textwidth]{png/destruction/%(armored)s-%(cri)s-%(dir)s.png}' % {
                    'armored': a,
                    'cri': c,
                    'dir': d+t
                })
                print('\\end{minipage}')
            print('\\\\')
        print(('\\caption{Область разрушения (армирование вдоль %(armored)s), вид против направления оси %(dir)s (слева)' +
               ' и по направлению оси %(dir)s (справа). Критерии, сверху вниз: Друкер-Прагер, Хашин, Пак, Цай-Хилл, Цай-Ву}') % {
                'armored': a.upper(),
                'dir': d.upper()
        })
        print('\\label{рис:столкновение-с-%s-монослоем-%s}' % (a, d))
        print('\\end{figure}')
