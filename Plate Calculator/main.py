weight = int(input("Enter desired weight: "))
bar = int(input("Enter bar weight: "))
kilolbs = str(input("imperial or metric: ")).lower()
#olynorm = str(input("Olympic or Standard: "))

def imperial(weight, bar):
  weights = {
  "red": 0,
  "blue": 0,
  "yellow": 0,
  "green": 0,
  "black": 0,
  "red2": 0,
  "blue2": 0,
  "yellow2": 0,
  "green2": 0,
  "black2": 0}

  weight = (weight-bar) / 2
  while weight > 0:
    if weight >= 55:
      weight -= 55
      weights["red"] += 1
    elif weight >= 45:
      weight -= 45
      weights["blue"] += 1
    elif weight >= 35:
      weight -= 35
      weights["yellow"] += 1
    elif weight >= 25:
      weight -= 25
      weights["green"] += 1
    elif weight >= 10:
      weight -= 10
      weights["black"] += 1
    elif weight >= 5:
      weight -= 5
      weights["blue2"] += 1
    elif weight >= 2.5:
      weight -= 2.5
      weights["green2"] += 1
    elif weight >= 1.25:
      weight -= 1.25
      weights["black2"] += 1
  return(weights)

def metric(weight, bar):
  weights = {
  "red": 0,
  "blue": 0,
  "yellow": 0,
  "green": 0,
  "black": 0,
  "red2": 0,
  "blue2": 0,
  "yellow2": 0,
  "green2": 0,
  "black2": 0}

  weight = (weight-bar) / 2
  while weight > 0:
    if weight >= 25:
      weight -= 25
      weights["red"] += 1
    elif weight >= 20:
      weight -= 20
      weights["blue"] += 1
    elif weight >= 15:
      weight -= 15
      weights["yellow"] += 1
    elif weight >= 10:
      weight -= 10
      weights["green"] += 1
    elif weight >= 5:
      weight -= 5
      weights["black"] += 1
    elif weight >= 2.5:
      weight -= 2.5
      weights["red2"] += 1
    elif weight >= 2:
      weight -= 2
      weights["blue2"] += 1
    elif weight >= 1.5:
      weight -= 1.5
      weights["yellow2"] += 1
    elif weight >= 1:
      weight -= 1
      weights["green2"] += 1
    elif weight >= .5:
      weight -= .5
      weights["black2"] += 1
  return(weights)
  



if kilolbs == "imperial":
  print(imperial(weight, bar))
elif kilolbs == "metric":
  print(metric(weight, bar))
else:
  print("invalid input")