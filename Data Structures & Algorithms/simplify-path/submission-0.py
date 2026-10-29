class Solution:
    def simplifyPath(self, path: str) -> str:
        raw_path = path
        clean_path_list = list()

        raw_path_dirs = raw_path.split('/')

        for d in raw_path_dirs:
            if not d or d == '.':
                continue

            if d == '..':
                if len(clean_path_list) > 0:
                    clean_path_list.pop()
                else:
                    continue
            else:
                clean_path_list.append(d)

        return '/' + '/'.join(clean_path_list)