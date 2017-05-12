#!/usr/bin/env/python

def f1(x,y=0):
    return x**2+y

def f2(s):
    if s==[]:
	return 'BUUUUM'
    else:
	return s[0]

def f3(s):
    if s==1:
	return 'jeden'
    elif s==2:
	return 'dwa'
    elif s==3:
	return 'trzy'
    else:
	return 'other'

def f4(s,y=0):
    if y!=0:
	return s+' ma kota i '+y
    else:
	return s+' ma kota'

def f5(s,y=1):
    return range(0,s,y)

def f6(s,y):
    return s*y

def f8(s,y):
    if s in y:
	return 'true'
    else:
	return 'false'

def f9(s,y):
    if s>0 and y>0 and s!=y:
	return 'dodatnie'
    elif s<0 and y<0 and s!=y:
	return 'ujemne'
    elif  s==y:
	return 'rowne'
    elif s==0 or y==0:
	return 'jest zero'
    
    elif s<0 or y<0 and s>0 or y>0:
	return 'roznych znakow'
