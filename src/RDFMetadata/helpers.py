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

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral"
                    : ( "The RDF Vocabulary (RDF)",
                        "PlainLiteral",
                        "The class of plain (i.e. untyped) literal values."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"
                    : ( "The RDF Vocabulary (RDF)",
                        "Property",
                        "The class of RDF properties."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement"
                    : ( "The RDF Vocabulary (RDF)",
                        "Statement",
                        "The class of RDF statements."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#subject"
                    : ( "The RDF Vocabulary (RDF)",
                        "subject",
                        "The subject of the subject RDF statement."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate"
                    : ( "The RDF Vocabulary (RDF)",
                        "predicate",
                        "The predicate of the subject RDF statement."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#object"
                    : ( "The RDF Vocabulary (RDF)",
                        "object",
                        "The object of the subject RDF statement."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#Bag"
                    : ( "The RDF Vocabulary (RDF)",
                        "Bag",
                        "The class of unordered containers."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#Seq"
                    : ( "The RDF Vocabulary (RDF)",
                        "Seq",
                        "The class of ordered containers."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#Alt"
                    : ( "The RDF Vocabulary (RDF)",
                        "Alt",
                        "The class of containers of alternatives."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#value"
                    : ( "The RDF Vocabulary (RDF)",
                        "value",
                        "Idiomatic property used for structured values."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#List"
                    : ( "The RDF Vocabulary (RDF)",
                        "List",
                        "The class of RDF Lists."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"
                    : ( "The RDF Vocabulary (RDF)",
                        "nil",
                        "The empty list, with no items in it. If the rest of a list is nil then the list has no more items in it."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#first"
                    : ( "The RDF Vocabulary (RDF)",
                        "first",
                        "The first item in the subject RDF list."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest"
                    : ( "The RDF Vocabulary (RDF)",
                        "rest",
                        "The rest of the subject RDF list after the first item."),

                "http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral"
                    : ( "The RDF Vocabulary (RDF)",
                        "XMLLiteral",
                        "The class of XML literal values."),

                # Creative Commons
                "http://creativecommons.org/ns#Work"
                    : ( "CC REL ",
                        "Work",
                        "A potentially copyrightable work"),

                "http://creativecommons.org/ns#License"
                    : ( "CC REL",
                        "License",
                        "A set of requests/permissions to users of a Work, e.g. a copyright license, the public domain, information for distributors."),

                "http://creativecommons.org/ns#Jurisdiction"
                    : ( "CC REL",
                        "Jurisdiction",
                        "The legal jurisdiction of a license."),

                "http://creativecommons.org/ns#Permission"
                    : ( "CC REL",
                        "Permission",
                        "An action that may or may not be allowed or desired."),

                "http://creativecommons.org/ns#Requirement"
                    : ( "CC REL",
                        "Requirement",
                        "An action that may or may not be requested of you."),

                "http://creativecommons.org/ns#Prohibition"
                    : ( "CC REL",
                        "Prohibition",
                        "Something you may be asked not to do."),

                "http://creativecommons.org/ns#Reproduction"
                    : ( "CC REL",
                        "Reproduction",
                        "Making multiple copies."),

                "http://creativecommons.org/ns#Distribution"
                    : ( "CC REL",
                        "Distribution",
                        "Distribution, public display, and publicly performance."),

                "http://creativecommons.org/ns#DerivativeWorks"
                    : ( "CC REL",
                        "Derivative Works",
                        "Distribution of derivative works."),

                "http://creativecommons.org/ns#Sharing"
                    : ( "CC REL",
                        "Sharing",
                        "Permits commercial derivatives, but only non-commercial distribution."),

                "http://creativecommons.org/ns#Notice"
                    : ( "CC REL",
                        "Notice",
                        "Copyright and license notices be kept intact."),

                "http://creativecommons.org/ns#Attribution"
                    : ( "CC REL",
                        "Attribution",
                        "Credit be given to copyright holder and/or author."),

                "http://creativecommons.org/ns#ShareAlike"
                    : ( "CC REL",
                        "Share Alike",
                        "Derivative works be licensed under the same terms or compatible terms as the original work."),

                "http://creativecommons.org/ns#SourceCode"
                    : ( "CC REL",
                        "Source Code",
                        "Source code (the preferred form for making modifications) must be provided when exercising some rights granted by the license."),

                "http://creativecommons.org/ns#Copyleft"
                    : ( "CC REL",
                        "Copyleft",
                        "Derivative and combined works must be licensed under specified terms, similar to those on the original work."),

                "http://creativecommons.org/ns#LesserCopyleft"
                    : ( "CC REL",
                        "Lesser Copyleft",
                        "Derivative works must be licensed under specified terms, with at least the same conditions as the original work; combinations with the work may be licensed under different terms."),

                "http://creativecommons.org/ns#CommercialUse"
                    : ( "CC REL",
                        "Commercial Use",
                        "Exercising rights for commercial purposes."),

                "http://creativecommons.org/ns#HighIncomeNationUse"
                    : ( "CC REL",
                        "High Income Nation Use",
                        "Use in a non-developing country."),

                "http://creativecommons.org/ns#permits"
                    : ( "CC REL",
                        "permits",
                        "A License permits a Permission."),

                "http://creativecommons.org/ns#requires"
                    : ( "CC REL",
                        "requires",
                        "A License requires a Requirement."),

                "http://creativecommons.org/ns#prohibits"
                    : ( "CC REL",
                        "prohibits",
                        "A License prohibits a Prohibition."),

                "http://creativecommons.org/ns#jurisdiction"
                    : ( "CC REL",
                        "jurisdiction",
                        "A License may have a jurisdiction, as defined by Jurisdictions."),

                "http://creativecommons.org/ns#legalcode"
                    : ( "CC REL",
                        "legalcode",
                        "The URL of the legal text of a License."),

                "http://creativecommons.org/ns#deprecatedOn"
                    : ( "CC REL",
                        "deprecatedOn",
                        "A License may be deprecated; provides the date deprecated on."),

                "http://creativecommons.org/ns#license"
                    : ( "CC REL",
                        "license",
                        "A Work has license a License. (a subproperty of dc:license, the same as xhtml:license)."),

                "http://creativecommons.org/ns#morePermissions"
                    : ( "CC REL",
                        "morePermissions",
                        "A related resource which describes additional permissions or alternative licenses for a Work which may be available."),

                "http://creativecommons.org/ns#attributionName"
                    : ( "CC REL",
                        "attributionName",
                        "The name the creator of a Work would like used when attributing re-use."),

                "http://creativecommons.org/ns#attributionURL"
                    : ( "CC REL",
                        "attributionURL",
                        "The URL the creator of a Work would like used when attributing re-use."),

                "http://creativecommons.org/ns#useGuidelines"
                    : ( "CC REL",
                        "useGuidelines",
                        "A related resource which defines non-binding use guidelines for the work."),

                # TODO: Couldn't find this at the URI, is it valid?
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
