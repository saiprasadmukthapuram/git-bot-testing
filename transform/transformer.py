import os

from lxml import etree
from lxml.etree import XMLParser



def transform_xml_with_xslt(input_file, xslt_file_name, processed_file):
    """

    :param input_file:
    :param xslt_file_name:
    :param processed_file:
    :return:
    """
    try:
        xslt_path = xslt_file_name
        parser = XMLParser(huge_tree=True)
        xml = etree.parse(input_file, parser=parser)
        xml.getroot()
        xslt_root = etree.parse(xslt_path)
        transform = etree.XSLT(xslt_root)
        try:
            new_text = transform(xml)
            with open(processed_file, 'w') as file:
                file.write(str(new_text))
        finally:
            if os.path.getsize(processed_file) != 0:
                file.close()

    except OSError as ex:
        raise OSError(f'Error reading file {input_file}:'
                      f' failed to load external entity {input_file}')
    return processed_file



transform_xml_with_xslt("test.xml", "test.xslt", "output.xml")