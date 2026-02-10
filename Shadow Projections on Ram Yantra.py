import math
import pandas as pd
ang = 0 # Angle in degrees
r = 15  # Radius
data = []
for ang in range (0, 91):
    if ang <= 45:
        proj = math.tan(math.radians(ang))  # Projection component
        length = r*proj # Length of projection on surface
        data.append([ang, proj, length])
    else:
        proj = 1/math.tan(math.radians(ang))
        length = r*proj
        data.append([ang, proj, length])
df = pd.DataFrame(data, columns=['Angle in degrees', 'Projection Component', 'Projection in cm'])
df.to_excel('Projections.xlsx', index=False)
