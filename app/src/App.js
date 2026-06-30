import { createBrowserRouter, RouterProvider} from 'react-router-dom'
import './App.css';
import Home from './components/Home'
import Login from './components/Login'
import Regsiter from './components/Register'
import Dashboard from './components/Dashboard';

const router = createBrowserRouter([
  {
    path: '/',
    element : <Home />
  },
  {
    path: '/login',
    element : <Login />
  },
  {
    path: '/register',
    element: <Regsiter />
  },
  {
    path: '/dashboard',
    element: <Dashboard />
  }
])

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
