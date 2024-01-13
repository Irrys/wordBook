

class HTMLParser:

    def __init__(self, parser, label_class):
        self.parser = parser
        self.label_class = label_class
        self.definitions_info = []

    def parse(self, html_content):
        pass


class CambridgeDicParser(HTMLParser):

    def parse(self, html_content):
        p = self.parser(html_content, 'html.parser')
        for block in p.find_all("div", class_=self.label_class["block"]):
            # Find English definition
            eng_def = block.find("div", class_=self.label_class["definition"])
            # Find Chinese translation
            chn_trans = block.find("span", class_=self.label_class["translation"])
            # Find Example sentences
            examples = block.find_all("div", class_=self.label_class["example"])
            example_sentences = []
            for example in examples:
                eng_example = example.find("span", class_=self.label_class["en_exam"])
                chn_example = example.find("span", class_=self.label_class["zh_exam"])
                if eng_example and chn_example:
                    example_sentences.append((eng_example.text.strip(), chn_example.text.strip()))
            if eng_def and chn_trans:
                self.definitions_info.append({
                    "definition": eng_def.text.strip(),
                    "translation": chn_trans.text.strip(),
                    "examples": example_sentences
                })


