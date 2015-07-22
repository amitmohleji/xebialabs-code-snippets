import sys, string
from com.xebialabs.xlrelease.plugin.webhook import JsonPathResult
from com.xebialabs.xlrelease.plugin.webhook import XmlPathResult
from urlparse import urlparse


def isJson():
    return 'jsonPathExpression' in globals() or 'jsonPathExpression2' in globals() or 'jsonPathExpression3' in globals()

def isXml():
    return 'xPathExpression' in globals() or 'xPathExpression2' in globals() or 'xPathExpression3' in globals()

def process(response, expression, ExpressionProcessor):
    result_expected = expression is not None and len(expression) > 0

    if result_expected:
        resultVariable = ExpressionProcessor(response, expression).get()
        if resultVariable is None:
            print "Expression %s did not match anything in the response" % expression
            sys.exit(1)
        print "Result: %s" % resultVariable
        return resultVariable

def process_json(response, jsonPathExpression):
    return process(response, jsonPathExpression, JsonPathResult)

def process_xml(response, xPathExpression):
    return process(response, xPathExpression, XmlPathResult)


if isJson():
    content_type = 'application/json'
elif isXml():
    content_type = 'application/xml'
else:
    print 'Could not determine Webhook format, neither JsonPath nor XPath expression was provided'
    sys.exit(1)


uri = urlparse(URL)

host = '%s://%s' % (uri.scheme, uri.netloc)
context = uri.path

if uri.query:
    context = '%s?%s' % (context, uri.query)

server = { 'url': host, 'username': username, 'password': password, 'proxyHost': proxyHost, 'proxyPort': proxyPort}
request = HttpRequest(server, username, password)

if body is None:
    body = ""

i = [ count for count,item in enumerate(phase.getTasks()) if task == item ]
if len(phase.getTasks()[i[0]-1].comments) > 0:
    body ='{state:3,work_notes:\'' + phase.getTasks()[i[0]-1].comments[-1].getText() + '\'}'


response = request.doRequest(method = method, context = context, body = body, contentType = content_type)

if response.isSuccessful():
    print "Http Status: %s" % response.status

    if isJson():
        result = process_json(response.response, jsonPathExpression)
        result2 = process_json(response.response, jsonPathExpression2)
        result3 = process_json(response.response, jsonPathExpression3)
    if isXml():
        result = process_xml(response.response, xPathExpression)
        result2 = process_xml(response.response, xPathExpression2)
        result3 = process_xml(response.response, xPathExpression3)
else:
    print "Failed to connect at %s." % URL
    response.errorDump()
    sys.exit(1)
