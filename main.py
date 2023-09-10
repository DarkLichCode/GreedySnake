
from tkinter import messagebox
import pygame
import sys
import config
import SnakeClass

pygame.init()
screen = pygame.display.set_mode(config.screenSize)
pygame.display.set_caption("贪吃蛇")

def DrawSnake(SnakeBody: list[tuple[int, int]], food: tuple[int, int]):
	screen.fill((200, 200, 200))

	pygame.draw.line(screen, (0, 0, 0),
					 config.gameAreaLeftTop,
					 (config.gameAreaLeftTop[0] + config.gameAreaSide, config.gameAreaLeftTop[1]))
	pygame.draw.line(screen, (0, 0, 0),
					 config.gameAreaLeftTop,
					 (config.gameAreaLeftTop[0], config.gameAreaLeftTop[1] + config.gameAreaSide))
	pygame.draw.line(screen, (0, 0, 0),
					 (config.gameAreaLeftTop[0] + config.gameAreaSide, config.gameAreaLeftTop[1]),
					 (config.gameAreaLeftTop[0] + config.gameAreaSide, config.gameAreaLeftTop[1] + config.gameAreaSide))
	pygame.draw.line(screen, (0, 0, 0),
					 (config.gameAreaLeftTop[0], config.gameAreaLeftTop[1] + config.gameAreaSide),
					 (config.gameAreaLeftTop[0] + config.gameAreaSide, config.gameAreaLeftTop[1] + config.gameAreaSide))


	pygame.draw.rect(screen, "red", (
		config.gameAreaLeftTop[0] + SnakeBody[0][0] * config.snakeWidth,
		config.gameAreaLeftTop[1] + SnakeBody[0][1] * config.snakeWidth,
		config.snakeWidth, config.snakeWidth
	))
	for i in range(1, len(SnakeBody)):
		pygame.draw.rect(screen, "black",
						 (config.gameAreaLeftTop[0] + SnakeBody[i][0] * config.snakeWidth,
						  config.gameAreaLeftTop[1] + SnakeBody[i][1] * config.snakeWidth,
						  config.snakeWidth, config.snakeWidth)
						 )

	pygame.draw.rect(screen, "green", (
		config.gameAreaLeftTop[0] + food[0] * config.snakeWidth,
		config.gameAreaLeftTop[1] + food[1] * config.snakeWidth,
		config.snakeWidth, config.snakeWidth
	))



def StartGame():
	clock = pygame.time.Clock()
	time_counter = 0
	snakeDirection = SnakeClass.Direction.RIGHT

	SnakeBody = SnakeClass.SnakeInstance.GetBody()
	SnakeClass.FoodInstance.Generate(SnakeBody)

	score = 0

	speed = 1000

	while True:
		dt = clock.tick(60)  # 返回从上次调用该方法以来的毫秒数
		time_counter += dt

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					snakeDirection = SnakeClass.Direction.UP
				elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
					snakeDirection = SnakeClass.Direction.LEFT
				elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
					snakeDirection = SnakeClass.Direction.DOWN
				elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					snakeDirection = SnakeClass.Direction.RIGHT

		SnakeBody = SnakeClass.SnakeInstance.GetBody()
		if SnakeBody[0] == SnakeClass.FoodInstance.GetPos():
			SnakeClass.SnakeInstance.Grow()
			SnakeBody = SnakeClass.SnakeInstance.GetBody()
			SnakeClass.FoodInstance.Generate(SnakeBody)
			score += 10
			speed = speed - score
			if speed < 100:
				speed = 100

		for i in range(1, len(SnakeBody)):
			if SnakeBody[i] == SnakeBody[0]:
				messagebox.showinfo("游戏结束", "得分 " + str(score))
				pygame.quit()
				sys.exit()


		if SnakeBody[0][0] > config.gameAreaMaxPos or SnakeBody[0][0] < 0 or \
				SnakeBody[0][1] > config.gameAreaMaxPos or SnakeBody[0][1] < 0:
			messagebox.showinfo("游戏结束", "得分 " + str(score))
			pygame.quit()
			sys.exit()

		DrawSnake(SnakeBody, SnakeClass.FoodInstance.GetPos())
		pygame.display.flip()

		if time_counter >= speed:
			SnakeClass.SnakeInstance.SetDirection(snakeDirection)
			SnakeClass.SnakeInstance.Move()
			time_counter = 0  # 重置计数器

if __name__ == '__main__':
	StartGame()
