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
        
        ### Decision Tree for Claim Denials

        1. **Claim Denial Reason**
        - Is the claim denied due to **Authorization Issues**?
            - **Yes**: 
            - Check if there’s a valid authorization.
                - If **valid authorization exists**: Raise an appeal with the authorization and denied EOB.
                - If **no valid authorization**: Verify if the claim was submitted correctly and gather needed documentation before resubmission.
            - **No**:
            - Proceed to the next reason.

        2. **Claim Denial Reason - Missing/incomplete/invalid UPN/Serial Number**
        - Check if the correct UPN was submitted.
            - If **UPN is missing**: 
            - Review billing history for prior claims made with the same code to confirm payment precedent. 
            - Amend UPN according to submission standards and resubmit the corrected claim.
            - If **incorrect UPN**: Send corrected claim with the correct format and required documentation.
            
        3. **Claim Denial Reason - Claim/service lacks information (Denial Code 16)**
        - Review the submission for errors or missing details.
            - If information is found to be **missing**: Gather the necessary documentation and resubmit the claim.
            - If **authorization is valid**: Prepare an appeal along with the documentation explaining the oversight.
        
        4. **Claim Denial Reason - Paid but exceeds Allowed Amount**
        - Verify the allowed payment limits.
            - If **exceeds allowed amount**: Calculate the overage and adjust the claim balance.
            - If under the allowed amount, no further action is required.

        5. **Claim Denial Reason - Incorrect UPN**
        - Review the denial details.
            - Check if it was billed in the correct box.
            - If yes: Resend a corrected claim with proper UPN and fee schedule to support.
            - If no: Properly format the UPN and resubmit the claim according to guidelines.

        6. **Claim Denial Reason - Missing Authorization or Invalid Treatment Code**
        - Confirm current status of the authorization.
            - If valid authorization is in place: Prepare appeal with supporting documents (EOB, AUTH Sheet).
            - If missing: Verify need for a prior auth and follow procedures to obtain it.

        7. **Claim Denial Reason - Timely Filing Issues**
        - Determine if it’s within the filing deadline.
            - If within the timeframe: Gather evidence and prepare an appeal.
            - If **beyond timeframe**: Evaluate if exceptional circumstances exist to warrant reconsideration.

        8. **Claim Denial Reason - CO-16 - Submission Errors**
        - Identify exact submission errors.
            - If found: Correct details in the claim and resubmit.
            - If no errors are present: Review the case for previous payments to support an appeal.

        9. **Monitoring and Follow-up**
        - After submitting appeals or resubmissions:
            - **Set reminders** to follow up on the status of appeals after designated periods (30/60/90 days).
            - Ensure team members are updated on changes to claim status to enhance communication and strategy.

        ### Notes for New Agents
        - Review prior claims for patterns in denials.
        - Utilize team members’ expertise when facing unfamiliar denials.
        - Document all actions taken for future reference.
        - Stay organized and proactive in managing claims to avoid backlogs.
        """,


        'Claim lacks information': """
            ### Decision Tree for Addressing Claim Denials

            1. **Claim Status Inquiry**
            - **Action**: Review claim status in the appropriate system (Payspan, caretend, etc.)
            - **Outcome**: Identify denial reason.

            2. **Denial Reason: Missing Authorization or No Auth (AUT) Obtained**
            - **Sub-check**: Verify if authorization was submitted for the date of service.
                - **Yes**: 
                - Action: Verify validity of authorization in the system.
                - Outcome: If valid, prepare and submit appeal with authorization documentation and denied EOB.
                - **No**:
                - Action: Obtain necessary authorization and submit claim if applicable.

            3. **Denial Reason: Claim/Service Lacks Information (16)**
            - **Sub-check**: Review documentation for any missing components.
                - **Missing Treatment Authorization Code**:
                - Action: Check authorization details and prepare appeal with valid documents.
                - **Incorrect or Incomplete Billing**:
                - Action: Review submission details and correct errors. Resubmit the claim with necessary information.

            4. **Denial Reason: Paid but Exceeds Allowed Amount**
            - **Action**: Calculate allowed amount from pricing structure.
            - **Sub-outcome**: Adjust balance based on your findings.
                - **Action**: Post payment or adjust balance as necessary.

            5. **Denial Reason: Incorrect UPN (Universal Product Number)**
            - **Action**: Review designated section of the claim for UPN.
            - **Sub-check**: Verify format and correctness.
                - **Correct Format**:
                - Action: Ensure correct billing box number and conditions are followed, then resubmit.
                - **Incorrect Format**:
                - Action: Correct UPN and resubmit with updated information.

            6. **Denial Reason: Prior Authorization Expired**
            - **Action**: Verify if the authorization was valid for the date of service.
            - **Outcome**: If valid, prepare appeal documenting the valid authorization.
            - **No Valid Authorization**: 
                - Action: Forward claim to the necessary team for closure.

            7. **Claim Denial due to Timely Filing Expiration**
            - **Action**: Check the timely filing limits.
            - **Outcome**: If outside the limit, forward claim to the client for closure.
            - **Within Limits**:
                - Action: Gather documentation, and if possible, appeal for reconsideration based on valid reasons.

            8. **Finalizing Actions**
            - Ensure that all appeals, corrections, and resubmissions include detailed documentation and are sent to the correct address or portal as required.
            - Maintain follow-up procedures to verify the receipt and progress of appeals or corrections.
            - Document all findings, actions taken, and correspondence for future reference.

            ### Key Points for New Agents:
            - Always verify the claim details before taking any action.
            - Maintain clear documentation of the steps taken and ensure that appeals are sent within the required timeframes.
            - Familiarize yourself with the billing codes and authorization processes specific to your claims.
            - If in doubt, consult with more experienced team members for guidance.
                    
        """,


        "Authorization" : """
        
        ### Decision Tree for Handling Claim Denials in AR Team:

        #### 1. **Identify the Denial Reason**
        - **Authorization Issues**
            - **No Authorization Obtained**
            - Check in the system for valid authorization.
                - If valid authorization exists for the date of service:
                - **Action**: Raise appeal with the authorization proof.
                - If no valid authorization:
                - **Action**: Notify the provider or adjust the claim.
                
            - **Pre-Authorization Absent**
            - Check if pre-authorization was obtained.
                - If obtained but not recognized:
                - **Action**: Verify authorization status in the system and raise an appeal with proof.
                - If not obtained:
                - **Action**: Notify the provider to obtain authorization for future claims.

            - **Authorization Does Not Cover DOS**
            - Verify coverage period for authorization.
                - If the authorization is valid but denied for the wrong DOS:
                - **Action**: Raise an appeal including valid authorization documentation.
                - If the authorization period has expired:
                - **Action**: Notify the provider to obtain a new authorization.

        - **Insufficient Information**
            - **Claim/Service Lacks Information**
            - Review submitted documentation.
                - If relevant information can be located:
                - **Action**: Submit corrected claim or appeal including necessary details.
                - If information is missing:
                - **Action**: Collect required documents and submit an appeal.
                
            - **Missing UPN**
            - Check if the Universal Product Number (UPN) was required.
                - If UPN was not required for the specific service:
                - **Action**: Raise appeal clarifying the requirement.
                - If UPN is necessary and is absent:
                - **Action**: Request the correct UPN from the provider.
            
        - **Payment Issues**
            - **Claim Paid More than Allowed Amount**
            - Review payment details.
                - If payment exceeds limits, proceed with:
                - **Action**: Adjust balance in the system.
                - If payment is within limits but ticketed as excessive:
                - **Action**: Investigate and appeal if necessary.
                
            - **Primary EOB Required**
            - Verify if the primary insurance has been billed appropriately.
                - If no primary claim has been made:
                - **Action**: Submit primary claim and follow up for resolution.
                - If primary EOB is available:
                - **Action**: Send primary EOB as part of the appeal.
            
        #### 2. **Submission of Appeal**
        - **Prepare Documentation**
            - Collect denial EOB, authorization sheets, and any other required documents.
            - Complete necessary forms with accurate claim details.
            
        - **Determine Appeal Address**
            - Confirm the mailing address:
            - **Example**: "PO BOX 811610 LOS ANGELES, CA 90081"
            - Ensure to include a note regarding the appeal time limits.

        #### 3. **Follow-Up**
        - Mark the claim for follow-up.
        - Set reminders to check the status after the expected processing period.
        - Document all communications and actions in the system for future reference.

        ### 4. **Escalation**
        - If the claim denial is not resolved after two follow-ups:
            - **Action**: Escalate the situation to a supervisor for further assistance.""",


    
    "Past timely filing limit" : """
    ### Claim Denial Decision Tree

    1. **Identify the Denial Reason**
    - **Is the claim denied for timely filing limits?**
        - If **Yes**, proceed to verify eligibility and necessary documentation.
        - If **No**, continue to the next step.

    2. **Check Payment Status**
    - **Was the claim paid?**
        - If **Yes**:
        - **Was the paid amount within the allowed limit?**
            - If **Yes**, review payment details and adjust the balance appropriately.
            - If **No**, adjust the balance as it was paid more than allowed.
        - If **No**, proceed to the next step.

    3. **Identify Documentation Issues**
    - **Does the claim lack information?**
        - If **Yes**:
        - **Is there a valid treatment authorization code?**
            - If **Yes**, prepare an appeal with necessary documentation (EOB and AUTH sheet).
            - If **No**, check and gather required information before appealing.
        - If **No**, continue to the next step.

    4. **Review for Additional Issues**
    - **Is there a billing error or missing information in submission?**
        - If **Yes**, review the claim submission for any errors and prepare to correct them.
        - If **No**, proceed to the resolution or appeal process.

    5. **Next Steps for Appeal**
    - **Prepare appeal documentation**:
        - Include all relevant information (EOBs, authorizations, corrected claims).
    - **Submit appeal** to the designated address for further review.

    ### Conclusion:
    - After taking steps according to the decision tree and resolving the claim, ensure to **document all actions taken** for future reference and standard operating procedures. Always consult a senior agent if uncertain about a specific case.
    """, 


    "Invoice" : """
    
        ### Decision Tree for Addressing Claim Denials

        1. **Claim Denial Reason Identification:**
            - Check the **denial reason** on the claim.
            
        2. **Denial Reason: "Paid"**
            - **Action: Review payment status in Payspan/EOB**
                - **If payment was received:** 
                    - **Compare paid amount with allowed amount.**
                        - **If paid amount > allowed amount:** 
                            - Action: Adjust balance due to overpayment.
                        - **If paid amount ≤ allowed amount:**
                            - Action: No action needed; payment is within limits.
                        - **If payment not posted:** 
                            - Action: Post payment and adjust balance if under $6.00.
                        
        3. **Denial Reason: "Claim/service lacks information" (Code 16)**
            - **Action: Review claim submission.**
                - **Action: Check authorization status.**
                    - **If authorization is valid:**
                        - Action: Prepare appeal with necessary documentation (EOB and AUTH sheet), and submit appeal.
                    - **If authorization is invalid/missing:**
                        - **Next Steps:**
                            - Review claim details to identify missing information.
                            - Correct the submission errors and resubmit the claim.

        4. **Denial Reason: "Claim/service lacks information" (other than Code 16)**
            - **Action: Investigate further based on specifics.**
                - **Action: Review any additional documentation needed.**
                    - Prepare appeal if valid documentation can be provided. 
                    - Submit appeal to the designated address.

        5. **Claim Status Review**
            - **If the claim requires additional follow-up:**
                - Action: Allow time to process a claim status update.
                - Action: Verify eligibility to confirm patient's insurance coverage.

        6. **Documentation Management**
            - Ensure all actions taken are documented properly and shared within the team.
            - Update PDFs and files in the shared folder to maintain current records.

        ### Additional Notes
        - Always verify the timeline of actions taken and ensure all follow-up actions are within the designated timeframes.
        - Keep an open line of communication with other team members for any clarifications or shared insights from similar cases.""",



    "Duplicate Claim" : """ 
    
        ### Decision Tree for Handling Claim Denials

        1. **Identify Denial Reason**
        - Is the claim denied due to "Paid" status?
            - **Yes**: Proceed to Step 2.
            - **No**: Go to Step 3.
        
        2. **Claim Paid**  
        - Check the payment status in Payspan.
            - If payment was made more than the allowed amount:
            - **Action**: Calculate the allowed amount.
            - **Action**: Adjust balance.
            - If payment was made but not posted (less than $6.00):
            - **Action**: Post payment and adjust balance.
        
        3. **Claim Missing Information (Denial Reason: 16)**
        - Review claim submission.
            - If there is a submission/billing error:
            - **Action**: Check authorization status in PSI.
            - If the authorization code is valid:
                - **Action**: Prepare appeal with necessary documentation (EOB and AUTH sheet).
                - **Action**: Submit appeal.
            - If the authorization code is invalid or missing:
                - **Action**: Gather details about the missing/incomplete authorization.
                - **Action**: Re-submit the claim with the correct information.

        4. **Verify Eligibility**
        - Confirm the patient's insurance coverage.
            - If eligible:
            - Proceed with claim processing.
            - If not eligible:
            - **Action**: Communicate with the patient regarding coverage issues.

        5. **Documentation Update**
        - Ensure that all necessary documentation is updated and available.
            - **Action**: Update PDF files in the shared folder for team access.
        
        6. **Allow Time to Process**
        - After making the necessary actions (updating documentation, adjusting balance, or submitting appeals), allow time for the system to process the changes.
            - Once time has passed, **Action**: Check status updates in the system.

        ### Summary Flow
        - Start → Identify Denial Reason
        - Denial Reason = Paid → Check Payment Status → Adjust or Post Payment
        - Denial Reason = 16 (Missing Info) → Review Submission → Check Authorization → Prepare and Submit Appeal or Re-submit Claim
        - Verify Eligibility → Process Claim (if eligible) or Communicate Issues (if not)
        - Update Documentation → Allow Processing Time → Check Status """,


    "Diagnosis Code" : """
    
        ### Decision Tree for Handling Claim Denials

        1. **Determine Denial Reason:**
        - **Was the claim denied for "Lack of Information (e.g., AUTH missing or incomplete)"?**
            - **Yes:** 
            - Review claim submission for accuracy.
            - Check authorization status in PSI or MPM to find valid authorization details.
            - Prepare an appeal with necessary documentation (EOB and AUTH sheet).
            - Submit the appeal to the specified address.
            - **No: Go to next question.**

        2. **Was the claim denied as "Paid (Exceeds Allowed Amount)"?**
        - **Yes:**
            - Review payment status in Payspan or EOB.
            - Calculate the allowed amount using Cost + Percentage formula.
            - Adjust the balance as necessary since payment exceeds the allowed amount.
        - **No: Go to next question.**

        3. **Was the claim denied for "Incorrect UPN (Universal Product Number)"?**
        - **Yes:**
            - Review EOB for details on the UPN issue.
            - Submit a corrected claim with the appropriate information and fee schedule.
            - Gather and ensure all documentation is accurate for resubmission.
        - **No: Go to next question.**

        4. **Was the claim denied due to "No Authorization (AUT) or Pre Auth Absent"?**
        - **Yes:**
            - Check in Payspan and Zirmed for denial details.
            - Look for valid authorization in PSI.
            - If there is a valid auth, raise an appeal with the authorization and EOB.
        - **No: Go to next question.**

        5. **Was the denial due to "Claim lacks Documentation"?**
        - **Yes:**
            - Verify eligibility and insurance coverage.
            - Update necessary documentation and files in the shared folder for team access.
            - Allow time to process and check for updates on the claim status.
        - **No:** 
            - **Not in the Given Scenarios.** Seek escalation if the reason is unclear.

        ### Tips for New Agents:
        - Always confirm the specific denial reason as a starting point.
        - Ensure proper documentation is collected: EOB, authorization details, corrected claim forms, etc.
        - Document all communications and actions taken for accountability and follow-up purposes.
        - Use the specified appeal mailing addresses accurately.
        - If unsure, consult with more experienced team members or escalate cases as needed.
        """, 

    
    "Incorrect Modifier": """
    
        ### Decision Tree for Addressing Claim Denials

        1. **Claim Denial Reason Identified**
        
        a. **Denial Reason: "Paid"**
        
        - **Sub-Scenario 1: Paid More Than Allowed Amount**
            - Action: **Review in Payspan**
                - Reason: Verify the payment status and details.
            - Action: **Calculate Allowed Amount**
                - Reason: Determine if the payment was within allowed limits.
            - Action: **Adjust Balance**
                - Reason: Adjust balance since the claim was paid more than the allowed amount.
        
        - **Sub-Scenario 2: Paid Amount Below Minimum Posting Threshold**
            - Action: **Review in Payspan EOB**
                - Reason: Check the payment status and details.
            - Action: **Calculate Paid Amount**
                - Reason: Verify the payment calculation.
            - Action: **Post Payment and Adjust Balance**
                - Reason: Balance was not posted due to being less than $6.00, hence adjust accordingly.
        
        b. **Denial Reason: "Claim/service lacks information" (Denial Code 16)**
        
        - Action: **Review Claim Submission**
            - Reason: Identify the reason for denial and verify submission errors.
        - Action: **Check Authorization Status in PSI**
            - Reason: Verify if the treatment authorization code is valid.
        - Action: **Prepare Appeal**
            - Reason: Provide necessary documentation (EOB and AUTH sheet).
        - Action: **Submit Appeal to Designated Address**
            - Reason: Formally appeal the claim denial.

        2. **Additional Scenarios**

        a. **Eligibility Issues**
        
        - Action: **Verify Eligibility**
            - Reason: Confirm the patient's insurance coverage.
        
        b. **Documentation Updates**
        
        - Action: **Update PDF in Shared Folder**
            - Reason: Ensure all team members have access to the latest documentation.

        c. **Processing Time**
        
        - Action: **Allow Time to Process**
            - Reason: Give the system time to update the claim status."""


    }
    
    # Display the common steps and selected mapping
    st.markdown(mappings[co16_option])
    
    # Appeal Process

elif option == 'CO45':
    st.markdown("No additional information to display.")
