from flask import Flask
from flask import request, Response
app=Flask(__name__)

@app.route('/')
def man():
	return 'Examples:<br>1)/build_script/scriptType?from=1&to=10<br>2)/build_script/scriptType/all<br>where scriptType can be:import, publish, verify, torrent'

@app.route('/build_script/<scriptType>/all')
def generateScriptAll(scriptType):
	fromI=request.args.get('from')
	toI=request.args.get('to')

	if scriptType == 'import':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= \nSubmission		= \nUpdatestate     = Imported\nFillAPIDossiers = True\n\n\n\n'
	elif scriptType == 'publish':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= \nSubmission		= \nUpdatestate     = Published\nFillAPIDossiers = True\n\n\n\n'
	elif scriptType == 'verify':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= \nSubmission		= \nUpdatestate     = Verified\nFillAPIDossiers = True\n\n\n\n'
	elif scriptType == 'torrent':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= \nSubmission		= \n\n\n\n'
	else:
		return 'unknown command: ' + scriptType

	result = ""
	fI = open('toImport.ini', 'w')

	i=1
	result = result + template.format(i)
		
	response = Response(result, mimetype="text/plain")
	response.headers['Content-Type'] = 'image/plain'
	response.headers['Content-Disposition']='attachment;filename='+scriptType+'.ini'
	return response

@app.route('/build_script/<scriptType>')
def generateScript(scriptType):

	fromI=request.args.get('from')
	toI=request.args.get('to')

	if fromI is None:
		return 'provide a from' 

	if toI is None:
		return 'provide a to ' 		

	fromI=int(fromI)
	toI=int(toI)

	if fromI>toI:
		return 'wrong variable range'

	if scriptType == 'import':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= {1}\nSubmission		= \nUpdatestate     = Imported\nFillAPIDossiers = True\n\n\n\n'
	elif scriptType == 'publish':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= {1}\nSubmission		= \nUpdatestate     = Published\nFillAPIDossiers = True\n\n\n\n'
	elif scriptType == 'verify':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= {1}\nSubmission		= \nUpdatestate     = Verified\nFillAPIDossiers = True\n\n\n\n'
	elif scriptType == 'torrent':
		template='[Job{0}]\nCmdTyp			= T\nDossier			= {1}\nSubmission		= \n\n\n\n'
	else:
		return 'unknown command: ' + scriptType

	result = ""
	fI = open('toImport.ini', 'w')

	i=1
	for x in range(fromI,toI+1):
		dossier=x
		result = result + template.format(i,str(dossier).zfill(6))
		i=i+1
		
	response = Response(result, mimetype="text/plain")
	response.headers['Content-Type'] = 'image/plain'
	response.headers['Content-Disposition']='attachment;filename='+scriptType+'.ini'
	return response

if __name__ == '__main__':
	#app.debug=True
	app.run(host='0.0.0.0', port=9000, threaded=True)