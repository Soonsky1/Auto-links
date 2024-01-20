print("Привет,вижу ты впервый раз зашел в python давай быстро расскажу об этом скрипте.Этот скрипт сравнивает 2 разных текста и находит в них отличие,вставляй свои 2 файла и сравнивай.Удачи!")
print("Вот тебе пример")
file1=open("Ссылки1.txt")
file2=open("Ссылки2.txt")
file1=file1.read().splitlines()
file2=file2.read().splitlines()
matching_links=set()
not_matching_links=set()
for i in file1:
    if i in file2:
        matching_links.add(i)
    else:
        not_matching_links.add(i)
for i in file2:
    if i not in file1:
        not_matching_links.add(i)
print("Сыллки1")
print(matching_links)
print("Ссылки2")
print(not_matching_links)
