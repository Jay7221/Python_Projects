import re
regex1=re.compile(r'(\d\d)(-|\\|/)(\d\d)(-|\\|/)(\d\d\d\d)')
regex2=re.compile(r'(\d\d\d\d)(-|\\|/)(\d\d)(-|\\|/)(\d\d)')
def dateStd(text):
    feed=regex1.sub(r'\1 / \3 / \5',text)
    feed1=regex2.sub(r'\5 / \3 / \1',feed)
    print(feed1)
    return feed1

print('Use dateStd(text) function to convert all dates in text to dd/mm/yyyy format.')
