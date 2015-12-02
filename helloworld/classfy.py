#!/usr/bin/env python

import subprocess

# subprocess.call(["ls", "-l", "-a"])

outp = subprocess.check_output(["python", "caffe/python/classify.py", "--print_results", "--model_def", "caffe/models/bvlc_reference_caffenet/deploy.prototxt", "--pretrained_model", "caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel", "--center_only", "--labels_file", "caffe/data/ilsvrc12/synset_words.txt", "--images_dim", "1200,808", "caffe/python/test1.jpg", "foo"])
# outp = subprocess.check_output(["python", "caffe/python/classify.py"])
# outp = subprocess.check_output(["ls", "-al"])
# python python/classify.py --print_results --model_def models/bvlc_reference_caffenet/deploy.prototxt 
# --pretrained_model models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel --center_only 
# --labels_file data/ilsvrc12/synset_words.txt --images_dim 1200,808 python/test1.jpg foo

# idx_hash = outp.index("#")
# outp = outp[idx_hash+1:]

#print "Output goes here"
print outp
