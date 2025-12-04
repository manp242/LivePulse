import {
  SignedIn,
  SignedOut,
  SignInButton,
  UserButton,
} from "@clerk/clerk-react";
import { Link } from "react-router-dom";
import "./Navbar.css";

export default function Navbar() {
  return (
    <nav className="nav">
      <Link to="/" className="logo">
        LivePulse
      </Link>

      <div className="actions">
        <SignedOut>
          <SignInButton>
            <button className="nav-btn">Sign In</button>
          </SignInButton>
        </SignedOut>

        <SignedIn>
          {/* NEW Dashboard Link */}
          <Link to="/dashboard" className="nav-btn">
            Dashboard
          </Link>

          {/* Clerk profile dropdown */}
          <UserButton />
        </SignedIn>
      </div>
    </nav>
  );
}
