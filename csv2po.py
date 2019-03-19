from __future__ import print_function
import csv
import os

def read_csv(path):
    """
		Reads file from CSV file, CSV file includes two column. One is English, the other is the language which you want to transfer
		:param path: the CSV file's name
		:type path: string
		:return: the translations table
		:rtype: dictionary
		:raises: IOError if path is invalid
	"""
    if not os.path.exists(path):
        raise IOError("Invalid path: {0}.".format(path))

    textDic = {}

    #csv file
    if path[-3:] == "csv":
        with open(path, 'r', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                textDic[row[0]] = row[1]
        return textDic
    else:
        print("Please provide .csv file")

def write_po(fileName,content):
    """
    output content to .po file
    :path: /LC_MESSAGES/survey.po
    please double check the output file, and move it into right folder after check
    """
    if not os.path.exists("LC_MESSAGES"):
        os.mkdir("LC_MESSAGES")
    with open("LC_MESSAGES/" + fileName+ ".po", "w+") as fout:
        for en,trans in content.items():
            fout.write("msgid " + '\"' + en + '\"' + '\n')
            fout.write("msgstr " + '\"' + trans + '\"' + '\n')
            fout.write('\n')

if __name__ == '__main__':
    file_name = input("Please input the file name you want to transfer(under save folder): ")
    content = read_csv(file_name)
    file_output_name = input("Please input the output file name(name is 'survey' if make it blank): ")
    if file_output_name:
        write_po(file_output_name, content)
    else:
        write_po("survey", content)
    print("Finished! Check the file under LC_MESSAGES folder")