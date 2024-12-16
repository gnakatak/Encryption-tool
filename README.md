# Encryption Tool

This program is based on a simple character substitution cipher. The encryption process works by replacing each letter or number in the input with a corresponding character from a predefined substitution table. There are two types of ciphers available: **Simple Cipher** and **Complex Cipher**.

## Ciphers

### 1. Simple Cipher

In the **Simple Cipher**, a fixed substitution table is used, where each letter or number is mapped to a specific symbol or character. The substitution follows a direct and immutable pattern, for example:
- The letter 'a' is always replaced by '1'
- The letter 'b' is always replaced by '2'
- And so on...

This makes it easier to break the cipher using frequency analysis, as the substitution pattern does not change. The **Simple Cipher** is not very secure on its own but can be useful in some basic encryption scenarios.

### 2. Complex Cipher

The **Complex Cipher** introduces variability by altering the substitution pattern. The character substitution may depend on certain criteria, such as the position of the letter or a secret key. For example:
- The letter 'a' could be replaced by '1' in one part of the text and by 'r' in another.
- The letter 'b' might be replaced by different symbols depending on the context.

This makes the **Complex Cipher** more secure, as the substitution pattern is not fixed, making it harder to break without knowledge of the key or cipher logic.

## Substitution Tables

The program uses two substitution tables: one for letters and another for numbers. Each character has multiple possible substitutions.

### Letter Substitution Table
| Letter | Substitutions | Alternatives |
|--------|---------------|--------------|
| a      | 1             | r            |
| b      | 2             | s            |
| c      | 3             | t            |
| d      | 4             | u            |
| e      | 5             | v            |
| f      | 6             | w            |
| g      | 7             | x            |
| h      | 8             | y            |
| i      | 9             | z            |
| j      | a             | !            |
| k      | b             | @            |
| l      | c             | #            |
| m      | d             | $            |
| n      | e             | %            |
| o      | f             | ^            |
| p      | g             | &            |
| q      | h             | *            |
| r      | i             | (            |
| s      | j             | )            |
| t      | k             | -            |
| u      | l             | _            |
| v      | m             | =            |
| w      | n             | +            |
| x      | o             | <            |
| y      | p             | >            |
| z      | q             | ~            |
| ' '    | ' '           | ' '          |

### Number Substitution Table
| Number | Substitutions | Alternatives |
|--------|---------------|--------------|
| 1      | a             | t            |
| 2      | b             | s            |
| 3      | c             | r            |
| 4      | d             | q            |
| 5      | e             | p            |
| 6      | f             | o            |
| 7      | g             | n            |
| 8      | h             | m            |
| 9      | i             | l            |
| 0      | j             | k            |
| ' '    | ' '           | ' '          |
| ,      | ,             | ,            |
| .      | .             | .            |

Each character in the text is replaced according to these tables, creating either a **Simple Cipher** or **Complex Cipher**, depending on the user's choice.


