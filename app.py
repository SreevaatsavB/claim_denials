import streamlit as st

st.markdown("# Claim denials ")
# First dropdown for CO16 and CO45
option = st.selectbox('Select an option', ['CO16', 'CO45'])

if option == 'CO16':
    # Second dropdown for CO16 options
    co16_option = st.selectbox('Select a denial reason', [
        "",
        "UPN",
        'No Authorization',
        "Prior Authorization Needed",
        'Missing Documentation (Authorization)',
        'Authorization Code Does Not Cover DOS',
        'Past timely filing limit',
        'Duplicate Claim',
        'Diagnosis Code',
        'Missing Invoice',
        'Incorrect / Missing Modifier'

    ])
    
    # Mappings based on selected option
    mappings = {
        "" : "",

        "UPN" : """

### Workflow for Claim Denials Due to UPN Issues

---

#### Scenario 1: Claim Denied Due to Incorrect UPN

1. **Identify Denial Reason**

  - The claim was denied due to an "Incorrect UPN."

2. **Review Claim Details in Payspan**

  - Verify the specific denial reason and note the billed UPN.

3. **Check the Claim Form**

  - Check the UPN submitted in the claim form for inaccuracies.

4. **Consult Fee Schedule**

  - Look up the correct UPN for the HCPCS code in the Fee Schedule.

5. **Prepare a Corrected Claim**

  - If the UPN is incorrect, prepare a corrected claim using the correct UPN.

6. **Submit Corrected Claim**

  - Submit the corrected claim through the designated method (Waystar, paper submission, etc.).

7. **Await Response**

  - Check for updates in Payspan after a few days to verify if the claim was processed.

8. **If Claim is Rejected Again**

  - If denied again, gather the needed documents and prepare for an appeal.

9. **Raise Appeal**

  - Appeal the decision with the denied claim, fee schedule, and other relevant documents.

---

#### Scenario 2: Claim Denied Due to Missing UPN

1. **Identify Denial Reason**

  - The claim was denied due to a "Missing UPN."

2. **Review Claim in Payspan**

  - Confirm the specific denial reason and note the absence of UPN.

3. **Check Medical Portal**

  - Search in the medical portal for any UPN details related to the service.

4. **Examine Payment Report**

  - Review payment history to confirm if the code has been paid without a UPN previously.

5. **Call Customer Service**

  - Contact customer service to verify if the UPN is required for the specific code.

6. **Determine UPN Requirement**

  - If UPN is confirmed as required:

     - Request UPN information from the patient or provider.

  - If UPN is not required:

     - Prepare to appeal the claim denial.

7. **If UPN is Obtained**

  - Update the claim with the provided UPN and resubmit.

8. **If UPN is Not Obtained**

  - Raise an appeal with supporting documents that state the denial reason.

---

#### Scenario 3: Claim Denied Due to Invalid UPN

1. **Identify Denial Reason**

  - The claim was denied due to an "Invalid UPN."

2. **Review Claim in Payspan**

  - Check the specific entry for the invalid UPN.

3. **Check Previous Entries**

  - Examine the claim form for the UPN that was submitted.

4. **Validate UPN in Medical Portal**

  - Search for the UPN within the medical portal to determine its validity.

5. **Consult Previous Claims**

  - Review payment reports or previous claims that may have successfully used the UPN.

6. **Call Customer Service**

  - Speak to a customer service representative to confirm the correct UPN requirements.

7. **Update Submission**

  - Correct any inaccuracies and prepare the resubmission as needed.

8. **Appeal if Needed**

  - Raise an appeal if the claim continues to be denied based on invalid UPN after resubmission.

---

#### Software Utilization References:

- **Payspan**: Used for checking claim status and denial reasons.

- **Medical Portal**: For UPN information and verification against patient records.

- **Fee Schedule**: For determining correct UPN codes and ensuring compliance.

- **Waystar**: Platform for submitting claims and corrections electronically.

---
 

""",

      'No Authorization': """

### Claim Denied Due to No Authorization


1. *Claim Denied Due to Lack of Authorization*  
 - Reviewed the claim details in Payspan.
 - *Action:* Verify denial reason.
 - *Outcome:* Claim denied for lacking authorization.
 - *Next Step:* Check the submission in billing software.

2. *Check Submission in Billing Software*  
 - Confirm whether the claim was submitted with a valid authorization number.
 - If authorization number is provided:
 - *Action:* Check if the authorization is valid in PSI or other portals.
 - If no authorization number is found:
 - *Action:* Reach out to the provider for the necessary authorization documents.

3. *Verify Validity of Authorization*  
 - In PSI, confirm authorization is active for the date of service.
 - If valid authorization exists:
 - *Action:* Prepare an appeal including:
 - Authorized document
 - Denied EOB (Explanation of Benefits)
 - Fee schedule
 - *Next Step:* Send the appeal to the designated mailing address (e.g., PO BOX 811610, LOS ANGELES, CA 90081).
 - If authorization is not valid or not found:
 - *Next Step:* Request the necessary authorization from the patient or provider.

""",

        "Prior Authorization Needed" : """

  ### Denied Claims Related to No Prior Authorization 

1. *Claim Denied for Lack of Prior Authorization*  
 - Reviewed claim in caretend to check status.
 - *Action:* Check on provider portal for specific denial reasons.
 - *Outcome:* Determine if the authorization was not obtained.

2. *Verify Patient's Insurance Coverage*  
 - Check the patient's coverage using the medical portal or specific insurance guidelines (e.g., Noridian).
 - If no valid authorization found:
 - *Action:* Contact the provider to clarify authorization status.

3. *Prepare to Appeal Denial*  
 - Compile documents related to prior authorization.
 - *Include:* Denied claim EOB, authorization document, and any relevant supporting documentation.
 - *Next Step:* Submit the appeal through the mailing address (e.g., PO BOX 811610, LOS ANGELES, CA 90081).

""", 

"Missing Documentation (Authorization)" : """

### Claim Denied Due to Missing Documentation 

1. *Claim Denied Due to Missing Documentation*  
 - Review claim submission details in Payspan or billing software.
 - *Action:* Verify if proper documentation was submitted.

2. *Check for Required Documents*  
 - Investigate the claim in the PSI.
 - If missing authorization:
 - *Action:* Contact the provider for missing documents or information.

3. *Provide Documentation*  
 - Once documentation is obtained, review and compile it.
 - *Action:* Raise an appeal if documentation is complete; include:
 - Denied claim EOB
 - Required documents
 - *Next Step:* Submit appeal to the designated mailing address.
""",

"Authorization Code Does Not Cover DOS" : """

### Claim Denied as authorization code does not cover DOS


1. *Claim Denied Based on Authorization Validity*  
 - Reviewed denial reason in Payspan.
 - *Action:* Verify that the claim was billed with the correct authorization codes.

2. *Check Authorization Coverage Dates*  
 - Validate whether authorization covers the date of service.
 - If authorization is valid but claims are denied:
 - *Action:* Contact patient or provider to resolve issues related to scope.

3. *Prepare Parameters for Appeal*  
 - Include all relevant facts:
 - Authorization documentation
 - Denial reasoning
 - Billed codes
 - *Next Step:* Send appeal documentation to the designated address.

**Final Notes:**

*Software Tools to Use:*
 - Payspan for claim status and denial reasons.
 - PSI for authorization validity verification.
 - Caretend for checking submission status.
 - Medical portal for insurance eligibility and coverage details.
. *Documentation:* Always maintain clear records of all communications and actions taken to ensure a smooth appeal process.

""", 

"Past timely filing limit" : """

### Denied Claims Related to Past Timely Filing Limits (TFL)


1. *Claim Denied Due to Past TFL*
 - Reviewed the claim in *Caretend*; noted the reason for denial as Past TFL.
 - Checked in *LA CARE Web Portal* to verify denial details; confirmed the claim was denied due to timely filing expiration.
 - *Check Submission Dates*
 - Policy: Timely filing limit for LA CARE is 180 days from the Date of Service (DOS).
 - Determine if the claim was submitted within the allowed timeframe:
 - *Claim Submitted Within 180 Days*:
 - Follow up with *Payspan Web Portal* to find any discrepancies.
 - Gather any necessary evidence for a possible appeal (e.g., submission confirmation).
 - Prepare appeal with all supporting documentation (EOB, proof of submission, etc.).
 - *Claim Submitted After 180 Days*:
 - Confirm the claim was last billed to the carrier before the TFL expired.
 - If submitted after expiration:
 - *Forward Claim for Adjustment*
 - Task the client for approval on adjustments based on TFL denial.
 - Document all communications regarding the next steps for the claim.
  
2. *Initial Claim Check for Valid Proof*
 - Reviewed in *Caretend* and *LA CARE Web Portal*; found no additional information about the claim.
 - Cross-check with *Payspan Web Portal* for confirmation of the denial reason:
 - If claims were denied with a matching DOS and similar HCPCS, consider historical patterns for similar claims.
 - Further, validate received dates using *Zermied Web Portal*:
 - Confirm the initial submission and acknowledgment.
 - If no discrepancies found or they validate the denial:
 - Task client for adjustment approval requests.

3. *Follow-up Actions for Claim Resubmission*
 - After confirming denial due to past TFL:
 - Check for any other similar invoices that may have been denied under the same criteria.
 - Check *Redbook* for any missing documentation required for appeal.
 - Collect and prepare the necessary documentation for appeal:
 - *Prepare and Identify Submission*
 - Prepare appeal with necessary documents: Denial EOB, invoice copies, etc.
 - Ensure to identify the appeal mailing address accurately (e.g., PO BOX 811610 LOS ANGELES CA 90081).
 - If the claim is processed manually, provide all documentation to the client for resubmission.

4. *Final Review of Denial Outcomes*
 - If adjustments are approved:
 - Resubmit claims as per client direction.
 - If UPN or other required documentation is missing:
 - Request needed information from the patient or provider to support claim re-evaluation.
 - Document every action taken on the claims:
 - Maintain records in *Caretend* and format notes for clear chronologies on reasons and actions.

5. *Appeal Process*
 - If claim is past TFL without possible adjustments or evidence:
 - Raise an appeal with detailed documentation provided to justify the grounds for request.
 - Await response from carrier; meanwhile, monitor claim status regularly in both *LA CARE* and *Payspan* portals.

By following this structured workflow, agents can systematically address denied claims related to past timely filing limits and implement the required measures effectively.

""",

"Duplicate Claim" : """

### Claim Denied Due to Duplicate Claim

1. *Claim is Denied as Duplicate*
 - *Action:* Review the claim in Caretend software.
 - *Check:* Is there any payment received for this claim?
 - If *Yes*: Confirm payment details.
 - If *No*: Proceed to the next step.
  
2. *Verify Denial Reason*
 - *Action:* Check in Payspan web portal.
 - *Check:* What is the denial reason?
 - If *Reason is Duplicate*: Go to the next step.
 - If *Reason is Not Duplicate*: Different resolution needed; take appropriate actions based on the new reason.

3. *Identify Original Claim*
 - *Action:* Locate the original claim.
 - *Software Used:* Caretend or Payspan.
 - *Check:* Is there a previously paid claim?
 - If *Yes*: Confirm claim details (invoice number, DOS, HCPCS).
 - *Action:* Adjust balance to resolve the duplicate issue.
 - If *No*: Proceed to the next step.

4. *Assess Billing Errors (Applicable for Incorrectly Billed Claims)*
 - *Action:* Review guidelines for the procedure code (e.g., E0971).
 - *Check:* Was the claim incorrectly billed?
 - If *Yes*: Identify incorrect billing formats (e.g., units).
 - *Action:*
 - Update charge and units according to guidelines (e.g., change amount to $13.00 and add LT RT modifier).
 - Submit corrected claim electronically.
 - If *No*: Confirm the original claim was valid, and no actions are required.

5. *Submit Corrected Claim*
 - *Software Used:* Zermied web portal.
 - *Action:* If no corrected claim was submitted previously, ensure proper submission.
 - *Check:* Has the TFL duration (365 days from the denied date) been followed?
 - If *Yes*: Submit the corrected claim.
 - If *No*: Assess if appeal is needed based on timing.

6. *Final Confirmation*
 - *Action:* Review submitted claims in Zermied.
 - *Check:* Was the corrected claim successfully submitted?
 - If *Yes*: Monitor the status of the claim.
 - If *No*: Investigate and re-submit as necessary, including any necessary documentation for appeals if claims remain denied.

---

**Key Notes:**

• Software Tools:

 - Caretend software
 - Payspan web portal
 - Zermied web portal

""" ,  

"Diagnosis Code" : """

### Claim Denial Workflow Due to Diagnosis Code Issues

#### Scenario 1: Claim Denied Due to Missing Diagnosis Code
1. *Claim Denial Reason Identified*: Claim was denied due to a missing diagnosis code.
2. *Action*: Review the claim in the Payspan portal.
 - Check for the specific reason for the denial.
3. *Action*: Check authorization details in PSI.
 - Verify effective dates and authorization for the date of service (DOS).
4. *Action*: Verify diagnosis codes in the authorization.
 - Confirm which codes were approved.
5. *Action*: Review the claim form for discrepancies.
 - Identify which diagnosis code(s) were submitted and which were missing.
6. *If Missing Diagnosis Code Found*: 
 - *Action*: Submit a corrected claim through paper with the missing diagnosis code.
 - Include updated claim form and resubmit to the correct address (e.g., PO BOX 811580 LOS ANGELES CA 90081).
7. *If No Missing Code Found*: 
 - Consider alternative reasons for denial or escalate.

---

#### Scenario 2: Claim Denied Due to Invalid Diagnosis Code
1. *Claim Denial Reason Identified*: Claim was denied due to an invalid diagnosis code.
2. *Action*: Review claim in the Payspan portal to determine denial specifics.
3. *Action*: Review the submitted diagnosis code in Caretend.
 - Confirm if the correct DX code was submitted.
4. *Action*: Check any supportive documentation in PSI.
 - Validate the usage of the provided DX code.
5. *Action*: If validation documents are not found, forward the claim to the client for further assistance in confirming the correct DX code.
6. *Action: Once you receive a valid DX code from the client, **submit a corrected claim* in Zirmed or the appropriate system.

---

#### Scenario 3: Claim Denied Due to Incorrect Diagnosis Code
1. *Claim Denial Reason Identified*: Claim was denied due to an incorrect diagnosis code.
2. *Action*: Review previous notes to identify past actions taken.
3. *Action*: Check the status of the resubmitted claim in Payspan.
4. *Action*: Review patient documents to determine the correct diagnosis code.
5. *If Correct Diagnosis Code Identified*: 
 - *Action*: Resubmit the claim using the correct DX code in Waystar.
 - *Action*: Ensure the claim mailing address is correct.
6. *If Still Denied*: Consider requesting more information from the patient or provider.

---

#### Scenario 4: Claims with General Assumptions about DX Codes
1. *Claim Denial Reason Identified*: General error regarding diagnosis codes without specifics.
2. *Action*: Review the claim details in Payspan.
3. *Action*: Cross-reference with documentation and check the claim form in Caretend.
4. *If Documents Support Submission*: 
 - Follow standard operating procedures for escalation or resubmission.
5. *If Documents Do Not Support Submission*:
 - Forward the claim to the client for clarification and further assistance.

""", 

 "Missing Invoice" : """

### Claim Denial Due to Missing Invoice Workflow

1. *Identify the Claim Denial Reason* 
 The claim was denied due to a missing invoice.

2. *Action Step 1: Review the Claim in Payspan* 
 - Check Payspan for details on the claim denial. 
 - Note the denial reason (e.g., Missing Invoice).

3. *Action Step 2: Verify Claim Submission Status* 
 - *Use Software: Check in **Caretend* for the submission status.
 - If response found, proceed with actions based on findings.
 - If no response found, continue to the next step.

4. *Action Step 3: Check Additional Resources* 
 - *Software Options*: 
 - Check the *LA CARE Portal* or *PaySpan* for confirmation of the denial details.
 - Verify if the invoice exists in the system.
 - *If invoice found*, note down the valid details.
 - *If invoice not found*, continue to the next step.

5. *Action Step 4: Search for Supporting Documentation* 
 - Check for any similar invoices that may support the claim.
 - Use *Redbook* to find any potential invoice copies.

6. *Action Step 5: Document Findings* 
 - If no valid invoice is available, document that no valid documents are available for appeal.
 - If invoice copy is found, prepare it for submission.

7. *Action Step 6: Communicate with Client* 
 - If no invoice is found, *task the client* to obtain a necessary invoice copy.

8. *Action Step 7: Prepare and File an Appeal* (if invoice found or client provides invoice) 
 - Attach the necessary documentation (EOB, AUTH documentation, invoice copy).
 - *Mailing Address for Appeal*: PO BOX 811610, LOS ANGELES, CA 90081.

9. *Action Step 8: Confirm Timeliness of Appeal* 
 - Ensure the appeal is filed within the Time Frame Limit (TFL) of 365 days from denial date.
 - Keep track of submission dates and follow up as needed.

10. *Action Step 9: Follow Up* 
 - Check back in the systems (e.g., Payspan, Caretend) for updates regarding the appeal status.
 - If no response is received after a certain period, follow up with payer.

### Special Notes:
• Always treat each claim individually and adjust actions based on the specifics of the claim.

• Maintain clear records of all actions taken, including dates, to provide a comprehensive history if needed.

""",

'Incorrect / Missing Modifier' : """

### Claim Denied Due to Incorrect or Missing Modifier

1. *Claim Denial Identification*
 - Identify the reason for claim denial (e.g., "Incorrect Modifier" or "Missing Modifier").
 - Confirm the date of service (DOS) and relevant invoice.

2. *Review Claim Details in Software*
 - *Action: Review the claim in **Caretend*.
 - If payment was not received, proceed to the next step.
 - If payment was received, further investigation may be required.

3. *Check Claim Status in Payment Portals*
 - *Action: Check status in **Payspan*.
 - If claim is marked as denied due to modifier issues, proceed.
 - Note the denial reason and any details provided.

4. *Check Other Portals for Submission and Modifier Details*
 - *Action: Check **Zermied* web portal for claim submission details.
 - Confirm if the correct modifiers were used during submission.
 - If submitted with incorrect or missing modifiers, proceed to correct the information.
 - If modifiers appear correct, further investigation may be warranted (e.g., contacting support).

5. *Contacting Support for Clarification*
 - *Action: Contact support of the payer (like **LA CARE*).
 - Confirm receipt of any previously submitted corrected claims.
 - Ask if any additional information is required to resolve the issue.

6. *Modify Claims as Needed*
 - For *Missing Modifier*:
 - *Action*: Review any recent updates from the client regarding modifier requirements.
 - Correctly resubmit claims including the necessary modifiers (e.g., LT/RT for procedure code E0971).
 - For *Incorrect Modifier*:
 - *Action*: Change the incorrect modifier and ensure adherence to submission guidelines.
 - Resubmit the corrected claim electronically through *Zermied* or relevant software.
 - Reference previous claim numbers for tracking.

7. *Final Steps*
 - After resubmitting, monitor the claim status regularly using *Caretend* and *Payspan*.
 - Document all actions taken and maintain a record for future reference.

8. *In Case of Non-Resolution*
 - If the claim remains denied after resubmission:
 - Consider raising an appeal with supporting documentation if applicable.
 - Review and ensure compliance with payer instructions.
 - Keep the patient/provider informed of the situation and follow-up actions.

### Notes:
• Make sure to document every action taken, specifying the reason and details for clarity in future reference.

• If the outcome is satisfactory (claim gets processed), ensure the payment details are updated accordingly.
"""

  }
    
    # Display the common steps and selected mapping
    st.markdown(mappings[co16_option])
    
    # Appeal Process

elif option == 'CO45':
    st.markdown("No additional information to display.")
