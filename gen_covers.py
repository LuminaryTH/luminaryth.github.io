from PIL import Image, ImageDraw, ImageFilter
import math, os, random

assets = r'C:\Users\HP\.qclaw\workspace\personal-homepage\assets'
W, H = 800, 180

random.seed(42)

# ===== 项目1：虚拟试穿 - 紫色抽象人体+衣物流动感 =====
img1 = Image.new('RGBA', (W, H), (10, 10, 20, 255))
draw1 = ImageDraw.Draw(img1)

# 背景渐变
for y in range(H):
    r = int(18 + 14 * math.sin(y / H * math.pi))
    g = int(8 + 6 * math.sin(y / H * math.pi + 0.5))
    b = int(32 + 20 * math.sin(y / H * math.pi + 1.0))
    draw1.line([(0, y), (W, y)], fill=(r, g, b, 255))

# 抽象人体轮廓
for i in range(12):
    cx = W//2 + int(30 * math.sin(i * 0.6))
    cy = 30 + i * 14
    rx = 22 + int(8 * math.cos(i * 0.4))
    ry = 14 + int(5 * math.sin(i * 0.3))
    alpha = int(40 + 30 * math.sin(i * 0.5))
    color = (150, 100, 200, alpha)
    draw1.ellipse([cx-rx, cy-ry, cx+rx, cy+ry], fill=color)

# 流动线条（衣物感）
for i in range(6):
    pts = []
    for x in range(0, W, 8):
        y_base = 60 + i * 22
        y = y_base + int(18 * math.sin(x / 60 + i) * math.cos(x / 120 + i * 0.7))
        pts.append((x, y))
    for j in range(len(pts) - 1):
        alpha = int(60 + 40 * math.sin(j * 0.1 + i))
        color = (180, 130, 220, alpha)
        draw1.line([pts[j], pts[j+1]], fill=color, width=2)

# 光点
for _ in range(25):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(1, 3)
    alpha = random.randint(80, 200)
    draw1.ellipse([x-r, y-r, x+r, y+r], fill=(200, 160, 255, alpha))

img1 = img1.filter(ImageFilter.GaussianBlur(radius=0.8))
img1 = img1.convert('RGB')
img1.save(os.path.join(assets, 'proj1-cover.jpg'), 'JPEG', quality=88)
print('proj1-cover.jpg saved:', os.path.getsize(os.path.join(assets, 'proj1-cover.jpg')))

# ===== 项目2：花卉分类 - 绿色抽象花瓣+神经网络感 =====
img2 = Image.new('RGBA', (W, H), (8, 16, 12, 255))
draw2 = ImageDraw.Draw(img2)

# 背景
for y in range(H):
    r = int(8 + 5 * math.sin(y / H * math.pi * 2))
    g = int(24 + 12 * math.sin(y / H * math.pi))
    b = int(12 + 8 * math.cos(y / H * math.pi))
    draw2.line([(0, y), (W, y)], fill=(r, g, b, 255))

# 抽象花瓣（旋转的椭圆群）
for i in range(20):
    angle = i * 18
    cx = W//2 + int(90 * math.cos(math.radians(angle)))
    cy = H//2 + int(60 * math.sin(math.radians(angle)))
    rx = 14 + int(8 * math.sin(i * 0.7))
    ry = 35 + int(12 * math.cos(i * 0.5))
    alpha = int(25 + 35 * math.sin(i * 0.4))
    # Draw rotated ellipse using polygon approximation
    pts = []
    for t in range(0, 360, 5):
        px = rx * math.cos(math.radians(t))
        py = ry * math.sin(math.radians(t))
        rx2 = px * math.cos(math.radians(angle)) - py * math.sin(math.radians(angle)) + cx
        ry2 = px * math.sin(math.radians(angle)) + py * math.cos(math.radians(angle)) + cy
        pts.append((rx2, ry2))
    if len(pts) > 2:
        draw2.polygon(pts, fill=(100, 200, 130, alpha))

