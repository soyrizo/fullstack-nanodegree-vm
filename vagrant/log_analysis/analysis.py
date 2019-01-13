#!/usr/bin/env python3
#
# A log analysis tool for reporting.

from logdb import question_1, question_2, question_3

QUESTION_1 = '''\nWhat are the most popular three articles of all time?'''
QUESTION_2 = '''\nWho are the most popular article authors of all time?'''
QUESTION_3 = '''\nOn which days did more than 1% of requests lead to errors?'''

ANSWER = '''● %s — %s views\n'''


def main():
    one()
    two()


def one():
    '''Answer to question one, most popular three articles of all time.'''
    print(QUESTION_1)
    answer_1 = "".join(ANSWER % (title, num) for title, num in question_1())
    print(answer_1)


def two():
    '''Answer to question two, most popular authors of all time.'''
    print(QUESTION_2)
    answer_2 = "".join(ANSWER % (author, num) for author, num in question_2())
    print(answer_2)


def three():
    '''Answer to question three, which day had > 1% of request errors.'''
    print(QUESTION_3)
    answer_3 = "".join(ANSWER % (author, num) for author, num in question_3())
    print(answer_3)


if __name__ == '__main__':
    main()
