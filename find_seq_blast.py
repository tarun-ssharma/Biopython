from Bio.Blast import NCBIWWW, NCBIXML
import socket
import sys

socket.getaddrinfo('localhost',8080)

fasta_string = open('dna1.fasta').read()
result_handle = NCBIWWW.qblast("blastn","nt", fasta_string)
blast_record = NCBIXML.read(result_handle)

'''
#To get all matches with e value < a threshold
E_VALUE_THRESH = 0.1
for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
		if hsp.expect < E_VALUE_THRESH:
			print('****Alignment****')
			print('sequence:',alignment.title)
			print('length',alignment.length)
			print('e value', hsp.expect)
			print(hsp.query); print(hsp.match); print(hsp.sbjct)
'''

#Find min e
min_e = sys.float_info.max
for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
		if(hsp.expect < min_e):
			min_e = hsp.expect
			min_sequence = alignment.title


print(min_sequence)