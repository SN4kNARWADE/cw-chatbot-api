from bardapi import Bard



from flask import Flask, request,jsonify,json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


token = "aAjoeqVK-nN-lSmwNUq5XpZYsn8I7aMXeUTlMaJCzG6jbLVOsfntEiKmJIfNhiFhvm4YQQ."



# questionString = str(questionsData)

@app.route('/bot', methods=['GET'])
def search():

    try:

        args = request.args
        question = args.get("question", default="", type=str)
        prompt = "warning!! only answer the question which is requested and do not give any other texts in the response! i am giving you this json with keys as some questions and the values as answer to the respective question, i will tell you what is the question and you will answer me by finding that question in the json as key and tell me the answer according to the value of that key, the json is {'hi' :'hello','how are you?':'i am good','hello':'hii',‘What is a strong password?’:
‘A strong password is long, includes a mix of uppercase and lowercase letters, numbers, and symbols. It should be unique and not easily guessable.’,‘What is encryption?’:
‘Encryption is the process of converting information into a code to prevent unauthorized access. It ensures that only authorized parties can understand the information.’,

‘How can I secure my home Wi-Fi network?’:
‘Use a strong, unique Wi-Fi password, enable WPA3 encryption, and consider hiding your network's SSID to prevent unauthorized access.’,

‘How can I protect my personal information online?’:
‘Protect your information by using strong, unique passwords, being cautious about sharing personal details on social media, and using privacy settings on your accounts.’,

‘How do I identify phishing emails or scams?’:
‘Look for suspicious email addresses, grammatical errors, and urgent requests for personal or financial information. Never click on links from unknown sources.’,

‘What is end-to-end encryption?’:
‘End-to-end encryption ensures that only the sender and intended recipient can read messages, as the data is encrypted throughout transmission and decrypted upon arrival.’,

‘What is social engineering?’:
‘Social engineering is a technique where attackers manipulate individuals into revealing confidential information or performing actions that compromise security.’,

‘How does biometric authentication enhance security?’:
‘Biometric authentication uses unique physical traits like fingerprints or facial features to verify identity, making it difficult for unauthorized users to gain access.’,

‘Why should I avoid using the same password for multiple accounts?’:
‘Using the same password across multiple accounts increases the risk of a security breach. If one account is compromised, all your other accounts become vulnerable.’,

‘What is a DDoS attack?’:
‘A Distributed Denial of Service (DDoS) attack is when multiple compromised devices overwhelm a target's network or website, causing it to become slow or unavailable.’,

‘How often should I update my software and applications?’:
‘Regularly updating software and applications is important because updates often include security patches that protect against known vulnerabilities.’

‘How can I secure my smartphone from cyber threats?’:
‘Answer: Secure your smartphone by using a strong PIN or biometric lock, updating your apps and OS regularly, avoiding suspicious app downloads, and using mobile security software.’,

‘What is a phishing attack?’:
‘Phishing is a type of cyber attack where attackers trick you into revealing sensitive information by pretending to be a legitimate source, often through email or fake websites.’,

‘What are the latest cybersecurity threats I should be aware of?’:
‘Stay informed about threats like ransomware, phishing, and social engineering attacks. Regularly update your knowledge to adapt to new challenges.’,

‘What steps can I take to protect my children's online safety?’:
‘ Educate your children about online risks, set parental controls on devices, monitor their online activities, and encourage open communication about their online experiences.’,

‘Can you explain the concept of VPNs and their role in online security?’:
‘A VPN (Virtual Private Network) encrypts your internet connection, making it more secure and private. It's especially useful when using public Wi-Fi or accessing sensitive data.’,

‘What is malware and how can I prevent it?’:
‘Malware is malicious software that can harm your device. Prevent it by using reputable antivirus software, avoiding suspicious downloads, and keeping your software up to date.’,

‘Is it safe to click on links in emails from unknown senders?’:
‘ No, it's best to avoid clicking on links in emails from unknown sources, as they could lead to phishing sites or malware downloads.’,

‘How can I create a strong, memorable password?’:
‘ Use a passphrase with a mix of random words, numbers, and symbols. For example, "Purple3$Banana#Sky9."’,

‘What is two-factor authentication and why is it important?’:
‘Two-factor authentication adds an extra layer of security by requiring a second form of verification, like a code sent to your phone, in addition to your password.’,

‘Can you recommend good password management tools?’:
‘Yes, tools like LastPass, Dashlane, and 1Password can securely store and manage your passwords.’,

‘What steps should I take if my accounts are hacked?
Change your passwords immediately, enable two-factor authentication, and monitor your accounts for any unauthorized activity.’,

 ‘How can small businesses implement cost-effective cyber security measures?’:
    ‘Small businesses can use free or affordable security tools, regularly update software, and conduct employee training on cyber security best practices.’,
‘What should I do if I suspect my identity has been stolen?’:
    ‘Contact your bank, credit reporting agencies, and law enforcement, and place fraud alerts on your accounts.’:
 ‘How can I securely dispose of old electronic devices?’:
 Erase all data from devices before disposal or recycling, or consider using a professional data destruction service.’,
