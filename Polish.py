print("here we go")

def polish(s):
  assert "-, +, /, *" not in s, "No signs -, +, /, *"
  for q, w, e in s:
    if q == "+":
      print(int(w)+int(e))
    elif q == "-":
      print(int(w) - int(e))
    elif q == "*":
      print(int(w) * int(e))
    elif q == "/":
      print(int(w) / int(e))
try:      
  polish(input().split(","))
except (Exception) as e:
  print(f"errors {e}")