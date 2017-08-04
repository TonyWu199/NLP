from nltk.parse.stanford import StanfordDependencyParser
import jieba
from Semantic_sim import SIM
import time

#这是语义分析

chi_parse = StanfordDependencyParser(
    r"D:\PycharmProjects\Shiyanshi\stanford\StanfordNLTK\stanford-parser.jar",
    r"D:\PycharmProjects\Shiyanshi\stanford\StanfordNLTK\stanford-parser-3.6.0-models.jar",
    r"D:\PycharmProjects\Shiyanshi\stanford\StanfordNLTK\classifiers\chinesePCFG.ser.gz"
)
# time_3 = time.time()
# res = list(chi_parse.parse(u'四川 已 成为 中国 西部 对外开放 中 升起 的 一 颗 明星'.split()))
# for row in res[0].triples():
#     print(row)
# time_4 = time.time()
# print(time_4 - time_3)
# sim = SIM.Semantic_sim("喜欢", "讨厌")
# print(sim.get_sim())

sentence = input()
wordlist = list(jieba.cut(sentence))
wordstr = ""
for word in wordlist:
    wordstr = wordstr + word + " "
res = list(chi_parse.parse(wordstr.split()))
for row in res[0].triples():
    print(row)