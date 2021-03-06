#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1, 1, 1, 5, 1]) => 1150 points
# score([2, 3, 4, 6, 2]) => 0 points
# score([3, 4, 5, 3, 3]) => 350 points
# score([1, 5, 1, 2, 4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

# !/usr/bin/env python


# -*- coding: utf-8 -*-

from runner.koan import *


# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1, 1, 1, 5, 1]) => 1150 points
# score([2, 3, 4, 6, 2]) => 0 points
# score([3, 4, 5, 3, 3]) => 350 points
# score([1, 5, 1, 2, 4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def is_one(item):
    return True if item == 1 else False


def is_five(item):
    return True if item == 5 else False


def apply_simple_rules(dice):
    if len(dice) == 0: return 0
    one_score = len(filter(is_one, dice)) * 100
    five_score = len(filter(is_five, dice)) * 50
    return one_score + five_score


def remove_three_occurances_of_item_in_list(item, list):
    count = 0
    new_list = []
    for x in list:
        if x == item and count < 3:
            # list.remove(item)
            #print "list:", list, "count:", count
            count += 1
        else:
            new_list.append(x)

    return new_list


def apply_triad_rules(srtd_list):
    print "applying triad rules"
    if srtd_list.count(1) > 2:
        return remove_three_occurances_of_item_in_list(1, srtd_list), 1000
    srtd_set = set(srtd_list)
    if len(srtd_set) <= (len(srtd_list) - 2):
        for item in srtd_set:
            if srtd_list.count(item) > 2:
                return remove_three_occurances_of_item_in_list(item, srtd_list), 100 * item

    return srtd_list, 0


def score(dice):
    # You need to write this method
    srtd = sorted(dice)
    if (len(dice) < 3): return apply_simple_rules(srtd)
    fltrd, scr = apply_triad_rules(srtd)
    print "filtered:", fltrd, "original:", dice, "score_so_far:", scr

    return scr + apply_simple_rules(fltrd)


class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1, 5, 5, 1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2, 3, 4, 6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1, 1, 1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2, 2, 2]))
        self.assertEqual(300, score([3, 3, 3]))
        self.assertEqual(400, score([4, 4, 4]))
        self.assertEqual(500, score([5, 5, 5]))
        self.assertEqual(600, score([6, 6, 6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2, 5, 2, 2, 3]))
        self.assertEqual(550, score([5, 5, 5, 5]))
        self.assertEqual(1150, score([1, 1, 1, 5, 1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1, 2, 2, 2]))
        self.assertEqual(350, score([1, 5, 2, 2, 2]))
