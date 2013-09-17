here_check              = ('id', 'shortcuts-items')
groups                  = ('xpath', "//*[@id='shortcuts-items']//li")
add_group_button        = ("xpath", "//li[@class='shortcut add']")
remove_group_icon       = ("xpath", "./span[@class='remove']")
loading_groups_message  = ("id", "shortcuts-customize-loading")
apps                    = ('xpath', "//ul[@id='evmeAppsList']/li[contains(@class,'cloud')]")
back_btn                = ('id', 'button-clear')
add_app_to_homescreen   = ('id', 'modal-dialog-confirm-ok')
connection_warning_msg  = ("class name", "connection-message")
search_field            = ("id", "search-q")
start_eme_icon          = ("id", "evme-activation-icon")
# search_suggestions      = ('css selector', '#helper ul li[data-index]')
search_suggestions      = ("xpath", "//div[@id='helper-header']//span[@class='query']")
searching_spinner       = ("class name", "loading-apps")
search_result_icon_xpath= "//li[@data-name='%s']"
search_result_area      = ("id", "evmeApps")
app_installed_banner    = ("id","evmeBanner")

launched_activity_bar   = ("id","wrapper-activity-indicator")   # (in the top level frame)
launched_button_bar     = ("id", "buttonbar")                   # (in the top level frame)
