const mongoose = require('mongoose');


mongoose.connect('mongodb://127.0.0.1:27017/salesdb')
  .then(() => console.log('MongoDB connected...'))
  .catch(err => console.error('MongoDB connection error:', err));


const db = mongoose.connection;
const sales = db.collection('sales');




// sales.insertMany([
//   {
//     store: "Store A",
//     product: "Laptop",
//     price: 1200,
//     quantity: 2,
//     date: new Date() 
//   },
//   {
//     store: "Store A",
//     product: "Mouse",
//     price: 200,
//     quantity: 3,
//     date: new Date() 
//   },
//   {
//     store: "Store B",
//     product: "Monitor",
//     price: 800,
//     quantity: 1,
//     date: new Date() 
//   }
// ])
//   .then(result => {
//     console.log('Documents inserted:', result);
//   })
//   .catch(err => {
//     console.error('Error inserting documents:', err);
//   });




// Define the map function
var mapFunction = function () {
    var month = this.date.toISOString().substring(0, 7); // Format: "YYYY-MM"
    var revenue = this.price * this.quantity;
    emit({ store: this.store, month: month }, revenue);
  };
  
  // Define the reduce function
  var reduceFunction = function (key, values) {
    return Array.sum(values);
  };
  
  // Execute the mapReduce operation
  db.sales.mapReduce(
    mapFunction,
    reduceFunction,
    {
      out: "monthly_store_revenue"
    }
  );
  
  // View results
  db.monthly_store_revenue.find().pretty();
  