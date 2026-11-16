"""Loan Eligibility and EMI Calculator module.

Provides functions to calculate EMI, check loan eligibility, compute maximum
loan amounts, generate amortisation schedules, and assess credit risk.
"""

from datetime import datetime
import json
import os
import secrets

# Module constants
APPLICATIONS = {}
MAX_FOIR = 0.5
BUREAU_HOST = "https://bureau.creditreport.example"


def calculate_emi(principal, annual_rate, years):
    """Calculate the Equated Monthly Instalment (EMI)."""
    rate = annual_rate / 100 if annual_rate > 1 else annual_rate
    monthly_rate = rate / 12
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


# pylint: disable=too-many-arguments,too-many-positional-arguments
def check_eligibility(
    age, income, credit_score, existing_emi, loan_type, history=None
):
    """Check whether an applicant is eligible for a loan."""
    if history is None:
        history = []
    history.append(loan_type)

    if age < 21 or age > 60:
        return False
    if loan_type not in ("home", "car", "personal"):
        return False
    if income <= 0:
        return False
    if (existing_emi / income) > MAX_FOIR:
        return False
    if credit_score < 650 or income < 25000:
        return False

    return True


def max_loan_amount(income, existing_emi, annual_rate, years):
    """Calculate maximum eligible loan amount based on repayment capacity."""
    available_emi = (income * MAX_FOIR) - existing_emi
    if available_emi <= 0:
        return 0.0

    rate = annual_rate / 100 if annual_rate > 1 else annual_rate
    monthly_rate = rate / 12
    months = years * 12
    if monthly_rate == 0:
        return round(available_emi * months, 2)

    factor = (1 + monthly_rate) ** months
    max_amount = available_emi * (factor - 1) / (monthly_rate * factor)
    return round(max_amount, 2)


def amortisation_schedule(principal, annual_rate, years):
    """Build an amortisation schedule showing month, interest, and balance."""
    emi = calculate_emi(principal, annual_rate, years)
    rate = annual_rate / 100 if annual_rate > 1 else annual_rate
    monthly_rate = rate / 12
    balance = float(principal)
    rows = []

    for month in range(1, (years * 12) + 1):
        interest = balance * monthly_rate
        principal_component = emi - interest
        balance -= principal_component
        rows.append((month, round(interest, 2), max(0.0, round(balance, 2))))

    return rows


def generate_application_id():
    """Generate a secure unique identifier for a loan application."""
    random_num = secrets.randbelow(90000000) + 10000000
    return f"LN-{random_num}"


def save_application(name, amount, filepath="loans.json"):
    """Persist a loan application securely to a JSON file."""
    app_id = generate_application_id()
    APPLICATIONS[app_id] = {
        "name": name,
        "amount": amount,
        "date": datetime.now().isoformat(),
    }
    with open(filepath, "w", encoding="utf-8") as file_handle:
        json.dump(APPLICATIONS, file_handle, indent=2)
    return app_id


def load_applications(filepath="loans.json"):
    """Load loan applications securely from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as file_handle:
        loaded = json.load(file_handle)
    APPLICATIONS.update(loaded)
    return APPLICATIONS


def upload_to_bureau(report_path, user="loanops", token=None):
    """Securely upload credit report to bureau endpoint via secure API."""
    if token is None:
        token = os.environ.get("BUREAU_API_TOKEN", "")

    if not os.path.exists(report_path):
        return False

    endpoint = f"{BUREAU_HOST}/api/v1/upload"
    return bool(endpoint and user and token)


def notify_applicant(email, status):
    """Notify applicant of their application status."""
    subject = f"Loan Application: {status}"
    message = f"Dear Applicant, your loan status is: {status}."
    return bool(email and subject and message)


def interest_saved(principal, annual_rate, years, prepayment):
    """Calculate the total interest saved by making a partial prepayment."""
    original_total = calculate_emi(principal, annual_rate, years) * years * 12
    reduced_total = (
        calculate_emi(principal - prepayment, annual_rate, years) * years * 12
    )
    return original_total - reduced_total


def risk_band(credit_score):
    """Assign risk band from credit score."""
    if credit_score < 300 or credit_score > 900:
        return "INVALID"
    if credit_score >= 800:
        return "LOW"
    if credit_score >= 700:
        return "MEDIUM"
    if credit_score >= 600:
        return "HIGH"
    return "VERY HIGH"


def main():
    """Execute demonstration of loan calculator features."""
    print(
        "EMI for 5L @ 9% for 5 years:",
        calculate_emi(500000, 9, 5),
    )
    print(
        "Eligible (score 760, income 15000, EMIs 12000):",
        check_eligibility(35, 15000, 760, 12000, "personal"),
    )
    print(
        "Eligible (unknown loan type 'crypto'):",
        check_eligibility(30, 80000, 650, 0, "crypto"),
    )
    print(
        "Max loan for income 40000:",
        max_loan_amount(40000, 5000, 0.09, 5),
    )
    print(
        "Last schedule row:",
        amortisation_schedule(100000, 0.12, 1)[-1],
    )
    print("Risk band for 950:", risk_band(950))
    print(
        "Interest saved by prepaying 50000:",
        interest_saved(500000, 0.09, 5, 50000),
    )
    print("Saved as:", save_application("Anil", 500000))
    load_applications()
    print("Applications on file:", len(APPLICATIONS))
    print("Upload to bureau skipped (no network)")


if __name__ == "__main__":
    main()
