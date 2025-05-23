const { MongoClient } = require('mongodb');+

async function main() {
    const uri = "mongodb://localhost:27017";
    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("MongoDB connected");

        const adminDb = client.db('admin');

        // Enabling sharding for 'logDB'
        await adminDb.command({ enableSharding: "logDB" });
        console.log("Sharding enabled for logDB");

    } catch (err) {
        console.error("Error:", err);
    } finally {
        await client.close();
    }
}

main();
