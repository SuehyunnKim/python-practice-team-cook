# 回文とは’しんぶんし’のように上から読んで下から読んでも同じような文章や単語のことを言います。
# 続けてinputされた文字列が回文なのかを判別するプログラムを作成しよう

# 回答1
print('回文判別プログラムです。終了したい場合は、‘exit’を入力してください')
while True:
  word = input('判別したい文章や単語を入力してください：')
  if word == 'exit':
    break
  elif word == word[::-1]:
    print(f'{word}は回文です')
  else:
    print(f'{word}は回文ではないです')

# 回答2
print('回文判別プログラムです。終了したい場合は、‘exit’を入力してください')
while True:
  word = input('判別したい文章や単語を入力してください：')
  if word == 'exit':
    break
  else:
    is_palindrome = True
    for i in range(len(word)//2):
      if word[i] != word[-1-i]:
        is_palindrome = False
        print(f'{word}は回文ではないです')
        break
    print(f'{word}は回文です')


# exceptions need to be deal with later
# 1. space(' ') included in input
# 2. Capital letters of english