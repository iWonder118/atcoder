def main():
  feald = [list(input().split()) for _ in range(4)]

  for i in range(3, -1, -1):
    print(" ".join(reversed(feald[i])))

if __name__ == "__main__":
  main()