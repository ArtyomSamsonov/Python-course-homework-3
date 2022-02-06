texts = ["python", "c++", "c+", "scala", "java", "mama", "coffee", "clone"]
letter = "c"

#определяем функцию
def count_letter(texts, letter):

  #заводим счетчик
  count = 0

  #проверяем циклом каждое слово в списке
  for word in texts:

    #если “c” присутствует с слове
    if letter in word:
      #увеличиваем счетчик на 1
      count += 1
  return count

print(count_letter((texts), letter))