#!/bin/env python2
# -*- coding: utf-8 -*-

quantities =  ['vx', 'vy', 'vz', 'sxx', 'sxy', 'sxz', 'syy', 'syz', 'szz']

qs = {
    'XP': ['vx', 'sxx', 'syy'],
    'XS': ['vy', 'sxy', 'sxz'],
    'YP': ['vy', 'sxx', 'syy'],
    'YS': ['vx', 'sxy', 'syz'],
    'ZP': ['vz', 'sxx', 'syy'],
    'ZS': ['vy', 'sxz', 'syz']
}

titles = {
    'vx': 'v_x',
    'vy': 'v_y',
    'vz': 'v_z',
    'sxx': '\\\\sigma_{xx}',
    'sxy': '\\\\sigma_{xy}',
    'sxz': '\\\\sigma_{xz}',
    'syy': '\\\\sigma_{yy}',
    'syz': '\\\\sigma_{yz}',
    'szz': '\\\\sigma_{zz}'
}

for d in ['X', 'Y', 'Z']:
    for t in [('P', 'продольной'), ('S', 'поперечной')]:
        print('\\begin{figure}[ht]')
        for step in range(6):
            for q in qs[d+t[0]]:
                print('\\begin{minipage}[h]{0.30\\linewidth}')
                print('\\centering')
                print('\\tiny')
                print('\\begin{gnuplot}')
                print('set datafile separator " "')
                print('set terminal epslatex color size 6cm, 3cm 8')
                print('set grid ytics xtics')
                print('set grid')
                print('set key left top')
                print(('plot "csv/AnisotropicMaterial%(type)sWavePropagationAlongO%(dir)s/step%(step)d.csv" using 1:%(q)d with lines lw 2 title "$%(title)s$",' +
                      '     "csv/AnisotropicMaterial%(type)sWavePropagationAlongO%(dir)s/step%(step)d.csv" using 1:%(qa)d with lines lw 2 title "$\\\\hat %(title)s$"') % {
                        'step': step,
                        'type': t[0],
                        'dir': d,
                        'q': (quantities.index(q)+1)*2+1,
                        'qa': (quantities.index(q)+1)*2,
                        'title': titles[q]
                      })
                print('\\end{gnuplot}')
                print('\\end{minipage}')
            print('\\\\')
        print('\\caption{Эволюция %s волны вдоль оси %s}' % (t[1], d))
        print(('\\label{рис:анизотропные-волны-%s-%s}' % (t[0], d)).lower())
        print('\\end{figure}')