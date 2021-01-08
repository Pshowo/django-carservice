# Car Service Center
A web application to make a handle queue management in a car service.

The application will have a server that creates new tickets for customers and ensures that the queue is ordered correctly.

## 
The Hypercar service center provides three services to its customers:
Menu: *Change oil, Inflate tires, Get diagnostic test*

- [x] Create menu page with three menu elements
    * Change oil - /get_ticket/change_oil
    * Inflate tires - /get_ticket/inflate_tires
    * Get diagnostic test - /get_ticket/diagnostic
    
-  [x] Menu page be avaiable at <base_url>/menu 
   
   After clicking on an item, the customer should be redirected to a page where they can get a ticket for the correct service.
   Use special HTML elements to prepare the necessary links.
   
---
Time to services: 

1. Change oil 2min. Any customers waiting in line for an oil change should be served **first**.
2. Inflate tires 5 min. Those who want their tires inflated should be dealt with **next**.
3. Diagnostic 30 min. Customers who require a diagnostic check should be served **last**.

- [x] create a handler that gives tickets to the customers. The handler should serve GET requests on the following URLs:
       
        <base_url>/get_ticket/change_oil
        <base_url>/get_ticket/inflate_tires
        <base_url>/get_ticket/diagnostic
        
    Each page should contain a element with the content Your number is `<ticket_number>`, where `<ticket_number>` is the ticket's reference number.
  
    > The line should be processed in the correct order!>

- [x] To calculate the estimated time, you should sum the time it will take to process all the tickets that will be worked on before the current one.
        The estimated time should be in a element with the content Please wait around <minutes_to_wait> minutes, where <minutes_to_wait> is the estimated number of minutes:<div><div>

        <div>Your number is 7</div>
        <div>Please wait around 49 minutes</div>


  ### Examples:
    
If you have two customers that require an oil change, three customers waiting for their tires to be inflated, and one needing diagnostics, the estimated time for the next customer would be one of the following:

To change oil: 2 * 2 minutes = 4 minutes
To inflate tires: 2 * 2 minutes + 3 * 5 minutes = 19 minutes
To get diagnostics: 2 * 2 minutes + 3 * 5 minutes + 1 * 30 minutes = 49 minutes
 
- [x] Page for operators with view on queue
- [ ] They also want the ability to select when to process the next customer. A simple button that can be clicked to complete this action will work just fine.
When a customer gets to the front of the queue, the operator needs to click the Process next button so work can begin. This should happen when one of the mechanics has finished the previous job and is ready to serve the next customer
  
- [x] When the `Process next` button is clicked, the application selects the next customer according to the priority defined by the algorithm:

    * If there are any customers in the oil change queue, they are served first.
    * When the oil change queue is empty, customers in the tire inflation queue are next in line.
    * Customers requiring diagnostics are served last.
  
  As soon as the operator presses the button, the selected ticket number should be displayed on screen for all customers to see, and the relevant queue's length should be reduced by one

