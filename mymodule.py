#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sum(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b
