from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class QControlMainWindow(VCPMainWindow):
    """Main window class for the QControl VCP."""
    def __init__(self, *args, **kwargs):
        super(QControlMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("LinuxCNC - QControl")
