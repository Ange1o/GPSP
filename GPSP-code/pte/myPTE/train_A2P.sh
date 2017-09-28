#!/bin/sh

./reconstruct -train Author2PaperNetwork.txt -output Author2PaperNetwork_dense.txt -depth 2 -k-max 1000
./line -train Author2PaperNetwork_dense.txt -output Author2PaperNetwork_2nd_wo_norm.txt -size 128 -order 2 -negative 5 -samples 10000 -threads 40
