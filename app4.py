import streamlit as st

st.markdown("# Claim denials ")
# First dropdown for CO16 and CO45
option = st.selectbox('Select an option', ['CO16', 'CO45', 'CO29'])

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


1. **Verify Claim Submission Status in Waystar**
    - Check Waystar to see whether the claim was submitted with an authorization number.
    - If yes,
      - Check Authorization Availability in Software
      - Verify the availability of the authorization in the billing software.
      - Determine who provided the authorization (HP, IPA, or Hospital).

2. **Validate Authorization**
    - Using the authorization number, search the portal of the entity that provided the authorization or check PSI. 
    - Download the authorization sheet and validate its details.

3. **Prepare Appeal with Authorization Sheet**

    - If a valid authorization is found, prepare an appeal with the following documents:
      - Authorization sheet
      - Denied EOB (Explanation of Benefits)
      - Additional documentation to prevent future denials, such as payer contract or fee schedule
    - Send the appeal to the designated mailing address (e.g., PO BOX 811610, LOS ANGELES, CA 90081).

  
4. **If Authorization is not found**

    - Place a call to the insurance company to inquire about the possibility of retroactive authorization.
      - If retroactive authorization is possible, task the  to handle it.
      - If no retroactive authorization is possible and the balance is less than $150, proceed with write-off and add back-end billing if it is a rental.
      - If the balance is more than $150, task the client for write-off approval.

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


1. **Action Step 1: Check Additional Resource**
    - Check LA CARE Portal or Payspan for confirmation of the denial details.
    - Verify if the invoice exists in the system. 
    - Check if it is a listed code or unlisted code in the fee schedule.
      - If the code is listed in the fee schedule, no invoice copy is needed. Attach the fee schedule and appeal the invoice.
      - If the code is unlisted in the fee schedule, look for the invoice copy in CARDINAL, RED BOOK, or PSI. If an invoice copy is found, appeal with the invoice copy.

2. **Action Step 2 : Communicate with Client**
    - If no invoice is found, task the client to obtain a necessary invoice copy.  
    - If unable to find a valid invoice copy, task the client for a valid invoice copy for payment.

3. **Action Step 3: Prepare and File an Appeal (if invoice found or client provides invoice)**
    - Attach the necessary documentation (EOB, AUTH documentation, invoice copy)
    - Use the mailing address for appeal: PO BOX 811610, LOS ANGELES, CA 90081.

4. **Action Step 4: Confirm Timeliness of Appeal**
    - Ensure the appeal is filed within the Time Frame Limit (TFL) of 365 days from the denial date.

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

elif option == 'CO29':


    co29_option = st.selectbox('Select a denial reason', [
        "",
        'Past timely filing limit',

    ])

    mappings = {

        "" : "",

        "Past timely filing limit" : """ 

### Workflow for Addressing Claims Denied Due to Past TFL

1. **Identify Denial Reason**
   - The claim was denied due to a "Past TFL".

2. **Review Claim Information**
   - **Action**: Review the claim in Payspan EOB.
     - **Details**: Verify the reason for denial. Confirm claim was denied due to filing timeline expiration.

3. **Check Submission Date**
   - **Action**: Check the claim submission date in the software (e.g., your billing system).
     - **Details**: Confirm if the claim was submitted within the TFL.
       - If **submitted within TFL**: 
         - Investigate if it was billed incorrectly or requires resubmission.
       - If **submitted past TFL**: 
         - Document the submission date and flag for appeal.

4. **Investigate Previous Submissions**
   - **Action**: Research previous submissions related to the same HCPCS and DOS.
     - **Details**: Check if initially submitted to another insurer within TFL.
       - If **found prior submission within TFL**:
         - Gather evidence for appeal.
       - If **no prior submission found**: 
         - Conclude that the claim submission is outside acceptable guidelines.

5. **Prepare for Appeal**
   - **Action**: Prepare an appeal with necessary documentation.
     - **Details**: 
       - Include denied EOB, proof of past submissions, and any authorizations.
       - Mailing address for appeal (e.g., PO BOX 811610 LOS ANGELES CA 90081).

6. **Submit Appeal**
   - **Action**: Submit the appeal to LA Care (or relevant insurer).
     - **Details**: Ensure all documents are included and follow the appeal format required by the carrier.

7. **Follow-Up on Appeal Submission**
   - **Action**: Monitor the status of the appeal.
     - **Details**: Utilize the software to check for updates.
       - If **appeal is approved**: Process payment and close the claim.
       - If **appeal is denied**: Determine reason for denial and consider further actions (e.g., escalating the appeal or consulting a supervisor).

8. **Conclusion of Claim Handling**
   - Document all actions taken and outcomes in the claims management system.
   - Review if any systemic changes are needed to avoid future denials related to TFL.

        """
    
    }

    st.markdown(mappings[co29_option])



