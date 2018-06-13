import filecmp
import os
import smtplib

def fileCompare(emailaddr):
		
	# Determine the items that exist in both directories
	d1_contents = set(os.listdir('//mnt/c/Users/Matthew\ Houy/Documents/Python/FedRAMPParser/FedRAMPCompare'))
	d2_contents = set(os.listdir('//mnt/c/Users/Matthew\ Houy/Documents/Python/FedRAMPParser/FedRAMPAuthoritative'))
	common = list(d1_contents & d2_contents)
	common_files = [f 
					for f in common 
					if os.path.isfile(os.path.join('//mnt/c/Users/Matthew\ Houy/Documents/Python/FedRAMPParser/FedRAMPCompare', f))
					]

	# Determine the item that exist in one directory, but not the other
	uncommon = list(d1_contents ^ d2_contents)
		
	# Compare the directories
	match, mismatch, errors = filecmp.cmpfiles('//mnt/c/Users/Matthew\ Houy/Documents/Python/FedRAMPParser/FedRAMPCompare', '//mnt/c/Users/Matthew\ Houy/Documents/Python/FedRAMPParseFedRAMPAuthoritative',common_files,shallow=False)
				
	# Create strings for email and printing 							
	matchstr = "\n\t".join(match)
	mismatchstr = "\n\t".join(mismatch)
	uncommonstr = "\n\t".join(uncommon)
	errorstr = "\n\t".join(errors)
	
	# Print comparison output
	print 'Match:', matchstr
	print 'Mismatch:', mismatchstr
	print 'Uncommon:', uncommonstr
	print 'Errors:', errorstr
	
	
	if mismatch or uncommon or errors:
		fromaddr = 'fedrampalerts@gmail.com'
		toaddrs  = emailaddr
		msg = "\r\n".join([
				"From: FedRAMPalerts@verisgroup.com",
				"",
				"Subject: FedRAMP GUIDANCE ALERT",
				"",
				"The following files have been altered:",
				"",
				mismatchstr,
				"",
				"The following files have been added or removed as guidance:",
				"",
				uncommonstr,
				"",
				"The following files have caused an error:",
				"",
				errorstr,
				""
				])
		username = 'fedrampalerts@gmail.com'
		password = 'VerisGroup123!'
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()
		
