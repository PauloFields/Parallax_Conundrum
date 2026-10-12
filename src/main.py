
import pygame
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parallax Conundrum")
clock = pygame.time.Clock()

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

BACKGROUND = (35, 45, 40)
PANEL = (24, 31, 28)
BORDER = (100, 115, 100)
TEXT = (235, 235, 220)
ACCENT = (225, 190, 95)

font = pygame.font.SysFont("arial", 20)
small_font = pygame.font.SysFont("arial", 16)
title_font = pygame.font.SysFont("arial", 28, bold=True)


def load_card(filename, size):
    image = pygame.image.load(ASSETS_DIR / filename).convert_alpha()
    return pygame.transform.smoothscale(image, size)

wave_image = load_card("nem-17-parallax-wave.png", (150, 210))
opalescence_image = load_card("uds-13-opalescence.png", (150, 210))

def draw_text(text, x, y, color=TEXT, font_obj=font):
    surface = font_obj.render(text, True, color)
    screen.blit(surface, (x, y))

def draw_panel(rect, color=PANEL):
    pygame.draw.rect(screen, color, rect, border_radius=8)
    pygame.draw.rect(screen, BORDER, rect, width=2, border_radius=8)


def draw_counters(x, y, count=5):
    for i in range(count):
        cx = x + i * 27
        pygame.draw.circle(screen, ACCENT, (cx, y), 10)
        pygame.draw.circle(screen, TEXT, (cx, y), 10, width=1)
        label = small_font.render("5" if False else str(i + 1), True, PANEL)
        screen.blit(label, label.get_rect(center=(cx, y)))


def draw_battlefield():
    screen.fill(BACKGROUND)

    draw_text("PARALLAX CONUNDRUM", 30, 20, ACCENT, title_font)

    # Player B
    draw_panel((30, 70, 780, 265))
    draw_text("JOGADOR B", 50, 82)
    screen.blit(wave_image, (65, 120))
    draw_text("Marcadores de fading: 5", 230, 175)

    # Central battlefield card
    screen.blit(opalescence_image, (645, 395))

    # Player A
    draw_panel((30, 350, 780, 265))
    draw_text("JOGADOR A", 50, 362)
    screen.blit(wave_image, (65, 400))
    draw_text("Marcadores de fading: 5", 230, 455)

    # Stack
    draw_panel((830, 70, 420, 370))
    draw_text("STACK", 850, 85, ACCENT, title_font)
    draw_text("Vazia", 850, 135)

    # Priority
    draw_panel((830, 470, 420, 170))
    draw_text("PRIORIDADE", 850, 485, ACCENT)
    draw_text("Jogador A", 850, 525)
    draw_text("Estado inicial", 850, 560, TEXT, small_font)

    pygame.draw.rect(screen, ACCENT, (850, 590, 160, 35), border_radius=6)
    draw_text("RESET", 895, 596, PANEL)


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_battlefield()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
