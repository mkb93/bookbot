
def main():
  print('--- Begin report of books/frankenstein.txt ---')
  def sortAmount(dict):
    return dict['num']

  def charAmount():
    with open('./books/frankenstein.txt') as f:
      file_contents = f.read()
      words = len(file_contents.split())
      print('{} words found in the document'.format(words))
      file_contentsLowered = file_contents.lower() 
      dictObj = {}
      for x in file_contentsLowered:
        if x in dictObj:
          dictObj[x] += 1
        elif x.isalpha():
          dictObj[x] = 1
    return dictObj
  def arrMaker(dict):
    arr = []
    for x in dict:
      temp = {"name": x, "num": dict[x]}
      arr.append(temp)
    
    return arr
  finalList = arrMaker(charAmount())
  finalList.sort(reverse=True, key=sortAmount)
  print('\n')
  for x in finalList:
    print('the "{}" character was found {} times'.format(x['name'],x['num']))  
  print('--- End report ---')
main()