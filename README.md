# gpt_query_example

An example how to run an AI query using a llama_index trained model or vanilla GPT.

To use this, you will need to acquire an open AI API key and set up an environment variable. See `src\gpt_query_example\example.py` for details.

Run `example.py`. This trains a model locally, so give it a few seconds. You will be presented with a prompt, from which you can

    * `ask_li("some question")`
    * `ask_gpt("some question")`
    * `ask("some question")`

Trained on Moby Dick, because I like it and it is in the public domain, but this makes for a pretty useless example, because chat gpt already knows enough about Moby Dick to answer questions about it. In fact, GPT may me more reliable than the locally trained llama_index model. This will of course not be the case with more proprietary documents.

If you're using Windows, you will need Visual Studio C++ build tools to compile llama_index. You won't have to do this explicitly, pip will compile it for you.

    * [[https://visualstudio.microsoft.com/visual-cpp-build-tools/]]
    * click `Download Build Tools`
    * run installer
    * select the C++ compiler when running the installer
    * Install "Desktop development with C++"
    * You could *probably* go into "Individual Components" and install "C++ CMake tools for Windows" and "Windows 11 SDK" only, but the entire "Workload" is only 1.75GB and it's not worth the hassle to figure out what you need and what you don't.

## installation

```
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## run

from the virtual environment
```
python src\gpt_query_example\example.py
```

## examples

### (Pdb) ask("What sentence in Moby Dick would most please a Brazilian nanny?")
The sentence in Moby Dick that would most please a Brazilian nanny is: "The people of his island of Rokovoko, it seems, at their wedding feasts express the fragrant water of young cocoanuts into a large stained calabash like a punchbowl; and this punchbowl always forms the great central ornament on the braided mat where the feast is held."

----

This sentence from Moby Dick may please a Brazilian nanny because it mentions the use of young coconuts, which are a common and beloved ingredient in Brazilian cuisine. Coconuts are widely used in traditional Brazilian dishes and beverages, so a Brazilian nanny might appreciate the reference to this familiar and culturally significant ingredient in the novel. Additionally, the mention of a wedding feast and ornate decorations such as a punchbowl could be seen as a celebration of special occasions and cultural traditions, which could resonate with someone from a country with rich and vibrant cultural celebrations like Brazil.

### (Pdb) ask("What is the most confusing sentence in Moby Dick?")

The most confusing sentence in Moby Dick is the one that describes the vast pulpy mass floating on the water, with innumerable long arms radiating from its center, curling and twisting like a nest of anacondas, appearing as an unearthly, formless, chance-like apparition of life.

----

The sentence described above is from Chapter 60 of Moby Dick, titled "The Line." In this chapter, the crew of the Pequod encounters a mysterious sight on the ocean, which turns out to be a giant squid or octopus. The description of this sea creature is intentionally vague and confusing, adding to the sense of unease and mystery surrounding the encounter. This passage is emblematic of Herman Melville's rich and complex writing style, which often blends elements of naturalistic description with philosophical musings and symbolism. Overall, the sentence captures the sense of wonder, awe, and terror that mariners would have felt when encountering such a magnificent and otherworldly creature on the open sea.
