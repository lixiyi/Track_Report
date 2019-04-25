#!/usr/bin/python3

import xml.sax


class XmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.tag = ""
        self.num = ""
        self.docid = ""
        self.url = ""
        self.entities = []
        self.emp = {}

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.tag = tag
        if self.tag == "top":
            print("*****Topic*****")
        elif self.tag == "entities":
            print("=====Entities=====")

    # Call when an elements ends
    def endElement(self, tag):
        if self.tag == "num":
            print("num:", self.num)
        elif self.tag == "docid":
            print("docid:", self.docid)
        elif self.tag == "url":
            print("url:", self.url)
        elif tag == "entity":
            self.entities.append(self.emp)
            print(self.emp)
            self.emp = {}
        self.tag = ""

    # Call when a character is read
    def characters(self, content):
        if self.tag == "num":
            self.num = content
        elif self.tag == "docid":
            self.docid = content
        elif self.tag == "url":
            self.url = content
        elif self.tag == "id" or self.tag == 'mention' or self.tag == 'link':
            self.emp[self.tag] = content


if __name__ == "__main__":

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = XmlHandler()
    parser.setContentHandler(Handler)

    # parser.parse("D:/Download/Projects/TREC2019/WashingtonPost.v2/data/newsir18-topics.txt")
    parser.parse("E:/Track/WashingtonPost.v2/data/newsir18-entities.txt")


