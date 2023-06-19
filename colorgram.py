import colorgram  
colors = colorgram.extract('insa.jpg', 25)

total_color= []

for num in range(0,25):
  
  first_color = colors[num]
  r = first_color.rgb.r
  g = first_color.rgb.g
  b = first_color.rgb.b
  rgbb= (r, g, b)
  total_color.append(rgbb)

print(total_color)

