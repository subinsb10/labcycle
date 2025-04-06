const mongoose = require('mongoose');

async function main() {
  try {
    await mongoose.connect('mongodb://127.0.0.1:27017/salesdb');
    console.log('MongoDB connected...');

    const db = mongoose.connection;
    const sales = db.collection('sales');

    
    await sales.insertMany([
        {
          store: "Store A",
          product: "Laptop",
          price: 1200,
          quantity: 2,
          date: new Date()
        },
        {
          store: "Store A",
          product: "Mouse",
          price: 200,
          quantity: 3,
          date: new Date()
        },
        {
          store: "Store B",
          product: "Monitor",
          price: 800,
          quantity: 1,
          date: new Date()
        }
      ]);

    const results = await sales.aggregate([
      {
        $addFields: {
          month: { $dateToString: { format: "%Y-%m", date: "$date" } }
        }
      },
      {
        $group: {
          _id: { store: "$store", month: "$month" },
          totalRevenue: {
            $sum: { $multiply: ["$price", "$quantity"] }
          }
        }
      },
      {
        $project: {
          _id: 0,
          store: "$_id.store",
          month: "$_id.month",
          totalRevenue: 1
        }
      }
    ]).toArray();

    console.log("Monthly store revenue:");
    console.log(JSON.stringify(results, null, 2));

  } catch (err) {
    console.error("Error:", err);
  } finally {
    await mongoose.disconnect();
  }
}

main();
