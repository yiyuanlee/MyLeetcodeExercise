class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        list1 = []
        list2 = []
        for i in range(len(paths)):
            list1.append(paths[i][0])
            list2.append(paths[i][1])
        for j in range(len(list2)):
            if list2[j] not in list1:
                return list2[j]