elif option == 'CO45':


    co45_option = st.selectbox('Select a denial reason', [
        "",
        "Denials Due to Charges Exceeding Fee Schedule",
        'Paid'

    ])


    mappings = {

        "" : "",

        "Denials Due to Charges Exceeding Fee Schedule" :  """

    ### Workflow for Handling Claim Denials Due to Charges Exceeding Fee Schedule

**1. Claim Denial Identified: Charge Exceeds Fee Schedule**

- **Step 1:** Review the claim in **Payspan**
  - Action: Check the initial denial reason for any specific details.
  - Outcome: Confirmed reason for denial (e.g., Charge exceeds fee schedule).
  
- **Step 2:** Check claim details in **Caretend**
  - Action: Verify the original billing and payment information.
  - Outcome: Find out the initial billing details and payment from primary carrier.
  
- **Step 3:** Calculate the paid amount
  - Action: Use the formula for paid calculation (e.g., 1 * unit price * quantity).
  - Outcome: Determine if the calculated amount is in line with the fee schedule.
  
- **Step 4:** Check for Co-Insured Amount
  - Action: Review co-insurance amounts post-payment.
  - Outcome: If balance is less than $6.00, follow steps below.

**2. If Balance is Less Than $6.00**
  
- **Step 5:** Write off the amount
  - Action: Document the low balance decision and write off the claim.
  - Outcome: No appeal is raised due to low balance.

**3. If Balance is Greater Than or Equal to $6.00**
  
- **Step 6:** Determine Appeal Eligibility
  - Action: Use denial reason to assess if an appeal is justifiable.
  - Outcome: If covered with proper documentation, proceed to next steps.

- **Step 7:** Prepare Appeal Documentation
  - Action: Collect necessary documents such as primary EOB, denied EOB, and fee schedule.
  - Outcome: Prepare a complete appeal package.

- **Step 8:** Submit the Appeal
  - Action: Send all appeal documents to the relevant address (PO BOX 811610 LOS ANGELES CA 90081).
  - Outcome: Document submission and track for any responses.

**4. Review Future Payments and Status**

- **Step 9:** Monitor Payment Recoupment
  - Action: Confirm any future recoupment of overpayments and adjust the claim.
  - Outcome: Ensure all payments and adjustments are documented.

**5. Handle Additional Scenarios**

- **For Claims Initially Billed to Medicare:**
  - Review secondary submissions status in **Caretend**.
  - Ensure the primary claim was processed and payments verified.

- **For Recoupment or Co-Ins Adjustment Issues:**
  - Follow contact protocols for customer service verification.
  
- **For Claims Involving Multiple Medical Identities:**
  - Thoroughly verify the primary payer and secondary considerations.
  
- **Step 10:** Document All Actions
  - Ensure all actions and findings are logged in appropriate systems (Payspan and Caretend).


    """, 



    "Paid" : """

The claim was denied due to "Paid" status on the claim.

1. **Review Claim Details**
   - Access **Payspan EOB** to check the payment status.
   - Verify the paid amount against the claim in **Caretend**.

2. **Payment Information Verification**
   - If the payment is confirmed:
     - Determine if the amount posted matches the payment received.
     - If discrepancies exist, calculate the allowed amounts based on the fee schedule applicable to each HCPCS code.
     - If discrepancies are less than $6.00:
       - Adjust the balance accordingly and document the adjustment.
     - If discrepancies exceed $6.00:
       - Escalate to your supervisor or a senior agent for further advice.

3. **Check Payment Posting**
   - If the claim is paid but not posted:
     - Verify in **Caretend** whether the payment was documented.
     - Check if the payment was included in a bulk payment transaction on **Payspan**.
     - If payment received is less than the posted total, proceed to:
       - Post any missing payment in **Caretend**.
       - Ensure the balance is correctly adjusted.

4. **Assess Secondary Insurance Payment**
   - For claims with multiple payers:
     - Confirm initial primary insurance payments.
     - If primary payment left a deductible, check for secondary payment.
     - Post the secondary payment in **Caretend** once received.
  
5. **Calculate Allowable Fees**
   - For any charges that are above the allowed fee:
     - Review the payer’s fee schedule.
     - Calculate the allowable amount and adjust the remaining balance or write-off if under the threshold (typically $5.00).

6. **Adjustments and Finalization**
   - If payment received aligns with contract terms, finalize by:
     - Posting payment in **Caretend**.
     - Notate adjustments with reasons for documentation.
   - If balance remains and justifies further action:
     - Consider submitting an appeal if allowable based on the findings.

7. **Documentation**
   - Document all actions taken in the patient's account in **Caretend**.
   - Ensure clear notes are available for future reference on the claim's history.

8. **Communication**
   - If issues persist:
     - Notify the patient for any required information (e.g., additional documentation if necessary).
     - Keep clear communication with other departments involved to facilitate the process.


    """ 

    }


    st.markdown(mappings[co45_option])