# 中心花蕊
for r in range(25, 5, -3):
    alpha = int(50 + (25 - r) * 8)
    draw2.ellipse([W//2-r, H//2-r, W//2+r, H//2+r], fill=(150, 230, 160, alpha))

# 神经网络节点
for x in range(40, W, 45):
    for y in range(15, H, 28):
        dist = ((x - W//2)**2 + (y - H//2)**2) ** 0.5
        alpha = int(70 * math.exp(-dist / 200))
        if alpha > 8:
            draw2.ellipse([x-2, y-2, x+2, y+2], fill=(120, 220, 150, alpha))

# 连线
for x in range(40, W-45, 45):
    for y in range(15, H-28, 28):
        dist = ((x - W//2)**2 + (y - H//2)**2) ** 0.5
        alpha = int(30 * math.exp(-dist / 180))
        if alpha > 5:
            draw2.line([(x,y),(x+45,y)], fill=(100,180,120,alpha), width=1)
            draw2.line([(x,y),(x,y+28)], fill=(100,180,120,alpha), width=1)

img2 = img2.filter(ImageFilter.GaussianBlur(radius=0.5))
img2 = img2.convert('RGB')
img2.save(os.path.join(assets, 'proj2-cover.jpg'), 'JPEG', quality=88)
print('proj2-cover.jpg saved:', os.path.getsize(os.path.join(assets, 'proj2-cover.jpg')))

# ===== 项目3：天气预测 - 蓝色抽象云+数据流动感 =====
img3 = Image.new('RGBA', (W, H), (8, 12, 20, 255))
draw3 = ImageDraw.Draw(img3)

# 背景渐变
for y in range(H):
    r = int(8 + 6 * math.sin(y / H * math.pi + 0.3))
    g = int(14 + 8 * math.sin(y / H * math.pi + 1.0))
    b = int(30 + 15 * math.sin(y / H * math.pi))
    draw3.line([(0, y), (W, y)], fill=(r, g, b, 255))

# 抽象云朵
cloud_positions = [(120, 55), (300, 40), (520, 60), (680, 45)]
for idx, (bx, by) in enumerate(cloud_positions):
    for r in [32, 26, 38, 22, 30]:
        ox = random.randint(-22, 22)
        oy = random.randint(-10, 10)
        alpha = random.randint(12, 35)
        draw3.ellipse([bx+ox-r, by+oy-r, bx+ox+r, by+oy+r],
                       fill=(100, 160, 220, alpha))

# 数据折线（PCA感）
colors = [(80,180,255), (100,220,200), (180,160,100)]
for series in range(3):
    pts = []
    for x in range(0, W, 6):
        y = H//2 + series * 30 + int(40 * math.sin(x/80 + series*2) * math.cos(x/150 + series))
        pts.append((x, int(y)))
    for j in range(len(pts)-1):
        alpha = int(100 + 50 * math.sin(j * 0.05 + series))
        draw3.line([pts[j], pts[j+1]], fill=(*colors[series], alpha), width=2)

# 雨滴/粒子
for _ in range(40):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(1, 4)
    alpha = random.randint(40, 160)
    c = (random.randint(80,180), random.randint(150,220), random.randint(210,255))
    draw3.ellipse([x-r, y-r, x+r, y+r], fill=(*c, alpha))

# 坐标轴暗示（PCA降维）
draw3.line([(60, 150), (740, 150)], fill=(60, 100, 150, 40), width=1)
draw3.line([(60, 30), (60, 150)], fill=(60, 100, 150, 40), width=1)

img3 = img3.filter(ImageFilter.GaussianBlur(radius=0.6))
img3 = img3.convert('RGB')
img3.save(os.path.join(assets, 'proj3-cover.jpg'), 'JPEG', quality=88)
print('proj3-cover.jpg saved:', os.path.getsize(os.path.join(assets, 'proj3-cover.jpg')))

print('All 3 covers generated!')
