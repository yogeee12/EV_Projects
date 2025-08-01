def char_count(s):
  df={}
  li=s.split(" ")
  for i in range(len(li)):
    if li[i] not in df.keys():
      df[li[i]] = 1
    else:
      df[li[i]] +=1
  return df

p1=char_count("hello my name my is is yoge")
print(p1)
