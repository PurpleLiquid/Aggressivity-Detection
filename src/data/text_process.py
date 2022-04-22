import re

def clean_urls(string):
    regex = r"\b(?:https?://)?(?:(?i:[a-z]+\.)+)[^\s,]+\b"
    string_wo_urls = re.sub(regex, '', string)
    return string_wo_urls

def clean_usernames_and_hashtags(string):
    regex = r"([@#][A-Za-z0-9_]+)"
    string_wo_usernames_and_hashtags = re.sub(regex, '', string)
    return string_wo_usernames_and_hashtags

def clean_punct(string):
    regex = r"[^\w\s]"
    string_wo_punct = re.sub(regex, '', string)
    return string_wo_punct

def clean_nums(string):
    regex = r"[\d]"
    string_wo_nums = re.sub(regex, '', string)
    return string_wo_nums

def clean_extra(string):
    string_wo_extra = ' '.join( [w for w in string.split() if len(w)>1] )
    return string_wo_extra

def clean(string):
    string = clean_urls(string)
    string = clean_usernames_and_hashtags(string)
    string = clean_punct(string)
    string = clean_nums(string)
    string = clean_extra(string)

    string = string.lower()
    return string
