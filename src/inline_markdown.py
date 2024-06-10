from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        delimiter_count = 0
        for ch in node.text:
            if ch == delimiter:
                delimiter_count += 1
        if delimiter_count % 2 != 0:
            raise ValueError(f"Cannot find matching closing delimiter: {delimiter}")
        split_node = node.text.split(delimiter)
        for i in range(0, len(split_node)):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node[i], text_type_text))
            else:
                    new_nodes.append(TextNode(split_node[i], text_type))
    return new_nodes