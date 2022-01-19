#! python3
#getText.py - Returns text from a given docx document.

def getText(filename):
    import docx
    doc=docx.Document(filename)
    fullText=[]
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ('\n').join(fullText)
        
