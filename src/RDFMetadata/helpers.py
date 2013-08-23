# helpers - Different helper classes mostly for more user friendly
# presentation of values.
#
# Copyright 2013 Commons Machinery http://commonsmachinery.se/
#
# Authors: Christoffer Holmstedt <christoffer.holmstedt@gmail.com>
#
# Distributed under an GPLv2 license, please see LICENSE in the top dir.

class NSUri(object):
    def __init__(self):

        # Create the dictionary
        self.dictionary = {
                # W3.org
                "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                    : ( "The RDF Vocabulary (RDF)",
                        "Type",
                        "The subject is an instance of a class."),

                # Creative Commons
                "http://creativecommons.org/ns#Work"
                    : ( "CC REL ",
                        "Work",
                        "A potentially copyrightable work"),

                "http://creativecommons.org/ns#Agent"
                    : ( "CC REL ",
                        "Agent",
                        "Does this really exist?"),

                # Dublin Core terms
                "http://purl.org/dc/terms/title"
                    : ( "Dublin Core 1.1",
                        "Title",
                        "A name given to the resource."),

                "http://purl.org/dc/terms/title"
                    : ( "Dublin Core 1.1",
                        "Title",
                        "A name given to the resource."),

                "http://purl.org/dc/terms/abstract"
                    : ( "Dublin Core 1.1",
                        "Abstract",
                        "A summary of the resource."),

                "http://purl.org/dc/terms/accessRights"
                    : ( "Dublin Core 1.1",
                        "Access Rights",
                        "Information about who can access the resource or an indication of its security status."),

                "http://purl.org/dc/dcmitype/Image"
                    : ( "Dublin Core 1.1",
                        "Image",
                        "A visual representation other than text."),

                "http://purl.org/dc/elements/1.1/title"
                    : ( "Dublin Core 1.1",
                        "Title",
                        "A name given to the resource."),

                "http://purl.org/dc/elements/1.1/creator"
                    : ( "Dublin Core 1.1",
                        "Creator",
                        "An entity primarily responsible for making the resource."),

                "http://purl.org/dc/elements/1.1/date"
                    : ( "Dublin Core 1.1",
                        "Date",
                        "A point or period of time associated with an event in the lifecycle of the resource."),

                "http://purl.org/dc/elements/1.1/type"
                    : ( "Dublin Core 1.1",
                        "Type",
                        "The nature or genre of the resource."),

                "http://purl.org/dc/dcmitype/StillImage"
                    : ( "Dublin Core 1.1",
                        "Still Image",
                        "A static visual representation."),

                "http://purl.org/dc/elements/1.1/format"
                    : ( "Dublin Core 1.1",
                        "Format",
                        "The file format, physical medium, or dimensions of the resource.")}

    def get_standard(self, key):
        if key in self.dictionary:
            return self.dictionary[key][0]
        else:
            return str(key)

    def get_label(self, key):
        if key in self.dictionary:
            return self.dictionary[key][1]
        else:
            return str(key)

    def get_definition(self, key):
        if key in self.dictionary:
            return self.dictionary[key][2]
        else:
            return str(key)
