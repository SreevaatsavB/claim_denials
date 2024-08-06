import streamlit as st

st.markdown("# Claim denials (V4)")
# First dropdown for CO16 and CO45
option = st.selectbox('Select an option', ['CO16', 'CO45'])

if option == 'CO16':
    # Second dropdown for CO16 options
    co16_option = st.selectbox('Select a denial reason', [
        "",
        'UPN',
        "Claim lacks information",
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
        'UPN': """

### Claim Denial Handling Flowchart

1. **Start**
    - Identify Claim Denial Reason

2. **Denial Reason: Missing UPN**
    - **Action Steps:**
        - Review payspan for denial details.
        - Check medical portal for missing UPN.
        - Confirm payment history to see if code was paid without UPN.
        - **If UPN found**: Resubmit corrected claim with appropriate documentation.
        - **If UPN not found**: Raise an appeal with required documents (invoice, contract).

3. **Denial Reason: Invalid UPN**
    - **Action Steps:**
        - Check claim form and UPN against fee schedule.
        - Correct UPN in software or submit as per the correct item.
        - Submit a corrected claim with the valid UPN.
        - **If UPN was initially incorrect**: Resubmit with the correct box#.
        - **If UPN format issue**: Resubmit claim with the required format and fee schedule.

4. **Denial Reason: Incorrect UPN**
    - **Action Steps:**
        - Review payspan and check previous corrections.
        - Verify UPN against the current fee schedule.
        - Prepare and send a corrected claim to the appropriate address.
        - Raise an appeal if previous claims were not posted or processed.

5. **Denial Reason: General Documentation Issues**
    - **Action Steps:**
        - Verify what specific documentation is missing or incorrect.
        - Check EOBs (Explanations of Benefits) for details on necessary corrections.
        - Prepare an appeal or resend corrected claim with the required documentation.
        - Follow up with the insurance representative for clarity.

6. **After Claim Resubmission**
    - **Action Steps:**
        - Keep track of resubmitted claims and monitor for updates.
        - Document all communication with insurance representatives.
        - Use proper mailing addresses and ensure timely submissions (within 1 year for appeals).

7. **Final Steps: Monitor and Follow Up**
    - Track all appeals and corrected claims.
    - Maintain logs of claims and appeals for reporting and auditing purposes.
    - If there are repeated issues with UPNs for the same code, consider consulting internal policy for potential overrides.

8. **End**
    - Ensure consistency and accuracy in future claim submissions to minimize denials.
        """,


        "Incorrect Modifier" : """
  
### Claim Denial Handling Flowchart

1. **Claim Denial Received**  
   - Identify the denial reason (e.g., Incorrect Modifier, Missing Modifier).

2. **Review Claim Information**  
   - Check the **Claim Number** and **Date of Service (DOS)**.
   - Review details like **HCPCS code** and **invoice number**.

3. **Verify Claim Status**  
   - **Action:** Review in CareTend  
     - **Reason:** Verify payment status.  
     - **Details:** Was payment received?  
   - If payment not received, proceed to the next step.

4. **Check Additional Resources**  
   - **Action:** Check Payspan and Zermied web portals  
     - **Reason:** Confirm claim status and submitted modifiers.  
     - **Details:** Flag any inconsistencies with modifiers.

5. **Identify Previous Submissions**  
   - **Action:** Check for previously submitted claims  
     - **Reason:** Determine if a corrected claim was sent.  
     - **Details:** Was it received/processed correctly?

6. **Determine Modifier Requirements**  
   - **Action:** Confirm client’s updates on modifier requirements  
     - **Reason:** Ensure compliance with billing guidelines.  
     - **Details:** Are specific modifiers required for particular procedure codes?

7. **Correct Modifiers Based on Findings**  
   - If modifier errors are identified, prepare to submit corrected claims. 

8. **Submit Corrected Claims**  
   - **Action:** Change and resubmit the claim electronically  
     - **Reason:** Rectify incorrect or missing modifiers.  
     - **Details:** Include the original claim number and note any resubmission codes if applicable.

9. **Follow-Up**  
   - **Action:** Monitor the status of the newly submitted claims  
     - **Reason:** Ensure they are processed correctly.  
   - If further denials occur, return to Step 3.

10. **Document Actions Taken**  
   - Maintain detailed notes on each step taken to resolve the claim denial for future reference.

### Additional Scenarios:
- **Duplicate Claims:** Check if the claim was flagged as a duplicate and rectify the issue before resubmission.
- **Incorrect Modifier Submission:** Look into modifying the procedure code and resubmitting, ensuring compliance with current guidelines.

By following this flowchart, new agents can systematically address claim denials and ensure a thorough and efficient resolution process.

""",


"Claim lacks information" : """

### Flowchart for Handling Claim Denials due to Lack of Information

1. **Initial Claim Review**
   - Review the denial reason:
     - If denial reason is "Claim/service lacks information" or "Missing information (16)":
       - Proceed to Claim Verification.

2. **Claim Verification**
   - Check the submitted claim details in the portal:
     - Verify DOS (Date of Service), HCPCS code, and authorization code.
     - If information is missing or invalid:
       - Identify specific missing details (e.g., authorization code, Universal Product Number).

3. **Authorization Status Check**
   - Check the authorization status in the relevant software/system:
     - **If valid authorization found**:
       - Proceed to prepare and file an appeal.
     - **If no valid authorization found**:
       - Confirm if an authorization document exists.

4. **Preparation for Appeal**
   - Gather the necessary documentation:
     - EOB (Explanation of Benefits)
     - Valid AUTH sheets
   - Verify the appeal submission address:
     - Most appeals submitted to: **PO BOX 811610 LOS ANGELES CA 90081**
   - Prepare the appeal letter including:
     - Details of the claim, denial reason, and supporting documents.

5. **Submission of Appeal**
   - Submit the appeal to the designated address.
   - Document the submission, including date and any tracking information.

6. **Follow-up Actions**
   - If no response received after the expected timeframe:
     - Follow up with the carrier or billing department for the status.

7. **Record Keeping**
   - Maintain detailed records of:
     - Original claim details
     - Denial reasons
     - Appeal submission and responses for future reference.
  
### Special Scenarios to Handle:
- **Invalid Authorization**
  - If the authorization is not valid for DOS:
    - Identify if retro authorization can be obtained.
    - If not, adjust the claim as necessary.

- **Missing Authorization Documentation**
  - Contact the provider (e.g., medical group) to obtain the missing authorization information.

- **Duplicate Claims**
  - Check for duplicate claims linked to the initial denial.
  - Address discrepancies if found and proceed with appropriate claims or appeals.

- **Lost or Unresponsive Claims**
  - If no responses are found in the system:
    - Re-check previous claims for similar issues.
    - Contact carrier representatives for clarification.

By adhering to this flowchart, new agents can efficiently navigate the complexities of claim denials related to information gaps, ensuring proper follow-up and resolution procedures are executed.""",

"Past timely filing limit" : """

### Flowchart for Addressing Claim Denials Due to Timely Filing Limits (TFL)

1. **Initial Claim Review**
   - **Action:** Review the claim in Caretend 
     - **Details:** Check claim status and submission details.
   - **Next Step:** Verify Denial Reason.

2. **Verify Denial Reason**
   - **Action:** Check in the web portal (e.g., LA CARE, Payspan)
     - **Details:** Confirm the reason for denial.
   - **Next Step:** Assess Timely Filing Period.

3. **Assess Timely Filing Period**
   - **If Denied due to Timely Filing Expiration:**
     - **Details:** Determine the Date of Service (DOS) and the filing limit (180 days for LA CARE).
     - **Next Step:** Confirm Receipt Date.
   - **If Claim Still Valid:**
     - **Next Step:** Prepare for resubmission or appeal.

4. **Confirm Receipt Date**
   - **Action:** Review claim submission dates
     - **Details:** Verify initial billing dates.
   - **Next Step:** Determine Action Based on Findings.
   
5. **Determine Action Based on Findings**
   - **If Submission was within the Filing Limit:**
     - **Details:** There may be grounds for appeal/resubmission.
     - **Next Step:** Prepare Appeal Documentation.
   - **If Submission was Past the Filing Limit:**
     - **Next Step:** Forward claim to Client for Adjustment.

6. **Prepare Appeal Documentation**
   - **Actions:**
     - Gather supporting documentation (denied EOB, invoice copies).
     - Identify appeal mailing address.
   - **Next Step:** Submit Appeal.

7. **Client Adjustment Approval**
   - **Action:** Task client for approval on necessary adjustments.
   - **Next Step:** Await Client Feedback.

8. **Final Steps**
   - **If Client Approves Adjustments:** Resubmit Claim.
   - **If Client Denies Adjustments:** Document outcome and close the claim.

### Note:
- Throughout the process, keep a record of all actions taken and maintain communication with involved parties (clients, carriers).
- Familiarize yourself with claim submission timelines and specific carrier guidelines to effectively address denials. 

This flowchart summarizes the steps agents have taken in various scenarios regarding claim denials due to Timely Filing Limits.


""",

"Missing Invoice" : """

### Claim Denial Handling Flowchart for Missing Invoices

1. **Claim Denial Identification**
   - Check claim notes for denial reason: **Missing Invoice**.

2. **Initial Review**
   - **Action**: Review in Payspan, Caretend, and relevant portals.
     - **Details**: Confirm the denial reason and check for any recorded responses.

3. **Document Verification**
   - **Action**: Check for existing invoice copies or similar claims.
     - If invoice found:
       - Retrieve and verify documentation.
       - Proceed to **Prepare Appeal**.
     - If no invoice found:
       - **Action**: Task client to obtain the invoice copy or check alternative documentation locations like Redbook.

4. **Prepare Appeal**
   - **Action**: Attach necessary documentation:
     - Include Denied EOB (Explanation of Benefits).
     - Attach Auth documentation if applicable.
     - Include any invoice copies found during verification.
   - **Details**: Ensure all documents that support the claim are included.

5. **Mail the Appeal**
   - **Action**: Raise and mail the appeal.
     - **Address**: PO BOX 811610, LOS ANGELES, CA 90081.
   - Provide necessary timelines (TFL) for appeal (e.g., **365 DAYS FROM RECENT DENIAL DATE**).

6. **Follow Up**
   - After submission, follow up for responses:
     - Check in Caretend and other relevant systems for updates on the appeal status.
     - Note any responses or further actions needed.

### Potential Scenarios:

- **Scenario 1**: Valid invoice copy exists.
  - Retrieves and attaches invoice for appeal.

- **Scenario 2**: No valid documents available.
  - Tasks client to fetch the necessary invoice.

- **Scenario 3**: Claim has expired TFL.
  - Note expiration but attempt to appeal if there are valid reasons (e.g., miscommunication).

- **Scenario 4**: Auth documentation exists.
  - Use for supporting the appeal, especially if the denial reasons relate to authorization.

### Final Notes:
- Always document actions taken, and reasons for each step to ensure clarity and traceability.
- Collaborate with team members if uncertain about specific processes or if additional help is needed. 


""",

"Duplicate Claim" : '''

### Flowchart for Addressing Claim Denials for Duplicates

1. **Claim Received**
   - Identify the denial reason as "Duplicate."

2. **Initial Review**
   - **Action:** Review claim in Caretend or Payspan.
     - **If payment received:** 
       - Note the payment details and claim number that the denied claim duplicates.
       - **Action:** Adjust balance and close the claim.
     - **If no payment received:** 
       - Proceed to check for details of the original claim.

3. **Find Original Claim**
   - **Action:** Check original claim status.
     - **If original claim is found and paid:** 
       - Document the invoice and payment information.
       - **Action:** Adjust balance for the duplicate.

4. **Check for Billing Errors**
   - **Action:** Determine if there is a billing error (e.g., incorrect units billed).
     - **If billing error exists:** 
       - **Action:** Prepare a corrected claim:
         - Change the charged amount (e.g., update from a single unit to 2 units).
         - Add necessary modifiers (e.g., LT/RT).
         - Ensure all details conform to billing guidelines.
     - **If no billing error:** 
       - Confirm no additional actions required.

5. **Submit Corrected Claim**
   - **Action:** Submit the corrected claim electronically via specified web portal (e.g., Zermied).
   - **If previously attempted submission noted:** Verify the status of the submission.
     - **If no record found:** Resubmit the corrected claim.
     - **If original submission found:** Update and ensure compliance with billing guidelines.

6. **Follow-Up Actions**
   - **Action:** Check for TFL (Time Frame Limit) duration for submission.
   - **If within TFL:** Proceed with appeals as necessary.
   - **If outside TFL:** Document and close the investigation on this claim.

7. **Document Actions and Outcome**
   - Ensure all actions taken, including reasons and details of the findings, are accurately recorded in the claim notes for future reference.

### Summary
This flowchart guides agents through the process of handling claims denied due to duplication, starting from initial review to resolving billing errors and resubmitting corrected claims. It emphasizes checking for details of initial claims and following up with appropriate actions based on findings.

''' ,  

"Diagnosis Code" : """

**Flowchart for Handling Claim Denials Related to Diagnosis Codes**

1. **Claim Denial Identification**
   - Check claim notes for denial reason.
   - Identify the specific denial reason: 
     - Missing Diagnosis Code
     - Invalid/Missing Diagnosis Code
     - Incorrect Diagnosis Code

2. **Initial Actions for All Denials**
   1. **Review Claim in Payspan Portal**
      - Determine the exact reason for the denial.
   2. **Check Authorization Status**
      - Verify if the authorization was active for the date of service (DOS).
   3. **Verify Diagnosis Codes in Authorization**
      - Confirm which diagnosis codes were approved.

3. **Specific Actions Based on Denial Reason**
   - **If Denial Reason is "Missing Diagnosis Code":**
     - **Review Claim Form**
       - Identify any discrepancies in submitted DX codes.
     - **Identify Missing Diagnosis Code**
       - Determine which diagnosis code was not included.
     - **Submit Corrected Claim**
       - Include the missing diagnosis code and submit a corrected claim on paper.

   - **If Denial Reason is "Invalid/Missing Diagnosis Code":**
     - **Check Submitted DX Code**
       - Verify the DX code submitted with the claim.
     - **Search for Validation Documents**
       - Look for documents that can validate the DX code.
     - **Forward Claim to Client**
       - If no validation is found, seek further assistance from the client.

   - **If Denial Reason is "Incorrect Diagnosis Code":**
     - **Review Patient Documents and Payment History**
       - Identify the correct diagnosis code for the claim.
     - **Resubmit Claim with Correct Code**
       - Update the diagnosis code and resubmit the claim.
     - **Correct Claim Mailing Address**
       - Ensure the claim is sent to the correct address for processing.

4. **Follow-up Actions**
   - Confirm the status of the resubmitted claim in Payspan or the respective portal used.
   - Maintain communication with the client for ongoing issues or missing information regarding submitted codes.

5. **Documentation**
   - Document all actions taken and communications for future reference and follow-up.

This flowchart provides a structured approach for new agents to effectively manage claim denials related to diagnosis codes, ensuring that they follow standard procedures based on the specific denial situation.

""", 

 "No Authorization" : """

### Claim Denial Handling Flowchart

1. **Claim Denied for Lack of Authorization**
   - **Is there a valid authorization number?**
     - **Yes → Go to Step 2**
     - **No → Raise Appeal for Lack of Authorization**

2. **Verify Claim in Payspan/Claims Portal**
   - **Is the denial reason due to missing/incomplete/invalid authorization code?**
     - **Yes → Go to Step 3**
     - **No → Check Billing History and Provider Portal for Other Issues**

3. **Check System for Submitted Authorization**
   - **Is the authorization valid and active for the Date of Service (DOS)?**
     - **Yes → Prepare Appeal Documentation**
     - **No → Contact the Provider to Obtain Necessary Authorization**

4. **Prepare Appeal Documentation**
   - **Include:**
     - Denied Explanation of Benefits (EOB)
     - Authorization Sheet
     - Fee Schedule
   - **Submit Appeal to Appropriate Address**

5. **If Claim Denied Due to Prior Authorization Issues**
   - **Verify patient's active insurance coverage during DOS.**
     - **If coverage exists → Prepare Appeal**
     - **If no coverage → Forward Claim to AR EV Team for Further Action**

6. **If an Agent Contacted the Carrier**
   - **Verify if the representative confirmed the denial can be contested.**
     - **Yes → Use information provided as grounds for appeal**
     - **No → Document details and continue with appeal preparation**

7. **If Claim Denial Source is Ambiguous**
   - **Check for Previous Payments for the Same Code**
     - **If payment exists → Contact Carrier for Reprocessing**
     - **If no payment exists → Document and Proceed to Appeal**

### Summary Steps for Appeal Submission
- Always verify the authorization's valid date range and presence prior to submitting an appeal.
- Maintain thorough documentation for each step taken in the process for potential follow-ups.
- Use standardized forms for appeal submission to ensure all necessary details are included.

This flowchart is designed to guide AR team members in systematically addressing claim denials due to authorization issues based on previous effective resolution pathways.

""", 

"Authorization Code Does Not Cover DOS" : """

1. **Claim Denial Received**  
   - Denial Reason: "Authorization obtained does not cover DOS"

2. **Initial Review of Claim**  
   - Action: Review claim submission  
   - Reason: To determine the reason for denial  
   - Result: Noted related codes (e.g., Claim/service lacks information)

3. **Check Authorization Validity**  
   - Action: Check PSI or relevant system for authorization details  
   - **Decision Point:** Is there a valid authorization for the Date of Service (DOS)?  
     - **Yes:** Proceed to prepare the appeal.  
     - **No:** Move to contacting the provider.

4. **If Valid Authorization Exists**  
   - Action: Prepare Appeal  
     - Gather necessary documentation (e.g., AUTH sheet, Explanation of Benefits (EOB))
     - Submit appeal to the corresponding address.
   - **End Process**
   
5. **If No Valid Authorization Exists**  
   - Action: Contact Provider (e.g., AXMINSTER MEDICAL GROUP)  
   - Result: Obtain missing authorization details or AUTH sheet.

6. **Check for Recent Authorizations**  
   - Action: Verify if recent authorization is valid  
   - **Decision Point:** Is the obtained authorization valid for the DOS?
     - **Yes:** Prepare and submit the appeal with the new authorization documentation.
     - **No:** Consider gathering supporting evidence; assess options for resolving the issue directly with the payer.

---

### Additional Scenarios to Consider:

- **Multiple DOS Issues**  
  If multiple claims for different DOS are received, repeat the flow from step 2 for each claim, noting the specific details for each one.

- **Appeal Timelines**  
  Always note appeal time frames for each case. Generally, timelines may be 1 year from denial date unless otherwise stated.

- **Contact Follow-Ups**  
  Ensure to document all contacts with providers or payers, including names of representatives spoken to and details of the conversation.

- **Documentation**  
  Keep copies of all appeals sent and received, maintaining a log to track the status of each claim.

---

This flowchart provides a step-by-step guide for addressing authorization-related claim denials, ensuring that new agents can efficiently navigate the appeals process while ensuring thorough documentation and communication at each step.

""", 

"Missing Documentation (Authorization)" : """

### Claim Denial Flowchart for Missing Documentation (Authorization)

1. **Claim Denial Identified**
   - Check if the claim is denied due to "missing documents (Auth)" or similar reasons.

2. **Review Claims Submission**
   - Action: Review claim submission in claims processing software.
   - Reason: To verify that the claim was submitted to the correct carrier.

   **If submission is verified:**
   - Move to Next Step.

3. **Check Claim Status**
   - Action: Check Payspan or other claim status tools.
   - Reason: To determine the status of the claim and details of the denial.

   **If denied for missing info or authorization:** 
   - Proceed to seek documentation.

4. **Verify Authorization Details**
   - Action: Check PSI (or equivalent) for valid authorization.
   - Reason: To find any existing valid authorization for the date of service.

   **If valid authorization is found:**
   - Move to Prepare Appeal.
   
   **If no valid authorization is available:**
   - Action: Check caregiver or submitter for valid auth documentation.

5. **Prepare Appeal**
   - Action: Compile necessary documents including:
     - Valid authorization (if found)
     - Explanation of benefits (EOB) from initial claim.
   - Reason: To contest the denial based on available documentation.

6. **Submit Appeal**
   - Action: Mail appeal to the appropriate address (e.g., PO BOX 811610 LOS ANGELES CA 90081).
   - Reason: Final step to contest the denial officially.

7. **Follow-up Actions**
   - Action: Monitor the status of the appeal submission through the claims processing software or payer portal.
   - Reason: To ensure the appeal is processed and to respond to any further requests for information.

---

### Additional Scenarios

- **Denied for Authorization Code (but valid authorization exists):**
  - Emphasize the need to submit a specific appeal highlighted on the authorization code issue.

- **Claim with Invalid Authorization Found:**
  - Check validity in Waystar or equivalent.
  - Prepare appeal including explanation of invalidity and supporting documentation.

- **Claim Resubmit after Client Interaction:**
  - If client submits the required authorization after initial denial, ensure proper re-submission protocols follow.

### Important Notes
- Always document each step taken, reasons for actions, and details about communications with clients or carriers.
- Maintain a record of feedback received from payer representatives during calls for better future submissions.


""", 

"Prior Authorization Needed" : """

### Flowchart for Handling Claim Denials due to Prior Authorization

1. **Claim Denied**
   - Identify the **Denial Reason** (e.g., "Lack of information," "Prior Authorization Not Found," etc.)

2. **Check Claim Status**
   - Review in **Caretend** for submission status and details.
   - Check **Provider Portal** or **Payspan** for detailed denial reasons.

3. **Determine Authorization Status**
   - Look for required authorizations:
     - Search in **PSI** for valid authorization documentation.
     - If **valid authorization exists**:
       - Proceed to **Prepare Appeal**.
     - If **authorization is missing**:
       - Update authorization details if a valid one is found.
       - Submit corrected claim electronically with the updated authorization.

4. **Prepare Appeal Documentation**
   - Gather necessary documents:
     - Authorization number(s).
     - EOB (Explanations of Benefits).
     - Any previous payment EOB if applicable.
   - Complete the appeal form and ensure all documents are attached.

5. **Submit Appeal**
   - Send appeal to appropriate address (e.g., "PO BOX 811610 LOS ANGELES CA 90081").
   - Note the **Time Limit for Appeal** (typically 365 days from the recent denial date).

6. **Follow-Up**
   - Monitor the status of the appeal using the Claim Portal or designated system.
   - Document any further communications or updates regarding the appeal.

### Special Cases

- **Multiple HCPCS Codes**:
   - Ensure each code has a valid authorization.
   - If authorizations differ per code, document each scenario in the appeal.

- **Previous Claims Paid**:
   - If previous claims for the same service were approved, include these details in the appeal to strengthen the case.

- **Recurrent Denials**:
   - Analyze the reasons behind recurring denials and update processes or documentation accordingly to avoid future mistakes.

By following this flowchart, new agents in the AR team can systematically address claim denials related to prior authorization and resolve claims effectively.

""",

"Incorrect / Missing Modifier" : """

### Claim Denial Handling Flowchart

1. **Claim Denial Received**  
   - Identify the denial reason (e.g., Incorrect Modifier, Missing Modifier).

2. **Review Claim Information**  
   - Check the **Claim Number** and **Date of Service (DOS)**.
   - Review details like **HCPCS code** and **invoice number**.

3. **Verify Claim Status**  
   - **Action:** Review in CareTend  
     - **Reason:** Verify payment status.  
     - **Details:** Was payment received?  
   - If payment not received, proceed to the next step.

4. **Check Additional Resources**  
   - **Action:** Check Payspan and Zermied web portals  
     - **Reason:** Confirm claim status and submitted modifiers.  
     - **Details:** Flag any inconsistencies with modifiers.

5. **Identify Previous Submissions**  
   - **Action:** Check for previously submitted claims  
     - **Reason:** Determine if a corrected claim was sent.  
     - **Details:** Was it received/processed correctly?

6. **Determine Modifier Requirements**  
   - **Action:** Confirm client’s updates on modifier requirements  
     - **Reason:** Ensure compliance with billing guidelines.  
     - **Details:** Are specific modifiers required for particular procedure codes?

7. **Correct Modifiers Based on Findings**  
   - If modifier errors are identified, prepare to submit corrected claims. 

8. **Submit Corrected Claims**  
   - **Action:** Change and resubmit the claim electronically  
     - **Reason:** Rectify incorrect or missing modifiers.  
     - **Details:** Include the original claim number and note any resubmission codes if applicable.

9. **Follow-Up**  
   - **Action:** Monitor the status of the newly submitted claims  
     - **Reason:** Ensure they are processed correctly.  
   - If further denials occur, return to Step 3.

10. **Document Actions Taken**  
   - Maintain detailed notes on each step taken to resolve the claim denial for future reference.

### Additional Scenarios:
- **Duplicate Claims:** Check if the claim was flagged as a duplicate and rectify the issue before resubmission.
- **Incorrect Modifier Submission:** Look into modifying the procedure code and resubmitting, ensuring compliance with current guidelines.

By following this flowchart, new agents can systematically address claim denials and ensure a thorough and efficient resolution process.

"""
    }
    
    # Display the common steps and selected mapping
    st.markdown(mappings[co16_option])
    
    # Appeal Process

elif option == 'CO45':
    st.markdown("No additional information to display.")
