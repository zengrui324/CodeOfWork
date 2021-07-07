import xlrd
import os
import xlsxwriter
def creat_xl(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0] # 读取第一个工作表sheet
    school = []
    team = []
    for i in range(0, sheet.nrows): # 读文件行数
        school.append(sheet.row_values(i, start_colx=0, end_colx=1))  #取第一列
        team.append(sheet.row_values(i, start_colx=1, end_colx=2))   #取第二列
    print(school)
    for i in range(sheet.nrows):
      print(i)
      school_name=str(school[i][0])
      team_name=str(team[i][0])
      team_length = len(team_name)
      if team_length>3: team_length = 3 #取第二列前3个字符
      i=str(i)
      add='-'
      os.mkdir(i+add+school_name+add+team_name)  #创建文件
      later='.xlsx'
      #excel = xlsxwriter.Workbook(i+school_name+team_name[0:team_length]+later)  #创建excel
      #excel.close()
if __name__ == "__main__":
  print('a')
  creat_xl('test.xls')
     
