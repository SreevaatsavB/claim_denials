import streamlit as st

st.markdown("# Claim denails ")
# First dropdown for CO16 and CO45
option = st.selectbox('Select an option', ['CO16', 'CO45'])

if option == 'CO16':
    # Second dropdown for CO16 options
    co16_option = st.selectbox('Select a denial reason', [
        "",
        'UPN',
        "Claim lacks information",
        'Authorization',
        'Past timely filing limit',
        'Invoice',
        'Duplicate Claim',
        'Diagnosis Code',
        'Incorrect Modifier'
    ])
    
    # Mappings based on selected option
    mappings = {
        "" : "",
        'UPN': """
### Decision Tree for Addressing Claim Denials Due to UPN Issues

1. **Claim Denial Reason: UPN Related**
   - Go to step 2.

2. **Is UPN Missing?**
   - **Yes:**
     - Action: Review denial details and check for UPN in medical portals.
     - Action: Verify patient eligibility for the date of service.
     - If UPN can be located:
       - Action: Submit a corrected claim with the found UPN.
       - Action: Raise appeal if necessary, sending all required documentation (invoice, denied EOB).

     - If UPN cannot be located:
       - Action: Call the health provider for clarification.
       - Action: Raise appeal stating that the code does not require a UPN based on the provider’s information.

   - **No:**
     - Go to step 3.

3. **Is UPN Invalid or Incorrect?**
   - **Yes:**
     - Action: Review claim details and check if the submitted UPN was correct.
     - Action: Refer to the appropriate Fee Schedule to identify the correct UPN.
     - If correct UPN identified:
       - Action: Prepare and submit a corrected claim with the valid UPN.
       - Action: Ensure all details on the claim are accurate to avoid future denials.

     - If correct UPN not identified:
       - Action: Call the payer for UPN requirements and details.
       - Action: Forward to a senior for further assistance if clarification is not obtained.

   - **No:**
     - Go to step 4.

4. **UPN Submission Format Issues:**
   - Action: Review how the UPN was submitted (check box#).
   - If submission was incorrect:
     - Action: Correct the submission error and resubmit the claim.
     - Action: Raise appeal if prior correction attempts have been made with no resolution.

5. **If Denial Reason Is Due to Missing Documentation:**
   - Action: Check if all required documents (invoices, EOBs) are included.
   - If documents are missing:
     - Action: Gather and submit all necessary documentation.
     - Action: Raise an appeal if initial claim denial was due to lack of documentation.
     
6. **For Claims That Have Already Been Resubmitted:**
   - Check follow-up on the status of the claim:
   - If the claim was denied again:
     - Action: Gather all error details and documentation.
     - Action: Raise an appeal with a focus on addressing the reasons for the latest denial.

7. **Consult with Team Leads or Supervisors:**
   - For complex denials or unresolved issues:
   - Action: Seek guidance from experienced colleagues or supervisors.

**End of Decision Tree**

### Note:
Always ensure to keep a well-documented record of each step taken, and communicate clearly with both payers and internal team members to facilitate smooth claims resolution processes.

        """,


        "Incorrect Modifier" : """

### Claim Denial Decision Tree

1. **Initial Claim Check**
   - Has the claim been denied?
     - Yes: Proceed to the next step.
     - No: No action needed.

2. **Identify Denial Reason**
   - Is the denial reason related to modifiers (e.g., "Incorrect Modifier," "Missing Modifier")?
     - Yes: Proceed to the next step.
     - No: Follow standard procedures for other denial reasons.

3. **Review Claim Details**
   - Check the following:
     - **Payment Status**: Is the payment marked as received or not?
       - Not Received: Investigate further in claim management system (e.g., CareTend).
       - Received: Note discrepancies for reporting.

4. **Verify Submission Frequency**
   - Is this claim a duplicate submission?
     - Yes: Verify the original claim and check for correct modifiers attached. If found, take necessary corrective actions to avoid resubmission errors in future.
     - No: Proceed to the next step.

5. **Gather Submission Information**
   - Check submitted claim portal (e.g., Payspan, Zermied):
     - **Modifiers Submitted**: Are the correct modifiers (e.g., LT, RT, NU) used per client guidelines?
       - No: Proceed to the correction steps.
       - Yes: Investigate client updates or further details and prepare for resubmission.

6. **Identify the Correct Modifiers Required**
   - Refer to the latest client requirements for the procedure code:
     - Are there updated modifier requirements?
       - Yes: Prepare the corrected claims using the required modifiers.
       - No: If original submission guidelines were correct, prepare a follow-up or inquiry to the payer.

7. **Correct and Resubmit Claim**
   - Update the claim with the correct modifier:
     - Submit the corrected electronic claim.
     - Note original claims and resubmission codes for records.
     - Confirm through the claim portal that the resubmission is successfully processed.

8. **Document Actions Taken**
   - Document all actions and findings in the claim notes including:
     - Dates of actions, invoice numbers, DOS, and specific actions taken (e.g., review, submit).
   - Review your documentation before finalizing and closing the claim.

9. **Follow-up**
   - Follow-up with payer as necessary if the resubmitted claim is denied again.
   - Use the information gathered to improve future submissions.

### Conclusion
This decision tree provides a straightforward guide to help new agents efficiently handle and navigate claim denials related to incorrect or missing modifiers. Adhering to these steps will help ensure clarity and thoroughness in resolving denials.""", 

"Claim lacks information" : """

### Decision Tree for Claim Denials: "Claim/Service Lacks Information"

1. **Claim Review**
   - **Action:** Review the claim denial reason.
     - If "Claim/service lacks information" is noted:
       - Proceed to check the **specific information lacking**.
       - Look for related denial codes (e.g., M62 - Missing/incomplete/invalid treatment authorization code).

2. **Check Authorization Status**
   - **Action:** Verify if there is a valid authorization for the date of service (DOS).
     - If valid authorization exists:
       - **Prepare an appeal** with the authorization document and EOB.
       - Submit the appeal to the designated address.
     - If no valid authorization:
       - Proceed to review claim submission details.

3. **Review Claim Submission**
   - **Action:** Check the details of the claim submission.
     - Analyze if there are missing/incomplete elements (e.g., treatment authorization code, UPN, etc.):
       - If the missing element exists:
         - **Action:** Identify what was missing (e.g., Universal Product Number, treatment authorization code).
         - Check if it can be obtained through client communication or internal resources.
       - If there’s a submission error:
         - **Action:** Correct the error (e.g., update UPN) and **resubmit the claim**.

4. **Contact Related Parties for Missing Information**
   - **Action:** Reach out to relevant parties (e.g., medical group, IPA).
     - If you can obtain the missing information/code:
       - **Prepare and submit appeal.**
     - If the information cannot be acquired:
       - Assess if the claim can be adjusted based on the available information.

5. **Evaluate Appeal Submission**
   - **Action:** Ensure all relevant documents are attached to the appeal (EOB, any supporting documentation).
     - Confirm the appeal address and submit the appeal.
     - Note the Time Frame for Appeal (TFL) based on the type of denial (typically 365 days from the denial date).

6. **Documentation for Future Reference**
   - **Action:** Maintain records of actions taken, correspondence, and any additional paperwork related to the claim.
     - Ensure to log the claim number and any associated call references or unique identifiers.

7. **Follow Up on Appeals**
   - **Action:** Check the status of the submitted appeal within a specified time frame.
     - If resolved, update relevant parties.
     - If not resolved and another denial occurs, revisit steps 1-6 as necessary or escalate if not addressed.

### Conclusion
If at any point a new agent feels uncertain, they should consult with a senior agent or supervisor for additional guidance. Always adhere to company policy and procedures for claim submissions and appeals.""",

"Past timely filing limit" : """

**Decision Tree for Handling Claim Denials Due to Timely Filing Limits (TFL)**

1. **Claim Review**
   - Action: Review claim in relevant systems (e.g., Caretend, Payspan).
     - If information is found: Proceed to the next step.
     - If no information found: Document findings and proceed to check denial reason.

2. **Verify Denial Reason**
   - Action: Check in the claims portal/Web Portal to confirm denial reason.
     - If denial reason is confirmed as Timely Filing Expiration:
       - Proceed to "Review Timely Filing Periods."
     - If denial reason is not related to TFL: Document alternative denial reason and proceed to follow up as appropriate.

3. **Review Timely Filing Periods**
   - Action: Review claim date of service (DOS) and timely filing guidelines for the carrier.
     - If claim submission is within timely filing period based on DOS:
       - Investigate further potential issues (e.g., billing errors).
     - If claim exceeded timely filing limit:
       - Document the finding and proceed to "Check for Proof of Timely Submission."

4. **Check for Proof of Timely Submission**
   - Action: Verify submission dates in relevant portals.
     - If proof is found showing timely submission:
       - Prepare an appeal (collect necessary documentation).
     - If no proof is found:
       - Document findings and prepare to forward the claim to the client for adjustment and closure.

5. **Prepare Appeal (if applicable)**
   - Action: Gather required documentation (denial EOB, proof of submission, payer contract).
   - Action: Identify and confirm appeal mailing address.
   - Action: Submit appeal.
     - Document the submission for follow-up.

6. **Forward Claim to Client (if applicable)**
   - Action: Inform client of the denial and suggest closure or adjustments as necessary.
   - Document any client responses or further instructions.

7. **Further Review & Follow-Up**
   - Action: Monitor any responses from the payer or client regarding the appeal or adjustments.
   - If appeal is upheld or adjustments made, document the outcome.
   - If denied again, review denial reasons again and reassess next steps.

**Documentation:**
- Always document each step taken, the findings, and actions for future reference and follow-up.

By following this flowchart, new agents can systematically analyze and address claim denials related to timely filing limits, ensuring thoroughness and consistency in handling such claims.""", 

"Invoice" : """

### Decision Tree for Addressing Claim Denials Related to Missing Invoices

1. **Claim Denial Reason Identified**
   - **Is the denial due to a "Missing Invoice"?**
     - Yes: Proceed to Step 2.
     - No: Review the denial reason and follow appropriate protocol for that specific issue.

2. **Check Documentation and Claim Status**
   - **Review the claim in appropriate platforms (Payspan, caretend, etc.)**
     - Did you find any response or submission status regarding the claim?
       - Yes: Follow the documentation trail indicated in the response.
       - No: Proceed to Step 3.

3. **Search for Invoice Documentation**
   - **Check other systems for invoice copies (Cardinal, PSI, Redbook, etc.)**
     - Did you find a valid invoice copy?
       - Yes: Attach it to the appeal and proceed to Step 4.
       - No: Proceed to Step 5.

4. **Prepare and Mail Appeal**
   - **Attach the necessary documentation (EOB, AUTH, valid invoice)**
   - **Prepare appeal and mail it to the indicated address (e.g., PO BOX 811610 LOS ANGELES CA 90081)**
   - **Document the submission with timelines (TFL information) for your records.**
   - **End Process**

5. **Request Invoice Copy from Client**
   - **Task the client to obtain a valid invoice copy.**
   - **Document the communications and follow-up actions taken.**
   - **Once received, proceed to Step 4.**
   - **End Process**

6. **Claim Denial Follow-Up (if no response)**
   - **If no response is found or the appeal is denied:**
   - **Review the status in various platforms (caretend, Payspan) again.**
   - **Consider reaching out to the carrier for clarification if necessary.**
   - **End Process**

### Additional Notes:
- **For Denials with Expired Timeframes (TFL)**
  - Acknowledge that the TFL has expired, but making an appeal with the best available documentation is essential.
- **When Preparing Appeals**
  - Always ensure you reference the correct claim and denial details. Providing comprehensive documentation increases the chances of a successful appeal.
- **Documentation and Record Keeping**
  - Every step taken should be documented clearly, along with dates and the outcomes of those actions for future reference and follow-up.""",


"Duplicate Claim" : '''

### Claim Denial Decision Tree

1. **Claim Denial Identified**
   - Check the **Denial Reason**.
     - If **"Duplicate"**, proceed to the next step.

2. **Review Claim Details**
   - Look for the **Invoice Number** and **Date of Service (DOS)**.
   - Verify if the claim has been paid previously.

3. **Check Claims Status**
   - **Access Caretend Software**:
     - If payment status indicates **No Payment Received**:
       - Record your observations.
       - Move to the next step.
     - If payment status shows **Claim Paid**:
       - Confirm details against the original claim.
       - Adjust balance as necessary.
       - Conclusion: **Claim is a Duplicate, no further action needed**.

4. **Action Steps for Duplicate Claims**
   - If claim is denied due to a duplicate:
     - **Check Payspan Portal**:
       - Confirm the denial reason.
       - Record the date of denial.
     - Determine the **Original Claim**
       - If the previous claim was paid, note details.

5. **Assess Billing Errors**
   - Review the **Billing Details**:
     - If there are indications of incorrect billing (e.g., units billed separately or incorrect codes):
       - Identify the correct billing format (e.g., units per procedure).
       - Document the changes needed.

6. **Update and Correct Claims**
   - **Adjust Claim Details**:
     - Modify charged amount and units as per guidelines.
     - Add any necessary modifiers (e.g., LT RT).
   - **Prepare Corrected Claim**:
     - Ensure no prior corrected claim was submitted.
     - If necessary, prepare to submit a new corrected claim electronically.

7. **Submit Corrected Claim**
   - Electronically submit the corrected claim using the relevant web portal (e.g., Zermied).
   - Document the submission details including date and confirmation.

8. **Verification Post-Submission**
   - After submitting, check status in the portal:
     - If confirmation shows **Corrected Claim Submitted**:
       - Document and close the issue.
     - If there are issues or no submission found:
       - Address the concern and resubmit if needed.

9. **Follow-Up**
   - Set reminders or follow up on the claim status after a specified time frame (e.g., 30 days).
   - Document all actions taken for future reference.

### Ending Procedure
- If the claim continues to face issues, escalate to a senior agent or supervisor for further assistance.
- Ensure all notes are clear and accessible for future inquiries or audits.

### Notes for Ease of Use
- Keep this flowchart accessible alongside actual claim examples.
- Regularly update the process as new billing regulations or software features are introduced. 


''' ,  

"Diagnosis Code" : """

### Claim Denial Decision Tree

1. **Start**
   - Is the claim denied?

2. **Identify Denial Reason**
   - If yes, check the denial reason:
     - **Missing Diagnosis Code**
       - Action: Review claim form.
         - Are all submitted diagnosis codes correct?
           - If **Yes**: Resubmit corrected claim with missing code.
           - If **No**: Identify the missing code and resubmit.
     - **Invalid Diagnosis Code**
       - Action: Review the diagnosis codes submitted.
         - Is the diagnosis code listed valid?
           - If **Yes**: Check for supporting documents.
           - If **No**: Obtain the correct code from the provider, then resubmit.
     - **Invalid/Missing Dx Code**
       - Action: Review in Payspan or other verification system.
         - Is there a valid authorization for the provided diagnosis code?
           - If **Yes**: Forward claim to the client for further assistance.
           - If **No**: Check authorization and resubmit with valid DX code.

3. **Check Authorization**
   - Is there an existing authorization on file for the date of service (DOS)?
     - If **Yes**: Confirm authorized diagnosis codes.
     - If **No**: Contact the provider for authorization details.

4. **Review Previous Actions**
   - Have there been any previous actions taken regarding this claim?
     - If **Yes**: Review previous notes and actions to ensure no steps were missed.
     - If **No**: Proceed with initial investigation.

5. **Validation and Resubmission**
   - After addressing missing or invalid diagnosis codes:
     - Ensure the claim is filled correctly.
     - Submit the corrected claim through the appropriate channels (paper or electronic).
     - Confirm the correct mailing address is utilized if sending via paper.

6. **Follow Up**
   - After resubmission, monitor the claim status:
     - Has the claim been processed?
       - If **Yes**: Document outcomes.
       - If **No**: Follow up with the carrier or internal team.

### End

""", 

 "Authorization" : """

### Decision Tree for Handling Denied Claims Due to Authorization Issues

1. **Claim Denial Reason**
   - Check the denial reason listed on the claim.
     - **No Auth / No Auth Obtained**
     - **Authorization Does Not Cover DOS**
     - **Missing/Incompleted/Invalid Treatment Authorization Code**
     - **Missing Documents (Auth)**

2. **If Denial Reason is "No Auth / No Auth Obtained"**
   - **Check Submission History** 
     - Was the claim submitted with an authorization number?
       - **Yes:** 
         - Verify the validity of the authorization in the system.
           - **Valid Authorization Exists:** 
             - Raise an appeal with supporting documents (denied EOB, authorization sheet).
           - **No Valid Authorization:** 
             - Contact relevant parties to obtain the necessary authorization.
       - **No:** 
         - Identify if the authorization should have been obtained.
           - If it should have been:
             - Obtain authorization, then re-submit claim.

3. **If Denial Reason is "Authorization Does Not Cover DOS"**
   - **Check Authorization Validity**
     - Confirm if the authorization was valid during the Date of Service (DOS):
       - **Valid for DOS:** 
         - Prepare and submit an appeal with documentation.
       - **Not Valid for DOS:** 
         - Investigate if further authorization can be granted for this service.

4. **If Denial Reason is "Missing/Incompleted/Invalid Treatment Authorization Code"**
   - **Review Claim Submission**
     - Verify the details on the authorization code.
       - **Auth Code Confirmed Valid:** 
         - Prepare an appeal providing proof of the authorization code's effectiveness.
       - **No Valid Authorization Found:** 
         - Seek necessary documentation from the provider.

5. **If Denial Reason is "Missing Documents (Auth)"**
   - **Gather Required Documentation**
     - Review the claim’s requirements for documentation.
       - **Document Available:** 
         - Submit the missing documentation as part of the appeal.
       - **Document Not Available:** 
         - Contact the provider to request necessary documents for processing the claim.

6. **Common Actions for Appealing Denied Claims**
   - **Prepare Appeal**
     - Collect necessary documentation (denied EOB, authorization sheets, fee schedules).
   - **Confirm Appeal Submission Addresses**
     - Generally, mail to PO BOX 811610 LOS ANGELES CA 90081.
   - **Maintain Records**
     - Keep a log of the appeals including dates, reasons for denial, and responses received.

7. **Follow-Up**
   - **Post-Appeal Submission**
     - Check back with the carrier's portal after a designated time for status updates.
     - Document all interactions with carriers and responses to appeals.


"""


    }
    
    # Display the common steps and selected mapping
    st.markdown(mappings[co16_option])
    
    # Appeal Process

elif option == 'CO45':
    st.markdown("No additional information to display.")
