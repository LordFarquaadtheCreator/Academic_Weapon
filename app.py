import chroma

def main():
    client = get_client()
    academic_db = create_collection(client)
    # academic_db = get_collection(client)

    None


if __name__ == "main":
    main()
    print("this is the main function")