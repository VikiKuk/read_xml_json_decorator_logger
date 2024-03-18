from decorator_logger import logger
import json
import xml.etree.ElementTree as ET

@logger
def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open(file_path, encoding="utf-8") as f:
        json_data = json.load(f)
    all_items = json_data["rss"]["channel"]["items"]
    dict_word_max_len = {}
    for item in all_items:
        for words in item["description"].split():
            if len(words) > word_max_len:
                if words in dict_word_max_len:
                    dict_word_max_len[words] = dict_word_max_len[words] + 1
                else:
                    dict_word_max_len[words] = 1
    word_max_len_list = list(dict_word_max_len.items())
    word_max_len_list_sorted = sorted(word_max_len_list, key=lambda x: x[1], reverse=True)
    result = [n[0] for n in word_max_len_list_sorted[:top_words_amt]]
    return (result)

@logger
def read_xml(file_path, word_max_len=6, top_words_amt=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    all_description = root.findall('channel/item')
    dict_word_max_len = {}
    for description in all_description:
        text = description.find('description').text.split()
        for words in text:
            if len(words) > word_max_len:
                if words in dict_word_max_len:
                    dict_word_max_len[words] = dict_word_max_len[words] + 1
                else:
                    dict_word_max_len[words] = 1
    word_max_len_list = list(dict_word_max_len.items())
    word_max_len_list_sorted = sorted(word_max_len_list, key=lambda x: x[1], reverse=True)
    result = [n[0] for n in word_max_len_list_sorted[:top_words_amt]]
    return (result)



if __name__ == '__main__':

    # print(read_json("newsafr.json"))
    print(read_xml("newsafr.xml"))