str = input()

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

if len(str) > 20:
    print("Wrong Input")
else:
    status = first_non_repeating_character(str)

    if status == None:
        print("Exceptional String")
    else:
        print(status)