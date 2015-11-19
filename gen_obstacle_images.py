#!/bin/env python2
# -*- coding: utf-8 -*-

def gen(name, steps, caption, m):
    itms = sorted(list(steps.items()))
    n = 0
    for t in ['straight', 'oblique']:
        for (i1, i2) in zip(itms[::2], itms[1::2]):
            print(('\\twofigs{рис:осколок-%(m)s-%(n)d}{Столкновение осколка с %(caption)s. Угол  %(a)d\\degree}' +
                  '{png/obstacle/%(name)s/%(type)s/2D-XZ-VELOCITY-ABS-%(step1)d.png}{Время %(time1).2eс}' +
                  '{png/obstacle/%(name)s/%(type)s/2D-XZ-VELOCITY-ABS-%(step2)d.png}{Время %(time2).2eс}') % {
                  'm': m,
                  'n': n,
                  'type': t,
                  'caption': caption,
                  'name': name,
                  'step1': i1[0],
                  'time1': i1[1][0 if t == 'straight' else 1],
                  'step2': i2[0],
                  'time2': i2[1][0 if t == 'straight' else 1],
                  'a': 0 if t == 'straight' else 30
            })
            n += 1