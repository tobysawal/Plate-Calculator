weight = int(input("Enter desired weight: "))
bar = int(input("Enter bar weight: "))
kilolbs = str(input("imperial or metric: ")).lower()
olynorm = str(input("Olympic or Standard: ")).lower()

def imperialoly(weight, bar):
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

def metricoly(weight, bar):
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

def imperialnorm(weight, bar):
  weights = {
  "45": 0,
	"25": 0,
	"10": 0,
	"5": 0,
	"2.5": 0
	}

  weight = (weight-bar) / 2
	
  while weight > 0:
    if weight >= 45:
      weight -= 45
      weights["45"] += 1
    elif weight >= 25:
      weight -= 25
      weights["25"] += 1
    elif weight >= 10:
      weight -= 10
      weights["10"] += 1
    elif weight >= 5:
      weight -= 5
      weights["5"] += 1
    elif weight >= 2.5:
      weight -= 2.5
      weights["2.5"] += 1
  return(weights)

def metricnorm(weight, bar):
  weights = {
  "20": 0,
	"10": 0,
	"5": 0,
	"2.5": 0,
	"1": 0
	}

  weight = (weight-bar) / 2
	
  while weight > 0:
    if weight >= 20:
      weight -= 20
      weights["20"] += 1
    elif weight >= 10:
      weight -= 10
      weights["10"] += 1
    elif weight >= 5:
      weight -= 5
      weights["5"] += 1
    elif weight >= 2.5:
      weight -= 2.5
      weights["2.5"] += 1
    elif weight >= 1:
      weight -= 1
      weights["1"] += 1
  return(weights)


def main():
	if olynorm == "olympic":
		if kilolbs == "metric":
			print(metricoly(weight, bar))
		elif kilolbs == "imperial":
			print(imperialoly(weight, bar))
		else:
			print("ERROR: invalid input")
	elif olynorm == "standard":
		if kilolbs == "metric":
			print(metricnorm(weight, bar))
		elif kilolbs == "imperial":
			print(imperialnorm(weight, bar))
		else:
			print("ERROR: invalid input")
	else:
		print("ERROR: invalid input")

main()
