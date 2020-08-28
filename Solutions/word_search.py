#!/usr/bin/python3

def word_search_horitzontal(row, j, matrix, word):
    num = 0
    word_iter = 0

    for it in range(j, len(matrix[0]), 1):
        if word_iter < len(word):
            if matrix[row][it] != word[word_iter]:
                return num
            else:
                num += 1
        else:
            pass
        word_iter += 1
    return num


def word_search_vertical(i, column, matrix, word):
    num = 0
    word_iter = 0

    for vector_iterator in range(i, len(matrix), 1):
        if word_iter < len(word):
            if matrix[vector_iterator][column] != word[word_iter]:
                return num
            else:
                num += 1
        else:
            return num  # all correct but still in matrix

        word_iter += 1
    return num


def word_search_diagonal(i, j, matrix, word):
    num = 0
    word_iter = 0
    while i < len(matrix) and j < len(matrix[0]):

        if word_iter < len(word):
            if matrix[i][j] != word[word_iter]:
                return num
            else:
                num += 1
        else:
            return num

        word_iter += 1
        i += 1
        j += 1

    return num


def word_search_util(i, j, matrix, word):
    vertical = word_search_vertical(i, j, matrix, word)
    horitzontal = word_search_horitzontal(i, j, matrix, word)
    diagonal = word_search_diagonal(i, j, matrix, word)
    return max(vertical, horitzontal, diagonal)


def word_search(matrix, word):
    # Fill this in.

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == word[0] and word_search_util(i, j, matrix, word) == len(word):
                return True

    return False


if __name__ == '__main__':
    matrix = [
        ['F', 'A', 'C', 'I', 'T'],
        ['O', 'B', 'Q', 'P', 'T'],
        ['A', 'N', 'O', 'B', 'T'],
        ['M', 'A', 'S', 'S', 'T']]

    print(word_search(matrix, "FOAM"))
