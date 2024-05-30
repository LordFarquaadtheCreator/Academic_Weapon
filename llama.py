from llama_ind.app import main
from llama_ind.get_db import get_db_index

if __name__ == "__main__":
    INDEX = get_db_index()
    main(INDEX, query="what are the main subjects of calculus?")
