import re

regex = r"www\.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*\.[a-z]+(\.[a-z]+)*"
sub_domain = r"www"
domain = r"[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*"
extension = r"[a-z]+(\.[a-z]+)*"

pattern = rf"{sub_domain}.{domain}.{extension}"

text = input()

result = re.findall(pattern, text)

print(result)
#while True:
 #   text = input()
#
   # if not text:
   #     break
#
   # result = re.findall(pattern, text)
#
  #  if len(result) > 0:
   #     print(result)

# to break up link into sub-domain, domain, extension