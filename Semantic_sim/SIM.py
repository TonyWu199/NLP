import math

class Semantic_sim():
    def __init__(self,sentence_1,sentence_2):
        self.sentence_1 = sentence_1
        self.sentence_2 = sentence_2
        self.cilin = open("D:\\PycharmProjects\\Semantic_sim\\Semantic_sim\\Cilin.txt","r").readlines()
        self.sim = 0
        self.a = float(0.65)
        self.b = float(0.8)
        self.c = float(0.9)
        self.d = float(0.96)
        self.e = float(0.5)
        self.f = float(0.1)

    def get_sim(self):
        # 获取词语对应的编号
        code_list = []
        code_list_1 = []
        code_list_2 = []

        if self.sentence_1 == self.sentence_2:
            self.sim = 1
            return self.sim
        else:
            for i in self.cilin:
                # 这里有一个细节处理.split(" ")不然所有包含sentence_1字符的行都会被搜索
                # strip()函数去除两遍的空格以及"\n"
                if self.sentence_1 in i.strip().split(" "):
                    code_list_1.append(i[:8])
                if self.sentence_2 in i.strip().split(" "):
                    code_list_2.append(i[:8])
            if code_list_1 == [] or code_list_2 == []:
                if code_list_1 == []:
                    if code_list_2 == []:
                        return "-----------------------------------------\n" \
                                "The first input is not in the dictionary\n"\
                                "The second input is not in the dictionary\n" \
                                "-----------------------------------------"
                    else:
                        return "----------------------------------------\n" \
                                "The first input is not in the dictionary\n" \
                                "----------------------------------------"
                else:
                    return "----------------------------------------\n" \
                           "The second input is not in the dictionary\n" \
                           "----------------------------------------"
            code_list.append(code_list_1)
            code_list.append(code_list_2)

            #排列组合编码
            i = 0
            compare_list = []  #保存所有待比较的编码
            for code_1 in code_list[i]:
                for code_2 in code_list[1-i]:
                    temp_list = []  # 临时保存两个待比较的编码
                    temp_list.append(code_1)
                    temp_list.append(code_2)
                    compare_list.append(temp_list)
            #print(compare_list)

            #比较编码
            sim_list = []
            for item in compare_list:
                temp_1 = item[0]
                temp_2 = item[1]
                #print(temp_1,temp_2)

                if temp_1[0] != temp_2[0]:    #不在一棵树上
                    self.sim = self.f

                elif temp_1[1] != temp_2[1]:  #在第二层分支
                    str = temp_1[0]
                    n = self.get_node_num(str)
                    k = abs(ord(temp_1[1]) - ord(temp_2[1]))
                    #print(n,k)
                    self.sim = self.a * math.cos(n * math.pi/180) * ((n - k + 1) / n)

                elif temp_1[2:4] != temp_2[2:4]: #第三层分支
                    str = temp_1[0:2]
                    n = self.get_node_num(str)
                    k = abs(int(temp_1[2:4]) - int(temp_2[2:4]))
                    #print(n,k)
                    self.sim = self.b * math.cos(n * math.pi/180 ) * ((n - k + 1) / n)

                elif temp_1[4] != temp_2[4]:  #第四层分支
                    str = temp_1[0:4]
                    n = self.get_node_num(str)
                    k = abs(ord(temp_1[4]) - ord(temp_2[4]))
                    #print(n, k)
                    self.sim = self.c * math.cos(n * math.pi/180) * ((n - k + 1) / n)

                elif temp_1[5:7] != temp_2[5:7]:  #第五层分支
                    str = temp_1[0:5]
                    n = self.get_node_num(str)
                    k = abs(int(temp_1[5:7]) - int(temp_2[5:7]))
                    #print(n, k)
                    self.sim = self.d * math.cos(n * math.pi/180) * ((n - k + 1) / n)

                else:  #编码相同
                    #编码末尾为"#"
                    if temp_1[7] == "#":
                        self.sim = self.e
                    #编码末尾为"="
                    elif temp_1[7] == "=":
                        self.sim = 1
                    #编码末尾为"@",不考虑

                sim_list.append(abs(self.sim))

            #取出所有语义相似度值最大的
            sim_list = sorted(sim_list,reverse=True)
            return sim_list[0]

    def get_node_num(self,str):
        node_set = set()
        for line in self.cilin:
            if str == line[0:len(str)]:
                if len(str) == 1:
                    node_set.add(line[0 : len(str) + 1])
                elif len(str) == 2:
                    node_set.add(line[0 : len(str) + 2])
                elif len(str) == 4:
                    node_set.add(line[0 : len(str) + 1])
                else:
                    node_set.add(line[0 : len(str) + 2])
        #print(sorted(list(node_set)))
        return len(list(node_set))

if __name__ == "__main__":
    sentence_1 = "公主"
    sentence_2 = "王子"
    Sim = Semantic_sim(sentence_1, sentence_2)
    print(Sim.get_sim())