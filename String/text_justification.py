def fullJustify(words, maxWidth):
    lines = []
    index = 0
    
    while index < len(words):
        count = len(words[index])
        last = index + 1
        
        # Find how many words fit in the current line
        while last < len(words):
            if count + 1 + len(words[last]) > maxWidth:
                break
            count += 1 + len(words[last])
            last += 1
        
        builder = words[index]
        diff = last - index - 1
        
        # If last line OR only one word → left justify
        if last == len(words) or diff == 0:
            for i in range(index + 1, last):
                builder += " " + words[i]
            
            # Fill remaining spaces at end
            builder += " " * (maxWidth - len(builder))
        
        else:
            # Fully justify
            spaces = (maxWidth - count) // diff
            extraSpaces = (maxWidth - count) % diff
            
            for i in range(index + 1, last):
                builder += " " * (spaces + (1 if extraSpaces > 0 else 0))
                if extraSpaces > 0:
                    extraSpaces -= 1
                builder += " " + words[i]
        
        lines.append(builder)
        index = last
    
    return lines


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(fullJustify(words, maxWidth))