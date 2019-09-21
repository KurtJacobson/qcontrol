from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# from qtpyvcp.actions import action

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class QControlMainWindow(VCPMainWindow):
    """Main window class for the QControl VCP."""
    def __init__(self, *args, **kwargs):
        super(QControlMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("LinuxCNC - QControl")

    # @action('window.maximize')
    # def maximize(self):
    #     self.showMaximized()

    def on_notificationButton_pressed(self):
        self.notificationButton.setText("")
        self.notificationButton.setStyleSheet("background-color: ")

