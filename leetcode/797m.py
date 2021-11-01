# (DFS)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target_node = len(graph) - 1
        paths = set()

        def recurse(current_node, current_path, next_nodes):
            if current_node == target_node:
                paths.add(tuple(current_path + [current_node]))
                return
            for next_node in next_nodes:
                recurse(next_node, current_path + [current_node], graph[next_node])

        recurse(0, [], graph[0])
        return [list(x) for x in paths]
