class Solution:
    def simplifyPath(self, path: str) -> str:
        path_components = path.split('/')
        starting_path = []
        for path_component in path_components:
            if not path_component:  # '//'
                continue
            if path_component == '.':
                continue
            if path_component == '..':
                starting_path = starting_path[:-1]
                continue
            starting_path.append(path_component)
        return '/' + '/'.join(starting_path)
