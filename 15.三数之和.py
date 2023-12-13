# 双指针
def threeSum(nums: list[int]) -> list[list[int]]:
    a_list = []  # 定义一个空列表进行排序
    nums.sort()  # 对列表进行排序
    n = len(nums)  # 获取列表长度
    if n < 3:
        return []  # 如果列表长度小于三则直接返回空列表
    for i in range(n):  # 按下标遍历列表
        if nums[i] > 0:
            break  # 因为列表已经排过序，如果 i 对应值大于 0 则说明后续内容已经不满足条件
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        Z1 = i + 1  # 定义指针 z1 从 i+1开始遍历
        Z2 = n - 1  # 定义指针 z2 从 n-1 开始遍历
        while Z1 < Z2:  # 如果 z1 < z2 说明指针未交叉 开始循环
            if nums[i] + nums[Z1] + nums[Z2] == 0:  # 如果符合判定条件
                a_list.append([nums[i], nums[Z1], nums[Z2]])  # 则将结果存储到列表 a_list 中
                while Z1 < Z2 and nums[Z1] == nums[Z1 + 1]:  # 如果 指针未交叉 并且 指针临近值相等则跳过这一个值
                    Z1 += 1
                while Z1 < Z2 and nums[Z2] == nums[Z2 - 1]:  # 同上
                    Z2 -= 1
                Z1 += 1
                Z2 -= 1
            elif nums[i] + nums[Z1] + nums[Z2] > 0:  # 如果三数和大于零 则说明正数过大，Z2 左移 减小正数
                Z2 -= 1
            else:  # 如果三数和小于 0 则说明负数过大， i 值不移动，指针 Z1 右移减小负值
                Z1 += 1
    return a_list  # 返回结果
