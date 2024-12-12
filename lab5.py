# #Задание№1
# import re


# texts = 'task1-en.txt'


# def words_dot(text):
#     res = re.findall(r'\b\w+\b(?=\.)', text)
#     return res


# def num_fractional(text):
#     res =  re.findall(r'\b\d+\.\d+\b', text)
#     return res


# with open(texts, encoding='utf-8') as text:
#     result1 = []
#     result2 = []
#     for line in text:
#         if words_dot(line):
#             res = words_dot(line)
#             result1.append(res)
#         if num_fractional(line):
#             res2 = num_fractional(line)
#             result2.append(res2)
# print(result1)
# print(result2)


##Задание№2
# import re


# texts = 'task2.html'


# def pixel(text):
#     res = re.findall(r'\d+px', text)
#     return res


# with open(texts, encoding='utf-8') as text:
#     result = []
#     for line in text:
#         if pixel(line):
#             res = pixel(line)
#             result.append(res)
# print(result)


#Задание№3


#№допзадание
import re


texts = 'task_add.txt'


def dates(text):
    res = re.findall(r'\s(\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{2,4}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}\s\w+\s\d{2,4})', text)
    return res 


def emails(text):
    res = re.findall(r'\s([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', text)
    return res
    
    
def urls(text):
    res = re.findall(r'\s(https?://[^\s]+|www\.[^\s]+)', text)
    return res


with open(texts, encoding='utf-8') as text:
    result_dates = []
    result_emails = []
    result_urls = []
    for line in text:
        if dates(line):
            res1 = dates(line)
            result_dates.append(res1)
        if emails(line):
            res2 = emails(line)
            result_emails.append(res2)
        if urls(line):
            res3 = urls(line)
            result_urls.append(res3)
print(result_dates)
print(result_emails)
print(result_urls)
