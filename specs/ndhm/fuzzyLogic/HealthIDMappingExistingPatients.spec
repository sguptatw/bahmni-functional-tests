# HealthID Mapping with existing patients Fuzzy Logic
|mobileNumber|
|+91-9876543210|

## Should be able to map NDHM Record with only first name
Tags:ndhm
* knownIssue
* Login to Bahmni location "General Ward" as a receptionist
* Open registration module
* Create a new patient, if patient does not exist with firstName "Soumya" middleName "Swaroop" lastName "Gupta", gender "F" mobileNumber <mobileNumber> age "30"
* Should fetch record with firstName "Somya" middleName "" lastName "G" gender "F" age "32" and mobileNumber "1234567890"
* Should display Bahmni record with firstName "Soumya" lastName "Gupta" gender "F" age "30" with mobile number <mobileNumber> 
* Should display NDHM record with firstName "Somya" middleName "" lastName "G" gender "F" age "32" with mobile number "1234567890"
## Should be able to map NDHM Record with first name, middle name and last name
Tags: ndhm
* Login to Bahmni location "General Ward" as a receptionist
* Open registration module
* Create a new patient, if patient does not exist with firstName "Soumya" middleName "Swaroop" lastName "Gupta", gender "F" mobileNumber <mobileNumber> age "30"
* Should fetch record with firstName "Somya" middleName "" lastName "G" gender "F" age "32" and mobileNumber "1234567890"
* Should display Bahmni record with firstName "Soumya" lastName "Gupta" gender "F" age "30" with mobile number <mobileNumber>
* Should display NDHM record with firstName "Somya" middleName "" lastName "G" gender "F" age "32" with mobile number "1234567890"

## Should be able to map NDHM Record with first and last name
Tags: ndhm
* Login to Bahmni location "General Ward" as a receptionist
* Open registration module
* Create a new patient, if patient does not exist with firstName "Soumya" middleName "Swaroop" lastName "Gupta", gender "F" mobileNumber <mobileNumber> age "30"
* Should fetch record with firstName "Somya" middleName "" lastName "G" gender "F" age "32" and mobileNumber "1234567890"
* Should display Bahmni record with firstName "Soumya" lastName "Gupta" gender "F" age "30" with mobile number <mobileNumber>
* Should display NDHM record with firstName "Somya" middleName "" lastName "G" gender "F" age "32" with mobile number "1234567890"

## Should be able to map NDHM Record with name spelling, date of birth and mobile number mismatch
Tags:ndhm
* Login to Bahmni location "General Ward" as a receptionist
* Open registration module
* Create a new patient, if patient does not exist with firstName "Soumya" middleName "Swaroop" lastName "Gupta", gender "F" mobileNumber <mobileNumber> age "30"
* Should fetch record with firstName "Sowmya" middleName "" lastName "G" gender "F" age "28" and mobileNumber "1234567890"
* Should display Bahmni record with firstName "Soumya" lastName "Gupta" gender "F" age "30" with mobile number <mobileNumber>
* Should display NDHM record with firstName "Sowmya" middleName "" lastName "G" gender "F" age "28" with mobile number "1234567890"

## Should be able to map NDHM Record with first name fuzzy match
Tags:ndhm
* Login to Bahmni location "General Ward" as a receptionist
* Open registration module
* Create a new patient, if patient does not exist with firstName "Soumya" middleName "Swaroop" lastName "Gupta", gender "F" mobileNumber <mobileNumber> age "30"
* Should fetch record with firstName "Somya" middleName "" lastName "Guptha" gender "F" age "28" and mobileNumber "1234567890"
* Should display Bahmni record with firstName "Soumya" lastName "Gupta" gender "F" age "30" with mobile number <mobileNumber>
* Should display NDHM record with firstName "Somya" middleName "" lastName "Guptha" gender "F" age "28" with mobile number "1234567890"