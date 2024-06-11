block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
    blocks_empties_removed = []
    for i in range(len(blocks)):
        if blocks[i] != '':
            blocks_empties_removed.append(blocks[i])
            
    return blocks_empties_removed

def block_to_block_type(block):
    if block.startswith("#"):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        lines = block.split("\n")
        for line in lines:
            if not (line.startswith("* ")):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if not (line.startswith("- ")):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        lines = block.split("\n")
        counter = 1
        for line in lines:
            if not line.startswith(f"{counter}. "):
                return block_type_paragraph
            counter += 1
        return block_type_ordered_list
    return block_type_paragraph