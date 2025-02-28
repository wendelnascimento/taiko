#Intercept Api

## With simple response body
* Respond to "http://localhost:3001/dropdown" with "mocked dropdown page"
* Navigate to "http://localhost:3001/"
* Click "Dropdown"
* Assert text "mocked dropdown page" exists on the page.

## With array as a response body
* Respond to "http://localhost:3001/dropdown" with json "[\"mocked\",\"dropdown\",\"page\"]"
* Navigate to "http://localhost:3001/"
* Click "Dropdown"
* Assert text "[\"mocked\",\"dropdown\",\"page\"]" exists on the page.

## With object as a response body
* Respond to "http://localhost:3001/dropdown" with json "{\"name\":\"Jon\",\"age\":\"20\"}"
* Navigate to "http://localhost:3001/"
* Click "Dropdown"
* Assert text "{\"name\":\"Jon\",\"age\":\"20\"}" exists on the page.

## With regex in URL
* Respond to "https://localhost/employees/(\\d+)/address" with json "{\"city\":\"City1\",\"State\":\"State1\"}"
* Navigate to "https://localhost/employees/1/address"
* Assert text "{\"city\":\"City1\",\"State\":\"State1\"}" exists on the page.

* Navigate to "https://localhost/employees/2/address"
* Assert text "{\"city\":\"City1\",\"State\":\"State1\"}" exists on the page.

## Override a response for a URL
* Respond to "https://localhost/employees/(\\d+)/address" with json "{\"city\":\"City1\",\"State\":\"State1\"}"
* Navigate to "https://localhost/employees/1/address"
* Assert text "{\"city\":\"City1\",\"State\":\"State1\"}" exists on the page.

* Respond to "https://localhost/employees/1/address" with json "{\"city\":\"CityOne\",\"State\":\"StateOne\"}"
* Navigate to "https://localhost/employees/1/address"
* Assert text "{\"city\":\"CityOne\",\"State\":\"StateOne\"}" exists on the page.

* Navigate to "https://localhost/employees/2/address"
* Assert text "{\"city\":\"City1\",\"State\":\"State1\"}" exists on the page.
