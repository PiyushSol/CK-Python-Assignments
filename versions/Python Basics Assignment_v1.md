`Q1. Write a Python program to perform the following:`
`● Validate a given public IP address to check if it follows the correct format (IPv4).`
`● Validate a given email address to check if it’s a valid Gmail address, considering:`
`○ It should contain "@gmail.com".`
`○ The username before "@gmail.com" should contain only lowercase letters , numbers and permitted`
`symbols.`
`○ Provide informative error messages for invalid IP or email.`

**Ans:**
With Regex Validation of IPv4 address :

![[Pasted image 20260312144747.png]]

![[Pasted image 20260312144850.png]]
Without Regex Validation Ipv4 address :
![[Pasted image 20260312145059.png]]
![[Pasted image 20260312145135.png]]

With Regex Validation of Gmail Address:
![[Pasted image 20260312145426.png]]

![[Pasted image 20260312145445.png]]

Without Regex Validation of Gmail Address:
![[Pasted image 20260312145728.png]]

![[Pasted image 20260312145705.png]]

`Q2. Write a Python program that generates a password with the following conditions:`
`● At least one uppercase letter.`
`● At least one lowercase letter.`
`● At least two numbers.`
`● At least one special character (e.g., !@#$%&*).`
`● The password should be exactly 16 characters long.`
`● The password should contain no repeating characters.`
`● The password should have a random order each time.`

**Ans:**

`import random`

`import string`

`import re`

  
`uppercase = string.ascii_uppercase`

`lowercase = string.ascii_lowercase`

`numbers = string.digits`

`special = "!@#$%&*"`

`def generate_password():`

`password_chars = []`

`password_chars.append(random.choice(uppercase))`

`password_chars.append(random.choice(lowercase))`

`password_chars.append(random.choice(numbers))`

`password_chars.append(random.choice(numbers))`

`password_chars.append(random.choice(special))`  

`all_chars = uppercase + lowercase + numbers + special`

`while len(password_chars) < 16:`

`char = random.choice(all_chars)`

`if char not in password_chars:`

`password_chars.append(char)`

`random.shuffle(password_chars)`

`return "".join(password_chars)`

`def validate_password_regex(password):`

`pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=(?:.*\d){2,})(?=.*[!@#$%&*])[A-Za-z\d!@#$%&*]{16}$'`

`if not re.match(pattern, password):`

`print("Regex Validation: Password format requirements not satisfied")`

`return`

`if len(set(password)) != len(password):`

`print("Regex Validation: Password contains repeating characters")`

`return`

`print("Regex Validation: Password is valid")`

`def validate_password_no_regex(password):`

`if len(password) != 16:`
`print("Manual Validation: Password must be 16 characters")`

`return`

`if len(set(password)) != 16:`
`print("Manual Validation: Password contains repeating characters")`

`return`

`upper = lower = digits = special_count = 0`

`for ch in password:`
`if ch.isupper():`
`upper += 1`
`elif ch.islower():`
`lower += 1`

`elif ch.isdigit():`
`digits += 1`

`elif ch in "!@#$%&*":`
`special_count += 1`

`else:`
`print("Manual Validation: Invalid character found")`
`return`

`if upper < 1:`
`print("Manual Validation: Must contain at least one uppercase letter")`
`return`

`if lower < 1:`
`print("Manual Validation: Must contain at least one lowercase letter")`
`return`

`if digits < 2:`
`print("Manual Validation: Must contain at least two numbers")`
`return`

`if special_count < 1:`
`print("Manual Validation: Must contain at least one special character")`
`return`

`print("Manual Validation: Password is valid")`
`password = generate_password()`
`print("Generated Password:", password)`
`print()`
`validate_password_regex(password)`
`validate_password_no_regex(password)`

![[Pasted image 20260312154250.png]]


