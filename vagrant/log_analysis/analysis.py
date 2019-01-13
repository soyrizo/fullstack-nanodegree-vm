#!/usr/bin/env python3
#
# Spencer Stenger
# Log Analysis Assignment
#
# A log analysis tool for reporting.

from logdb import popular_three_articles, popular_authors, log_errors

POPULAR_ARTICLES = '''
What are the most popular three articles of all time?\
'''
POPULAR_AUTHORS = '''
Who are the most popular article authors of all time?\
'''
LOG_ERRORS = '''
On which days did more than 1% of requests lead to errors?\
'''

VIEWS = '''● %s — %s views\n'''
LOG_ERROR = '''● %s — %s%% errors\n'''


def answer_one():
    '''Answer to question one, most popular three articles of all time.'''
    print(POPULAR_ARTICLES)
    answer_1 = "".join(VIEWS % (title, num) for title, num in popular_three_articles())
    print(answer_1)


def answer_two():
    '''Answer to question two, most popular authors of all time.'''
    print(POPULAR_AUTHORS)
    answer_2 = "".join(VIEWS % (author, num) for author, num in popular_authors())
    print(answer_2)


def answer_three():
    '''Answer to question three, which day had > 1% of request errors.'''
    print(LOG_ERRORS)
    answer_3 = "".join(LOG_ERROR % (date, errors) for date, errors in log_errors())
    print(answer_3)


def main():
    answer_one()
    answer_two()
    answer_three()


if __name__ == '__main__':
    main()
