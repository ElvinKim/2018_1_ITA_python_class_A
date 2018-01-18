import openpyxl

word_wb = openpyxl.load_workbook("words.xlsx")
word_ws = word_wb.get_sheet_by_name("words")

# Problem 1
problem1_ws = word_wb.create_sheet("problem 1")

for row_i, word in enumerate(word_ws["A"]):
    problem1_ws.cell(row=row_i + 1, column=1, value=word.value)

word_wb.save("words.xlsx")
