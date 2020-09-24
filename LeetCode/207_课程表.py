from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        """
        Solution:
        1. 确定每种课程的入度大小
        2. 确定每个边的邻接表（后面遍历时速度更快）
        3. 将入度为0的课程确定为先修课程 start_course
        4. 当 start_course 不为空时，不断循环：
            1. 取出 start_course 中的一门课程 course
            2. 将 course 的后序课程的入度减 1
            3. 如果 course 的入度为 0，将其加入 start_course

        :param numCourses: 课程数目
        :param prerequisites: 先修关系
        :return: 是否能完成所有课程的选修关系
        """
        start_course = deque()
        indegree = [0] * numCourses
        complete_course = 0
        adjacency_list = [[] for i in range(numCourses)]
        for x in prerequisites:
            indegree[x[1]] += 1
            adjacency_list[x[0]].append(x)

        for i, degree in enumerate(indegree):
            if degree == 0:
                start_course.append(i)

        while start_course:
            course = start_course.popleft()
            complete_course += 1
            for next_course in adjacency_list[course]:
                indegree[next_course[1]] -= 1
                if indegree[next_course[1]] == 0:
                    start_course.append(next_course[1])

        if complete_course == numCourses:
            return True
        else:
            return False


print(Solution().canFinish(2, [[1, 0], [0, 1]]))
print(Solution().canFinish(2, [[0, 1]]))
