from scripts import db_creation, data_extraction

def main():
    db_creation.create_raw_data_table()
    data_extraction.save()

if __name__ == "__main__":
    main()
