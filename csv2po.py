from __future__ import print_function
import csv
import os

class new_language_file:
    def __init__(self,filename):
        content = self.read_csv(file_name)
        self.write_po("survey", content)

    def read_csv(self,path):
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
        try:
            if path[-3:] == "csv":
                with open(path, 'r', encoding='UTF-8') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        textDic[row[0]] = row[1]
                return textDic
            else:
                print("\033[0;30;31m\tPlease provide .csv file.\033[0m")
        except UnicodeError:
            print("\033[0;30;31m\tPlease make sure .csv file is in UTF-8 format.\033[0m")
            os._exit(0)


    def write_po(self,fileName,content):
        if not os.path.exists("LC_MESSAGES"):
            os.mkdir("LC_MESSAGES")
        with open("LC_MESSAGES/" + fileName+ ".po", "w+") as fout:
            for language,text in content.items():
                fout.write("msgid " + '\"' + language + '\"' + '\n')
                fout.write("msgstr " + '\"' + text + '\"' + '\n')
                fout.write('\n')


class add_content:
    def __init__(self,filename):
        self.read_csv_columns(filename)

    def read_csv_columns(self,path):
        global languages
        if not os.path.exists(path):
            print("\033[0;30;31m\tPlease input correct path.\033[0m")
            os._exit(0)
        try:
            if path[-3:] == "csv":
                with open(path, 'r', encoding='UTF-8-sig') as csvfile:
                    reader = csv.reader(csvfile)
                    languages = next(reader)
                    csv_reader = csv.DictReader(csvfile,fieldnames=languages)
                    for row in csv_reader:
                        d = {}
                        for k,v in row.items():
                            d[k] = v
                        self.write_csv_columns(d)
        except UnicodeError:
            print("\033[0;30;31m\tPlease make sure .csv file is in UTF-8 format.\033[0m")
            os._exit(0)

    def write_csv_columns(self,content):
        for language in languages:
            if language == "en":
                continue
            if not os.path.exists(language + "/LC_MESSAGES"):
                os.makedirs(language + "/LC_MESSAGES")

        for language, text in content.items():
            if language == "en":
                continue
            with open(language + "/LC_MESSAGES/survey.po", "a+") as fout:
                fout.write("msgid " + '\"' + content['en'] + '\"' + '\n')
                fout.write("msgstr " + '\"' + text + '\"' + '\n')
                fout.write('\n')

if __name__ == '__main__':
    print("1. add new content")
    print("2. add new language")
    model = input("please chose mode:")

    if(model == "1"):
        file_name = input("Please input the file name you want to transfer(under save folder): ")
        add_content(file_name)
        print("Finished! Please Check every file under LC_MESSAGES folder")
    elif(model == "2"):
        file_name = input("Please input the file name you want to transfer(under save folder): ")
        new_language_file(file_name)
        print("Finished! Please Check the file under LC_MESSAGES folder")
    else:
        print("\033[0;30;31m\tPlease inlut 1 or 2.\033[0m")









