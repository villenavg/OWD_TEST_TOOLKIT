from OWDTestToolkit.global_imports import *
    
class main(GaiaTestCase):
        
    def getTabNumber(self, p_titleContains):
        #
        # Returns the number of the browser tab with a title that contains
        # p_titleContains, or False if it's not found.
        # <br>
        # Assumes we're in the main browser frame.
        #
        try:
            # We may already be in the 'tray' ...
            self.wait_for_element_displayed(*DOM.Browser.tab_tray_screen, timeout=1)
        except:
            # Nope!
            x = self.UTILS.getElement(DOM.Browser.tab_tray_open, "Tab tray open button")
            x.tap()
            
        self.UTILS.waitForElements(DOM.Browser.tab_tray_screen, "Tab screen", True, 2, False)
        
        x = self.UTILS.getElements(DOM.Browser.tab_tray_tab_list, "Tab list")
        boolOK = False
        for i in range(0,len(x)):
            _title = x[i].find_element(*DOM.Browser.tab_tray_tab_item_title)
            _title = _title.text.encode('ascii', 'ignore')
            if p_titleContains.lower() in _title.lower():
                boolOK = i
                break
            
        return boolOK
