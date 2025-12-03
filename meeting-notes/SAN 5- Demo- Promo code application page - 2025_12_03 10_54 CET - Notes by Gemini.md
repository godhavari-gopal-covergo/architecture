# 📝 Notes

Dec 3, 2025

## SAN 5- Demo- Promo code application page

Invited [NGHIEM EMMA](mailto:e.nghiem@santevet.com) [f.degravel@santevet.com](mailto:f.degravel@santevet.com) [a.pujo@santevet.com](mailto:a.pujo@santevet.com) [Quentin MASSON-PILET](mailto:qmassonpilet@valthena.com) [Alex Montgomery](mailto:alex@covergo.com) [Yashpal Deswal](mailto:yashpal.deswal@covergo.com) [Trideep Roy](mailto:trideep.roy@covergo.com) [Eugena Russell](mailto:eugena.russell@covergo.com) [a.anne@santevet.com](mailto:a.anne@santevet.com) [v.javaux@santevet.com](mailto:v.javaux@santevet.com) [Ahmad Elkassaby](mailto:ahmad.elkassaby@covergo.com) [Kate Oconer](mailto:kate.oconer@covergo.com) [NATHANAEL G'BAMY](mailto:n.gbamy-ext@santevet.com) [Godhavari Gopal](mailto:godhavari.gopal@covergo.com)

Attachments [SAN 5- Demo- Promo code application page](https://www.google.com/calendar/event?eid=MGZlNW1taGtwc3ZvNnA4MjFpdGZ0NGo3YTggYWhtYWQuZWxrYXNzYWJ5QGNvdmVyZ28uY29t) 

Meeting records [Transcript](?tab=t.24xgt2xtsyk) File 

### Summary

Kate Oconer demonstrated the promo code functionality on the proposal screen, which validates codes against Talon one, allows users to apply up to five codes, and includes a "View Code List" for tracking valid, invalid, and removed codes. Following a discussion, Kate Oconer agreed to limit promo codes to one per quotation, and NATHANAEL G'BAMY committed to checking the rules for combining promo and referral codes, while Kate Oconer clarified that the system does not support automatic code application and that only one valid referral code is allowed per quotation. EMMA NGHIEM inquired about displaying common promotions with future effects, such as free months, and Kate Oconer explained that the quotation's "Total Discount" only reflects immediate impacts, with future effects stored and applied via a job run, which NATHANAEL G'BAMY confirmed are based on statuses received from Talon one. Quentin Pilet and Yashpal Deswal questioned the promo code budget responsibility, which FABIEN DEGRAVEL confirmed is covered by the marketing budget, leading EMMA NGHIEM and NATHANAEL G'BAMY to agree to confirm internally if family discounts are adjusted against the SET marketing budget.

### Details

*Notes Length: Standard*

* **Promo Code Functionality on Proposal Screen** Kate Oconer demonstrated the promo code entry feature on the Cover Health proposal/quotation screen, which allows users to enter a promo code that is validated against talent one and displayed in the premium breakdown ([00:00:00](#00:00:00)). They clarified that some promo codes have a future effect and will be listed as valid in the breakdown even if they don't have an immediate monetary amount ([00:01:13](#00:01:13)). Users can add up to five promo codes per quotation, and the system prevents adding more if five valid codes are already applied ([00:02:27](#00:02:27)).

* **Managing Promo Codes and Code List** Kate Oconer explained the \`View Code List\` feature, which displays all codes, including valid, invalid, and removed ones, to assist customer service in tracking issues raised by customers ([00:03:51](#00:03:51)). They showed that users can remove promo codes and must enter a reason for removal for tracking purposes, with the removal description being visible on the code list ([00:04:59](#00:04:59)). NATHANAEL G'BAMY questioned if the system could be personalized to allow only one promo code per quotation and if automatic code application based on parameters, such as the family VIP code for two animals, was possible ([00:06:17](#00:06:17)).

* **Promo Code and Referral Code Limitations** Following a discussion with NATHANAEL G'BAMY, Kate Oconer agreed to limit promo codes to one per quotation, while NATHANAEL G'BAMY committed to checking the specific rules regarding the combination of promo and referral codes in a single quotation and reporting back ([00:07:38](#00:07:38)). Kate Oconer confirmed that the system does not currently support the automatic application of promo codes based on parameters, as the promo codes must always be explicitly passed. For referral codes, the system limits users to only one valid referral code per quotation, following a flow similar to promo codes ([00:08:45](#00:08:45)).

* **Display of Promo Codes in Policy Screen and Future Effects** Kate Oconer detailed that on the policy screen, all valid promo codes for the particular policy are displayed in the premium section, with an option to view the code list to see which codes were applied, removed, or invalid ([00:10:11](#00:10:11)). They explained that future effects from promo codes are handled by a job run which checks policies, applies effects when conditions are met, and updates the status to show that the effect has been used ([00:11:35](#00:11:35)). NATHANAEL G'BAMY confirmed that the "valid" and "invalid" statuses are received directly from Talon one ([00:13:07](#00:13:07)).

* **Handling Specific Promo Use Cases and Display on Quotation** EMMA NGHIEM inquired about displaying common promotions, such as three months offered on the first year (one month free initially and two months free at the end of the year), as they felt the 10% discount example was unrealistic. Kate Oconer explained that the one-month free would be a direct impact calculated on the quotation, while the future two-month free effect would be stored and applied later via a job run ([00:15:33](#00:15:33)). A discussion followed regarding whether the total discount shown on the quotation should include the value of the future free months ([00:16:49](#00:16:49)).

* **Discount Display on Quotation vs. Transactions** Kate Oconer clarified that the \`Total Discount\` displayed on the quotation is only for what is applied immediately on that calculation or initial payment, and not for future effects like the 11th and 12th months being free ([00:17:59](#00:17:59)). EMMA NGHIEM expressed interest in seeing a demonstration with their specific use cases, such as the family VIP code, which offers the 11th month free for the second animal, as they primarily use mechanisms other than simple percentage discounts ([00:19:16](#00:19:16)). Kate Oconer confirmed that for future effects like the family VIP code, the quotation would only show the description without a monetary value, which indicates it is pending the job run at the appropriate time ([00:22:18](#00:22:18)).

* **Promo Code Budget Responsibility and Feature Status** Quentin Pilet and Yashpal Deswal inquired about which entity, SET or the insurer, covers the cost of promo codes and their impact on the premium schedule ([00:23:29](#00:23:29)). FABIEN DEGRAVEL confirmed that the cost of promotions is covered by the marketing budget ([00:24:54](#00:24:54)). EMMA NGHIEM and NATHANAEL G'BAMY agreed to follow up internally to confirm whether the cost for family discounts, which are similar to one-month offers, is adjusted against the SET marketing budget ([00:27:43](#00:27:43)). Kate Oconer confirmed that the promo code feature is still a work in progress, with an expected launch by the end of the next sprint ([00:28:41](#00:28:41)). They agreed to share the Figma design link with the team for a deeper review ([00:30:18](#00:30:18)).

### Suggested next steps

- [ ] NATHANAEL G'BAMY will check the combination of promo and referral code in one quotation, get back to Kate Oconer with the specific rules on the DIT, and check internally regarding the family discount's impact on the insurer and the marketing budget of Santa.  
- [ ] Yashpal Deswal will send the question about the insurer impact or budget to NATHANAEL G'BAMY.

*You should review Gemini's notes to make sure they're accurate. [Get tips and learn how Gemini takes notes](https://support.google.com/meet/answer/14754931)*

*Please provide feedback about using Gemini to take notes in a [short survey.](https://google.qualtrics.com/jfe/form/SV_9vK3UZEaIQKKE7A?confid=piyonUFGy9cIl9J9e36BDxIQOAIIigIgABgDCA&detailid=standard)*

# 📖 Transcript

Dec 3, 2025

## SAN 5- Demo- Promo code application page \- Transcript

### 00:00:00 {#00:00:00}

   
**Ahmad Elkassaby:** and then um I'll hand over to Kate in order to  
**Kate Oconer:** Um, let me share my screen. Let me know if you can see it.  
**quentin pilet:** Yeah.  
**Kate Oconer:** Okay, perfect.  
**NATHANAEL G'BAMY:** Uh yeah.  
**Kate Oconer:** Okay, so um can I turn off my camera to save some um bandwidth? Okay. So I think most of you have seen if not yet um how cover uh cover health is with regards to how we have the uh proposals or the quotation. What we have done here is on the premium we have this section wherein we allow to enter the promo code. I I'll walk.  
**Godhavari Gopal:** Okay, could you zoom in a little bit more?  
**Kate Oconer:** Yes.  
**Godhavari Gopal:** It's Yes, please.  
**Kate Oconer:** Zoom in. Is this better?  
**Godhavari Gopal:** Anchor. Yeah.  
**Kate Oconer:** Okay.  
**NATHANAEL G'BAMY:** Yes, perfect.  
**Kate Oconer:** Okay. So, I'll walk through the promos first, then we'll go through referrals later. But in context, it's actually almost the same with regards to the design. So, this is on the uh cover health um propo proposals quotation screen.  
   
 

### 00:01:13 {#00:01:13}

   
**Kate Oconer:** Uh what we have here is we have the option or to allow the users to enter a promo code. So this is when the uh quotation is being created from the admin portal coverel admin portal when it's coming from the funnel. I'll show it to you later based on the on the design. So here we allow to enter the promo code. Once we enter the promo code and this promo code has been validated. You will see it on the premium breakdown. The example here that I'm showing you is one of those discounts, but we also understand that um some of the promo codes have like future effects. So what happens here is um as long as the promo code has been validated from talent one, we will show it on the breakdown. It could be a let's say what is what was one um an adjustment benefit adjustment. So the code for the benefit adjustment will be here. It just says valid and it doesn't have the amount because it's a future effect.  
   
 

### 00:02:27 {#00:02:27}

   
**Kate Oconer:** Then I'll zoom in and zoom out just to see the whole picture. Here we also have the option to remove the promo codes. And then moving on to this screen, we actually allow to add up to five promo codes in one quotation. Give me a second.  
**EMMA NGHIEM:** Sorry uh because I don't have the whole uh platform invite. So could you just share uh what page is it? So in which flow is it?  
**Kate Oconer:** is actually on the proposals when you're creating the proposal from the admin portal. I'm trying to zoom it in. Is this um clearer? Proposals v2. Here you can see it from the cover help admin portal.  
**EMMA NGHIEM:** Okay, thank you.  
**Kate Oconer:** So you see all the screens and on the premium section we have this option to enter the promo codes and display the promo codes that has been validated on the premium breakdown. Yeah. So, as I've mentioned, we allow up to five. So, what we also handle in case that we already have five valid promo codes and the user enters another one, we will not allow it.  
   
 

### 00:03:51 {#00:03:51}

   
**Kate Oconer:** Okay. As you can see here, we also have this view code list. This view code list, if you click on it, it will open a model wherein you will see um just just regard this. This is promo code. Am I under referral code? Okay, here better. On the promo code, this is all the promos promotional code that that has been used or entered for that particular quotation. As you can see here, we also list down the invalid ones. And since I also mentioned that we can remove the promo. So if the user has removed it, it will be removed from the premium breakdown list. But on the code list you will see all of those codes that has been used. The reason why we wanted to show this is to assist. Um if for example a customer calls in and say oh I think I've entered this promo code but it's not reflecting then there's um an easy way or an easy page for whoever got the call to see and check what happened to that promo code.  
   
 

### 00:04:59 {#00:04:59}

   
**Kate Oconer:** that we remove and this is the we have the description or it could be an invalid promo code from the check in talent one before pausing I will show you the removal because you see there the description right so here on the list we have this icons where we allow the promo codes to be removed if the user decides to remove a promo code they will have to enter a reason why they are removing again just for tracking purposes in case a customer calls and say I have this promo code in place but it's not reflecting in the pricing or I'm not getting the effects or I'm not getting the benefits that was um mentioned for that particular promo code. So this is the reason why we have this section to allow the users to enter the reason why they're removing the promo codes. So you see here too many applied promos for this offer and on the case in a code list you will see that it has been removed for this particular reason. I'll stop here for some questions before we move to referral.  
   
 

### 00:06:17 {#00:06:17}

   
**Kate Oconer:** Any questions or concerns so far? Okay, I'll take that as  
**NATHANAEL G'BAMY:** Uh yes, I do have a question regarding the code application because uh correct me if I'm wrong uh Emma or cont or anyone from a sivate side. Uh actually we don't allow to apply several promo code to one quotation. Uh so is it something that we can uh personalize uh for example to allow only one code application on a on a one quotation uh and also and also uh being able to apply an automatic code on a  
**Kate Oconer:** Have you  
**NATHANAEL G'BAMY:** quotation for example the family verify code um based on the parameters we have for example two animals uh do we have the possibility to to automatize some uh from a code application on this interface.  
**Kate Oconer:** Okay, So first question um is actually quite ideal and we also would want to limit one promo code or one referral code per quotation but I I have a a follow-up question on that is that is it limited to one promo code then we don't have referral codes or is it we can have promo code and referral  
   
 

### 00:07:38 {#00:07:38}

   
**NATHANAEL G'BAMY:** Um, we can have uh that's a good question. I don't have the specific rules in mind, but I assume that it's either uh referral with one promo code or uh only uh one promo code, which could be uh family VIP or something else.  
**Kate Oconer:** Okay. So, at least for promo codes, we will take it as one promo code per quotation. But if you could check um the combination of promo and referral code in one quotation and get back to us, would that be okay to check?  
**NATHANAEL G'BAMY:** Okay. Uh yeah, sure. Yeah, we have I think we have different scenario based on the the promo that we suggest because they're not the same.  
**Kate Oconer:** Okay. Mhm.  
**NATHANAEL G'BAMY:** So uh will be uh I would like to to have this specific flow in order to not uh I mean uh create some mess on the agent side. uh if we have the the correct rules on on natively it will be easier to to manage that in order to to make to match action. So yeah, we come back to you with that uh just to give you the specific rules on the DIT.  
   
 

### 00:08:45 {#00:08:45}

   
**NATHANAEL G'BAMY:** But uh if someone has the answers, maybe it could be easier to to to to understand that and if not uh we can continue and come back to you afterwards.  
**Kate Oconer:** Okay. Uh so we can come back to that afterwards. And on your second question on the auto application of promo codes based on parameters, we actually don't have that.  
**NATHANAEL G'BAMY:** Here you go.  
**Kate Oconer:** we would always require to pass the um promo codes.  
**NATHANAEL G'BAMY:** Okay.  
**Kate Oconer:** Yeah. Okay. So, now moving on to the referrals. Referrals is actually almost the same flow. It's actually the same flow. It's just that instead of the promo, we click on referrals. We enter the referral code. With referral codes, we actually limit it only to one referral code per quotation.  
**NATHANAEL G'BAMY:** Okay.  
**Kate Oconer:** Yeah. And then it goes the same flow when we are viewing the code list. You will also still see all of the referral code that has been removed or validated but or invalidated but um on the system we will only allow one valid referral code per quotation.  
   
 

### 00:10:11 {#00:10:11}

   
**NATHANAEL G'BAMY:** Okay.  
**Kate Oconer:** Yeah. Okay. the same functionalities. You can still remove, you can still update. Say for example, for this referral code, you don't want to give this to your to the particular customer, you have a better referral code for them, you just remove this and then you add a new one. Yeah. Then moving on to how it goes to be viewed in the policy. So once everything is done on the proposal level and we will issue the policy or the policy has been issued on the policy screen. Do I have okay here on the policy screen policy is enforced on the premium section. We also display all of the valid promo codes for this particular policy. Again, it could be like an effect that is just a statement. See if I have it here. I don't think I have, but there is a promo code that's just say uh adjustment to benefits. Um, we also have this option to view the code list. Again, it's just going to be showing you or showing the user which codes has been applied, remove or is invalid.  
   
 

### 00:11:35 {#00:11:35}

   
**Kate Oconer:** Again, just to assist the um customer service who would go into this policy, say an inquiry comes up regarding promo codes. Uh what happens then if for example we have a future effect? See, I know I have one here. Give me a second. I'm trying to look for it. Okay, let's just let's just use our imaginations. Say for example, this insurance promo 30 is a 30% or uh one month uh free. So it's here valid since it's been validated in in talent one but the calculation is not here and then the date comes that we will run this effect and validate that this effect should be applied on the 11 month. What happens then is we will uh have the job run. we will uh check all the effects for each policy and then if all the conditions have been met we will tag that um that effect as done or uh finished or applied. So then it will go into the um finance transactions or billing and collection transactions. Yeah.  
   
 

### 00:13:07 {#00:13:07}

   
**Kate Oconer:** So those are for the future handing of effects. So what the uh agent will see or what the customer service will see after an effect has been run successfully, they will see a status update instead of valid here or another um status here that says this effect has been run and this effect has been used. So I don't have that screen but that's how it will be for future effects. Yeah.  
**NATHANAEL G'BAMY:** Um I have a question regarding the the status. The status is what you get from Talenmon in terms of configuration if it's active or not. That's correct.  
**Kate Oconer:** Yes. Correct. So in cover health we have it as valid and invalid.  
**NATHANAEL G'BAMY:** Okay. Okay. And uh do you also manage uh natively uh error messages?  
**Kate Oconer:** Any?  
**NATHANAEL G'BAMY:** For example, if the the users the the client is giving a promo code that is uh uh invalid and the agent is uh is using it uh in the form. Uh do we display some errors or manage is it manageable to impersonate that uh especially clearly in the in the the policy and theation.  
   
 

### 00:14:17

   
**Kate Oconer:** Yes. Um, not on the policy but on the quotation.  
**NATHANAEL G'BAMY:** Yes. Sorry.  
**Kate Oconer:** Yeah. from the quotation.  
**NATHANAEL G'BAMY:** Okay.  
**Kate Oconer:** Um, once a promo code has been entered, just go back to that screen. Okay. So here when we enter a promo code here, we will check from Talon one. We will call Talon one to validate that um that code and we will expect Talon one to give us the response if it's valid or not. Then we will display it here.  
**NATHANAEL G'BAMY:** Okay, perfect.  
**Kate Oconer:** Um any other questions? Because I think that's um it for what uh we have designed so far.  
**EMMA NGHIEM:** So I just have a question. So one of our top promo is to have three month offered on the first year. So I think it's one month on the first month and then two month at the end of the year. So how would you dis display this type of promo? I think we rarely do 20% on the whole year things like that.  
   
 

### 00:15:33 {#00:15:33}

   
**EMMA NGHIEM:** I don't I'm not you know we usually do and and we would not do every year. Uh so um yeah I'm thinking how does it so the 10% uh doesn't seem super um at least uh realistic to me. I think the the use cases that Anel has them and shared but it's more likely one month offered per month offer per year or three month for the first year things like that. So how would you manage that?  
**Kate Oconer:** Okay. So, um from what I understand in that scenario, we use a promo code and the effect of that promo code is one month free and then the last two months free. Correct?  
**EMMA NGHIEM:** Yeah. Yeah.  
**Kate Oconer:** Okay. So for the one month free we will consider that as the uh direct impact direct effect and then we will we will um calculate it on the pricing on the quotation level. When Talon one passes us the effect for the additional two months free last two months of the policy, we will store it in our campaign service and then we will wait for the job to run and pick up this policies with this particular effects and then we will apply those effects to this policy.  
   
 

### 00:16:49 {#00:16:49}

   
**Kate Oconer:** So that would mean on the 10th on the 11th and the 12th month this effects take place and then we will not we will recalculate or perform those effects and apply it to the policy.  
**EMMA NGHIEM:** And and sorry just to to be crystal clear the total discount so it would be the free month right? So what would appear in the total discount would I have three month offer, you know, I'm I have a quotation for a€1,000, you know, uh contract.  
**Kate Oconer:** This Oh yeah. So this total discount that you're you're saying.  
**EMMA NGHIEM:** I have three month offer. So 300 would appear in the total discounts even though it's going to only be unlocked at the end of the year.  
**Kate Oconer:** That's a very good question. Let me check on that. Um let me check on that. I I would say yes, we will have it um on a yearly. Give me a second. Let me think this through or let me get back to you on that.  
**EMMA NGHIEM:** Okay, thank you.  
**Kate Oconer:** Because what you see here is for the initial payment.  
   
 

### 00:17:59 {#00:17:59}

   
**Kate Oconer:** We don't display what will be paid on the 11th or on the 12th month. Your scenario in that case will apply on the transactions. It will be reflected on the transactions what you see here.  
**EMMA NGHIEM:** Yeah, but not a percentage.  
**Kate Oconer:** Yeah. So what we will yeah that would be that would reflect on the transactions because what we are showing here is just the initial payment.  
**EMMA NGHIEM:** Yeah. So that's why I was um uh Yeah. I I was not sure. Okay.  
**Kate Oconer:** So it will just apply for that specific monthly or specific yearly. Do you have it monthly or yearly per policy or you have the option to select  
**EMMA NGHIEM:** At Santet you can pay monthly or yearly and we also have quarterly and semesterly but it's not really used. Uh so it means that yeah so so you you most of our customers select monthly you have no uh advantage to select yearly so it's not very you know useful.  
**Kate Oconer:** Mhm. Yeah. Okay. So what you see here um on the total discounts is only for what is applied on that um on that calculation that you will uh that the customer will pay.  
   
 

### 00:19:16 {#00:19:16}

   
**Kate Oconer:** So the 11 and the 12 month is not included here.  
**EMMA NGHIEM:** Okay.  
**Kate Oconer:** The total discounts will not be included here. So only the valid promos with that is applicable on the spot or on the direct impact on the pricing the 11 12 month we don't display  
**EMMA NGHIEM:** Okay. Okay. Um, Natal, could you share me again the list of promos, but uh um I'm thinking we so we we is is maybe we can discuss family VIP maybe where yeah additional pet coverage but even family VIP is one month offered on the last on the on the cheapest formula at at the end of the year. So I'm not sure if we actually do 10% uh I I don't think we do this kind of promos. Yeah, I think this interface is useful, but I just want to make sure it's relevant with our promotions use cases.  
**NATHANAEL G'BAMY:** I'm sharing uh I'm checking it uh so yes the family vap yes but what you are saying ami is that uh today we want we need to display uh the specific information about our use case which means it's not an amount offered but more uh for example am a month offer uh but if we have I I assume that uh we need to to display to the to the agent the correct information in order to communicate  
   
 

### 00:20:50

   
**NATHANAEL G'BAMY:** to the to the client what he will uh he will pay every month and what are these benefits. Uh but I can check exactly what is the use case for family VIP. Just give me a a second. Uh um yeah, it's the 11th month offered for the second animal.  
**EMMA NGHIEM:** Uhoh.  
**NATHANAEL G'BAMY:** Um yeah.  
**EMMA NGHIEM:** So yeah, I I would be interested.  
**Kate Oconer:** Okay. So in that  
**NATHANAEL G'BAMY:** Yeah. I think we have we have Yeah.  
**EMMA NGHIEM:** Yeah, I would be interested to have the demo with these specific use cases because basically I but can permanent discount on formula for employees. It's really the only one where we have this type of discount where it's 25% discount for all the rest. It's um it's more it's a different mechanisms which are not basically 10% on the whole subscription.  
**Kate Oconer:** Yeah, I I actually understand where uh what you're describing over there. Um with regards to that, let's say we use the family code and it says it's an 11 month, right? Is it 11?  
   
 

### 00:22:18 {#00:22:18}

   
**NATHANAEL G'BAMY:** Mhm.  
**Kate Oconer:** 11 month reimburse on second animal. Um we are going to expect from Talon one to give us this description and the effects that comes to it that comes with it. So what you will see on the quotation assuming this is the family family VIP you will have here the description 11 month is that again 11 month reimbured on second animal.  
**NATHANAEL G'BAMY:** Okay.  
**Kate Oconer:** then you will not see any value. You see we don't display any value here. That would mean it's waiting for and the effects of that 11 month value will be on our campaign service. That means it's waiting for the job to run and when once we reach the 11th month the job would pick up this policy. Uh notice that it has this effect that on the 11th month is for free. Then we will apply that effect. You won't see any any values here like this. I I understand that um you don't have this use cases. I think you only have one that is for the employees discount.  
   
 

### 00:23:29 {#00:23:29}

   
**EMMA NGHIEM:** Okay, that's fine. So, it means that on the total discans I don't see anything and it would just be applied and triggered based on the rules which are predefined.  
**Kate Oconer:** Yeah, exactly.  
**EMMA NGHIEM:** Okay.  
**Kate Oconer:** Yes. Okay. Any other questions?  
**quentin pilet:** Natan, do we know on the schedule uh how it is impacting the schedule? Is it uh the promo code is related to is take in charge by SET or by the insurer.  
**NATHANAEL G'BAMY:** Um I don't know uh we can discuss that afterwards but I don't uh I don't know sorry uh the the most uh your question is more about the promo code application right?  
**quentin pilet:** Okay. Yes. On the schedule is it uh is it split between SET and the insurer or is it fully taken to taken charge by SET? I think today it's paid by SET but uh  
**NATHANAEL G'BAMY:** I don't know. Uh maybe uh I don't know if uh uh Fabian is still in the meeting but maybe we'll have an info about this or maybe so it's on the Sunday side if it's on marketing but yes side  
   
 

### 00:24:54 {#00:24:54}

   
**EMMA NGHIEM:** Yeah. So I assume it's it's on the promo in the marketing budget, right? Our promotions.  
**FABIEN DEGRAVEL:** Yes. Yes, it is. I confirm it's on the the marketing side.  
**NATHANAEL G'BAMY:** okay is that Yeah,  
**quentin pilet:** Okay. Okay. No. No. Yeah. Great. And in the future it should be the the same.  
**FABIEN DEGRAVEL:** Yes.  
**quentin pilet:** Okay.  
**Yashpal Deswal:** Yeah. Hi. Uh sorry. Uh in continuation what Quenton just discussed uh I just need to understand we have those two type of promo codes. I may be wrong. Correct me in case if I goes wrong anywhere. Uh that employee discount and the family discount and in both these items we have like some impact on the premium. So are we uh saying currently as a part of process whether it's a employee discount promo code or the family discount promo code in both the scenarios the uh money would be adjusted like the discount would be adjusted against the center marketing budget or still there is some scenario where we may have some Okay.  
   
 

### 00:26:22

   
**EMMA NGHIEM:** Sorry, could you repeat the question? I'm not sure to understand.  
**Yashpal Deswal:** Okay. Let me repeat. See uh what just now we discussed like the query which Quinton asked and we confirmed that in case of the promo code where we are adjusting the premium the premium has been adjusted against the Santa with marketing budget. Now uh as per my understanding we have two promo codes where we can have impact on premium. one is the employee discount. The second is the family discount which we just discussed. So in yeah  
**EMMA NGHIEM:** So for me, sorry, for me the family discount is a bit similar to the one month offered at the end of the year, right? It's not um it's not on the so sorry I will use my own words and please correct me but it's it's not impacting the premium for me it's like um an additional of month offer that you trigger on the 11th month if you still have those two pets so I assume it's something that you trigger with different rules but in the same way that you would trigger one month offer at the end of the year you know for me it's not really in the premium calculation If the others are not, it's a bit more similar.  
   
 

### 00:27:43 {#00:27:43}

   
**Yashpal Deswal:** Okay, understand.  
**EMMA NGHIEM:** The only one where it's like premium calculation every time always, it's for me it's the employee promotion.  
**Yashpal Deswal:** Okay. Now the family discount I understand it is not having a direct impact on the premium but if we calculate the premium for the insurer perspective insurer is expecting a complete 12-month premium but we are only going to collect  
**EMMA NGHIEM:** Yeah.  
**Yashpal Deswal:** 11th month. So that one month premium would be adjusted against the marketing budget of Santa.  
**EMMA NGHIEM:** So, um I think Fabian is not here. Uh I'm not sure if you have the answer, Valentine, if you're in the call. No, you're she's not. Um we'll need to get back to you. I assume it's from the marketing budget, but I'm not sure.  
**Yashpal Deswal:** Understand?  
**EMMA NGHIEM:** So, we we'll let you know.  
**Yashpal Deswal:** No worries.  
**EMMA NGHIEM:** We will let you know.  
**Yashpal Deswal:** Yeah.  
**EMMA NGHIEM:** Yeah.  
**NATHANAEL G'BAMY:** Yeah, you can send send to me Ashpel the the question you may have uh about this topic and then we check that internally because uh it might not be the don't right audience for that.  
   
 

### 00:28:41 {#00:28:41}

   
**Yashpal Deswal:** Okay. noise.  
**NATHANAEL G'BAMY:** So feel free to to ask and then we come back to you fastly with the with the answers but uh yeah we didn't expect that there is a question relative to insure impact or budget etc. So if you  
**Yashpal Deswal:** Yes. Sure, we'll share that  
**NATHANAEL G'BAMY:** quite clarify that uh at the on the basis uh will be easier to to integrate. So yeah ask send the question and then we we get back to you. Yeah. Thank you. Um uh Kate, I I have a question. Is this um feature uh live uh on covergo? Is it still work in progress?  
**Kate Oconer:** It's still a work in progress.  
**NATHANAEL G'BAMY:** Okay. And do you when do you expect to to launch it and to propose that to your clients?  
**Kate Oconer:** Um, by end of next sprint, we're actually still doing some testings here.  
**NATHANAEL G'BAMY:** Okay. Okay. Okay. Um, right. Um, okay. Uh, is it possible to maybe to review that uh on our side to share the the Figma or the the elements in order to to have a deep uh understanding of what uh what it what can be done?  
   
 

### 00:30:18 {#00:30:18}

   
**Kate Oconer:** Yep. Yep. I can share you the I can pass the link to Yashpal and Yashpal can it I I I'm not sure if you are in one group in Slack or I don't know how best to or I can just share it here. I'm not sure if you can access.  
**NATHANAEL G'BAMY:** Okay.  
**Kate Oconer:** Let me see.  
**NATHANAEL G'BAMY:** But uh from right I see it's it seems uh it seems great uh because there is a personalization but uh we still have work to do about the automatization of our business rules to match exactly what we what we do uh on SET. Um so yeah like the question that yes asked and some business rules for to manage uh some some promo. Um but uh yeah. Okay.  
**Kate Oconer:** Okay, let me um because um I'm not the owner of this Figma link and the UX designer is actually on a convention right now. Let me uh get first uh the link that I can share with you. I'll share it with Gina, then Gina will forward it.  
**NATHANAEL G'BAMY:** Yeah, great.  
**Kate Oconer:** Yeah.  
**NATHANAEL G'BAMY:** Okay, I will put that also in our our documentation in order to track uh what we we plan to do. Uh okay. Okay. Okay. Great. So, thank you for that, Kate.  
**quentin pilet:** Thank you. Bye.  
**NATHANAEL G'BAMY:** Thank you.  
   
 

### Transcription ended after 00:32:05

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*