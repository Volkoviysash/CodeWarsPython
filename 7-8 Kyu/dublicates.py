def main():
  text = input("Enter: ")

  
def dublicates():
  outp = ""
  for c in text:
      if text.count(c) > 1 and not c in outp:
          outp += c
  return len(outp))
  

if __name__ == "__main__":
  main()
