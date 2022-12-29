from chikkarpy import Chikkar
from chikkarpy.dictionarylib import Dictionary

chikkar = Chikkar()
# chikkar.add_dictionary(Dictionary()) # For prepared dict, we may not use this if not neccessary
user_dic = Dictionary("sudachi.dic", enable_trie=True) # This is file we converted
chikkar.add_dictionary(user_dic)

print(chikkar.find("支払い"))
# Expected ['支払', '支払う', '勘定', '精算', '会計', '御愛想']
print(chikkar.find("インフル"))
# Expected ['インフルエンザ', 'influenza', '流行性感冒', '流感']