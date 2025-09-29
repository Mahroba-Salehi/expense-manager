from model.repository.database_manager import create_database
from view.main_view import menu

def main():
    create_database()

    menu()

if __name__ == "__main__":
    main()

