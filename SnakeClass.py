from enum import Enum
from random import *

# 方向枚举
class Direction(Enum):
	RIGHT = 0
	UP = 1
	LEFT = 2
	DOWN = 3

# 食物类
class Food:
	def __init__(self):
		self._posCollect = []
		for i in range(20):
			for j in range(20):
				self._posCollect.append((i, j))
		self._pos = (0, 0)

	# 根据蛇的身体坐标生成食物，避免生成在蛇的身上
	def Generate(self, snakeBody: list[tuple[int, int]]):
		posCollectTemp = self._posCollect.copy()
		for i in range(len(snakeBody)):
			for j in range(len(posCollectTemp)):
				if snakeBody[i] == posCollectTemp[j]:
					posCollectTemp.remove(posCollectTemp[j])
					break

		posIndex = randint(0, len(posCollectTemp))
		self._pos = posCollectTemp[posIndex]


	# 获取食物的坐标
	def GetPos(self) -> tuple[int, int]:
		return self._pos

# 蛇的类
class Snake:
	def __init__(self):
		self._body = [(5, 19), (4, 19), (3, 19)]
		self._direction = Direction.RIGHT
		self._tail = (3, 19)

	# 移动，从尾部开始，依次移动到前一个节点的当前坐标，头按照方向移动到新的坐标，保留移动之前的尾部坐标数据
	def Move(self):
		if self._direction == Direction.RIGHT:
			nextHead = (self._body[0][0] + 1, self._body[0][1] + 0)
		elif self._direction == Direction.UP:
				nextHead = (self._body[0][0] + 0, self._body[0][1] - 1)
		elif self._direction == Direction.LEFT:
				nextHead = (self._body[0][0] - 1, self._body[0][1] + 0)
		elif self._direction == Direction.DOWN:
				nextHead = (self._body[0][0] + 0, self._body[0][1] + 1)

		self._tail = self._body[len(self._body) - 1]

		for i in range(len(self._body) - 1, 0, -1):
			self._body[i] = self._body[i - 1]

		self._body[0] = nextHead

	# 设置方向，如果新的方向是之前的反向，则无法修改方向
	def SetDirection(self, direction : Direction):
		if direction == Direction.LEFT and self._direction == Direction.RIGHT:
			return
		if direction == Direction.RIGHT and self._direction == Direction.LEFT:
			return
		if direction == Direction.UP and self._direction == Direction.DOWN:
			return
		if direction == Direction.DOWN and self._direction == Direction.UP:
			return
		self._direction = direction

	# 吃到食物后边长一节，将移动之前的尾部获取出来
	def Grow(self):
		self._body.append(self._tail)

	# 获取蛇身体的坐标
	def GetBody(self) -> list[tuple[int, int]]:
		return self._body

SnakeInstance = Snake()
FoodInstance = Food()
