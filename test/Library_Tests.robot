*** Settings ***
Library   ../src/AutoNexus/APILibrary.py
Library   ../src/AutoNexus/WebLibrary.py
Library   Zoomba.GUILibrary
Library   Zoomba.APILibrary
Library   JSONLibrary

*** Variables ***
${HEADLESS}                ${False}
${INCOGNITO}               ${False}
${EXAMPLE_PATH}            ${EXECDIR}${/}test${/}Example${/}example.json
${MAPPING_PATH}            ${EXECDIR}${/}test${/}Mapping${/}mapping.json
${DEFAULTS_PATH}           ${EXECDIR}${/}test${/}Defaults${/}defaults.json
${REPSONSE_PATH}           ${EXECDIR}${/}test${/}Mapping${/}responsemapping.json
&{HEADER}                  Accept=application/json  Content-type=application/json

*** Keywords ***
Launch Browser
    ${webdriver_path}  Install Webdriver    Chrome
    ${chrome_options}  Create Chrome Options  ${HEADLESS}  ${INCOGNITO}
    Create Webdriver    Chrome  chrome_options=${chrome_options}
    ...   executable_path=${webdriver_path}

*** Test Cases ***
WebdriverManager Test
    Launch Browser
    Go To    https://google.com

API Request Payload Test
    ${payload}  Build Request Data    ${EXAMPLE_PATH}    ${MAPPING_PATH}   ${DEFAULTS_PATH}
    Log  ${payload}
    &{response}  Call Post Request  endpoint=https://demoqa.com/Account/v1/GenerateToken  data=${payload}
    ...  headers=${HEADER}
    ${token}  Get Value From Response    ${response}    ${REPSONSE_PATH}    token
    Log  ${token}
