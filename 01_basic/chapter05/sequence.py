# 在Python中，序列是最基本的数据结构，它是一块用于存放多个值的连续内存空间。
# 序列是一块用于存放多个值的连续内存空间，并且按一定顺序排列，每个值（称为元素）都分配一个数字，称为索引或位置。
# Python中内置了5个常用的序列结构，分别是列表、元组、集合、字典和字符串。
# 对于这些序列结构有以下几个通用的操作。其中，集合和字典不支持索引、切片、相加和相乘操作。

# 索引
# 序列中的每个元素都有一个编号，也称为索引（Indexing）。
# 这个索引是从0开始递增的，即下标为0表示第一个元素，下标为1表示第二个元素，依此类推。
# Python的索引可以是负数。
# 这个索引从右向左计数，也就是从最后的一个元素开始计数，即最后一个元素的索引值是−1，倒数第二个元素的索引值为−2，依此类推。
# 在采用负数作为索引值时，是从−1开始的，而不是从0开始的，即最后一个元素的下标为−1，这是为了防止与第一个元素重合。
verse = [1, 2, 3, 4]
print(verse[2])  # 输出第三个元素
print(verse[-1])  # 输出最后一个元素

# 切片
# 切片（slicing）操作是访问序列中元素的另一种方法，它可以访问一定范围内的元素。
# 通过切片操作可以生成一个新的序列。
# sname[start:end:step]
# sname：表示序列的名称；
# start：表示切片的开始位置（包括该位置），如果不指定，则默认为0；
# end：表示切片的截止位置（不包括该位置），如果不指定，则默认为序列的长度；
# step：表示切片的步长，如果省略，则默认为1，当省略该步长时，最后一个冒号也可以省略。
verse = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(verse[1:6])
print(verse[1:6:2])
# 如果想要复制整个序列，可以将start和end参数都省略，但是中间的冒号需要保留。
# 例如，verse[:]就表示复制整个名称为verse的序列。

# 序列相加
# 在Python中，支持两种相同类型的序列相加（adding）操作。即将两个序列进行连接，不会去除重复的元素，使用加（+）运算符实现。
verse1 = [1, 2, 3, 4]
verse2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(verse1 + verse2)

# 乘法
# 在Python中，使用数字n乘以一个序列会生成新的序列。新序列的内容为原来序列被重复n次的结果。
verse = [1, 2, 3, 4]
print(verse * 3)
# 在进行序列的乘法（Multiplying）运算时，还可以实现初始化指定长度列表的功能。
emptylist = [None] * 5
print(emptylist)

# 检查某个元素是否是序列的成员（元素）
# 在Python中，可以使用in关键字检查某个元素是否是序列的成员，即检查某个元素是否包含在该序列中。
# value in sequence
# value表示要检查的元素；
# sequence表示指定的序列。
verse = [1, 2, 3, 4]
print(5 in verse)
# 运行上面的代码，将显示True，表示在序列中存在指定的元素。
# 另外，在Python中，也可以使用not in关键字实现检查某个元素是否不包含在指定的序列中。
verse = [1, 2, 3, 4]
print(5 not in verse)

# 计算序列的长度、最大值和最小值
# 使用len()函数计算序列的长度，即返回序列包含多少个元素；
num = [7, 14, 21, 28, 35, 42, 49, 56, 63]
print("序列num的长度为", len(num))

# 使用max()函数返回序列中的最大元素；
print("序列", num, "中最大值为", max(num))

# 使用min()函数返回序列中的最小元素。
print("序列", num, "中最小值为", min(num))

# 函数	      说明
# list()	  将序列转换为列表
# str()	      将序列转换为字符串
# sum()	      计算元素和
# sorted()	  对元素进行排序
# reversed()  反向序列中的元素
# enumerate() 将序列组合为一个索引序列，多用在for循环中