import { SignUpButton } from "@clerk/clerk-react";
import "./LandingPage.css";

export default function LandingPage() {
  return (
    <div className="landing-container">
      <h1>Welcome to LivePulse</h1>
      <p>Your personalized AI-powered content hub.</p>

      <SignUpButton>
        <button className="landing-btn">Get Started</button>
      </SignUpButton>
    </div>
  );
}
