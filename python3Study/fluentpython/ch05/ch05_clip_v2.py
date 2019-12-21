# 示例5-19 有注解的 clip 函数
# 如何引用参考 ch05_tag.py

def clip(text:str, max_len:'int > 0'=80) -> str: #(1)
    """
    在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)

    return text[:end].rstrip()