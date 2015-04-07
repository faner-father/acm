#!/bin/env python
#coding:utf-8

debug = lambda :__import__('pdb').set_trace()

count = 0

def increament(inc=1):
    global count
    count += inc

#increament()
#print count

def seqSearchStr(s, sub):
    assert len(s) >= len(sub)
#    debug()
    sub_len = len(sub)
    s_len = len(s)
    def one_match(s_pos):
        global count
        count += 1
        sub_pos = start_sub_pos = 0
        start_s_pos = s_pos
        while sub_pos<sub_len:
            count += 1
            if sub[sub_pos]==s[s_pos]:
                    sub_pos += 1
                    s_pos += 1
            else:
                return False, start_s_pos+1
        else:
            return True, start_s_pos
    s_limit = s_len - sub_len + 1
    s_begin = 0
    while s_limit>0:
        succ, next_pos = one_match(s_begin)
        if succ:
            print 'count is {}'.format(count)
            return next_pos
        else:
            s_limit -= 1
            s_begin = next_pos
    print 'count is {}'.format(count)

def seqSearch(l, e):
    i = len(l)
    l.insert(0, e)
    while l[i] != e:
        i -= 1
    return i - 1

def _bin_search_move(left, right, left_or_right):
    if left_or_right:
        #left
        return (right - left) / 2 + left
    else:
        #right
        


def binSearch(l, e):
    assert len(l)>0
    if len(l) == 1:
        return 0 if l[0]==e else -1
    l = sorted(l)
    mid = len(l) / 2
    if l[mid]==e:
        return mid
    elif l[mid]>e:
        return binSearch(l[:mid-1], e)
    else:
        return binSearch(l[mid+1:], e)
