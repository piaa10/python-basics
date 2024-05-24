import openpyxl

inv_file = openpyxl.load_workbook("inve")
product_list = inv_file["Sheet1"]

product_per_supplier = {}

print(product_list.max_row)