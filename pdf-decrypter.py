import pikepdf
import pypdf
import os

original_file_name = input("--- 請輸入 原始的 PDF 檔名 ---\n")
password = input("--- 請輸入密碼 ---\n")
saved_file_name = input("--- 請輸入 轉存的 PDF 檔名 (default: 原始檔名) ---\n")

with pikepdf.open(original_file_name, password=password) as pdf:
    pdf.save('tmp.pdf')
    reader = pypdf.PdfReader('tmp.pdf')
    file_name = saved_file_name if saved_file_name is not None else original_file_name
    pdf.save(file_name)
    pdf.close()
