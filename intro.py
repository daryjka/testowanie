def div(a, b):
    return a/b
# TUTAJ PSUJ +1


assert div(3, 6) == 0.5, "FAILED"
# zamiast 4 linijek kodu, asercja- po przecinku- co jeżeli nie przejdzie
print("First PASSED")
assert div(2.5, 0.5) == 5, "FAILED"
print("Sec PASSED")
assert div(-4, 2) == -2, "FAILED"
print("Third PASSED")

try:
    div(4, 0)
except:
    print("PASSED")

# istotne w testowaniu są warunki brzegowe!!


print(div(2, 1) + div(-4, 2))
# wyjątki wyrzucają nas z programu, trzeaba je obsłużyć, jeśli tego nie chcemy

# if div(3, 6) == 0.5:
  # print("PASSED")
# else:
   # raise Exception("FAILED")
# proste testowanko. ważne żeby nie mieszać skryptu z testem!!!
