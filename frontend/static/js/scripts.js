document.addEventListener('DOMContentLoaded', () => {
 const addMemberForm = document.getElementById('addMemberForm');
 const addEventForm = document.getElementById('addEventForm');
 const registerMemberForm = document.getElementById('registerMemberForm');
 const submitBidForm = document.getElementById('submitBidForm');
 const declareWinnerForm = document.getElementById('declareWinnerForm');

 addMemberForm.addEventListener('submit', function(event) {
     event.preventDefault();
     const data = {
         memberId: document.getElementById('memberId').value,
         memberName: document.getElementById('memberName').value,
         wishCoins: document.getElementById('wishCoins').value
     };
     fetch('/add_member', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify(data)
     })
     .then(response => response.json())
     .then(data => alert(data.message));
 });

 addEventForm.addEventListener('submit', function(event) {
     event.preventDefault();
     const data = {
         eventId: document.getElementById('eventId').value,
         eventName: document.getElementById('eventName').value,
         prizeName: document.getElementById('prizeName').value,
         eventDate: document.getElementById('eventDate').value
     };
     fetch('/add_event', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify(data)
     })
     .then(response => response.json())
     .then(data => alert(data.message));
 });

 registerMemberForm.addEventListener('submit', function(event) {
     event.preventDefault();
     const data = {
         memberId: document.getElementById('registerMemberId').value,
         eventId: document.getElementById('registerEventId').value
     };
     fetch('/register_member', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify(data)
     })
     .then(response => response.json())
     .then(data => alert(data.message));
 });

 submitBidForm.addEventListener('submit', function(event) {
     event.preventDefault();
     const bids = [
         document.getElementById('bid1').value,
         document.getElementById('bid2').value,
         document.getElementById('bid3').value,
         document.getElementById('bid4').value,
         document.getElementById('bid5').value
     ];
     const data = {
         memberId: document.getElementById('submitBidMemberId').value,
         eventId: document.getElementById('submitBidEventId').value,
         bids: bids
     };
     fetch('/submit_bid', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify(data)
     })
     .then(response => response.json())
     .then(data => alert(data.message));
 });

 declareWinnerForm.addEventListener('submit', function(event) {
     event.preventDefault();
     const data = {
         eventId: document.getElementById('declareWinnerEventId').value
     };
     fetch('/declare_winner', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify(data)
     })
     .then(response => response.json())
     .then(data => alert(data.message));
 });
});