import os
from typing import List
num_lines = []
only_nums  = []

def convert(lst):
    return ([i for item in lst for i in item.split()])

def select() -> List:
  multi_sel = []
  start_line = int(input("Start on which line? "))
  ending_line = int(input("End on which line? "))

  num_lines = num_limes()

  for x in num_lines:
    line_num = int(x.split()[0])
    print(line_num)
    if start_line >= line_num and ending_line <= line_num:
        multi_sel.append(x)
  return multi_sel

def num_limes() -> List:
    lines = load()
    num_lines = []
        
    for x, line in enumerate(lines):
        num_lines.append((f"{x+1} {line}"))

   
    return num_lines

def load():
    with open("main.py", "r") as file:
        lines = file.read().splitlines()
    return lines

def clear_main():
    with open("main.py", "w") as empty:
        pass

def main():
    num_lines = num_limes()
    
    for x in num_lines:
      line_num = int(x.split()[0])
      only_nums.append(line_num)
    
    while True:
        try:
            lines = load()
            ii = input("Please select mode\n[edit] [read]\n> ").title() ## ii is initial input
            if ii == "Edit":
                while True:
                    try:
                        print("Code Goes Here\n$$$ to access command prompt")
                        ui = input("> ")
                        if ui == "insertmode":
                            break
                        if ui[0:3] == "$$$":
                            ui = ""
                            command = input("Please Select Command\n[New] [Save] [Load]\n> ").title()
                          
                            if command == "Remove":
                                container = select()
                                empty_list = []
                                with open("main.py", "r") as holder:
                                    l = holder.read().splitlines()
                                    for x in num_lines:
                                        for y in container:
                                            if x == y:
                                                num_lines.remove(x)
                                    with open("main.py", "w") as empty:
                                        pass
                                    with open("main.py", "a") as replace:
                                        for x in num_lines:
                                            replace.write(x + "\n")
                                            
                                    
                            if command == "New":
                                with open("main.py", "r") as save:
                                  l = save.read().splitlines()
                                  with open("save_files/previous_code.txt", "w") as new:
                                      for x in l:
                                          new.write(x + '\n')
                                  with open("main.py", "w") as empty:
                                      pass
                                    
                            if command == "Save":
                                with open("main.py", "r") as save:
                                  l = save.read().splitlines()
                                  with open("save_files/back_up_file.txt", "w") as new:
                                      for x in l:
                                          new.write(x + '\n')
        
                            if command == "Load":
                                with open("save_files/back_up_file.txt", "r") as back:
                                    l = back.read().splitlines()
                                    with open("main.py", "w") as new:
                                        for x in l:
                                            new.write(x + '\n')
        
                        if os.path.exists("main.py"):
                            with open("main.py", "a") as file:
                                file.write(ui + "\n")
                                file.close
                        else:
                            with open("main.py", "w") as holder:
                                holder.write(ui + "\n")
                                holder.close
        
                    except KeyboardInterrupt:
                        print("\ndone")
                        break
        
            if ii == "Read": #only reads files
                while True:
                  try:
                    file_sel = input("Select File to Read: ")
                    if os.path.exists(file_sel):
                        line_mode = input("[One] line - [all] lines: - [Multi] line: ").upper()
                        if line_mode == "ONE":
                          print()
                          line_input = int(input("Line index: "))
                          print(lines[line_input - 1].strip() + "\n")
        
                        elif line_mode == "ALL":
        
                          for x, line in enumerate(lines):
                            print(f"\n{x+1} {line}")
                            
                        elif line_mode == "MULTI":
                          multi_sel = []
                          start_line = int(input("Start on which line: "))
                          ending_line = int(input("End on which line: "))
                          if start_line not in only_nums or ending_line not in only_nums:
                            print("Invaild Number")
                            
                          print()
                          for x in num_lines:
                            line_num = int(x.split()[0])
                            if start_line <= line_num:
                              if ending_line >= line_num:
                                multi_sel.append(x)
                          print()
                              
                          for x in multi_sel:
                            print(x)
        
                        if line_mode == "QUIT" or line_mode == "Q":
                          break
                    else:
                        print("File does not exist")
                  except KeyboardInterrupt:
                        print("\ndone")
                        break
        except KeyboardInterrupt:
            print("\n\nThank you for using our program :)\n\n")
            break


if __name__ == "__main__":
    main()

