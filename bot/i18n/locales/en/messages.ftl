state-enabled = enabled
state-disabled = disabled

start-message =
    Use /generate to generate a password and adjust its settings.
    The bot also supports inline mode, so you can use the generator right in the current chat.

btn-try-inline = Try inline mode

generate-message =
    Here are your current settings:
    Word count: <b>{ $word_count }</b>
    Delimiters: <b>{ $delimiters }</b>
    Edge characters: <b>{ $edge_delimiters }</b>
    Generated password:
    <tg-spoiler>{ $password }</tg-spoiler>
    (tap spoiler above to reveal the password)


btn-word-minus = - word
btn-word-plus = + word
btn-hide-delimiters = Remove delimiters
btn-show-delimiters = Add delimiters
btn-remove-edge = Remove edge characters
btn-add-edge = Add edge characters
btn-regenerate = Regenerate
btn-copy-password = Copy password
btn-delete = Delete message
delete-failed = Failed to delete the message. Please delete it manually.

inline-strong-title = Strong password
inline-strong-description = 4 words, random UPPERCASE, separated by numbers or special characters
inline-normal-title = Normal password
inline-normal-description = 3 words, random UPPERCASE, separated by numbers
inline-weak-title = Weak password
inline-weak-description = 2 words, no digits or separators
