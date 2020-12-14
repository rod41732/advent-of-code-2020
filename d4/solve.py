import re
content = open('input.txt', 'r').read()
# split by blank line
passport = content.strip().split('\n\n')
# join multiple line in passport
passport = [' '.join(p.split('\n')) for p in passport]

print(f"num passports {len(passport)}")

req_fields = set('byr iyr eyr hgt hcl ecl pid'.split())
valid = 0
for p in passport:
  # find pattern foo:bar
  # Note: \S means non-whitespace (and \s means whitespace)
  matches = set(re.findall(r'(\S*):(\S)+', p))
  fields = set([k for k, v in matches])
  if not fields.issuperset(req_fields):
    break
  else:
    try:
      pass
    except:
      break

print(valid)
  