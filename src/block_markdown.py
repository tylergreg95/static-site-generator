def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
    blocks_empties_removed = []
    for i in range(len(blocks)):
        if blocks[i] != '':
            blocks_empties_removed.append(blocks[i])
            
    return blocks_empties_removed