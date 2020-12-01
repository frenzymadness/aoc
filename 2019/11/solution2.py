from robot import Robot

r = Robot()
r.whites.append(r.position)
end = True
while end:
    end = r.step()
r.draw()