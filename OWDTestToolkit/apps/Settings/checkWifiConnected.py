from OWDTestToolkit.global_imports import *
	
class main(GaiaTestCase):

    def checkWifiConnected(self, p_name, p_timeOut=30):
        #
        # Verify the expected network is listed as connected in 'available networks'.
        #

        # 
        # Wait a little time to be sure the networks are all listed.
        #
        time.sleep(5)
        
        #
        # Compare the available networks - if one's connected then check it's the
        # one we expect (starts at array 3).
        #
        x = self.UTILS.getElements(DOM.Settings.wifi_available_networks, "Available networks list", False, p_timeOut, False)
        for i in range(3, len(x)):
            connStatus = self.marionette.find_element('xpath', DOM.Settings.wifi_available_status % i)
            connName   = self.marionette.find_element('xpath', DOM.Settings.wifi_available_name   % i)
            
            if ("connected" in connStatus.text.lower()) and (p_name == connName.text):
                return True
               
        #
        # If we get to here, we didn't find the network we were looking for.
        #
        return False
        
