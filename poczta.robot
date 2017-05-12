*** Settings ***
Library  Selenium2Library

*** Variables ***
${SERVER}  localhost
${BROWSER}  Firefox
${username}  ******
${password}  *******
${LOGIN URL}  http://www.gmail.com

*** Test Cases ***
Valid Login
	Open Login Page
	Input Username
	Submit Credentials
	Enter Password
	Submit Credentials2
	Welcome Page Should Be Open
	Create Email
	Logout
	Close Browser

*** Keywords ***
Open Login Page
	Open Browser  ${LOGIN URL}  ${BROWSER}
	Maximize Browser Window
	Login Page Should Be Open
	
Login Page Should Be Open
	Title Should Be  Gmail

Input Username
	Input Text  Email  ${username}

Enter Password
	Wait Until Page Contains Element  id=Passwd
	Input Password   Passwd      ${password}

Submit Credentials
	Click Button  Next

Submit Credentials2
	Click Button  Sign in

Create email
	Wait Until Page Contains Element   xpath=//div[@class='T-I J-J5-Ji T-I-KE L3']
	Click Element  xpath=//div[@class='T-I J-J5-Ji T-I-KE L3']
	Input Text  to  dominique90@gmail.com  
	Input Text  subjectbox  Test selenium
	Input Text  xpath=//div[@class='Am Al editable LW-avf']   Witam, Automat 
	Click Element  xpath=//div[@class='T-I J-J5-Ji aoO T-I-atl L3']

Logout
	Click Element  xpath=//span[@class='gb_9a gbii']
	Click Element  gb_71  
	
Welcome Page Should Be Open
	Title Should Be   Gmail
