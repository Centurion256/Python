import random
import timeit
from binary_search_tree.linkedbst import LinkedBST
from binary_search_tree.bstnode import BSTNode

words = open('words.txt', 'r', encoding='utf-8').read().splitlines()
selected_words = random.sample(words, k=10000)
mixed_words = words[:]
random.shuffle(mixed_words)
def linear_word_search(words, selected_words):

    found = list()
    for word in words:

        if word in selected_words:

            found.append(word)

    return found


def binary_tree_search(words, selected_words):

    found = list()
    tree = LinkedBST()
    for word in words:

        tree.add(word)

    for word in selected_words:

        tree.find(word)
        found.append(word)

    return found

def bst_search(words, selected_words):


    found = list()
    tree = LinkedBST()

    def BSTConverter(lst_to_convert):

        if len(lst_to_convert) == 0:

            return None

        mid = len(lst_to_convert) // 2
        node = BSTNode(lst_to_convert[mid])
        node.left = BSTConverter(lst_to_convert[:mid])
        node.right = BSTConverter(lst_to_convert[mid+1:])
        return node

    tree._root = BSTConverter(words)
    for word in selected_words:

        tree.find(word)
        found.append(word)

    return found    

if __name__ == "__main__":
    
    t1 = timeit.Timer("linear_word_search(words, selected_words)", "from __main__ import linear_word_search, words, selected_words")
    t2 = timeit.Timer("binary_tree_search(mixed_words, selected_words)", "from __main__ import binary_tree_search, mixed_words, selected_words")
    t3 = timeit.Timer("bst_search(words, selected_words)", "from __main__ import bst_search, words, selected_words")
    print(f"Linear search execution time for 10.000 words in a regular list: {t1.timeit(1)}")
    print(f"Binary search tree execution time for 10.000 words in a random(unbalanced) bst: {t2.timeit(1)}")
    print(f"Binary search tree execution time for 10.000 words in a balanced bst: {t3.timeit(1)}")