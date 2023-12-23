def main():
   s = input()
   sn = convert(s)
   print(sn)

def convert(s):
   s2 = s.replace("Hello :)", "Hello 🙂")
   s3 = s2.replace("Goodbye :(", "Goodbye 🙁")
   return s3

main()