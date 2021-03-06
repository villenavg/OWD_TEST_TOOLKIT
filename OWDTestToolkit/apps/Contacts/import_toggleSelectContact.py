from OWDTestToolkit.global_imports import *

class main(GaiaTestCase):

    def import_toggleSelectContact(self, p_num):
        #
        # Toggles select / de-select a gmail contact( marionette doesn't work here yet, so use JS).
        # p_num is the actualt contact number (1 -> x).
        #
        el_num = p_num - 1

        x = self.UTILS.getElements(DOM.Contacts.import_conts_list, "Contact list")
        cont_name = x[el_num].get_attribute("data-search")
        
        self.UTILS.logResult("info", "Selecting contact %s ('%s') ..." % (p_num, cont_name))
        
        self.marionette.execute_script("document.getElementsByClassName('block-item')[%s].click()" % el_num)
        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot of current position", x)

