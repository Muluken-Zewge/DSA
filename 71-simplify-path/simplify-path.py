class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splited = path.split("/")

        # only store valid directory in stack
        for part in splited:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)