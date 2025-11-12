def words_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def characters_count(file_contents):
    file_contents = file_contents.lower()
    char_count = {}
    for char in file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def dic_list_sorted(characters_dic):
    def sort_on(chars):
        return chars["num"]
    dic_list = []
    for char in characters_dic.keys():
        dic_list.append({"char": char, "num": characters_dic[char]})
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list
