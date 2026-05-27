import pygame
import math
import random
import colorsys

# 初始化Pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("炫酷动态分形花")
clock = pygame.time.Clock()


class Particle:
    def __init__(self, x, y, angle, speed, color, size, life):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.size = size
        self.life = life
        self.max_life = life
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.99
        self.vy *= 0.99
        self.life -= 1
        self.size *= 0.98

    def draw(self, screen):
        if self.life > 0:
            alpha = self.life / self.max_life
            color = tuple(int(c * alpha) for c in self.color)
            # 绘制发光效果
            for i in range(3):
                radius = self.size * (1 + i * 0.5)
                alpha_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(alpha_surface, (*color, int(100 * alpha / (i + 1))),
                                   (radius, radius), radius)
                screen.blit(alpha_surface, (self.x - radius, self.y - radius))


class FractalFlower:
    def __init__(self):
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.time = 0
        self.particles = []
        self.trail_points = []

    def hsv_to_rgb(self, h, s, v):
        rgb = colorsys.hsv_to_rgb(h, s, v)
        return tuple(int(c * 255) for c in rgb)

    def create_petal(self, center_x, center_y, angle, length, depth, max_depth):
        if depth >= max_depth:
            return

        # 计算花瓣端点
        wave = math.sin(angle * 5 + self.time * 2) * 20
        end_x = center_x + math.cos(angle) * (length + wave)
        end_y = center_y + math.sin(angle) * (length + wave)

        # 根据深度计算颜色
        hue = (self.time * 0.1 + depth / max_depth) % 1.0
        color = self.hsv_to_rgb(hue, 0.8, 1.0)

        # 绘制花瓣线段
        thickness = max(1, int(4 - depth * 0.5))
        pygame.draw.line(screen, color, (center_x, center_y), (end_x, end_y), thickness)

        # 在端点生成粒子
        if random.random() < 0.3:
            particle_color = self.hsv_to_rgb((hue + 0.1) % 1.0, 0.9, 1.0)
            for _ in range(2):
                particle_angle = random.uniform(0, math.pi * 2)
                speed = random.uniform(1, 3)
                self.particles.append(Particle(end_x, end_y, particle_angle, speed,
                                               particle_color, random.uniform(2, 5),
                                               random.randint(20, 40)))

        # 递归创建子花瓣
        new_length = length * 0.7
        self.create_petal(end_x, end_y, angle + 0.5, new_length, depth + 1, max_depth)
        self.create_petal(end_x, end_y, angle - 0.5, new_length, depth + 1, max_depth)

    def update(self):
        self.time += 0.02

        # 更新粒子
        for particle in self.particles[:]:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)

        # 更新轨迹点
        radius = 150 + math.sin(self.time * 3) * 50
        angle = self.time * 2
        trail_x = self.center_x + math.cos(angle) * radius
        trail_y = self.center_y + math.sin(angle) * radius
        self.trail_points.append((trail_x, trail_y, self.time))

        # 限制轨迹点数量
        if len(self.trail_points) > 100:
            self.trail_points.pop(0)

    def draw(self, screen):
        # 创建半透明背景以产生拖尾效果
        alpha_surface = pygame.Surface((WIDTH, HEIGHT))
        alpha_surface.set_alpha(30)
        alpha_surface.fill((0, 0, 0))
        screen.blit(alpha_surface, (0, 0))

        # 绘制旋转的轨迹圆环
        for i, (x, y, t) in enumerate(self.trail_points):
            alpha = i / len(self.trail_points)
            hue = ((self.time * 0.5 + i * 0.01) % 1.0)
            color = self.hsv_to_rgb(hue, 0.7, 1.0)
            radius = 3 + alpha * 2
            # 发光效果
            for j in range(3):
                glow_radius = radius * (1 + j * 0.5)
                glow_surface = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(glow_surface, (*color, int(50 * alpha / (j + 1))),
                                   (glow_radius, glow_radius), glow_radius)
                screen.blit(glow_surface, (x - glow_radius, y - glow_radius))

        # 创建主花朵
        num_petals = 8
        for i in range(num_petals):
            angle = (i / num_petals) * math.pi * 2 + self.time
            self.create_petal(self.center_x, self.center_y, angle, 80, 0, 4)

        # 创建第二层花朵（反向旋转）
        for i in range(num_petals):
            angle = (i / num_petals) * math.pi * 2 - self.time * 0.7
            self.create_petal(self.center_x, self.center_y, angle, 60, 0, 3)

        # 创建中心光芒
        for i in range(12):
            angle = (i / 12) * math.pi * 2 + self.time * 1.5
            x = self.center_x + math.cos(angle) * 10
            y = self.center_y + math.sin(angle) * 10
            hue = (self.time * 0.2) % 1.0
            color = self.hsv_to_rgb(hue, 0.3, 1.0)

            # 绘制中心光柱
            for j in range(5):
                alpha = 255 - j * 50
                glow_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
                pygame.draw.circle(glow_surface, (*color, alpha), (10, 10), 8 - j)
                screen.blit(glow_surface, (x - 10, y - 10))

        # 绘制所有粒子
        for particle in self.particles:
            particle.draw(screen)

        # 绘制中心光点
        center_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        for i in range(10):
            alpha = 200 - i * 20
            radius = 12 - i
            hue = (self.time * 0.3) % 1.0
            color = self.hsv_to_rgb(hue, 0.2, 1.0)
            pygame.draw.circle(center_surface, (*color, alpha), (15, 15), radius)
        screen.blit(center_surface, (self.center_x - 15, self.center_y - 15))


def main():
    flower = FractalFlower()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # 按空格键重置
                    flower = FractalFlower()

        # 更新和绘制
        flower.update()
        flower.draw(screen)

        # 显示FPS
        fps = clock.get_fps()
        font = pygame.font.Font(None, 36)
        fps_text = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))

        # 显示提示
        hint_text = font.render("Press SPACE to reset, ESC to quit", True, (200, 200, 200))
        screen.blit(hint_text, (10, HEIGHT - 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()