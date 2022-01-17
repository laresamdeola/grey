from replit import db


def create_strand(strand, reach, moment):
  if strand in db:
    print(f"{strand} already exists in your memory")
  else:
    db[strand] = f"Phone Number: {reach} and you met: {moment}"
    print(f"{strand} has been added to your memory")


def remember_strand(strand):
  the_strand = db.get(strand)
  return the_strand





