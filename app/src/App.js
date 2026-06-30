import logo from './logo.svg';
import { createBrowserRouter, RouterProvider} from 'react-router-dom'
import './App.css';
import Home from './components/Home'
import Login from './components/Login'
import Regsiter from './components/Register'

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
  }
])

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
