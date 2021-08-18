from prompt_toolkit.shortcuts import print_tokens, style_from_dict, Token

def color_msg(col, msg):
    style = style_from_dict({
        Token.Color: col,
    })
    tokens = [
        (Token.Color, msg)
    ]
    print_tokens(tokens, style=style)
