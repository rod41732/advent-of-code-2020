import re
content = open('input.txt', 'r').read()
# split by blank line
passport = content.strip().split('\n\n')
# join multiple line in passport
passport = [' '.join(p.split('\n')) for p in passport]

print(f"num passports {len(passport)}")

req_fields = set('byr iyr eyr hgt hcl ecl pid'.split())

# validator function
def val_byr(byr: str) -> bool:
  match = re.match('^([1-2][0-9]{3})$', byr)
  if match is None: return False
  (year,) = match.groups()
  return 1920 <= int(year) <= 2002

def val_iyr(iyr: str) -> bool:
    match = re.match('^([2][0-9]{3})$', iyr)
    if match is None: return False
    (year,) = match.groups()
    return 2010 <= int(year) <= 2020

def val_eyr(eyr: str) -> bool:
  match = re.match('^([2][0-9]{3})$', eyr)
  if match is None: return False
  (year,) = match.groups()
  return 2020 <= int(year) <= 2030
  

def val_height(h: str) -> bool:
  match = re.match('^([1-9][0-9]+)([a-z]+)$', h)
  if match is None: return False
  height, unit = match.groups()
  if unit == 'cm':
    return 150 <= int(height) <= 193
  if unit == 'in':
    return 59 <= int(height) <= 76
  return False

def val_hcl(hcl: str) -> bool:
  match = re.match('^(#[0-9a-f]{6})$', hcl)
  return match is not None


eye_colors = set('amb blu brn gry grn hzl oth'.split())
def val_ecl(ecl: str) -> bool:
  return ecl in eye_colors

def val_pid(pid: str) -> bool:
  match = re.match('^[0-9]{9}$', pid)
  return match is not None

validator = {
  'byr': val_byr,
  'iyr': val_iyr,
  'eyr': val_eyr,
  'hgt': val_height,
  'hcl': val_hcl,
  'ecl': val_ecl,
  'pid': val_pid
}

valid = 0
nef = 0
for p in passport:
  matches = re.findall(r'(\S*):(\S+)\s', p + ' ')
  data = {field:val for field, val in matches}
  # print(data)
  if not set(data.keys()).issuperset(req_fields):
    nef += 1
    continue
  else:
    result = {field: validator[field](data[field]) for field in req_fields}
    if all(result.values()):
      # print("valid")
      valid += 1
    # else:
    #   print("invalid", *(k for k in result if result[k] == False))
    

# print("nef =", nef)
print(valid)
  

