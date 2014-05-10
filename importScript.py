fI = open('toImport.ini', 'w')
fP = open('toPublish.ini', 'w')
fT = open('toPublishWithTorrent.ini', 'w')

for x in range(1,39):
	dossier=2481+x
	IjobStr='[Job{0}]\n CmdTyp			= T\nDossier			= {1}\nSubmission		= \nUpdatestate     = Imported\nFillAPIDossiers = True\n\n\n\n'.format(x,str(dossier).zfill(6))
	PjobStr='[Job{0}]\n CmdTyp			= T\nDossier			= {1}\nSubmission		= \nUpdatestate     = Published\nFillAPIDossiers = True\n\n\n\n'.format(x,str(dossier).zfill(6))
	TjobStr='[Job{0}]\n CmdTyp			= T\nDossier			= {1}\nSubmission		= \n\n\n\n'.format(x,str(dossier).zfill(6))
	#print IjobStr
	#print PjobStr
	#print TjobStr
	fI.write(IjobStr)
	fP.write(PjobStr)
	fT.write(TjobStr)

fI.close()
fP.close()
fT.close()