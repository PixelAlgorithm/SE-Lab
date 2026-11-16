"""Loan eligibility and EMI calculator."""
import json
import os
import secrets
import smtplib
from datetime import datetime
from email.message import EmailMessage
from ftplib import FTP_TLS  # nosec B402

MAX_FOIR = 0.5
BUREAU_HOST = "ftp.creditbureau.example"
VALID_LOAN_TYPES = ("home", "car", "personal")

# Global loan book
applications = {}


def calculate_emi(principal, annual_rate, years):
    """Monthly EMI. annual_rate is a fraction (0.09 = 9%)."""
    rate = annual_rate / 12
    months = years * 12
    if rate == 0:
        return principal / months
    growth = (1 + rate) ** months
    return principal * rate * growth / (growth - 1)


def check_eligibility(age, income, existing_emi, loan_type):
    """Return True if applicant qualifies for the loan."""
    if age < 21 or age > 60:
        return False
    if income <= 0 or existing_emi / income > MAX_FOIR:
        return False
    return loan_type in VALID_LOAN_TYPES


def max_loan_amount(income, existing_emi, annual_rate, years):
    """Largest principal whose EMI fits within the FOIR limit."""
    available = income * MAX_FOIR - existing_emi
    if available <= 0:
        return 0
    rate = annual_rate / 12
    months = years * 12
    if rate == 0:
        return available * months
    return available * (1 - (1 + rate) ** -months) / rate


def amortisation_schedule(principal, annual_rate, years):
    """List of (month, interest, closing balance) rows."""
    emi = calculate_emi(principal, annual_rate, years)
    balance = principal
    rows = []
    for month in range(1, years * 12 + 1):
        interest = balance * annual_rate / 12
        balance = balance - (emi - interest)
        rows.append((month, round(interest, 2), round(balance, 2)))
    return rows


def application_id():
    """Unpredictable application id."""
    return "LN-" + str(secrets.randbelow(90000000) + 10000000)


def save_application(name, amount, file="loans.json"):
    """Store an application and persist the loan book."""
    app_id = application_id()
    applications[app_id] = {
        "name": name, "amount": amount, "date": str(datetime.now())}
    with open(file, "w", encoding="utf-8") as handle:
        json.dump(applications, handle)
    return app_id


def load_applications(file="loans.json"):
    """Load the loan book from disk."""
    with open(file, "r", encoding="utf-8") as handle:
        applications.clear()
        applications.update(json.load(handle))


def upload_to_bureau(report_path):
    """Upload a report over FTPS. Credentials come from the environment."""
    user = os.environ["BUREAU_USER"]
    password = os.environ["BUREAU_PASSWORD"]
    with FTP_TLS(BUREAU_HOST) as ftp:
        ftp.login(user, password)
        ftp.prot_p()
        with open(report_path, "rb") as handle:
            ftp.storbinary("STOR " + os.path.basename(report_path), handle)


def notify_applicant(email, status):
    """Email the applicant through the local mail server."""
    msg = EmailMessage()
    msg["Subject"] = "Loan " + status
    msg["To"] = email
    msg["From"] = "loans@bank.example"
    msg.set_content("Your loan application status: " + status)
    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)


def interest_saved(principal, annual_rate, years, prepayment):
    """Total interest saved by prepaying part of the principal."""
    months = years * 12
    original = calculate_emi(principal, annual_rate, years) * months
    reduced = calculate_emi(
        principal - prepayment, annual_rate, years) * months
    return original - reduced


def risk_band(credit_score):
    """Map a credit score to a risk band."""
    if credit_score > 900 or credit_score < 300:
        return "INVALID"
    if credit_score >= 800:
        return "LOW"
    if credit_score >= 700:
        return "MEDIUM"
    if credit_score >= 600:
        return "HIGH"
    return "VERY HIGH"


def main():
    """Run a short demo."""
    print("EMI for 5L @ 9% for 5 years:", calculate_emi(500000, 0.09, 5))
    print("Eligible (income 15000, EMIs 12000):",
          check_eligibility(35, 15000, 12000, "personal"))
    print("Eligible (unknown loan type 'crypto'):",
          check_eligibility(30, 80000, 0, "crypto"))
    print("Max loan for income 40000:",
          max_loan_amount(40000, 5000, 0.09, 5))
    print("Last schedule row:", amortisation_schedule(100000, 0.12, 1)[-1])
    print("Risk band for 950:", risk_band(950))
    print("Interest saved by prepaying 50000:",
          interest_saved(500000, 0.09, 5, 50000))
    print("Saved as:", save_application("Anil", 500000))
    load_applications()
    print("Applications on file:", len(applications))
    print("Upload to bureau skipped (no network)")


if __name__ == "__main__":
    main()
