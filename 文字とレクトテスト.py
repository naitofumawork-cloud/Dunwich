import pygame

# --- 事前準備（ループの外） ---
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 48)  # フォントの準備（サイズ48）

# 1. レクトAとテキストを定義
rect_a = pygame.Rect(300, 250, 200, 100)
t = "AA"

# 2. テキストを「画像（Surface）」に変換する
text_surface = font.render(t, True, (255, 255, 255))  # (文字, 滑らかさ, 色)

# 3. テキスト画像のRectを取得し、中心をレクトAの中心に合わせる
text_rect = text_surface.get_rect(center=rect_a.center)


# --- 描画処理（ゲームループの中） ---
# レクトA自体を描画
pygame.draw.rect(screen, (70, 75, 85), rect_a)

# 4. 画面(screen)にテキスト画像(text_surface)を貼り付ける
screen.blit(text_surface, text_rect)