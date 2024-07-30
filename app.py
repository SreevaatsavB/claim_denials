import streamlit as st

st.markdown("# Claim denails ")
# First dropdown for CO16 and CO45
option = st.selectbox('Select an option', ['CO16', 'CO45'])

if option == 'CO16':
    # Second dropdown for CO16 options
    co16_option = st.selectbox('Select a denial reason', [
        "",
        'Missing UPN',
        'Missing Invoice',
        'Authorization Needed',
        'Claim Lacks Information',
        'Paid (Overpayment)',
        'Primary EOB Required',
        'Service Not Covered by This Payor',
        'Invalid/Missing Dx Code',
        'Invalid UPN',
        'Duplicate Claim',
        'No Authorization'
    ])
    
    # Mappings based on selected option
    mappings = {
        "" : "",
        'Missing UPN': """
        
        - Review claim in Payspan to check the reason for denial.
        - Check the medical portal for the UPN.
        - If UPN not found, review the payment report.
        - Call customer service to verify if UPN is required.
        - If UPN is not required, raise an appeal with the necessary documents.
        """,
        'Missing Invoice': """
        
        - Review claim submission status.
        - Check Payspan for the denial reason.
        - Verify billing accuracy in Caretend.
        - Check for valid invoices in Teams.
        - Forward the claim to the client for the proper invoice.
        """,
        'Authorization Needed': """
        
        - Verify claim status in software and Payspan.
        - Check billing information for authorization details.
        - Verify authorization document in PSI.
        - Check claim status in Waystar for authorization number.
        - File an appeal with the required documents.
        """,
        'Claim Lacks Information': """
        
        - Review the claim denial reason.
        - Check for valid authorization in PSI.
        - Prepare and submit an appeal if valid authorization exists.
        """,
        'Paid (Overpayment)': """
        
        - Review payment details in Payspan.
        - Calculate allowed amount based on the fee schedule.
        - Adjust the balance if the payment exceeds the allowed amount.
        """,
        'Primary EOB Required': """
        
        - Check Payspan for claim status.
        - Obtain the patient's Medicare ID from the medical portal.
        - Verify the patient's Medicare plan status in Noridian.
        - Forward the claim to the EV team to bill Medicare.
        """,
        'Service Not Covered by This Payor': """
        
        - Review claim status in Payspan.
        - Verify claim submission details.
        - Check EOB in Waystar.
        - Confirm patient's eligibility and coverage details.
        - Task the client to determine the appropriate payor.
        """,
        'Invalid/Missing Dx Code': """
        
        - Review the claim billing details.
        - Verify the submitted Dx code in Caretend.
        - Check for validation documents in PSI.
        - Forward the claim to the client for assistance.
        """,
        'Invalid UPN': """
        
        - Review the claim in Payspan.
        - Verify the submitted UPN in the claim form.
        - Search for valid UPN in the medical portal.
        - Check payment reports for UPN discrepancies.
        - Forward the issue to the client for assistance.
        """,
        'Duplicate Claim': """
        
        - Review EOB in Payspan to check for duplicates.
        - Verify the original claim status in Caretend.
        - Confirm payment details of the original claim.
        - Adjust the balance for the duplicate claim.
        """,
        'No Authorization': """
        
        - Review the claim denial reason in Payspan.
        - Verify the claim submission with authorization details.
        - Confirm the validity of the authorization document.
        - Prepare an appeal with the required documents.
        """
    }
    
    # Display the common steps and selected mapping
    st.markdown(mappings[co16_option])
    
    # Appeal Process

elif option == 'CO45':
    st.markdown("No additional information to display.")
