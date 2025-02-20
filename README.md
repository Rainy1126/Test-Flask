# Test-Flask
implemented login and giving user JWT token
JWT token verification is in decorators.py

in short:
every login will create new session
user will get jwt token when login
next time no need login if jwt token is valid
if invalid jwt then given message "please log in again" -> could be improved to just redirect to login page
when jwt authentication returns invalid, terminate session associated with the jwt token
