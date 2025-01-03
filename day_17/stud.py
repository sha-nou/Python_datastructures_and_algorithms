
students=[]

def studBase():
    print('select an operation')
    print('1. Register student')
    print('2 . Update student Info')
    print('3. Delete student info')
    print('4. Display all students')
    print('5 . Exit')
    
    
    while True:
      try:
          choice =input('enter an option \n')
          if choice not in ['1','2','3','4','5']:
              raise ValueError('Invalid choice')
          name =input('enter your name\n')
          level =input('enter your class\n')
          if choice == '1':
              if level.isnumeric():
                  studInfo={name,level}
                  students.append(studInfo)
                  print(students)
              else:
                  print('try again')
                  continue
         
          elif choice == '2':
            student_exist=False
            for i in students:
                    if i['name'] == name:
                            student_exist=True
                            break
                    if student_exist:
                        new_level = input('enter your new class\n')
                        if new_level.isnumeric():
                            print(students)
                        else:
                            print('try again')
                            continue
                    else:
                        print('student not found')
                        continue
          elif choice == 3:
              student_exist=False
              for i in students:
                    if i['name'] == name:
                        student_exist=True
                        break
                    if student_exist:
                        students.remove(i)
                        print(students)
                    else:
                        print('student not found')
                        continue 
          elif choice == 4:
              print(students)
          elif choice == 5:
             print('Exiting the program')
             break
      except  ValueError :
          print('try agin another time')
          continue
      finally:
          new_choice =input('do you wish to continue yes / no ?')
          if new_choice == 'yes':
              continue
          else:
           print('exiting program')
           break
          

studBase()
