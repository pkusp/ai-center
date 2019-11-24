# from knowledge_base_qa.parser.taggers.company_subsidiary.subsidiary_name_tagger import SubsidiaryNameTagger
from knowledge_base_qa.parser.parse_tag import ParseTag
from knowledge_base_qa.parser.taggers.general.time_tagger import TimeTagger
import time

from collections import namedtuple

from knowledge_base_qa.parser.dependencies.post_process_parser import PostProcessParser
from knowledge_base_qa.parser.dependencies.preprocess_merge import PreprocessMerge
from knowledge_base_qa.parser.dependencies.preprocess_merge_rules import Ruler
from knowledge_base_qa.parser.dependencies.state import State
from knowledge_base_qa.parser.parse_tag import ParseTag
from knowledge_base_qa.utils import prettyprint
from knowledge_base_qa.parser.dependencies.preprocess_merge_rules import merge_rules
from knowledge_base_qa.e2e_tests.globalvar import ProcessStringSingleton

process_string = ProcessStringSingleton.get_process_string_instance()
t_start = time.time()


def test1():

    sentences = [

        "一带一路",
        "一带一路新签合同额增速是多少",
        "一带一路新签合同额是多少",
        "去年一带一路新签合同额是多少",
        "一带一路沿线新签承包项目是多少",
        "我国对一带一路沿线国家直接投资金额是多少",
        "我国对一带一路沿线国家投资金额是多少",
        "一带一路沿线投资合作情况",


    ]
    parser_tag = ParseTag()
    preprocess_merge = PreprocessMerge()
    post_process_parser = PostProcessParser()

    post_process_tags = ["Time", "TimeRecent"]
    tag_simple = namedtuple("tag_simple", ["index", "tag_name"])

    preprocess_merge.merge_rules = Ruler.convert_to_rules_without_conflict(merge_rules)

    for sentence in sentences:
        tags_list = parser_tag.tagging(sentence)

        print(tags_list)
        for tags in tags_list:
            prettyprint.tagger.print_tagging_result(sentence, tags)
            initial_queue = [tag_simple(i, tag.tag_name) for (i, tag) in enumerate(tags) if
                             tag.tag_name not in post_process_tags]
            state = State(initial_queue)
            preprocess_merge.merge(tags, state)
            prettyprint.dependency.print_dependency_tree(tags, sentence)
            post_process_parser.parse(tags)
            prettyprint.dependency.print_dependency_tree(tags, sentence)


def run():
    test1()


# def tag_subname(sentence):
#     sb = SubsidiaryNameTagger()
#     tag_out = sb.tag_sentence(sentence)
#
#     print(tag_out)
#     print('\n\n')
#     return tag_out
def tag_time(sentence):
    tt = TimeTagger()
    tag_out = tt.tag_sentence(sentence)
    print(tag_out)


def tag_all(sentences):
    pt = ParseTag()
    for sent in sentences:
        print(sent)
        print('------------------------')
        parse_out = pt.tagging(sent)
        # print(parse_out)
        show_tag_result = []
        for tag in parse_out[0]:
            tag_pair = tag.word+' '+'['+tag.tag_name+']' + ' || tag data:' + str(tag.data)
            show_tag_result.append(tag_pair)
            print(tag_pair)
        print('\n')


if __name__ == '__main__':

    sentence_list = [

        "教育部控股了哪些上市公司",
        "教育部控股了哪些公司",
        "教育部控制了哪些医药公司",
        "哪些公司的实控人是教育部",
        "哪些公司的实际控制人是教育部",
        "哪些公司属于教育部",
        "教育部下面有哪些公司",
        "教育部下面有哪些医药公司",
    ]


    run()

    t_end = time.time()
    print('run %ss' % round(t_end - t_start, 4))

