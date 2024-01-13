from notion_client import Client, AsyncClient

from constants import NOTION_API_KEY


class Block:

    def __init__(self, block_type: str):
        self.children = []
        self.rich_text = []
        self.type = block_type
        self.anno = {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default",
        }

    def B(self):
        self.anno["bold"] = True
        return self

    def I(self):
        self.anno["italic"] = True
        return self

    def S(self):
        self.anno["strikethrough"] = True
        return self

    def U(self):
        self.anno["underline"] = True
        return self

    def add_child(self, child: dict):
        self.children.append(child)

    def add_children(self, children: list):
        self.children.extend(children)

    def create_text(self, content: str, color: str = "default",
                    anno_options: list | None = None, link: str = None,
                    href: str = None, ):
        if anno_options:
            for option in anno_options:
                self.anno[option] = True
        self.anno["color"] = color
        self.rich_text.append(
            {
                "type": "text",
                "text": {"content": content, "link": link},
                "annotations": self.anno,
                "href": href
            }
        )

    def create(self):
        item = {
            "type": self.type,
            self.type: {
                "rich_text": self.rich_text,
            }
        }
        if self.children:
            item[self.type]["children"] = self.children
        return item

    def create_block(self, content: str, color: str = "default",
                     anno_options: list | None = None, link: str = None,
                     href: str = None, ):

        self.create_text(content, color, anno_options, link, href)
        return self.create()


class NotionClient:

    def __init__(self):
        self.client = AsyncClient(auth=NOTION_API_KEY)

    def creat_blocks(self, page_id, blocks):
        return self.client.blocks.children.append(page_id, children=blocks)
