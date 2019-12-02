from typing import Dict, ValuesView, TYPE_CHECKING

from collections import defaultdict

from .filtering import ElementList

if TYPE_CHECKING:
    from .components import PDFDocument, PDFElement


class Section:
    """
    A continuous group of elements within a document.

    A section is intended to label a group of elements. Said elements must be continuous
    in the document. You should not instantiate a Section class yourself, but should
    call `create_section` from the `Sectioning` class below.

    Args:
        document (PDFDocument): A reference to the document.
        name (str): The name of the section.
        unique_name (str): Multiple sections can have the same name, but a unique name
            will be generated by the Sectioning class.
        start_element (PDFElement): The first element in the section.
        end_element (PDFElement): The last element in the section.
    """

    document: "PDFDocument"
    name: str
    unique_name: str
    start_element: "PDFElement"
    end_element: "PDFElement"

    def __init__(self, document, name, unique_name, start_element, end_element):
        self.document = document
        self.name = name
        self.unique_name = unique_name
        self.start_element = start_element
        self.end_element = end_element

    def __contains__(self, element: "PDFElement") -> bool:
        return element in self.elements

    @property
    def elements(self) -> "ElementList":
        """
        Returns an ElementList of all the elements in the section.
        """
        return self.document.elements.between(
            self.start_element, self.end_element, inclusive=True
        )


class Sectioning:
    """
    A sectioning utilities class, made available on all `PDFDocument`s as `.sectioning`.
    """

    document: "PDFDocument"
    name_counts: Dict[str, int]
    sections_dict: Dict[str, Section]

    def __init__(self, document: "PDFDocument"):
        self.sections_dict = {}
        self.name_counts = defaultdict(int)
        self.document = document

    def create_section(
        self, name: str, start_element: "PDFElement", end_element: "PDFElement"
    ):
        """
        Creates a new section with the specified name.

        Creates a new section with the specified name, starting at `start_element` and
        ending at `end_element` (inclusive). The unique name will be set to name_<idx>
        where <idx> is the number of existing sections with that name.

        Returns: The created `Section`.
        """
        current_count = self.name_counts[name]
        unique_name = f"{name}_{current_count}"
        self.name_counts[name] += 1

        section = Section(self.document, name, unique_name, start_element, end_element)
        self.sections_dict[unique_name] = section
        return section

    @property
    def sections(self) -> ValuesView[Section]:
        """
        Returns the list of all created `Section`s.
        """
        return self.sections_dict.values()
