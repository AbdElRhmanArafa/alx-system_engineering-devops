## Reguexs 
1. **Letters:** `[a-zA-Z]` matches any letter from a to z, regardless of case.
   Example: `regex = /[a-zA-Z]/` matches any letter in the string.

2. **Digits:** `\d` matches any digit from 0 to 9.
   Example: `regex = /\d/` matches any digit in the string.

3. **Any Digit:** `\d` is also used to match any digit from 0 to 9.
   Example: `regex = /\d/` matches any digit in the string.

4. **Any Non-digit character:** `\D` matches any character that is not a digit.
   Example: `regex = /\D/` matches any non-digit character in the string.

5. **Any Character:** `.` matches any character except newline (\n).
   Example: `regex = /./` matches any character in the string.

6. **Period:** `\.` matches a period (dot) character.
   Example: `regex = /\./` matches a period character in the string.

7. **Only a, b, or c:** `[abc]` matches any one character of a, b, or c.
   Example: `regex = /[abc]/` matches any occurrence of a, b, or c in the string.

8. **Not a, b, nor c:** `[^abc]` matches any character that is not a, b, or c.
   Example: `regex = /[^abc]/` matches any character except a, b, or c in the string.

9. **Characters a to z:** `[a-z]` matches any lowercase letter from a to z.
   Example: `regex = /[a-z]/` matches any lowercase letter in the string.

10. **Numbers 0 to 9:** `[0-9]` matches any digit from 0 to 9.
    Example: `regex = /[0-9]/` matches any digit in the string.

11. **Any Alphanumeric character:** `\w` matches any alphanumeric character (letters, digits, or underscore).
    Example: `regex = /\w/` matches any alphanumeric character in the string.

12. **Any Non-alphanumeric character:** `\W` matches any character that is not alphanumeric.
    Example: `regex = /\W/` matches any non-alphanumeric character in the string.

13. **m Repetitions:** `{m}` matches exactly m repetitions of the preceding character or group.
    Example: `regex = /a{3}/` matches 'aaa' in the string.

14. **m to n Repetitions:** `{m,n}` matches from m to n repetitions of the preceding character or group.
    Example: `regex = /\d{2,4}/` matches 2 to 4 digits in the string.

15. **Zero or more repetitions:** `*` matches zero or more repetitions of the preceding character or group.
    Example: `regex = /ab*/` matches 'a', 'ab', 'abb', 'abbb', etc. in the string.

16. **One or more repetitions:** `+` matches one or more repetitions of the preceding character or group.
    Example: `regex = /ab+/` matches 'ab', 'abb', 'abbb', etc. in the string.

17. **Optional character:** `?` matches zero or one occurrence of the preceding character or group.
    Example: `regex = /colou?r/` matches both 'color' and 'colour' in the string.

18. **Any Whitespace:** `\s` matches any whitespace character (space, tab, newline).
    Example: `regex = /\s/` matches any whitespace character in the string.

19. **Any Non-whitespace character:** `\S` matches any character that is not whitespace.
    Example: `regex = /\S/` matches any non-whitespace character in the string.

20. **Starts and ends:** `^` matches the start of a string, `$` matches the end of a string.
    Example: `regex = /^start.*end$/` matches strings that start with 'start' and end with 'end'.

21. **Capture Group:** `( )` is used to capture a group of characters.
    Example: `regex = /(ab)+/` captures and groups occurrences of 'ab' in the string.

22. **Capture Sub-group:** `(?: )` is used to create a non-capturing group.
    Example: `regex = /(?:ab)+/` groups occurrences of 'ab' without capturing them in the string.

23. **Capture all:** `(.*)` captures all characters greedily.
    Example: `regex = /start(.*)end/` captures everything between 'start' and 'end' in the string.

24. **Matches abc or def:** `abc|def` matches either 'abc' or 'def'.
    Example: `regex = /abc|def/` matches 'abc' or 'def' in the string.