`Q3. Uptime Monitoring and Alert System`
`Write a Python script that checks the uptime of provided URLs and notifies the user if any of the URLs return`
`4xx or 5xx HTTP status codes (indicating client or server errors). For demonstration purposes, you can use`
`the following URLs as inputs:`
`● 4xx (Client Error):`
`○ http://www.example.com/nonexistentpage or`
`○ http://httpstat.us/404`
`● 5xx (Server Error):`
`○ http://httpstat.us/500`
`● 200 (Successful Response):`
`○ https://www.google.com/`
`Requirements:`
1. `URL Check: The script should check the provided URLs and get their HTTP status codes.`
2. `Handle Multiple URLs: The script should be able to handle multiple URLs at once, checking each`
`one.`
3. `Error Detection: If the status code of any URL is either 4xx or 5xx, the program should:`
`○ Notify the user via a print message.`
`○ Alternatively, you can implement more advanced logging methods, (log in any log file).`
4. `Loop and Monitor: You should set up a simple loop that continuously monitors the URLs for a`
`certain interval (e.g., every 10 seconds) to simulate a basic uptime monitoring system.`
5. `Status Message: For each URL, the script should output the URL and its current HTTP status`
`code (e.g., 200 OK, 404 Not Found).`
`Bonus (Optional):`
`● Implement an exponential backoff in case of multiple consecutive errors (e.g., retry after`
`increasing intervals).`
`● Add logging functionality to save the status check results to a log file.`

**Ans:**
![[Pasted image 20260312161354.png]]

![[Pasted image 20260312161421.png]]
![[Pasted image 20260312161448.png]]
![[Pasted image 20260312161514.png]]
`Q4. Automating Software Package Updates`

`Write a Python program to automate the checking and updating of installed software packages on`
`a Linux server. The script should:`
`● Function to check for available updates using the system’s package manager (e.g., apt, yum).`
`and list all available updates.`
`● Ask user to Update all at once or provide any specific package name to update (take package`
`index number for ease)`
`● Install the available updates based on user input.`
`● If any updates fail to install, log the error and send an alert (e.g., console log).`
`● Optionally, schedule the script to run at a certain cron.`

**Ans:**

![[Pasted image 20260312170729.png]]
![[Pasted image 20260312170751.png]]
![[Pasted image 20260312170816.png]]

![[Pasted image 20260312171025.png]]

![[Pasted image 20260312171039.png]]

![[Pasted image 20260312171112.png]]

`Q5. Duplicate File Finder and Cleaner`
`Write a Python script to find duplicate files within a specified directory and its subdirectories. The`
`script should:`
`● Scan the directory for all files and calculate a checksum (e.g., sha256sum) for each file.`
`● Identify and list duplicate files by comparing their checksums.`

`● Optionally, give the user the option to delete or move duplicate files.`
`Bonus:`
`● Allow the user to specify the minimum file size for duplication detection (e.g., only`
`consider files larger than 1MB).`
`● Create a report listing the duplicate files and their checksums`.

**Ans:**

![[Pasted image 20260312175447.png]]

![[Pasted image 20260312175459.png]]

![[Pasted image 20260312175516.png]]


![[Pasted image 20260312175417.png]]


![[Pasted image 20260312175602.png]]

`Q6.CSV to Table Visualizer`

`Write a Python script which reads a csv file and Visualizes a table with proper indentations and`
`borders. (make sure to don’t use any table making module or package)`
`Example : CSV file like this`
`Name,Age,Department`
`Alice,30,HR`
`Bob,25,Engineering`
`Charlie,35,Marketing`
`Diana,28,Sales`

**Ans:**

![[Pasted image 20260312210014.png]]

![[Pasted image 20260312210031.png]]


![[Pasted image 20260312205943.png]]


`Q7. EC2 Recommendation`

`Python script that provides EC2 instance recommendations based on a given instance's type, size, and`
`CPU utilization. The script will help in recommending appropriate EC2 instances for optimizing`
`performance and costs based on the utilization metrics.`
`Input:`
`● Current EC2 Instance: A string representing the instance type and size (e.g., t2.nano,`
`t3.medium).`
`● CPU Utilization: A percentage value representing the current CPU utilization (e.g., 40%).`

