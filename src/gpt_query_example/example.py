"""Train an AI with a folder of local text files and then ask it questions.

For this to work, you will need to get an api key and define an environment variable,
OPENAI_API_KEY, with your key as the value.

Trained on Moby Dick. To change this, find a new data source (a folder of *.txt
files) and change `_DATA_FOLDER` (below) to something else.

:author: Shay Hill
:created: 2023-05-18
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import openai
from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader
from paragraphs import par

if TYPE_CHECKING:
    import os

    from llama_index.core.base.base_query_engine import BaseQueryEngine

# a metaparameter for the location of the data (txt files) used to train the
# llama_index query engine
_DATA_FOLDER = "moby_dick"

# alter this value to fit the open api key you have set up as an environment variable
# OPEN_API_KEY
_GPT_MODEL = "gpt-3.5-turbo"


def _build_query_engine(data_folder: str | os.PathLike[str]) -> BaseQueryEngine:
    """Build and train a query engine with contents of the data_folder.

    :param data_folder: folder containing documents to train the query engine
    :return: a trained query engine
    """
    documents = SimpleDirectoryReader(str(data_folder)).load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    return index.as_query_engine()  # type: ignore


_llama_index_query_engine = _build_query_engine(_DATA_FOLDER)


def ask_li(question: str) -> str:
    """Ask the locally trained llama index querry engine."""
    return str(_llama_index_query_engine.query(question))


def ask_gpt(question: str) -> str | None:
    """Ask chat gpt."""
    client = openai.OpenAI()
    completion = client.chat.completions.create(
        model=_GPT_MODEL, messages=[{"role": "user", "content": question}]
    )
    return completion.choices[0].message.content


def ask(question: str):
    """Get one answer from the locally trained querry engine. Suplement with GPT."""
    li_response = ask_li(question)

    question_for_gpt = par(
        f"""I asked the question "{question}" and received the answer "{li_response}"
        specifically in regards to Moby Dick. Provide additional useful information
        or context."""
    )
    gpt_response = ask_gpt(question_for_gpt)

    print(li_response, "----", gpt_response, "", sep="\n\n")


breakpoint()
