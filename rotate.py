import time
import rotatescreen as rs
pd = rs.get_primary_display()
angle_list = [90,180,270,0]

for i in range(10):
    for x in angle_list:
        pd.rotate_to(x)
        time.sleep(0.5)