‘What is ransomware, and how can I protect against it?’:
   ‘Ransomware is a type of malware that encrypts data and demands a ransom. Protect against it with regular data backups and robust security measures.’,
 ‘What resources are available for cyber security professionals to stay updated on industry trends?’:
    ‘Cyber security professionals can join forums, follow industry leaders on social media, and participate in specialized training and certifications.’,
 “  What is the definition of cyber security?”:
 “Cyber security refers to the practice of protecting computer systems, networks, and data from digital attacks.”
“: Why is cyber security important?”:
                                  
“ Cyber security is essential to safeguard sensitive information, prevent data breaches, and protect against cyber threats.”
 “What are common examples of cyber threats?”:
                                  
“Common cyber threats include malware, phishing, ransomware, DDoS attacks, and social engineering.”
 “How can I create strong passwords?”:
                                  
“To create strong passwords, use a mix of uppercase and lowercase letters, numbers, and special characters, and avoid common words or patterns.”
” What is multi-factor authentication (MFA)?”:
                                  
    “Multi-factor authentication adds an extra layer of security by requiring users to provide multiple forms of identification before accessing an account.”
“How can I identify phishing emails?”:
                                  
 ” Look for suspicious links, misspellings, and requests for sensitive information. Verify the sender's email address and avoid clicking on unknown links.”
 “What should I do if my computer is infected with malware?”:
     
 ” Disconnect from the internet, run a full system scan with reputable antivirus software, and seek professional help if needed.”
“What is the importance of software updates?”:
     
   “Software updates often include security patches that fix vulnerabilities, making your systems less susceptible to cyber attacks.”
 “How can I protect sensitive data when using public Wi-Fi?”:
     
“Use a virtual private network (VPN) to encrypt your internet connection and avoid accessing sensitive information on public Wi-Fi networks.”
 “What is a firewall, and why is it important?”:   
“A firewall is a security system that monitors and controls incoming and outgoing network traffic, protecting your network from unauthorized access.”
 “How can I recognize social engineering attacks?”:
    “Social engineering attacks manipulate individuals into revealing sensitive information. Be cautious of unsolicited requests for personal data.”
 “What is the role of encryption in cyber security?”:    
“Encryption converts data into a secure code, making it unreadable to unauthorized users, and is crucial for protecting sensitive information.”
“How can I secure my mobile devices?”:  
“Set up a strong password or biometric authentication, keep software up to date, and only download apps from reputable sources.”

     “What is a data breach, and how can I respond to one?”:   
“A data breach is unauthorized access to sensitive information. If you experience one, report it immediately, and take steps to mitigate the damage.”
“What is the dark web, and why is it a concern for cyber security?”:
    
“The dark web is a hidden part of the internet where illegal activities often occur, making it a breeding ground for cybercriminals.”
“How can businesses ensure cyber security for remote employees?”:
    
   “ Businesses should implement secure remote access methods, educate employees about cyber risks, and use VPNs for remote connections.”
“ What is a DDoS attack, and how can it be prevented?”:
“ A DDoS attack overwhelms a network with traffic, causing it to crash. Prevention includes using traffic filtering and load balancing solutions.”
“ How can I protect my online accounts from unauthorized access?”:
“Enable two-factor authentication, use unique passwords for each account, and regularly review account activity”.
“ What are the best practices for safe online shopping?”:
“ Shop on secure websites (look for "https" and a padlock icon), avoid sharing unnecessary personal information, and use a credit card for added protection.”
“ How can I report cyber incidents or suspicious activities?”:
“ Report cyber incidents to the appropriate authorities or your organization's IT department, and consider using national reporting agencies for more significant incidents.”
 
“ What are the different types of cyber security measures?”:
“ Cyber security measures include network security, endpoint security, application security, data security, and cloud security.
“ How can I spot a fake website or online scam?”:
“ Look for misspellings in the URL, check for secure website indicators, and avoid deals that seem too good to be true.”
“What is ethical hacking, and how does it contribute to cyber security?”:
    “ Ethical hacking involves authorized individuals testing systems for vulnerabilities to identify and fix potential security issues before malicious hackers exploit them.”
“ What steps can I take to secure my home network?:
“ Change the default router password, enable network encryption (WPA2/WPA3), and hide your network's SSID.”
“ How can I protect my personal information on social media?”:
“ Review and adjust privacy settings, avoid sharing sensitive data publicly, and be cautious about accepting friend requests from unknown individuals.”
“ What are the best practices for secure online banking?”:
“ Use strong passwords, avoid accessing accounts on public computers or networks, and enable transaction alerts for added security.”
“ How can employees contribute to their organization's cyber security?”:
“ Employees can undergo regular cyber security training, report suspicious activities, and follow the organization's security policies.”
“What are the potential consequences of cyber attacks for individuals and businesses?”:
“ Cyber attacks can lead to financial losses, data breaches, reputational damage, and legal repercussions.”
“ How can I stay informed about the latest cyber security threats?”:
“Follow reputable cyber security blogs, subscribe to threat intelligence newsletters, and attend cyber security conferences or webinars.”
“ What is the role of incident response in cyber security?”:
“ Incident response involves detecting, analyzing, and mitigating cyber security incidents promptly to minimize their impact.”} 
 and the question is '"+question+"' , wrap the answer in ]"

        bard = Bard(token=token)

        result = bard.get_answer(prompt)

        

        return result['content']

    except:
        return "there is an error"

print(search())

if __name__ == '__main__':
    app.run(debug=False)
    
