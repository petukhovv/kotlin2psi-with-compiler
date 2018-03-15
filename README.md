# kotlin-source2ast

Program for parsing Kotlin source code.
Program output — Kotlin CST (concrete syntax tree).

Program use custom version of Kotlin compiler (see [kotlin-academic](https://github.com/PetukhovVictor/kotlin-academic/tree/vp/ast_printing_text) repo).

Kotlin compiler located in `./lib/kotlinc/`.

## Program arguments

- `--input`, `-i`: folder with kotlin source codes (for example, obtained by [github-kotlin-code-collector](https://github.com/PetukhovVictor/github-kotlin-code-collector));
- `--output`, `-o`: output folder with CST (in JSON format);
- `--with_code`: if specified, then in the output CST, the nodes will have a chars property with the corresponding source code.

Example of use:
```
python3 main.py -i ./code -o ./ast
```

## Output

Program output is Kotlin CST in JSON format.

Example:
```
[
   {
      "type":"FILE",
      "chars":"package com.cognifide.gradle.aem\n\nimport groovy.lang.Closure\nimport org.gradle.api.Project\nimport org.gradle.util.ConfigureUtil\n\n/**\n * Gradle extensions cannot be serialized so that config need to be wrapped.\n */\nopen class AemExtension(project: Project) {\n\n    companion object {\n        val NAME = \"aem\"\n    }\n\n    val config = AemConfig(project)\n\n    fun config(closure: Closure<*>) {\n        ConfigureUtil.configure(closure, config)\n    }\n\n}",
      "children":[
         {
            "type":"PACKAGE_DIRECTIVE",
            "chars":"package com.cognifide.gradle.aem",
            "children":[
               {
                  "type":"package",
                  "chars":"package"
               },
               {
                  "type":"WHITE_SPACE",
                  "chars":" "
               }
            ]
         },
         {
            "type":"WHITE_SPACE",
            "chars":"\n\n"
         },
         {
            "type":"IMPORT_LIST",
            "chars":"import groovy.lang.Closure\nimport org.gradle.api.Project\nimport org.gradle.util.ConfigureUtil",
            "children":[
               {
                  "type":"IMPORT_DIRECTIVE",
                  "chars":"import groovy.lang.Closure",
                  "children":[
                     {
                        "type":"import",
                        "chars":"import"
                     },
                     {
                        "type":"WHITE_SPACE",
                        "chars":" "
                     },
                     {
                        "type":"DOT_QUALIFIED_EXPRESSION",
                        "chars":"groovy.lang.Closure",
                        "children":[
                           {
                              "type":"DOT_QUALIFIED_EXPRESSION",
                              "chars":"groovy.lang",
                              "children":[
                                 {
                                    "type":"REFERENCE_EXPRESSION",
                                    "chars":"groovy",
                                    "children":[
                                       {
                                          "type":"IDENTIFIER",
                                          "chars":"groovy"
                                       }
                                    ]
                                 },
                                 {
                                    "type":"DOT",
                                    "chars":"."
                                 },
                                 {
                                    "type":"REFERENCE_EXPRESSION",
                                    "chars":"lang",
                                    "children":[
                                       {
                                          "type":"IDENTIFIER",
                                          "chars":"lang"
                                       }
                                    ]
                                 }
                              ]
                           },
                           {
                              "type":"DOT",
                              "chars":"."
                           },
                           {
                              "type":"REFERENCE_EXPRESSION",
                              "chars":"Closure",
                              "children":[
                                 {
                                    "type":"IDENTIFIER",
                                    "chars":"Closure"
                                 }
                              ]
                           }
                        ]
                     }
                  ]
               },
               {
                  "type":"WHITE_SPACE",
                  "chars":"\n"
               },
               {
                  "type":"WHITE_SPACE",
                  "chars":"\n"
               }
            ]
         },
         {
            "type":"WHITE_SPACE",
            "chars":"\n\n"
         },
         {
            "type":"CLASS",
            "chars":"/**\n * Gradle extensions cannot be serialized so that config need to be wrapped.\n */\nopen class AemExtension(project: Project) {\n\n    companion object {\n        val NAME = \"aem\"\n    }\n\n    val config = AemConfig(project)\n\n    fun config(closure: Closure<*>) {\n        ConfigureUtil.configure(closure, config)\n    }\n\n}",
            "children":[
               {
                  "type":"KDoc",
                  "chars":"/**\n * Gradle extensions cannot be serialized so that config need to be wrapped.\n */"
               }
            ]
         }
      ]
   }
]
```
