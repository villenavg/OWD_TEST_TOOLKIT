from OWDTestToolkit.global_imports import *

class main(GaiaTestCase):

    def waitForNotElements(self, p_element, p_msg, p_displayed=True, p_timeout=False, p_stop=True):        
        #
        # Waits for an element to be displayed and captures the error if not.<br>
        # p_timeout defaults to _DEFAULT_ELEMENT_TIMEOUT (set in the utils.py file).
        #
        p_timeout = self._DEFAULT_ELEMENT_TIMEOUT if not p_timeout else p_timeout
        
        boolOK = True
        try:
            if p_displayed:
                p_msg = "<b>%s</b> no longer displayed within %s seconds.|%s" % (p_msg, str(p_timeout), str(p_element))
                self.wait_for_element_not_displayed(*p_element, timeout=p_timeout)
            else:
                p_msg = "<b>%s</b> no longer present within %s seconds.|%s" % (p_msg, str(p_timeout), str(p_element))
                self.wait_for_element_not_present(*p_element, timeout=p_timeout)
        except:
            boolOK = False
            
        self.TEST(boolOK, p_msg, p_stop)
        
        return boolOK
    
