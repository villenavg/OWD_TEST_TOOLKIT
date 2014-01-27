from OWDTestToolkit.global_imports import *
    
class main(GaiaTestCase):

    def waitForDownloadNotifier(self, name, p_timeout=40):
        #
        # Get the element of the new SMS from the status bar notification.
        # returns a boolean (True if found)
        #
        self.UTILS.logResult("info", "Waiting for statusbar notification of download of " + name + " ...")

        #
        # Create the string to wait for.
        #
        x=( DOM.DM.statusbar_new_notif[0],
            DOM.DM.statusbar_new_notif[1] % name)
        
        #
        # Wait for the notification to be present for this number 
        # in the popup messages (this way we make sure it's coming from our number,
        # as opposed to just containing our number in the notification).
        #
        time.sleep(5)
        x = self.UTILS.waitForStatusBarNew(x, p_displayed=False, p_timeOut=p_timeout)

        self.UTILS.logResult(x, "Download notifier from " + name + " found in status bar.")
        return x
    
