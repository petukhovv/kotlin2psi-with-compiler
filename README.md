# kotlin-source2ast

Program for parsing Kotlin source code.
Program output — Kotlin AST.

## Program arguments

- **--compiler_path (c-)**: path to custom version of Kotlin compiler (see [kotlin-academic](https://github.com/PetukhovVictor/kotlin-academic/tree/vp/ast_printing_text) repo)
- **--input (i-)**: folder with kotlin source codes (for example, obtained by [github-kotlin-code-collector](https://github.com/PetukhovVictor/github-kotlin-code-collector))
- **--output (o-)**: output folder with AST (in JSON format)

Example of use:
```
python3 main.py -c /Users/me/IdeaProjects/kotlin-academic/dist/kotlinc/bin/kotlinc -i ./code -o ./ast
```
