raw_file = "raw_dict.csv"
sudachi_file = "sudachi.csv"

import csv
from typing import List
import subprocess

def read_raw():
  raw_data = []
  with open(raw_file, newline='') as csvfile:
    raw_reader = csv.reader(csvfile)
    for row in raw_reader:
      raw_data.append(row)
  return raw_data
    
  
def build_sudachi_csv(raw_data: List[List[str]]):
  # Convert raw CSV to sudachi format 
  # https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md
  def build_sudachi_row(group_count: int, lexeme_id: int, heading: str):
    group_id = f'{group_count:06}'
    predicate = 1
    expansion = 0
    lexeme_id = lexeme_id
    classification = 0
    abbreviation = 0
    spelling = 0
    info = "()"
    heading = heading
    reserve = ""
    reserved = ""
    return (group_id, predicate, expansion, lexeme_id, classification, abbreviation, spelling, info, heading, reserve, reserved)
  with open(sudachi_file, "+w") as csvfile:
    writer = csv.writer(csvfile)
    group_count = 0
    for row in raw_data:
      sudachi_rows = []
      group_count += 1
      lexeme_id = 0
      for heading in row:
        if heading:
          lexeme_id += 1
          sudachi_row = build_sudachi_row(group_count, lexeme_id, heading)
          sudachi_rows.append(sudachi_row)
      writer.writerows(sudachi_rows)
      writer.writerow([]) # We need separate each group by empty line
    
  
def build_sudachi_dic():
  # Build CSV to dic 
  # https://github.com/WorksApplications/chikkarpy
  command = "chikkarpy build -i sudachi.csv -o sudachi.dic"
  subprocess.call(command, shell=True)
    
raw_data = read_raw()
build_sudachi_csv(raw_data)
build_sudachi_dic()