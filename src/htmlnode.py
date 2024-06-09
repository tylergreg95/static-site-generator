class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        html = ""
        for prop in self.props:
            html += f" {prop}=\"{self.props[prop]}\""
        return html
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f"TAG: {self.tag}\nVALUE: {self.value}\nCHILDREN: {self.children}\nPROPS: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node value cannot be None")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode tag cannot be None")
        if not self.children or self.children == None:
            raise ValueError("ParentNode children cannot be None or empty")
        html = ""
        for node in self.children:
            html += node.to_html()
        html = f"<{self.tag}>{html}</{self.tag}>"
        return html
        
