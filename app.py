from model.repository.database_manager import create_database
from view.main_view import MainView
from tools.logging import Logger

Logger.info("App Started")

# Create database if not exists
create_database()

# Start GUI
ui = MainView()
ui.run()
