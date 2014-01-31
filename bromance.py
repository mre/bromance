"""bromance

Usage: bromance.py <command>

Options:
    -h --help   Show this screen.
    --version   Show version.
"""

import sys
import requests
from docopt import docopt
from colorama import init, Style

# Reset color output after each print statement
init(autoreset=True)

# Retrieve entries from the following websites
BRO_URL =  "http://bropages.org/{}.json"
TLDR_URL = "https://raw.github.com/rprieto/tldr/master/pages/osx/{}.md"

# HTTP status code for successful retrieval
STATUS_OK = 200

def prettyprint(lines):
  """
  Format the output for the commandline
  """
  for line in lines:
    # Check for formatting in line
    if line.startswith("#") or line.startswith("-"):
      # We found an entry title.
      # Remove unneeded formatting and
      # print the line in titlecase
      print(Style.BRIGHT + line[2:].title())
    else:
      print(line)
  # Leave some space between each entry
  print("")

def is_good(entry):
  """
  Good entries on a bropage have more upvotes than downvotes.
  """
  try:
    return entry["up"] >= entry["down"]
  except:
    return True

def get_data(url, cmd):
  """
  Make an HTTP call to get all data for a command
  """
  r = requests.get(url.format(cmd))
  if r.status_code == STATUS_OK:
    print r.text
    if "json" in r.headers['content-type']:
      return r.json()
    else:
      return r.text

def lookup(cmd):
  """
  Get all entries for command on bropages and tldr
  and print the output to the commandline.
  """
  output = []
  data = get_data(BRO_URL, cmd)
  """
  if data:
    for entry in data:
      print "---"
      print entry["msg"]
      print "---"

  data = get_data(TLDR_URL, cmd)
  """
  """
  entries = [entry["msg"].strip().splitlines()
                for entry in data if is_good(entry)]
  bro_lines = [line for entry in entries for line in entry]
  print bro_lines
  output.append(bro_lines)

  data = get_data(TLDR_URL, cmd)
  print data
  tldr_lines = [line for line in data.strip().splitlines()[1:]
                if line and not line.startswith(">")]
  print tldr_lines
  output.append(tldr_lines)

  if not output:
      sys.exit("Oops. Can't find an entry for `{}`.".format(cmd))

  prettyprint(output)
  """


def main():
  """
  Parse the user input
  """
  args = docopt(__doc__, version='bromance 0.3')
  cmd = args['<command>']
  if cmd:
    lookup(cmd)
  else:
    print(args)

if __name__ == '__main__':
  main()
