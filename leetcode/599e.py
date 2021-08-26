class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        intersect = set(list1).intersection(set(list2))
        common_list = list(intersect)
        common_list_pair = [(x, list1.index(x) + list2.index(x)) for x in common_list]
        common_list_pair.sort(key=lambda x: x[1])
        lowest_score = common_list_pair[0][1]
        return [x[0] for x in common_list_pair if x[1] == lowest_score]
