def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print(f'The average is:, {result}')
