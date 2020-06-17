from collections import deque


# trap1: 动态规划
# trap2: 栈
# trap3: 双指针

def trap1(height: [int]) -> int:
    """
    解决题目的思路: 算出每根柱子上能放多少水
    1. 对于每根柱子，找到左边比他高的最高的柱子:left_max_height 右边比他高的最高的柱子:right_max_height
    2. 每根柱子能放的水就是 min(left_max_height, right_max_height) - height
    3. 动态规划法：
        从左到右遍历一遍数组，更新每根柱子左边最高的高度
        再从右往左遍历一遍数组，更新每根柱子右边最高的高度
        同时遍历数组，得到结果

    4. 单调栈：栈底大栈顶小
        由单调栈易知低洼处左边第一个大于它的位置和右边第一个大于它的位置
        计算此低洼处积水的场合宽，直至栈中都是单调递减的元素，或者栈为空

    5. 双指针法：
        因为每个柱子能存水取决于左边的最高柱子和右边的最高柱子，所以左指针指向数组开头，右指针指向数组结尾，直到两指针相遇
        若左指针指向元素高度小，左指针递增，每次更新左边最大高度并计算出遍历的每一根柱子的储水量，直到左边最大高度大于右边或两指针相遇
        否则，右指针递减，每次更新右边最大高度并计算出遍历的每一根柱子的储水量，直到右边最大高度大于左边或两指针相遇

    :param height:
    :return:
    """
    rain_water = 0
    left_max = [0] * len(height)
    right_max = [0] * len(height)

    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    for i in range(len(height)):
        rain_water = rain_water + min(left_max[i], right_max[i]) - height[i]

    return rain_water


def trap2(height: [int]) -> int:
    """
    单调栈里面存数组下标即可。
    提一个细节：
        当当前元素找到自己在递减栈中的位置时，直接入栈即可，不考虑是否与栈顶相等。
        假设栈中元素(这里假设放的是高度): stack=[2,1,1] 此时3要入栈，stack[-1]出栈时会不会被计算呢？
        如果被计算，就与stack[-2]重复计算了，答案时不会被计算，因为stack[-1]出栈后当前栈顶元素与3组成的矩形面积为0

    :param height:
    :return:
    """
    rain_water = 0
    stack = deque()
    i = 0
    while i < len(height):
        if not stack:
            stack.append(i)
        elif height[i] > height[stack[-1]]:
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                rain_water = rain_water + (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[top])
            # 将比较的元素放入栈中
            stack.append(i)
        else:
            stack.append(i)

        i = i + 1

    return rain_water


def trap3(height: [int]) -> int:
    """
    计算每根柱子能存多少水

    :param height:
    :return:
    """
    rain_water = 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            rain_water = rain_water + left_max - height[left]
            left = left + 1
        else:
            right_max = max(right_max, height[right])
            rain_water = rain_water + right_max - height[right]
            right = right - 1

    return rain_water


# 算法1验证
print(trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap1([5, 2, 1, 2, 1, 5]))

# 算法2验证
print(trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap2([5, 2, 1, 2, 1, 5]))

# 算法3验证
print(trap3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap3([5, 2, 1, 2, 1, 5]))
