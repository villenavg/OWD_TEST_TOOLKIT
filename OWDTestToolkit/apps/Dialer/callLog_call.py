from OWDTestToolkit.global_imports import *
	
class main(GaiaTestCase):

    def callLog_call(self, p_num):
        #
        # Calls a number from the call log.
        #
		try:
			self.wait_for_element_displayed(*DOM.Dialer.call_log_filter, timeout=1)
		except:
			self.openCallLog()

		x = self.UTILS.getElement( ("xpath", DOM.Dialer.call_log_number_xpath % p_num),
								   "The call log for number %s" % p_num)
		x.tap()
		
		x = self.UTILS.getElement( DOM.Dialer.call_log_numtap_call, "Call button")
		x.tap()
		time.sleep(1)
		
		self.UTILS.switchToFrame(*DOM.Dialer.frame_locator_calling)
		
		self.UTILS.waitForElements( ("xpath", DOM.Dialer.outgoing_call_numberXP % p_num),
									"Outgoing call found with number matching %s" % p_num)