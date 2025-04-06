import express from 'express';
import routes from './routes.js' 
import path from 'path';
const app = express();
const PORT = process.env.PORT || 3000;


app.use(express.static(path.join(path.resolve(),'public')))

app.use(express.json());
app.use('/',routes)

app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

app.use((err, req, res, next) => {
  console.error('Unhandled Error:', err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

app.listen(PORT, (err) => {
  if (err) {
    console.error('Failed to start server:', err);
    process.exit(1);
  }
  console.log(`Server is running on port  http://localhost:${PORT}`);
});