`The output will be a recommendation for a new EC2 instance based on the following logic:`
`● Underutilized: If the CPU utilization is less than 20%, recommend a smaller instance.`
`● Optimized: If the CPU utilization is between 20% and 80%, recommend the same instance size`
`but suggest the latest generation instance type.`
`● Overutilized: If the CPU utilization is greater than 80%, recommend a larger instance.`
`Instance Size Comparison: The EC2 instance sizes follow a specific hierarchy:`
`nano > micro > small > medium > large > xlarge > 2xlarge > 4xlarge > 8xlarge >`
`16xlarge > 32xlarge..`
`● If the CPU is underutilized (CPU < 20%), the script should recommend a smaller instance by one`
`step.`
`● If the CPU is overutilized (CPU > 80%), the script should recommend a larger instance by one`
`step.`
`● If the instance size is the smallest (nano), it cannot be reduced further, so no smaller size is`
`recommended.`
`● If the instance is the largest (32xlarge), it cannot be upgraded further.`
`Input 1:`
`Current EC2 : t2.large`
`CPU : 20%`

**Ans:**
![[Pasted image 20260312210602.png]]

![[Pasted image 20260312210616.png]]


![[Pasted image 20260312210522.png]]
![[Pasted image 20260312210539.png]]

`Q8. File Restructuring and JSON Formating`

`You are given a large dataset in JSON format representing an e-commerce platform's order history, which`
`includes orders from multiple customers. Each order has multiple items, with detailed attributes such as`
`price, quantity, and shipping cost. Additionally, you need to extract specific information, perform`
`calculations like the total cost, apply discounts, and sort the data based on various criteria like the total`
`amount spent by each customer.`
`The goal is to:`
`● Extract and restructure the data into a tabular format.`
`● Perform calculations such as:`
`● Total order value (price * quantity).`
`● Apply a discount based on the total value of an order (e.g., 10% discount if the order exceeds`
`$100).`
`● Calculate shipping cost based on the number of items ordered (e.g., $5 per item).`
`● Sort the data by the total amount spent by each customer.`
`● Format the output so that it can be easily saved into a CSV file.`

`So Write a Python program that:`

1. `Extract and restructure the data to create a flat list of each product purchased by each`
`customer, containing:`
`○ Order ID`
`○ Customer Name`
`○ Product Name`
`○ Product Price`
`○ Quantity Purchased`
`○ Total Value (price * quantity)`
`○ Discount (10% if the total order value > $100)`
`○ Shipping Cost (based on the number of items ordered)`
`○ Final Total (after discount + shipping)`
`○ Shipping Address`
`○ Country Code`
2. `Calculate:`
`○ For each order, apply a 10% discount to the total value if the total order value is over`
`$100.`
`○ Calculate the total shipping cost (e.g., $5 per item).`
`○ Compute the final total by adding the shipping cost and applying the discount (if any).`
3. `Sort the list of orders by the final total amount spent by each customer.`
4. `Output the data in CSV format with the following columns:`
`○ Order ID, Customer Name, Product Name, Product Price, Quantity Purchased, Total`
`Value, Discount, Shipping Cost, Final Total, Shipping Address, Country Code`

`Constraints:`
`● The JSON file can contain a variable number of orders.`
`● Each order contains a variable number of items.`
`● Handle missing fields or unexpected values gracefully.`

**Ans:**
![[Pasted image 20260312211401.png]]

![[Pasted image 20260312211411.png]]
![[Pasted image 20260312211438.png]]
![[Pasted image 20260312211455.png]]

`Q9. File Version Control System (optional)`

`Write a Python program to simulate a basic version control system for a directory of files. The script`
`should:`
`● Accept a directory path as input and store versions of files whenever changes are made.`
`● Each time a file is modified, the script should create a new version and save it in a separate folder`
`(e.g., ./versions).`
`● Keep track of file versions by naming them with a version number or timestamp (e.g.,`
`file_v1.txt, file_v2.txt).`
`● When a file is restored to a previous version, it should be copied from the version folder back to`

`the original directory.`
`Bonus:`
`● Implement the ability to compare file versions and show differences (similar to diff).`
`● Add an option to automatically clean up old versions, keeping only the last n versions of`
`each file.`

**Ans:**

