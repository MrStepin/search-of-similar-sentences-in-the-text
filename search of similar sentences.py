import os
import scipy
from scipy import spatial
import re
from collections import Counter
import numpy as np

def separate_data():
	with open("C:\\Users\\Stas\\Desktop\\P\\data.txt") as data:
		sentences_list = data.readlines()
	sentences_list = [re.split('[^a-z]', sentence.lower()) for sentence in sentences_list]
	return sentences_list

def create_matrix(qty_of_sentences, qty_of_uniq_words, clear_sentences_list, data_dict):
	matrix = np.zeros((qty_of_sentences, qty_of_uniq_words))
	i = 0
	for sent in clear_sentences_list:
		for word in sent:
			matrix[i, data_dict[word]] +=1
		i+=1	
	return matrix

def calculate_cosine_distance(matrix):
	distance = []
	for line in matrix:
		distance.append(scipy.spatial.distance.cosine(matrix[0], line))
	sorted_distance = sorted(distance)
	return print(distance.index(sorted_distance[1]), distance.index(sorted_distance[2]))

if __name__ == '__main__':

	sentences_list = separate_data()

	word_list = []
	clear_sentences_list = []
	for sentence in sentences_list:
		word_list_of_sentence = []
		for word in sentence:
			if word !='':
				word_list.append(word)
				word_list_of_sentence.append(word)
		clear_sentences_list.append(word_list_of_sentence)		

	uniq_word_list = []
	[uniq_word_list.append(word) for word in word_list if word not in uniq_word_list]
	qty_of_uniq_words = len(uniq_word_list)
	qty_of_sentences = len(sentences_list)

	temp_list = enumerate(set([word for sent in clear_sentences_list for word in sent]))
	data_dict = {word:i for i, word in temp_list}

	matrix = create_matrix(qty_of_sentences, qty_of_uniq_words, clear_sentences_list, data_dict)
	calculate_cosine_distance(matrix)