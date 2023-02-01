def char_count(str):
  dict = {}
  for i in str:
    if i not in dict.keys():
      dict.update({i:1})
    else:
      dict[i]+=1
  return dict