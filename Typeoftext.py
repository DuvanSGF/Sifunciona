# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:32:10 2018

@author: Mr Mejia
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
