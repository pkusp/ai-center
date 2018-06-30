# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@pkusp.com

@version: 1.0
@file: number_tagger.py
@time: 2018/5/8 下午4:26

这一行开始写关于本文件的说明与解释
"""
from collections import namedtuple

import re
import regex
from knowledge_base_qa.parser.taggers.__tagger import Tagger

TagTuple = namedtuple("tag", ["start_index", "end_index", "tag_name", "data"])


digit_map = {
    "一": 1,
    "二": 2,
    "两": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "百": 100,
    "千": 1000,
    "万": 10000,
    "亿": 100000000,
    "元": 1,
    "块": 1,
    "点": 1,
    "毛": 0.1,
    "角": 0.1,
    "分": 0.01,
}


regex_list = [
    "[0-9|一二两三四五六七八九十百千万亿零元块点毛角分|\.]+(?:元|元钱|块|块钱)?(?:rmb|RMB|人民币)?"
]


class Tokens:
    def __init__(self):
        self.number = r"[-+]?\d*\.\d+|\d+"  # e.g. 12.4, -12.4, +12
        self.ch_digit = r"一二两三四五六七八九"
        self.ch_scale = r"十百千万亿"
        self.ch_delimter = r"零"
        self.yuan_level = r"元"  # delete "块点" 20180109
        self.yuan_synonym_level = r"块点"  # add “块点” 20180109
        self.jiao_level = r"毛角"
        self.fen_level = r"分"
        self.mix_digit = r"(?:{})|(?:[{}])".format(self.number, self.ch_digit)
        self.mix_scale = r"{}{}{}{}".format(
            self.ch_scale,
            self.yuan_level,
            self.jiao_level,
            self.fen_level
        )
        self.money = r"钱?(?:rmb|RMB|人民币)?"


class NumberTagger(Tagger):
    def __init__(self):
        super(NumberTagger, self).__init__(regex_list)

    def parse_extracted_string(self, extracted_string, value, substrings):

        return self.parse_ch_number(extracted_string)

    def parse_ch_number(self,extracted_string):
        unit_number = self.decode_unit_number(extracted_string)
        if unit_number:
            return unit_number
        if extracted_string.startswith("十"):
            extracted_string = "一" + extracted_string
        if re.findall(r'[亿万]', extracted_string):
            self.decode_connect_unit(extracted_string)
        if re.findall(r'[块点]',extracted_string):
            self.decode_kuai(extracted_string)
        if re.findall(r'元',extracted_string):
            self.decode_yuan(extracted_string)
        if re.findall(r'^\w*十([一二两三四五六七八九])([万亿])\w*$',extracted_string):
            self.decode_post(extracted_string)
        x = self.decode_sub_number(extracted_string)
        return x

    def decode_unit_number(self,extracted_string):
        tokens = Tokens()
        # ch_scale = "十百千万亿"
        all_in_ch_scale = True
        for char in extracted_string:
            if char not in tokens.ch_scale:
                all_in_ch_scale = False
                break
        if all_in_ch_scale:  # 仅由单位组成的数字， 如千万、十亿、千万亿
            value = 1
            for char in extracted_string:
                value = value * digit_map[char]
            return value
        return None

    def decode_connect_unit(self,extracted_string):
        tokens = Tokens()
        # case 2: second special case, recursive dealing with 亿
        # split 五亿三千万 into 五亿 + 三千万
        index = extracted_string.find("亿")
        if index != -1 and index != len(extracted_string) - 1:  # 将’亿‘拆分为左右两部分，递归调用pars函数
            return self.parse_ch_number(extracted_string[:index + 1]) + self.parse_ch_number(
                extracted_string[index + 1:])

        # case 3: second+ special case, recursive dealing with “万”
        index = extracted_string.find("万")
        if index != -1 and index != len(extracted_string) - 1:  # 将’亿‘拆分为左右两部分，递归调用pars函数
            return self.parse_ch_number(extracted_string[:index + 1]) + self.parse_ch_number(
                extracted_string[index + 1:])

    def decode_yuan(self,extracted_string):
        tokens = Tokens()
        # case 4:(delete元) third special case, dealing with decimal part “元，块”
        match = regex.search("[{}]".format(tokens.yuan_level), extracted_string)  # 拆分，以元、块为分割点
        if not match:  # match 返回format内位置
            index = -1
        else:
            index = match.span()[0]  # match.span()[]分割两部分
        if index != -1 and index != len(extracted_string) - 1:  # 元、块非终点且存在（！=-1），将‘元’拆分为两部分，递归调用pars函数
            # igore index
            # 十块八 => 十块 + 0.1 * 八
            return self.parse_ch_number(extracted_string[:index]) + self.parse_ch_number(
                extracted_string[index + 1:])  # * 0.1

    def decode_kuai(self,extracted_string):
        tokens = Tokens()
        # case 5:(add 点，块) third+ special case, dealing with “点”
        match = regex.search("[{}]".format(tokens.yuan_synonym_level), extracted_string)  # 拆分，以点为分割点
        if not match:  # match 返回format内位置
            index = -1
        else:
            index = match.span()[0]  # match.span()[]分割两部分
        if index != -1:
            print("kuai：",extracted_string)
            print("index::",index)
            if index != len(extracted_string) - 1:  # 点非终点且存在（！=-1），将‘点’拆分为两部分，递归调用pars函数
                # igore index
                # 十块八 => 十块 + 0.1 * 八
                return self.parse_ch_number(extracted_string[:index]) + self.parse_ch_number(
                    extracted_string[index + 1:]) * 0.1
            else:
                print('else')
                print(extracted_string[:index])
                return self.parse_ch_number(extracted_string[:index])


    def decode_sub_number(self,extracted_string):
        # basically parse the pattern of ([ch_digit][ch_scale]ch_delimter?)*ch_scale -> 五千三百万
        #                             or ([ch_digit][ch_scale]ch_delimter?)*ch_digit -> 五千三
        #                             or [ch_digit][ch_scale]) -> 五千三百
        # print("sub string:",extracted_string)


       # self.number = r"[-+]?\d*\.\d+|\d+"  # e.g. 12.4, -12.4, +12
       #  self.ch_digit = r"一二两三四五六七八九"
       #  self.ch_scale = r"十百千万亿"
       #  self.ch_delimter = r"零"
       #  self.yuan_level = r"元"  # delete "块点" 20180109
       #  self.yuan_synonym_level = r"块点"  # add “块点” 20180109
       #  self.jiao_level = r"毛角"
       #  self.fen_level = r"分"
       #  self.mix_digit = r"(?:{})|(?:[{}])".format(self.number, self.ch_digit)
       #  self.mix_scale = r"{}{}{}{}".format(
       #      self.ch_scale,
       #      self.yuan_level,
       #      self.jiao_level,
       #      self.fen_level
       #  )
       #  self.money = r"钱?(?:rmb|RMB|人民币)?"


        tokens = Tokens()
        m = regex.match(
            r"^(?:({})([{}])[{}]?)*(?:({})|([{}]))?{}$".format(
                tokens.mix_digit,  # 1
                tokens.mix_scale,  # 2
                tokens.ch_delimter,
                tokens.mix_digit,  # 3
                tokens.mix_scale,  # 4
                tokens.money,
            ),
            extracted_string,
        )
        if not m:
            print("not m")
            print(extracted_string)
            return None

        result = 0
        last_scale = None

        assert len(m.captures(1)) == len(m.captures(2))  # 顺序读出数字和单位后匹配

        for number, scale in zip(m.captures(1), m.captures(2)):  # ch_digit + ch_scale unit e.g. ("五千", ”三百“)
            try:
                n = float(number)  # try to match on 阿拉伯数字first ”12.3“ -> 12.3
            except ValueError:
                n = digit_map[number]
            result += n * digit_map[scale]
            last_scale = scale

        if not m.captures(3) and not m.captures(4):
            return result

        if m.captures(3):  # is digit
            assert len(m.captures(3)) == 1
            number = m.captures(3)[0]
            try:
                n = float(number)  # try to match on 阿拉伯数字first ”12.3“ -> 12.3
            except ValueError:
                n = digit_map[number]
            if last_scale == None:
                return result + n
            if last_scale in tokens.jiao_level:
                return result + n * 0.01
            if last_scale in tokens.yuan_level:
                return result + n * 0.1
            if "零" in extracted_string:  # YYYY零X
                return result + n
            if last_scale == "十":
                return result + n
            elif last_scale == "百":  # 三百二 二 = 20
                return result + n * 10
            elif last_scale == "千":
                return result + n * 100
            elif last_scale == "万":
                return result + n * 1000
            elif last_scale == "亿":  # 一亿五？ no idea...
                raise FailParseChInteger(
                    "fail to parse number {}".format(extracted_string))
        if m.captures(4):
            assert len(m.captures(4)) == 1
            return result * digit_map[m.captures(4)[0]]

    def decode_post(self,extracted_string):
        n = regex.match(r'^\w*十([一二两三四五六七八九])([万亿])\w*$', extracted_string)
        pos = extracted_string.find(n.captures(1)[0])
        result = digit_map[n.captures(1)[0]] * digit_map[n.captures(2)[0]] + self.parse_ch_number(
            extracted_string[:pos] + extracted_string[pos + 1:])
        return result


class FailParseChInteger(Exception):
    pass


if __name__ == '__main__':
    test_tuple = namedtuple("test_tuple", ["input", "gold"])

    def test():
        tagger = NumberTagger()
        inputs = [
            # test_tuple(input="十块八", gold=10.8),
            test_tuple(input="五毛六", gold=0.56),
            test_tuple(input="五千三百万", gold=53000000),
            test_tuple(input="两千零六", gold=2006),
            test_tuple(input="10块钱", gold=10),
            test_tuple(input="10元钱", gold=10),
            test_tuple(input="10.5元", gold=10.5),
            test_tuple(input="10元五角", gold=10.5),
            # test_tuple(input="两亿三千八百万五千六百一十八块五",gold=238005618.5),
            test_tuple(input="2.5元", gold=2.5),
            # test_tuple(input="0元", gold=0),
            # test_tuple(input="0.0元", gold=0),
            # test_tuple(input="零元", gold=0),
            test_tuple(input="元", gold=0),

        ]
        for (input_, gold) in inputs:
            tags = tagger.tag_sentence(input_)
            print(input_)
            # print(tags)
            print("tag:::", tags[0].data)
            assert len(tags) == 1
            assert gold == tags[0].data
    test()