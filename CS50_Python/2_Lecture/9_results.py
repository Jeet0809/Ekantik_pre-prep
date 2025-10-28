results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")

# results.append(["Bowser", "Koopa Troopa"])
# results.remove(["Bowser", "Koopa Troopa"])
results.extend(["Bowser", "Koopa Troopa"])
print(results)

results.remove("Bowser")
print(results)

results.insert(0, "Bowser")
print(results)

results.reverse()
print(results)
