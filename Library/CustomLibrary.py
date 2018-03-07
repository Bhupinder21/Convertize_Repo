from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
import time

class CustomLibrary:

    def __init__(self):
        self.action_chains = None

    @property
    def s2l(self):
        return BuiltIn().get_library_instance('ExtendedSelenium2Library')

    def __lazy_init_action_chains(self):
        if self.action_chains == None:
            self.action_chains = ActionChains(self.s2l._current_browser())
        return self.action_chains

    def chain_click_and_hold(self, source):
        """ Click and hold the element identified by the 'source' locator
        """
        element = self.s2l._element_find(source,True,True)
        self.__lazy_init_action_chains().click_and_hold(element)


    def chain_move_to_element(self, target):
        element = self.s2l._element_find(target,True,True)
        self.__lazy_init_action_chains().move_to_element(element)
        time.sleep(5)

    def chains_perform_now(self):
        if self.action_chains != None:
            self.action_chains.perform()
            self.action_chains = None

    def chain_release(self, target):
        """ Move the mouse to the element identified by the 'target' locator
        Release the mouse.
        """
        element = self.s2l._element_find(target,True,True)
        self.__lazy_init_action_chains().release(element)
