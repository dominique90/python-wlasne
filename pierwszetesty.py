#!/usr/bin/env/python

import unittest
import wroc
import random

class WrocTest(unittest.TestCase):

    def test_f1(self):
        w=wroc.f1(0)
	self.assertEqual(w,0)
    
    def test_f2(self):
	w=wroc.f1(1)
	self.assertEqual(w,1)
    
    def test_f3(self):
	w=wroc.f1(2)
	self.assertEqual(w,4)

    def test_f4(self):
	w=wroc.f1(2,1)
	self.assertEqual(w,5)

    def test_f5(self):
	w=wroc.f1(2,3)
	self.assertEqual(w,7)

    def test_f6(self):
	w=wroc.f2('ala')
	self.assertEqual(w,'a')

    def test_f7(self):
	w=wroc.f2([1,2,3])
	self.assertEqual(w,1)

    def test_f8(self):
	w=wroc.f2([])
	self.assertEqual(w,'BUUUUM')

    def test_f9(self):
	w=wroc.f3(1)
	self.assertEqual(w,'jeden')

    def test_f10(self):
	w=wroc.f3(2)
	self.assertEqual(w,'dwa')

    def test_f11(self):
	w=wroc.f3(3)
	self.assertEqual(w,'trzy')

    def test_f12(self):
	w=wroc.f3(random.choice(range(4,1000)))
	self.assertEqual(w,'other')

    def test_f13(self):
	w=wroc.f4('ala')
	self.assertEqual(w,'ala ma kota')

    def test_f14(self):
	w=wroc.f4('kot')
	self.assertEqual(w,'kot ma kota')

    def test_f15(self):
	w=wroc.f4('kot','psa')
	self.assertEqual(w,'kot ma kota i psa')

    def test_f16(self):
	w=wroc.f4('kot','mysz')
	self.assertEqual(w,'kot ma kota i mysz')

    def test_f17(self):
	w=wroc.f5(0)
	self.assertEqual(w,[])

    def test_18(self):
	w=wroc.f5(1)
	self.assertEqual(w,[0])

    def test_19(self):
	w=wroc.f5(2)
	self.assertEqual(w,[0,1])

    def test_20(self):
	w=wroc.f5(7)
	self.assertEqual(w,[0,1,2,3,4,5,6])

    def test_21(self):
	w=wroc.f5(7,2)
	self.assertEqual(w,[0,2,4,6])

    def test_22(self):
	w=wroc.f5(17,2)
	self.assertEqual(w,[0,2,4,6,8,10,12,14,16])

    def test_23(self):
	w=wroc.f5(17,5)
	self.assertEqual(w,[0,5,10,15])

    def test_24(self):
	w=wroc.f6(1,'*')
	self.assertEqual(w,'*')

    def test_25(self):
	w=wroc.f6(7,'*')
	self.assertEqual(w,'*******')

    def test_33(self):
	w=wroc.f8('kot','ala ma kota')
	self.assertEqual(w,'true')

    def test_34(self):
	w=wroc.f8('pies','ala ma kota')
	self.assertEqual(w,'false')

    def test_35(self):
	w=wroc.f9(1,2)
	self.assertEqual(w,'dodatnie')

    def test_36(self):
	w=wroc.f9(-1,-2)
	self.assertEqual(w,'ujemne')

    def test_37(self):
	w=wroc.f9(-1,0)
	self.assertEqual(w,'jest zero')

    def test_38(self):
	w=wroc.f9(1,1)
	self.assertEqual(w,'rowne')

    def test_39(self):
	w=wroc.f9(-1,1)
	self.assertEqual(w,'roznych znakow')

if __name__=='__main__':
    unittest.main()
