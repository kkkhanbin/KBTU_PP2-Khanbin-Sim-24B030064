import pygame
pygame.init()


shapes = []


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    eraser = False

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                elif event.key == pygame.K_e:
                    eraser = True if not eraser else False
                
                elif event.key == pygame.K_l:
                    points.append((pygame.mouse.get_pos(), "r"))
                elif event.key == pygame.K_c:
                    points.append((pygame.mouse.get_pos(), "c"))
                elif event.key == pygame.K_1:
                    points.append((pygame.mouse.get_pos(), "square"))
                elif event.key == pygame.K_2:
                    points.append((pygame.mouse.get_pos(), "triangle"))
                elif event.key == pygame.K_3:
                    points.append((pygame.mouse.get_pos(), "equilateral triangle"))
                elif event.key == pygame.K_4:
                    points.append((pygame.mouse.get_pos(), "rhombus"))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list

                position = event.pos
                points.append((position, eraser))
                points = points[-256:]

        screen.fill((0, 0, 0))
        
        # for shape in shapes:
        #     drawShape(screen, shape, pygame.Color(mode), shape[0], 75)

        # draw all points
        i = 0
        prev = points[0] if points else None
        while i < len(points) - 1:
            if points[i][1] in ["r", "c"]:
                drawLineBetween(screen, i, points[i], [1, 1], radius, mode)
            else:
                drawLineBetween(screen, i, prev, points[i + 1], radius, mode)
            i += 1

            prev = points[i]
                
        pygame.display.flip()
        
        clock.tick(60)


def drawShape(screen, point1, color, start, size):
    if point1[1] == "r":
        pygame.draw.rect(screen, color, pygame.Rect(start[0] - size, start[1] - size, size * 2, size * 2.5))
    elif point1[1] == "c":
        pygame.draw.circle(screen, color, start, size)
    elif point1[1] == "square":
        pygame.draw.rect(screen, color, pygame.Rect(start[0] - size, start[1] - size, size * 2, size * 2))
    elif point1[1] == "triangle":
        pygame.draw.polygon(screen, color, [(start[0], start[1] - size), (start[0] - size // 2, start[1] + size // 2), (start[0] + size // 2, start[1] + size // 2)])
    elif point1[1] == "equilateral triangle":
        pygame.draw.polygon(screen, color, [(start[0], start[1] - size), (start[0], start[1] + size // 2), (start[0] + size // 2, start[1] + size // 2)])
    elif point1[1] == "rhombus":
        pygame.draw.polygon(screen, color, [(start[0], start[1] - size), (start[0] + size, start[1]), (start[0], start[1] + size), (start[0] - size, start[1])])


def drawLineBetween(screen, index, point1, point2, width, color_mode):
    global shapes

    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    start = point1[0]
    end = point2[0]

    size = 75

    if isinstance(point1[1], str):
        shapes.append(point1)
        # color = pygame.Color(color_mode)
        drawShape(screen, point1, color, start, size)
        return 
    
    if point1[1] or point2[1]:
        color = pygame.Color("black")

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


main()