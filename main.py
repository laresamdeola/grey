import strands
import datetime


message = """
GREYS. A contact app to help
you remember your friends.
1. Create a strand
2. Remember a strand
3. Dye a strand (update)
4. Pluck a strand (delete)
"""

def prompt_create_strand():
  strand = input("What is this strands' name? ").strip()
  reach = input("How to reach this strand? ").strip()
  moment = datetime.datetime.now()
  strands.create_strand(strand, reach, moment)


def prompt_remember_strand():
  strand = input("What is name of the strand you want to remember? ").strip()
  remember = strands.remember_strand(strand)
  if remember:
    print(f"Here are your strand details: {remember}")
  else:
    print(f"This strand, {strand} hasn't grown yet")


def prompt_dye_strand():
  old_strand = input("What is the name of the strand you want to dye? ").strip()
  old_reach = strands.remember_strand(old_strand)
  if old_reach:
    new_strand = input(f"What name do you want to give {old_strand} now? Leave empty if you want to leave {old_strand}'s name as it is ").strip()
    new_reach = input("What is their new number now? Leave empty if you do not want to change their number").strip()
    if not new_reach:
      new_reach = old_reach
    if not new_strand:
      strands.dye_strand(old_strand, new_reach)
    else:
      strands.dye_reach(old_strand, new_strand, new_reach)
  else:
    print(f"{old_strand} is not in your grey")
      

def main():
  print(message)
  stroke = input("What do you want to do? ").strip()
  if stroke == "1":
    prompt_create_strand()
  elif stroke == "2":
    prompt_remember_strand()
  elif stroke == "3":
    prompt_dye_strand()

main()

#prompt_remember_strand()
#moment = datetime.datetime.now()
#print(moment) 