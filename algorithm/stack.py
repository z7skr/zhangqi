# 单调栈
nums = [5, 2, 6, 8, 7, 4, 1, 3]
print(nums)


# ! 方法1: 出栈的时候处理, 不过是乱序
stack = []
for num in nums:
    # top < num, num 在 top 后面, top 的下一个更大值是 num
    while stack and num > stack[-1]:
        top = stack.pop()
        print(f"{top} 的下一个更大值是 {num}")
    stack.append(num)

stack = []
for num in reversed(nums):
    # top < num, num 在 top 前面, top 的上一个更大值是 num
    while stack and num > stack[-1]:
        top = stack.pop()
        print(f"{top} 的上一个更大值是 {num}")
    stack.append(num)

# ! 方法2: 出完栈了再处理, 顺序能对上
stack, arrs = [], []
for num in nums:
    # top < num就出栈
    while stack and num > stack[-1]:
        stack.pop()
    # top > num, top 在 num 前面, num 的上一个更大值是 top
    arrs.append(stack[-1] if stack else 0)
    stack.append(num)
print("上一个更大值数组\n", arrs, sep="")

stack, arrs = [], []
for num in reversed(nums):
    # top < num就出栈
    while stack and num > stack[-1]:
        stack.pop()
    # top > num, top 在 num 后面, num 的下一个更大值是 top
    arrs.append(stack[-1] if stack else 0)
    stack.append(num)
arrs = arrs[::-1]
print("下一个更大值数组\n", arrs, sep="")

# ! 方法1stack中保存索引, 也能得到顺序数组
stack, arrs = [], [0] * len(nums)
for i, num in enumerate(nums):
    while stack and num > nums[stack[-1]]:
        top = stack.pop()
        arrs[top] = num
    stack.append(i)  # 保存索引
print("下一个更大值数组\n", arrs, sep="")


