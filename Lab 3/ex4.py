# The build_xml_element function receives the following parameters:
# tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML
# element. Example: build_xml_element("a", "Hello there",
# href="http://python.org", _class="my-link", id="someid") =>
# "<a href=\"http://python.org\" _class=\"my-link\" id=\"someid\">Hello there</a>"


def build_xml_element(tag, content, href, clas, idd):
    result = "<" + tag + " href=\"" + href + "\" _class=\"" + clas + "\" id=\"" + idd + "\">" + content + "</" + tag + ">"

    return result


print(build_xml_element("a", "Hello there", "http://python.org", "my-link", "someid"))
