# Auto generated from dentmatmech.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-09-04T16:39:35
# Schema: dentmatmech
#
# id: https://w3id.org/caufieldjh/dentmatmech
# description: Schema for the Dental Materials Knowledge Base (dentmatmech). One YAML file per material, anchored to the Oral Health and Disease Ontology (OHD) branch under OHD:0000000 "dental restoration material". Each entry records what the material is made of, how it sets, what it is used for clinically, how it performs, what can go wrong, and how regulators (FDA first) classify it and what they permit it to be used for. Every claim can carry literature or regulatory-document evidence with an exact quoted snippet, following the DisMech evidence model.
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Float, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = None

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CFR = CurieNamespace('CFR', 'https://www.ecfr.gov/current/title-21/section-')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
DOI = CurieNamespace('DOI', 'https://doi.org/')
FDA_PRODUCT_CODE = CurieNamespace('FDA_PRODUCT_CODE', 'https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/classification.cfm?start_search=1&productcode=')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OHD = CurieNamespace('OHD', 'http://purl.obolibrary.org/obo/OHD_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
DENTMATMECH = CurieNamespace('dentmatmech', 'https://w3id.org/caufieldjh/dentmatmech/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DENTMATMECH


# Types
class ReferenceIdentifier(String):
    """ A CURIE-style identifier for a citable source. Literature references use PMID:, PMC:, DOI:, or PPR: (Europe PMC preprints). Web sources use url:. Regulatory documents should be cited by url: pointing at the eCFR section, the FDA 510(k)/PMA database record, or the guidance document. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ReferenceIdentifier"
    type_model_uri = DENTMATMECH.ReferenceIdentifier


# Class references
class ComponentName(extended_str):
    pass


class MaterialPropertyName(extended_str):
    pass


class ClinicalUseName(extended_str):
    pass


class ClinicalPerformanceName(extended_str):
    pass


class AdverseEffectName(extended_str):
    pass


class ApprovedUseName(extended_str):
    pass


class CommercialProductName(extended_str):
    pass


class DentalMaterialName(extended_str):
    pass


@dataclass(repr=False)
class Term(YAMLRoot):
    """
    A structured reference to an ontology term
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["Term"]
    class_class_curie: ClassVar[str] = "dentmatmech:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.Term

    id: Union[str, URIorCURIE] = None
    label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URIorCURIE):
            self.id = URIorCURIE(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Descriptor(YAMLRoot):
    """
    Base class for a thing described by a preferred term, an optional description, and an optional bound ontology term
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["Descriptor"]
    class_class_curie: ClassVar[str] = "dentmatmech:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.Descriptor

    preferred_term: Optional[str] = None
    description: Optional[str] = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.preferred_term is not None and not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DentalMaterialDescriptor(Descriptor):
    """
    A descriptor bindable to the OHD dental restoration material branch
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["DentalMaterialDescriptor"]
    class_class_curie: ClassVar[str] = "dentmatmech:DentalMaterialDescriptor"
    class_name: ClassVar[str] = "DentalMaterialDescriptor"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.DentalMaterialDescriptor

    term: Union[dict, Term] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DentalProcedureDescriptor(Descriptor):
    """
    A descriptor bindable to the OHD dental procedure branch
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["DentalProcedureDescriptor"]
    class_class_curie: ClassVar[str] = "dentmatmech:DentalProcedureDescriptor"
    class_name: ClassVar[str] = "DentalProcedureDescriptor"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.DentalProcedureDescriptor

    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntityDescriptor(Descriptor):
    """
    A descriptor bindable to CHEBI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["ChemicalEntityDescriptor"]
    class_class_curie: ClassVar[str] = "dentmatmech:ChemicalEntityDescriptor"
    class_name: ClassVar[str] = "ChemicalEntityDescriptor"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.ChemicalEntityDescriptor

    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalEntityDescriptor(Descriptor):
    """
    A descriptor bindable to UBERON
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["AnatomicalEntityDescriptor"]
    class_class_curie: ClassVar[str] = "dentmatmech:AnatomicalEntityDescriptor"
    class_name: ClassVar[str] = "AnatomicalEntityDescriptor"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.AnatomicalEntityDescriptor

    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeDescriptor(Descriptor):
    """
    A descriptor bindable to HP or MONDO
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["PhenotypeDescriptor"]
    class_class_curie: ClassVar[str] = "dentmatmech:PhenotypeDescriptor"
    class_name: ClassVar[str] = "PhenotypeDescriptor"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.PhenotypeDescriptor

    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualityDescriptor(Descriptor):
    """
    A descriptor bindable to PATO
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["QualityDescriptor"]
    class_class_curie: ClassVar[str] = "dentmatmech:QualityDescriptor"
    class_name: ClassVar[str] = "QualityDescriptor"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.QualityDescriptor

    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceItem(YAMLRoot):
    """
    A citation plus an exact quote, tied to the claim it sits under
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["EvidenceItem"]
    class_class_curie: ClassVar[str] = "dentmatmech:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.EvidenceItem

    reference: Union[str, ReferenceIdentifier] = None
    supports: Union[str, "EvidenceItemSupportEnum"] = None
    reference_title: Optional[str] = None
    evidence_source: Optional[Union[str, "EvidenceSourceEnum"]] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, ReferenceIdentifier):
            self.reference = ReferenceIdentifier(self.reference)

        if self._is_empty(self.supports):
            self.MissingRequiredField("supports")
        if not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self.reference_title is not None and not isinstance(self.reference_title, str):
            self.reference_title = str(self.reference_title)

        if self.evidence_source is not None and not isinstance(self.evidence_source, EvidenceSourceEnum):
            self.evidence_source = EvidenceSourceEnum(self.evidence_source)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mapping(YAMLRoot):
    """
    A mapping to a term in another vocabulary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["Mapping"]
    class_class_curie: ClassVar[str] = "dentmatmech:Mapping"
    class_name: ClassVar[str] = "Mapping"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.Mapping

    id: Union[str, URIorCURIE] = None
    label: str = None
    predicate: Union[str, "MappingPredicateEnum"] = None
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URIorCURIE):
            self.id = URIorCURIE(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, MappingPredicateEnum):
            self.predicate = MappingPredicateEnum(self.predicate)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Component(YAMLRoot):
    """
    A constituent of the material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["Component"]
    class_class_curie: ClassVar[str] = "dentmatmech:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.Component

    name: Union[str, ComponentName] = None
    description: Optional[str] = None
    role: Optional[Union[str, "ComponentRoleEnum"]] = None
    chemical: Optional[Union[dict, ChemicalEntityDescriptor]] = None
    proportion: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ComponentName):
            self.name = ComponentName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.role is not None and not isinstance(self.role, ComponentRoleEnum):
            self.role = ComponentRoleEnum(self.role)

        if self.chemical is not None and not isinstance(self.chemical, ChemicalEntityDescriptor):
            self.chemical = ChemicalEntityDescriptor(**as_dict(self.chemical))

        if self.proportion is not None and not isinstance(self.proportion, str):
            self.proportion = str(self.proportion)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialProperty(YAMLRoot):
    """
    A reported property value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["MaterialProperty"]
    class_class_curie: ClassVar[str] = "dentmatmech:MaterialProperty"
    class_name: ClassVar[str] = "MaterialProperty"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.MaterialProperty

    name: Union[str, MaterialPropertyName] = None
    property_type: Union[str, "PropertyTypeEnum"] = None
    quality_term: Optional[Union[dict, QualityDescriptor]] = None
    value: Optional[str] = None
    unit: Optional[str] = None
    test_method: Optional[str] = None
    conditions: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MaterialPropertyName):
            self.name = MaterialPropertyName(self.name)

        if self._is_empty(self.property_type):
            self.MissingRequiredField("property_type")
        if not isinstance(self.property_type, PropertyTypeEnum):
            self.property_type = PropertyTypeEnum(self.property_type)

        if self.quality_term is not None and not isinstance(self.quality_term, QualityDescriptor):
            self.quality_term = QualityDescriptor(**as_dict(self.quality_term))

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.test_method is not None and not isinstance(self.test_method, str):
            self.test_method = str(self.test_method)

        if self.conditions is not None and not isinstance(self.conditions, str):
            self.conditions = str(self.conditions)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalUse(YAMLRoot):
    """
    A clinical application of the material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["ClinicalUse"]
    class_class_curie: ClassVar[str] = "dentmatmech:ClinicalUse"
    class_name: ClassVar[str] = "ClinicalUse"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.ClinicalUse

    name: Union[str, ClinicalUseName] = None
    use_context: Union[str, "ClinicalUseContextEnum"] = None
    description: Optional[str] = None
    procedure: Optional[Union[dict, DentalProcedureDescriptor]] = None
    anatomical_site: Optional[Union[dict, AnatomicalEntityDescriptor]] = None
    indications: Optional[Union[str, list[str]]] = empty_list()
    contraindications: Optional[Union[str, list[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ClinicalUseName):
            self.name = ClinicalUseName(self.name)

        if self._is_empty(self.use_context):
            self.MissingRequiredField("use_context")
        if not isinstance(self.use_context, ClinicalUseContextEnum):
            self.use_context = ClinicalUseContextEnum(self.use_context)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.procedure is not None and not isinstance(self.procedure, DentalProcedureDescriptor):
            self.procedure = DentalProcedureDescriptor(**as_dict(self.procedure))

        if self.anatomical_site is not None and not isinstance(self.anatomical_site, AnatomicalEntityDescriptor):
            self.anatomical_site = AnatomicalEntityDescriptor(**as_dict(self.anatomical_site))

        if not isinstance(self.indications, list):
            self.indications = [self.indications] if self.indications is not None else []
        self.indications = [v if isinstance(v, str) else str(v) for v in self.indications]

        if not isinstance(self.contraindications, list):
            self.contraindications = [self.contraindications] if self.contraindications is not None else []
        self.contraindications = [v if isinstance(v, str) else str(v) for v in self.contraindications]

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalPerformance(YAMLRoot):
    """
    A longevity or outcome statistic
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["ClinicalPerformance"]
    class_class_curie: ClassVar[str] = "dentmatmech:ClinicalPerformance"
    class_name: ClassVar[str] = "ClinicalPerformance"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.ClinicalPerformance

    name: Union[str, ClinicalPerformanceName] = None
    measure_type: Union[str, "PerformanceMeasureEnum"] = None
    value: Optional[str] = None
    unit: Optional[str] = None
    follow_up_years: Optional[float] = None
    population: Optional[str] = None
    comparator: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ClinicalPerformanceName):
            self.name = ClinicalPerformanceName(self.name)

        if self._is_empty(self.measure_type):
            self.MissingRequiredField("measure_type")
        if not isinstance(self.measure_type, PerformanceMeasureEnum):
            self.measure_type = PerformanceMeasureEnum(self.measure_type)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.follow_up_years is not None and not isinstance(self.follow_up_years, float):
            self.follow_up_years = float(self.follow_up_years)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.comparator is not None and not isinstance(self.comparator, str):
            self.comparator = str(self.comparator)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseEffect(YAMLRoot):
    """
    An adverse effect, safety concern, or failure mode
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["AdverseEffect"]
    class_class_curie: ClassVar[str] = "dentmatmech:AdverseEffect"
    class_name: ClassVar[str] = "AdverseEffect"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.AdverseEffect

    name: Union[str, AdverseEffectName] = None
    effect_category: Union[str, "AdverseEffectCategoryEnum"] = None
    description: Optional[str] = None
    effect_term: Optional[Union[dict, PhenotypeDescriptor]] = None
    frequency: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, AdverseEffectName):
            self.name = AdverseEffectName(self.name)

        if self._is_empty(self.effect_category):
            self.MissingRequiredField("effect_category")
        if not isinstance(self.effect_category, AdverseEffectCategoryEnum):
            self.effect_category = AdverseEffectCategoryEnum(self.effect_category)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.effect_term is not None and not isinstance(self.effect_term, PhenotypeDescriptor):
            self.effect_term = PhenotypeDescriptor(**as_dict(self.effect_term))

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApprovedUse(YAMLRoot):
    """
    A use the regulator permits for this device type or product
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["ApprovedUse"]
    class_class_curie: ClassVar[str] = "dentmatmech:ApprovedUse"
    class_name: ClassVar[str] = "ApprovedUse"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.ApprovedUse

    name: Union[str, ApprovedUseName] = None
    use_context: Union[str, "ClinicalUseContextEnum"] = None
    description: Optional[str] = None
    procedure: Optional[Union[dict, DentalProcedureDescriptor]] = None
    anatomical_site: Optional[Union[dict, AnatomicalEntityDescriptor]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ApprovedUseName):
            self.name = ApprovedUseName(self.name)

        if self._is_empty(self.use_context):
            self.MissingRequiredField("use_context")
        if not isinstance(self.use_context, ClinicalUseContextEnum):
            self.use_context = ClinicalUseContextEnum(self.use_context)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.procedure is not None and not isinstance(self.procedure, DentalProcedureDescriptor):
            self.procedure = DentalProcedureDescriptor(**as_dict(self.procedure))

        if self.anatomical_site is not None and not isinstance(self.anatomical_site, AnatomicalEntityDescriptor):
            self.anatomical_site = AnatomicalEntityDescriptor(**as_dict(self.anatomical_site))

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegulatoryStatus(YAMLRoot):
    """
    Regulatory classification of the material as a device type, under one agency and one regulation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["RegulatoryStatus"]
    class_class_curie: ClassVar[str] = "dentmatmech:RegulatoryStatus"
    class_name: ClassVar[str] = "RegulatoryStatus"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.RegulatoryStatus

    agency: Union[str, "RegulatoryAgencyEnum"] = None
    status: Union[str, "RegulatoryStatusEnum"] = None
    jurisdiction: Optional[str] = None
    regulation_number: Optional[str] = None
    regulation_title: Optional[str] = None
    device_class: Optional[Union[str, "DeviceClassEnum"]] = None
    product_codes: Optional[Union[str, list[str]]] = empty_list()
    pathways: Optional[Union[Union[str, "RegulatoryPathwayEnum"], list[Union[str, "RegulatoryPathwayEnum"]]]] = empty_list()
    special_controls: Optional[Union[str, list[str]]] = empty_list()
    identification: Optional[str] = None
    approved_uses: Optional[Union[dict[Union[str, ApprovedUseName], Union[dict, ApprovedUse]], list[Union[dict, ApprovedUse]]]] = empty_dict()
    restrictions: Optional[Union[str, list[str]]] = empty_list()
    effective_date: Optional[Union[str, XSDDate]] = None
    source_url: Optional[Union[str, URI]] = None
    notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.agency):
            self.MissingRequiredField("agency")
        if not isinstance(self.agency, RegulatoryAgencyEnum):
            self.agency = RegulatoryAgencyEnum(self.agency)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, RegulatoryStatusEnum):
            self.status = RegulatoryStatusEnum(self.status)

        if self.jurisdiction is not None and not isinstance(self.jurisdiction, str):
            self.jurisdiction = str(self.jurisdiction)

        if self.regulation_number is not None and not isinstance(self.regulation_number, str):
            self.regulation_number = str(self.regulation_number)

        if self.regulation_title is not None and not isinstance(self.regulation_title, str):
            self.regulation_title = str(self.regulation_title)

        if self.device_class is not None and not isinstance(self.device_class, DeviceClassEnum):
            self.device_class = DeviceClassEnum(self.device_class)

        if not isinstance(self.product_codes, list):
            self.product_codes = [self.product_codes] if self.product_codes is not None else []
        self.product_codes = [v if isinstance(v, str) else str(v) for v in self.product_codes]

        if not isinstance(self.pathways, list):
            self.pathways = [self.pathways] if self.pathways is not None else []
        self.pathways = [v if isinstance(v, RegulatoryPathwayEnum) else RegulatoryPathwayEnum(v) for v in self.pathways]

        if not isinstance(self.special_controls, list):
            self.special_controls = [self.special_controls] if self.special_controls is not None else []
        self.special_controls = [v if isinstance(v, str) else str(v) for v in self.special_controls]

        if self.identification is not None and not isinstance(self.identification, str):
            self.identification = str(self.identification)

        self._normalize_inlined_as_list(slot_name="approved_uses", slot_type=ApprovedUse, key_name="name", keyed=True)

        if not isinstance(self.restrictions, list):
            self.restrictions = [self.restrictions] if self.restrictions is not None else []
        self.restrictions = [v if isinstance(v, str) else str(v) for v in self.restrictions]

        if self.effective_date is not None and not isinstance(self.effective_date, XSDDate):
            self.effective_date = XSDDate(self.effective_date)

        if self.source_url is not None and not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegulatorySubmission(YAMLRoot):
    """
    One premarket submission for a commercial product and its outcome
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["RegulatorySubmission"]
    class_class_curie: ClassVar[str] = "dentmatmech:RegulatorySubmission"
    class_name: ClassVar[str] = "RegulatorySubmission"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.RegulatorySubmission

    agency: Union[str, "RegulatoryAgencyEnum"] = None
    submission_number: Optional[str] = None
    pathway: Optional[Union[str, "RegulatoryPathwayEnum"]] = None
    decision: Optional[Union[str, "RegulatoryStatusEnum"]] = None
    decision_date: Optional[Union[str, XSDDate]] = None
    product_code: Optional[str] = None
    regulation_number: Optional[str] = None
    indications_for_use: Optional[str] = None
    source_url: Optional[Union[str, URI]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.agency):
            self.MissingRequiredField("agency")
        if not isinstance(self.agency, RegulatoryAgencyEnum):
            self.agency = RegulatoryAgencyEnum(self.agency)

        if self.submission_number is not None and not isinstance(self.submission_number, str):
            self.submission_number = str(self.submission_number)

        if self.pathway is not None and not isinstance(self.pathway, RegulatoryPathwayEnum):
            self.pathway = RegulatoryPathwayEnum(self.pathway)

        if self.decision is not None and not isinstance(self.decision, RegulatoryStatusEnum):
            self.decision = RegulatoryStatusEnum(self.decision)

        if self.decision_date is not None and not isinstance(self.decision_date, XSDDate):
            self.decision_date = XSDDate(self.decision_date)

        if self.product_code is not None and not isinstance(self.product_code, str):
            self.product_code = str(self.product_code)

        if self.regulation_number is not None and not isinstance(self.regulation_number, str):
            self.regulation_number = str(self.regulation_number)

        if self.indications_for_use is not None and not isinstance(self.indications_for_use, str):
            self.indications_for_use = str(self.indications_for_use)

        if self.source_url is not None and not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommercialProduct(YAMLRoot):
    """
    A branded product that is an instance of this material type
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["CommercialProduct"]
    class_class_curie: ClassVar[str] = "dentmatmech:CommercialProduct"
    class_name: ClassVar[str] = "CommercialProduct"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.CommercialProduct

    name: Union[str, CommercialProductName] = None
    manufacturer: Optional[str] = None
    description: Optional[str] = None
    submissions: Optional[Union[Union[dict, RegulatorySubmission], list[Union[dict, RegulatorySubmission]]]] = empty_list()
    see_also: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CommercialProductName):
            self.name = CommercialProductName(self.name)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="submissions", slot_type=RegulatorySubmission, key_name="agency", keyed=False)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, URI) else URI(v) for v in self.see_also]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(YAMLRoot):
    """
    A technical standard or specification
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["Standard"]
    class_class_curie: ClassVar[str] = "dentmatmech:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.Standard

    identifier: str = None
    title: Optional[str] = None
    organization: Optional[str] = None
    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.organization is not None and not isinstance(self.organization, str):
            self.organization = str(self.organization)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DentalMaterial(YAMLRoot):
    """
    A dental material entry. One file per material in kb/materials/, anchored to an OHD term.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DENTMATMECH["DentalMaterial"]
    class_class_curie: ClassVar[str] = "dentmatmech:DentalMaterial"
    class_name: ClassVar[str] = "DentalMaterial"
    class_model_uri: ClassVar[URIRef] = DENTMATMECH.DentalMaterial

    name: Union[str, DentalMaterialName] = None
    material_term: Union[dict, DentalMaterialDescriptor] = None
    category: Union[str, "MaterialCategoryEnum"] = None
    description: Optional[str] = None
    creation_date: Optional[str] = None
    curation_status: Optional[Union[str, "CurationStatusEnum"]] = None
    parents: Optional[Union[str, list[str]]] = empty_list()
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    mappings: Optional[Union[Union[dict, Mapping], list[Union[dict, Mapping]]]] = empty_list()
    setting_mechanisms: Optional[Union[Union[str, "SettingMechanismEnum"], list[Union[str, "SettingMechanismEnum"]]]] = empty_list()
    composition: Optional[Union[dict[Union[str, ComponentName], Union[dict, Component]], list[Union[dict, Component]]]] = empty_dict()
    properties: Optional[Union[dict[Union[str, MaterialPropertyName], Union[dict, MaterialProperty]], list[Union[dict, MaterialProperty]]]] = empty_dict()
    clinical_uses: Optional[Union[dict[Union[str, ClinicalUseName], Union[dict, ClinicalUse]], list[Union[dict, ClinicalUse]]]] = empty_dict()
    clinical_performance: Optional[Union[dict[Union[str, ClinicalPerformanceName], Union[dict, ClinicalPerformance]], list[Union[dict, ClinicalPerformance]]]] = empty_dict()
    adverse_effects: Optional[Union[dict[Union[str, AdverseEffectName], Union[dict, AdverseEffect]], list[Union[dict, AdverseEffect]]]] = empty_dict()
    regulatory_status: Optional[Union[Union[dict, RegulatoryStatus], list[Union[dict, RegulatoryStatus]]]] = empty_list()
    products: Optional[Union[dict[Union[str, CommercialProductName], Union[dict, CommercialProduct]], list[Union[dict, CommercialProduct]]]] = empty_dict()
    standards: Optional[Union[Union[dict, Standard], list[Union[dict, Standard]]]] = empty_list()
    see_also: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DentalMaterialName):
            self.name = DentalMaterialName(self.name)

        if self._is_empty(self.material_term):
            self.MissingRequiredField("material_term")
        if not isinstance(self.material_term, DentalMaterialDescriptor):
            self.material_term = DentalMaterialDescriptor(**as_dict(self.material_term))

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, MaterialCategoryEnum):
            self.category = MaterialCategoryEnum(self.category)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.curation_status is not None and not isinstance(self.curation_status, CurationStatusEnum):
            self.curation_status = CurationStatusEnum(self.curation_status)

        if not isinstance(self.parents, list):
            self.parents = [self.parents] if self.parents is not None else []
        self.parents = [v if isinstance(v, str) else str(v) for v in self.parents]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_list(slot_name="mappings", slot_type=Mapping, key_name="id", keyed=False)

        if not isinstance(self.setting_mechanisms, list):
            self.setting_mechanisms = [self.setting_mechanisms] if self.setting_mechanisms is not None else []
        self.setting_mechanisms = [v if isinstance(v, SettingMechanismEnum) else SettingMechanismEnum(v) for v in self.setting_mechanisms]

        self._normalize_inlined_as_list(slot_name="composition", slot_type=Component, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="properties", slot_type=MaterialProperty, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="clinical_uses", slot_type=ClinicalUse, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="clinical_performance", slot_type=ClinicalPerformance, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="adverse_effects", slot_type=AdverseEffect, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="regulatory_status", slot_type=RegulatoryStatus, key_name="agency", keyed=False)

        self._normalize_inlined_as_list(slot_name="products", slot_type=CommercialProduct, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="standards", slot_type=Standard, key_name="identifier", keyed=False)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, URI) else URI(v) for v in self.see_also]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


# Enumerations
class EvidenceItemSupportEnum(EnumDefinitionImpl):
    """
    How the cited source relates to the claim it is attached to
    """
    SUPPORT = PermissibleValue(
        text="SUPPORT",
        title="Supports",
        description="The cited evidence directly supports the claim")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        title="Partially supports",
        description="The cited evidence partially or indirectly supports the claim")
    REFUTE = PermissibleValue(
        text="REFUTE",
        title="Refutes",
        description="The cited evidence directly contradicts the claim")
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        title="No evidence",
        description="The cited reference does not contain evidence relevant to the claim")
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        title="Wrong statement",
        description="""The claim contains a demonstrable factual error and the cited source documents the correct information""")

    _defn = EnumDefinition(
        name="EvidenceItemSupportEnum",
        description="How the cited source relates to the claim it is attached to",
    )

class EvidenceSourceEnum(EnumDefinitionImpl):
    """
    The kind of source an evidence item comes from
    """
    HUMAN_CLINICAL = PermissibleValue(
        text="HUMAN_CLINICAL",
        title="Human clinical",
        description="Clinical trials, cohort studies, case series, or practice-based research in patients")
    IN_VITRO = PermissibleValue(
        text="IN_VITRO",
        title="In vitro / laboratory",
        description="Bench testing of the material (mechanical, physical, chemical, cytotoxicity, wear simulation)")
    IN_SILICO = PermissibleValue(
        text="IN_SILICO",
        title="Computational",
        description="Finite element analysis, simulation, or other modeling")
    SYSTEMATIC_REVIEW = PermissibleValue(
        text="SYSTEMATIC_REVIEW",
        title="Systematic review or meta-analysis",
        description="Pooled or systematically reviewed evidence")
    REGULATORY_DOCUMENT = PermissibleValue(
        text="REGULATORY_DOCUMENT",
        title="Regulatory document",
        description="""A regulation (e.g. 21 CFR 872), a classification database record, a 510(k) summary, a PMA approval order, a guidance document, or an equivalent from another jurisdiction""")
    STANDARD = PermissibleValue(
        text="STANDARD",
        title="Technical standard",
        description="An ISO, ADA/ANSI, or ASTM standard or specification")
    MANUFACTURER = PermissibleValue(
        text="MANUFACTURER",
        title="Manufacturer document",
        description="Instructions for use, safety data sheet, technical profile, or product literature")
    TEXTBOOK = PermissibleValue(
        text="TEXTBOOK",
        title="Textbook or monograph",
        description="A textbook, monograph, or reference work")
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other",
        description="Evidence not fitting the above")

    _defn = EnumDefinition(
        name="EvidenceSourceEnum",
        description="The kind of source an evidence item comes from",
    )

class MaterialCategoryEnum(EnumDefinitionImpl):
    """
    Broad material class. Derived from the OHD ancestry of the bound term when seeding, and kept as an explicit slot
    so the browser can facet on it without walking the ontology.
    """
    METAL = PermissibleValue(
        text="METAL",
        description="Metals and alloys (amalgam, noble and base metal alloys, titanium, stainless steel)",
        meaning=OHD["0000048"])
    CERAMIC = PermissibleValue(
        text="CERAMIC",
        description="Glass-matrix, polycrystalline, and resin-matrix ceramics",
        meaning=OHD["0000135"])
    RESIN_COMPOSITE = PermissibleValue(
        text="RESIN_COMPOSITE",
        description="Resin-based composites (polymer matrix reinforced with filler)",
        meaning=OHD["0000036"])
    CEMENT = PermissibleValue(
        text="CEMENT",
        description="Luting, lining, base, and endodontic cements, whether acid-base, resin, or hydraulic")
    POLYMER = PermissibleValue(
        text="POLYMER",
        description="Unfilled or lightly filled polymers (denture base resins, impression materials, sealants)")
    ADHESIVE = PermissibleValue(
        text="ADHESIVE",
        description="Bonding agents, primers, and their monomers")
    HYBRID = PermissibleValue(
        text="HYBRID",
        description="""Materials that deliberately combine two categories (e.g. compomers, resin-modified glass ionomers)""")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Does not fit the other categories")

    _defn = EnumDefinition(
        name="MaterialCategoryEnum",
        description="""Broad material class. Derived from the OHD ancestry of the bound term when seeding, and kept as an explicit slot so the browser can facet on it without walking the ontology.""",
    )

class SettingMechanismEnum(EnumDefinitionImpl):
    """
    How the material hardens or is formed into its final state
    """
    LIGHT_CURED = PermissibleValue(
        text="LIGHT_CURED",
        description="Photopolymerization initiated by visible (typically blue) light")
    SELF_CURED = PermissibleValue(
        text="SELF_CURED",
        description="Chemically initiated polymerization (two-paste or powder-liquid)")
    DUAL_CURED = PermissibleValue(
        text="DUAL_CURED",
        description="Both light-initiated and chemically initiated polymerization")
    ACID_BASE_REACTION = PermissibleValue(
        text="ACID_BASE_REACTION",
        description="Acid-base setting reaction between a basic powder and an acidic liquid")
    AMALGAMATION = PermissibleValue(
        text="AMALGAMATION",
        description="Reaction of mercury with alloy particles")
    HYDRATION = PermissibleValue(
        text="HYDRATION",
        description="Hydraulic setting on contact with water (e.g. calcium silicate cements)")
    SINTERING = PermissibleValue(
        text="SINTERING",
        description="Densification of a powder compact or milled blank at high temperature")
    HEAT_PRESSING = PermissibleValue(
        text="HEAT_PRESSING",
        description="Pressing of a heated glass ceramic ingot into a mold")
    CASTING = PermissibleValue(
        text="CASTING",
        description="Lost-wax casting of a molten alloy")
    MILLING = PermissibleValue(
        text="MILLING",
        description="Subtractive CAD/CAM machining of a prefabricated block or disc")
    ADDITIVE_MANUFACTURING = PermissibleValue(
        text="ADDITIVE_MANUFACTURING",
        description="3D printing (stereolithography, selective laser melting, etc.)")
    COLD_WORKING = PermissibleValue(
        text="COLD_WORKING",
        description="Condensation or burnishing without a chemical set (e.g. gold foil)")
    NONE = PermissibleValue(
        text="NONE",
        description="Supplied in final form; no setting step")

    _defn = EnumDefinition(
        name="SettingMechanismEnum",
        description="How the material hardens or is formed into its final state",
    )

class ComponentRoleEnum(EnumDefinitionImpl):
    """
    The functional role a component plays in the material's formulation
    """
    MATRIX = PermissibleValue(
        text="MATRIX",
        description="Continuous phase (polymer matrix, glass phase, metal matrix)")
    FILLER = PermissibleValue(
        text="FILLER",
        description="Dispersed reinforcing or bulking particles or fibers")
    COUPLING_AGENT = PermissibleValue(
        text="COUPLING_AGENT",
        description="Agent bonding filler to matrix (e.g. silane)")
    INITIATOR = PermissibleValue(
        text="INITIATOR",
        description="Initiates polymerization (e.g. camphorquinone, benzoyl peroxide)")
    ACTIVATOR = PermissibleValue(
        text="ACTIVATOR",
        description="Co-initiator or accelerator (e.g. tertiary amine)")
    INHIBITOR = PermissibleValue(
        text="INHIBITOR",
        description="Stabilizer that prevents premature polymerization")
    POWDER = PermissibleValue(
        text="POWDER",
        description="Powder component of a powder-liquid system")
    LIQUID = PermissibleValue(
        text="LIQUID",
        description="Liquid component of a powder-liquid system")
    ALLOYING_ELEMENT = PermissibleValue(
        text="ALLOYING_ELEMENT",
        description="Element present in an alloy")
    CRYSTALLINE_PHASE = PermissibleValue(
        text="CRYSTALLINE_PHASE",
        description="Crystalline phase in a ceramic")
    STABILIZER = PermissibleValue(
        text="STABILIZER",
        description="Phase stabilizer (e.g. yttria in zirconia)")
    RADIOPACIFIER = PermissibleValue(
        text="RADIOPACIFIER",
        description="Added to make the material radiopaque")
    PIGMENT = PermissibleValue(
        text="PIGMENT",
        description="Colorant or opacifier")
    SOLVENT = PermissibleValue(
        text="SOLVENT",
        description="Carrier or solvent")
    FLUORIDE_SOURCE = PermissibleValue(
        text="FLUORIDE_SOURCE",
        description="Component that releases fluoride")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other role")

    _defn = EnumDefinition(
        name="ComponentRoleEnum",
        description="The functional role a component plays in the material's formulation",
    )

class PropertyTypeEnum(EnumDefinitionImpl):
    """
    Physical, mechanical, chemical, optical, and biological properties commonly reported for dental materials. Units
    are recorded on the property itself; this enum only names the quantity.
    """
    FLEXURAL_STRENGTH = PermissibleValue(
        text="FLEXURAL_STRENGTH",
        description="Flexural (bending) strength, typically MPa")
    COMPRESSIVE_STRENGTH = PermissibleValue(
        text="COMPRESSIVE_STRENGTH",
        description="Compressive strength, typically MPa")
    TENSILE_STRENGTH = PermissibleValue(
        text="TENSILE_STRENGTH",
        description="Tensile or diametral tensile strength, typically MPa")
    ELASTIC_MODULUS = PermissibleValue(
        text="ELASTIC_MODULUS",
        description="Elastic (Young's) modulus, typically GPa")
    FRACTURE_TOUGHNESS = PermissibleValue(
        text="FRACTURE_TOUGHNESS",
        description="Fracture toughness, typically MPa·m^0.5")
    HARDNESS = PermissibleValue(
        text="HARDNESS",
        description="Surface hardness (Vickers, Knoop)")
    WEAR_RESISTANCE = PermissibleValue(
        text="WEAR_RESISTANCE",
        description="Wear or abrasion resistance")
    BOND_STRENGTH = PermissibleValue(
        text="BOND_STRENGTH",
        description="Bond strength to tooth structure or another substrate, typically MPa")
    POLYMERIZATION_SHRINKAGE = PermissibleValue(
        text="POLYMERIZATION_SHRINKAGE",
        description="Volumetric or linear shrinkage on setting, typically percent")
    SHRINKAGE_STRESS = PermissibleValue(
        text="SHRINKAGE_STRESS",
        description="Stress generated during setting")
    DEGREE_OF_CONVERSION = PermissibleValue(
        text="DEGREE_OF_CONVERSION",
        description="Fraction of monomer converted to polymer, typically percent")
    DEPTH_OF_CURE = PermissibleValue(
        text="DEPTH_OF_CURE",
        description="Depth to which a light-cured material polymerizes adequately, typically mm")
    WATER_SORPTION = PermissibleValue(
        text="WATER_SORPTION",
        description="Water sorption, typically µg/mm^3")
    SOLUBILITY = PermissibleValue(
        text="SOLUBILITY",
        description="Solubility or disintegration in water or acid")
    THERMAL_EXPANSION = PermissibleValue(
        text="THERMAL_EXPANSION",
        description="Coefficient of thermal expansion")
    THERMAL_CONDUCTIVITY = PermissibleValue(
        text="THERMAL_CONDUCTIVITY",
        description="Thermal conductivity")
    RADIOPACITY = PermissibleValue(
        text="RADIOPACITY",
        description="Radiopacity, typically relative to aluminum thickness")
    TRANSLUCENCY = PermissibleValue(
        text="TRANSLUCENCY",
        description="Translucency or contrast ratio")
    COLOR_STABILITY = PermissibleValue(
        text="COLOR_STABILITY",
        description="Resistance to discoloration")
    FLUORIDE_RELEASE = PermissibleValue(
        text="FLUORIDE_RELEASE",
        description="Fluoride release or recharge")
    SETTING_TIME = PermissibleValue(
        text="SETTING_TIME",
        description="Time to set, typically minutes")
    WORKING_TIME = PermissibleValue(
        text="WORKING_TIME",
        description="Time available for manipulation, typically minutes")
    FILM_THICKNESS = PermissibleValue(
        text="FILM_THICKNESS",
        description="Film thickness of a luting agent, typically µm")
    CORROSION_RESISTANCE = PermissibleValue(
        text="CORROSION_RESISTANCE",
        description="Resistance to corrosion or tarnish")
    BIOCOMPATIBILITY = PermissibleValue(
        text="BIOCOMPATIBILITY",
        description="Biological response (cytotoxicity, sensitization, irritation)")
    ANTIBACTERIAL_ACTIVITY = PermissibleValue(
        text="ANTIBACTERIAL_ACTIVITY",
        description="Antibacterial or antimicrobial effect")
    DENSITY = PermissibleValue(
        text="DENSITY",
        description="Density")
    MELTING_RANGE = PermissibleValue(
        text="MELTING_RANGE",
        description="Melting or fusion temperature range")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other property")

    _defn = EnumDefinition(
        name="PropertyTypeEnum",
        description="""Physical, mechanical, chemical, optical, and biological properties commonly reported for dental materials. Units are recorded on the property itself; this enum only names the quantity.""",
    )

class ClinicalUseContextEnum(EnumDefinitionImpl):
    """
    The broad clinical context in which the material is used
    """
    DIRECT_RESTORATION = PermissibleValue(
        text="DIRECT_RESTORATION",
        description="Placed and shaped directly in the prepared tooth (fillings)")
    INDIRECT_RESTORATION = PermissibleValue(
        text="INDIRECT_RESTORATION",
        description="Fabricated outside the mouth and cemented (inlays, onlays, crowns, bridges, veneers)")
    LUTING = PermissibleValue(
        text="LUTING",
        description="Cementing an indirect restoration, post, or orthodontic appliance")
    LINER_OR_BASE = PermissibleValue(
        text="LINER_OR_BASE",
        description="Cavity liner or base under a restoration")
    PULP_THERAPY = PermissibleValue(
        text="PULP_THERAPY",
        description="Pulp capping, pulpotomy, or other vital pulp therapy")
    ENDODONTIC = PermissibleValue(
        text="ENDODONTIC",
        description="Root canal filling, sealing, perforation repair, apexification")
    IMPLANT = PermissibleValue(
        text="IMPLANT",
        description="Endosseous implant fixture or abutment")
    PROSTHODONTIC = PermissibleValue(
        text="PROSTHODONTIC",
        description="Denture base, denture teeth, or framework")
    ORTHODONTIC = PermissibleValue(
        text="ORTHODONTIC",
        description="Brackets, wires, or bonding of appliances")
    PREVENTIVE = PermissibleValue(
        text="PREVENTIVE",
        description="Pit and fissure sealant or protective coating")
    ADHESIVE = PermissibleValue(
        text="ADHESIVE",
        description="Bonding agent or primer")
    IMPRESSION = PermissibleValue(
        text="IMPRESSION",
        description="Impression or bite registration")
    TEMPORARY = PermissibleValue(
        text="TEMPORARY",
        description="Provisional restoration or temporary filling")
    SURGICAL = PermissibleValue(
        text="SURGICAL",
        description="Bone graft, membrane, or other surgical use")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other context")

    _defn = EnumDefinition(
        name="ClinicalUseContextEnum",
        description="The broad clinical context in which the material is used",
    )

class PerformanceMeasureEnum(EnumDefinitionImpl):
    """
    Kind of clinical performance statistic being reported
    """
    SURVIVAL_RATE = PermissibleValue(
        text="SURVIVAL_RATE",
        description="Proportion of restorations surviving at a given follow-up")
    SUCCESS_RATE = PermissibleValue(
        text="SUCCESS_RATE",
        description="Proportion meeting a stricter success criterion (survival without repair or complication)")
    ANNUAL_FAILURE_RATE = PermissibleValue(
        text="ANNUAL_FAILURE_RATE",
        description="Annual failure rate, percent per year")
    MEDIAN_SURVIVAL_TIME = PermissibleValue(
        text="MEDIAN_SURVIVAL_TIME",
        description="Median time to failure or replacement")
    RETENTION_RATE = PermissibleValue(
        text="RETENTION_RATE",
        description="Proportion retained (sealants, veneers, cervical restorations)")
    COMPLICATION_RATE = PermissibleValue(
        text="COMPLICATION_RATE",
        description="Proportion experiencing a named complication (chipping, secondary caries, fracture)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other measure")

    _defn = EnumDefinition(
        name="PerformanceMeasureEnum",
        description="Kind of clinical performance statistic being reported",
    )

class AdverseEffectCategoryEnum(EnumDefinitionImpl):
    """
    Broad category of an adverse effect or safety concern
    """
    ALLERGIC_OR_HYPERSENSITIVITY = PermissibleValue(
        text="ALLERGIC_OR_HYPERSENSITIVITY",
        description="Contact allergy, lichenoid reaction, or systemic hypersensitivity")
    TOXICITY = PermissibleValue(
        text="TOXICITY",
        description="Local or systemic toxicity, including cytotoxicity and leachables")
    MECHANICAL_FAILURE = PermissibleValue(
        text="MECHANICAL_FAILURE",
        description="Fracture, chipping, debonding, or wear of the restoration")
    SECONDARY_CARIES = PermissibleValue(
        text="SECONDARY_CARIES",
        description="Recurrent caries at the restoration margin")
    PULPAL_RESPONSE = PermissibleValue(
        text="PULPAL_RESPONSE",
        description="Pulpal irritation, sensitivity, or necrosis")
    PERIODONTAL_RESPONSE = PermissibleValue(
        text="PERIODONTAL_RESPONSE",
        description="Gingival or periodontal inflammation adjacent to the material")
    ANTAGONIST_WEAR = PermissibleValue(
        text="ANTAGONIST_WEAR",
        description="Wear of opposing natural teeth or restorations")
    ESTHETIC = PermissibleValue(
        text="ESTHETIC",
        description="Discoloration, staining, or shade mismatch")
    OCCUPATIONAL = PermissibleValue(
        text="OCCUPATIONAL",
        description="Hazard to dental personnel during handling")
    ENVIRONMENTAL = PermissibleValue(
        text="ENVIRONMENTAL",
        description="Environmental release (e.g. mercury in wastewater)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other")

    _defn = EnumDefinition(
        name="AdverseEffectCategoryEnum",
        description="Broad category of an adverse effect or safety concern",
    )

class RegulatoryAgencyEnum(EnumDefinitionImpl):
    """
    The regulator whose decision or classification is being recorded. FDA is the first target; the others are listed
    so the model does not have to change when they are curated.
    """
    FDA = PermissibleValue(
        text="FDA",
        title="US Food and Drug Administration",
        description="United States. Dental devices are regulated under 21 CFR part 872 by CDRH.")
    EU_MDR = PermissibleValue(
        text="EU_MDR",
        title="European Union (MDR 2017/745)",
        description="CE marking under the Medical Device Regulation, via a notified body for class IIa and above.")
    HEALTH_CANADA = PermissibleValue(
        text="HEALTH_CANADA",
        title="Health Canada")
    MHRA = PermissibleValue(
        text="MHRA",
        title="UK Medicines and Healthcare products Regulatory Agency")
    TGA = PermissibleValue(
        text="TGA",
        title="Australian Therapeutic Goods Administration")
    PMDA = PermissibleValue(
        text="PMDA",
        title="Japan Pharmaceuticals and Medical Devices Agency")
    NMPA = PermissibleValue(
        text="NMPA",
        title="China National Medical Products Administration")
    ANVISA = PermissibleValue(
        text="ANVISA",
        title="Brazil Agência Nacional de Vigilância Sanitária")
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other regulator")

    _defn = EnumDefinition(
        name="RegulatoryAgencyEnum",
        description="""The regulator whose decision or classification is being recorded. FDA is the first target; the others are listed so the model does not have to change when they are curated.""",
    )

class DeviceClassEnum(EnumDefinitionImpl):
    """
    Risk-based device class. FDA uses I, II, III. The EU MDR uses I, IIa, IIb, III. Record the class as the regulator
    states it; the agency slot disambiguates the scheme.
    """
    CLASS_I = PermissibleValue(
        text="CLASS_I",
        title="Class I",
        description="Lowest risk; general controls (FDA) or self-certification (EU)")
    CLASS_IIA = PermissibleValue(
        text="CLASS_IIA",
        title="Class IIa",
        description="EU MDR medium-low risk")
    CLASS_II = PermissibleValue(
        text="CLASS_II",
        title="Class II",
        description="FDA moderate risk; general and special controls")
    CLASS_IIB = PermissibleValue(
        text="CLASS_IIB",
        title="Class IIb",
        description="EU MDR medium-high risk")
    CLASS_III = PermissibleValue(
        text="CLASS_III",
        title="Class III",
        description="Highest risk; premarket approval (FDA) or full conformity assessment (EU)")
    UNCLASSIFIED = PermissibleValue(
        text="UNCLASSIFIED",
        title="Unclassified",
        description="No classification regulation applies or classification not yet determined")
    NOT_A_DEVICE = PermissibleValue(
        text="NOT_A_DEVICE",
        title="Not regulated as a device",
        description="The material is not regulated as a medical device in this jurisdiction")

    _defn = EnumDefinition(
        name="DeviceClassEnum",
        description="""Risk-based device class. FDA uses I, II, III. The EU MDR uses I, IIa, IIb, III. Record the class as the regulator states it; the agency slot disambiguates the scheme.""",
    )

class RegulatoryPathwayEnum(EnumDefinitionImpl):
    """
    The premarket route by which the material or product reached the market
    """
    PREMARKET_NOTIFICATION_510K = PermissibleValue(
        text="PREMARKET_NOTIFICATION_510K",
        title="510(k) premarket notification",
        description="FDA clearance by demonstrating substantial equivalence to a predicate device")
    PREMARKET_APPROVAL_PMA = PermissibleValue(
        text="PREMARKET_APPROVAL_PMA",
        title="Premarket approval (PMA)",
        description="FDA approval of a class III device on its own safety and effectiveness data")
    DE_NOVO = PermissibleValue(
        text="DE_NOVO",
        title="De Novo classification",
        description="FDA pathway for novel low-to-moderate risk devices without a predicate")
    EXEMPT_510K = PermissibleValue(
        text="EXEMPT_510K",
        title="510(k) exempt",
        description="""Marketed without premarket notification, subject to the limitations of 21 CFR 872.9, but still subject to registration, listing, and general controls""")
    HUMANITARIAN_DEVICE_EXEMPTION = PermissibleValue(
        text="HUMANITARIAN_DEVICE_EXEMPTION",
        title="Humanitarian device exemption")
    PRE_AMENDMENT = PermissibleValue(
        text="PRE_AMENDMENT",
        title="Pre-amendment device",
        description="Marketed before the 1976 Medical Device Amendments and grandfathered")
    CE_MARK = PermissibleValue(
        text="CE_MARK",
        title="CE marking",
        description="EU conformity assessment under MDR or the earlier MDD")
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other")

    _defn = EnumDefinition(
        name="RegulatoryPathwayEnum",
        description="The premarket route by which the material or product reached the market",
    )

class RegulatoryStatusEnum(EnumDefinitionImpl):
    """
    The current standing of the material or product with the regulator
    """
    CLEARED = PermissibleValue(
        text="CLEARED",
        description="Cleared for marketing (FDA 510(k))")
    APPROVED = PermissibleValue(
        text="APPROVED",
        description="Approved for marketing (FDA PMA, or equivalent)")
    GRANTED = PermissibleValue(
        text="GRANTED",
        description="De Novo request granted")
    EXEMPT = PermissibleValue(
        text="EXEMPT",
        description="Exempt from premarket notification; may be marketed under general controls")
    CE_MARKED = PermissibleValue(
        text="CE_MARKED",
        description="Carries a CE mark under EU device law")
    REGISTERED = PermissibleValue(
        text="REGISTERED",
        description="Registered or listed with the regulator without a specific marketing decision")
    PENDING = PermissibleValue(
        text="PENDING",
        description="Submission under review")
    RESTRICTED = PermissibleValue(
        text="RESTRICTED",
        description="""Marketed with use restrictions imposed by the regulator (e.g. population-specific recommendations)""")
    WITHDRAWN = PermissibleValue(
        text="WITHDRAWN",
        description="Withdrawn from the market by the manufacturer")
    RECALLED = PermissibleValue(
        text="RECALLED",
        description="Subject to a recall")
    BANNED = PermissibleValue(
        text="BANNED",
        description="Prohibited by the regulator")
    NOT_REGULATED = PermissibleValue(
        text="NOT_REGULATED",
        description="Not regulated as a device in this jurisdiction")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Status not yet curated")

    _defn = EnumDefinition(
        name="RegulatoryStatusEnum",
        description="The current standing of the material or product with the regulator",
    )

class CurationStatusEnum(EnumDefinitionImpl):
    """
    How far along this entry is
    """
    STUB = PermissibleValue(
        text="STUB",
        description="Seeded from the ontology only; no curated content beyond name, definition, and term")
    IN_PROGRESS = PermissibleValue(
        text="IN_PROGRESS",
        description="Some sections curated")
    CURATED = PermissibleValue(
        text="CURATED",
        description="All recommended sections populated with evidence")
    REVIEWED = PermissibleValue(
        text="REVIEWED",
        description="Curated and reviewed by a domain expert")

    _defn = EnumDefinition(
        name="CurationStatusEnum",
        description="How far along this entry is",
    )

class MappingPredicateEnum(EnumDefinitionImpl):
    """
    SKOS mapping relation between this material and a term in another vocabulary
    """
    EXACT_MATCH = PermissibleValue(
        text="EXACT_MATCH",
        meaning=SKOS["exactMatch"])
    CLOSE_MATCH = PermissibleValue(
        text="CLOSE_MATCH",
        meaning=SKOS["closeMatch"])
    BROAD_MATCH = PermissibleValue(
        text="BROAD_MATCH",
        meaning=SKOS["broadMatch"])
    NARROW_MATCH = PermissibleValue(
        text="NARROW_MATCH",
        meaning=SKOS["narrowMatch"])
    RELATED_MATCH = PermissibleValue(
        text="RELATED_MATCH",
        meaning=SKOS["relatedMatch"])

    _defn = EnumDefinition(
        name="MappingPredicateEnum",
        description="SKOS mapping relation between this material and a term in another vocabulary",
    )

class DentalMaterialTerm(EnumDefinitionImpl):
    """
    A dental restoration material term from OHD. The root itself is included so the top-of-tree entry validates.
    """
    _defn = EnumDefinition(
        name="DentalMaterialTerm",
        description="""A dental restoration material term from OHD. The root itself is included so the top-of-tree entry validates.""",
    )

class DentalProcedureTerm(EnumDefinitionImpl):
    """
    A dental procedure term from OHD
    """
    _defn = EnumDefinition(
        name="DentalProcedureTerm",
        description="A dental procedure term from OHD",
    )

class ChemicalEntityTerm(EnumDefinitionImpl):
    """
    A chemical entity from CHEBI
    """
    _defn = EnumDefinition(
        name="ChemicalEntityTerm",
        description="A chemical entity from CHEBI",
    )

class AnatomicalEntityTerm(EnumDefinitionImpl):
    """
    An anatomical entity from UBERON
    """
    _defn = EnumDefinition(
        name="AnatomicalEntityTerm",
        description="An anatomical entity from UBERON",
    )

class PhenotypeTerm(EnumDefinitionImpl):
    """
    A phenotype (HP) or disease (MONDO) term, for adverse effects
    """
    _defn = EnumDefinition(
        name="PhenotypeTerm",
        description="A phenotype (HP) or disease (MONDO) term, for adverse effects",
    )

class QualityTerm(EnumDefinitionImpl):
    """
    A quality from PATO, for typed material properties
    """
    _defn = EnumDefinition(
        name="QualityTerm",
        description="A quality from PATO, for typed material properties",
    )

# Slots
class slots:
    pass

slots.name = Slot(uri=DENTMATMECH.name, name="name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.name, domain=None, range=URIRef)

slots.description = Slot(uri=DENTMATMECH.description, name="description", curie=DENTMATMECH.curie('description'),
                   model_uri=DENTMATMECH.description, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=DENTMATMECH.synonyms, name="synonyms", curie=DENTMATMECH.curie('synonyms'),
                   model_uri=DENTMATMECH.synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.creation_date = Slot(uri=DENTMATMECH.creation_date, name="creation_date", curie=DENTMATMECH.curie('creation_date'),
                   model_uri=DENTMATMECH.creation_date, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.curation_status = Slot(uri=DENTMATMECH.curation_status, name="curation_status", curie=DENTMATMECH.curie('curation_status'),
                   model_uri=DENTMATMECH.curation_status, domain=None, range=Optional[Union[str, "CurationStatusEnum"]])

slots.notes = Slot(uri=DENTMATMECH.notes, name="notes", curie=DENTMATMECH.curie('notes'),
                   model_uri=DENTMATMECH.notes, domain=None, range=Optional[str])

slots.id = Slot(uri=DENTMATMECH.id, name="id", curie=DENTMATMECH.curie('id'),
                   model_uri=DENTMATMECH.id, domain=None, range=Union[str, URIorCURIE])

slots.label = Slot(uri=DENTMATMECH.label, name="label", curie=DENTMATMECH.curie('label'),
                   model_uri=DENTMATMECH.label, domain=None, range=str)

slots.preferred_term = Slot(uri=DENTMATMECH.preferred_term, name="preferred_term", curie=DENTMATMECH.curie('preferred_term'),
                   model_uri=DENTMATMECH.preferred_term, domain=None, range=Optional[str])

slots.term = Slot(uri=DENTMATMECH.term, name="term", curie=DENTMATMECH.curie('term'),
                   model_uri=DENTMATMECH.term, domain=None, range=Optional[Union[dict, Term]])

slots.material_term = Slot(uri=DENTMATMECH.material_term, name="material_term", curie=DENTMATMECH.curie('material_term'),
                   model_uri=DENTMATMECH.material_term, domain=None, range=Union[dict, DentalMaterialDescriptor])

slots.category = Slot(uri=DENTMATMECH.category, name="category", curie=DENTMATMECH.curie('category'),
                   model_uri=DENTMATMECH.category, domain=None, range=Union[str, "MaterialCategoryEnum"])

slots.parents = Slot(uri=DENTMATMECH.parents, name="parents", curie=DENTMATMECH.curie('parents'),
                   model_uri=DENTMATMECH.parents, domain=None, range=Optional[Union[str, list[str]]])

slots.setting_mechanisms = Slot(uri=DENTMATMECH.setting_mechanisms, name="setting_mechanisms", curie=DENTMATMECH.curie('setting_mechanisms'),
                   model_uri=DENTMATMECH.setting_mechanisms, domain=None, range=Optional[Union[Union[str, "SettingMechanismEnum"], list[Union[str, "SettingMechanismEnum"]]]])

slots.mappings = Slot(uri=DENTMATMECH.mappings, name="mappings", curie=DENTMATMECH.curie('mappings'),
                   model_uri=DENTMATMECH.mappings, domain=None, range=Optional[Union[Union[dict, Mapping], list[Union[dict, Mapping]]]])

slots.predicate = Slot(uri=DENTMATMECH.predicate, name="predicate", curie=DENTMATMECH.curie('predicate'),
                   model_uri=DENTMATMECH.predicate, domain=None, range=Union[str, "MappingPredicateEnum"])

slots.source = Slot(uri=DENTMATMECH.source, name="source", curie=DENTMATMECH.curie('source'),
                   model_uri=DENTMATMECH.source, domain=None, range=Optional[str])

slots.see_also = Slot(uri=DENTMATMECH.see_also, name="see_also", curie=DENTMATMECH.curie('see_also'),
                   model_uri=DENTMATMECH.see_also, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.composition = Slot(uri=DENTMATMECH.composition, name="composition", curie=DENTMATMECH.curie('composition'),
                   model_uri=DENTMATMECH.composition, domain=None, range=Optional[Union[dict[Union[str, ComponentName], Union[dict, Component]], list[Union[dict, Component]]]])

slots.role = Slot(uri=DENTMATMECH.role, name="role", curie=DENTMATMECH.curie('role'),
                   model_uri=DENTMATMECH.role, domain=None, range=Optional[Union[str, "ComponentRoleEnum"]])

slots.chemical = Slot(uri=DENTMATMECH.chemical, name="chemical", curie=DENTMATMECH.curie('chemical'),
                   model_uri=DENTMATMECH.chemical, domain=None, range=Optional[Union[dict, ChemicalEntityDescriptor]])

slots.proportion = Slot(uri=DENTMATMECH.proportion, name="proportion", curie=DENTMATMECH.curie('proportion'),
                   model_uri=DENTMATMECH.proportion, domain=None, range=Optional[str])

slots.properties = Slot(uri=DENTMATMECH.properties, name="properties", curie=DENTMATMECH.curie('properties'),
                   model_uri=DENTMATMECH.properties, domain=None, range=Optional[Union[dict[Union[str, MaterialPropertyName], Union[dict, MaterialProperty]], list[Union[dict, MaterialProperty]]]])

slots.property_type = Slot(uri=DENTMATMECH.property_type, name="property_type", curie=DENTMATMECH.curie('property_type'),
                   model_uri=DENTMATMECH.property_type, domain=None, range=Union[str, "PropertyTypeEnum"])

slots.quality_term = Slot(uri=DENTMATMECH.quality_term, name="quality_term", curie=DENTMATMECH.curie('quality_term'),
                   model_uri=DENTMATMECH.quality_term, domain=None, range=Optional[Union[dict, QualityDescriptor]])

slots.value = Slot(uri=DENTMATMECH.value, name="value", curie=DENTMATMECH.curie('value'),
                   model_uri=DENTMATMECH.value, domain=None, range=Optional[str])

slots.unit = Slot(uri=DENTMATMECH.unit, name="unit", curie=DENTMATMECH.curie('unit'),
                   model_uri=DENTMATMECH.unit, domain=None, range=Optional[str])

slots.test_method = Slot(uri=DENTMATMECH.test_method, name="test_method", curie=DENTMATMECH.curie('test_method'),
                   model_uri=DENTMATMECH.test_method, domain=None, range=Optional[str])

slots.conditions = Slot(uri=DENTMATMECH.conditions, name="conditions", curie=DENTMATMECH.curie('conditions'),
                   model_uri=DENTMATMECH.conditions, domain=None, range=Optional[str])

slots.clinical_uses = Slot(uri=DENTMATMECH.clinical_uses, name="clinical_uses", curie=DENTMATMECH.curie('clinical_uses'),
                   model_uri=DENTMATMECH.clinical_uses, domain=None, range=Optional[Union[dict[Union[str, ClinicalUseName], Union[dict, ClinicalUse]], list[Union[dict, ClinicalUse]]]])

slots.use_context = Slot(uri=DENTMATMECH.use_context, name="use_context", curie=DENTMATMECH.curie('use_context'),
                   model_uri=DENTMATMECH.use_context, domain=None, range=Union[str, "ClinicalUseContextEnum"])

slots.procedure = Slot(uri=DENTMATMECH.procedure, name="procedure", curie=DENTMATMECH.curie('procedure'),
                   model_uri=DENTMATMECH.procedure, domain=None, range=Optional[Union[dict, DentalProcedureDescriptor]])

slots.anatomical_site = Slot(uri=DENTMATMECH.anatomical_site, name="anatomical_site", curie=DENTMATMECH.curie('anatomical_site'),
                   model_uri=DENTMATMECH.anatomical_site, domain=None, range=Optional[Union[dict, AnatomicalEntityDescriptor]])

slots.indications = Slot(uri=DENTMATMECH.indications, name="indications", curie=DENTMATMECH.curie('indications'),
                   model_uri=DENTMATMECH.indications, domain=None, range=Optional[Union[str, list[str]]])

slots.contraindications = Slot(uri=DENTMATMECH.contraindications, name="contraindications", curie=DENTMATMECH.curie('contraindications'),
                   model_uri=DENTMATMECH.contraindications, domain=None, range=Optional[Union[str, list[str]]])

slots.clinical_performance = Slot(uri=DENTMATMECH.clinical_performance, name="clinical_performance", curie=DENTMATMECH.curie('clinical_performance'),
                   model_uri=DENTMATMECH.clinical_performance, domain=None, range=Optional[Union[dict[Union[str, ClinicalPerformanceName], Union[dict, ClinicalPerformance]], list[Union[dict, ClinicalPerformance]]]])

slots.measure_type = Slot(uri=DENTMATMECH.measure_type, name="measure_type", curie=DENTMATMECH.curie('measure_type'),
                   model_uri=DENTMATMECH.measure_type, domain=None, range=Union[str, "PerformanceMeasureEnum"])

slots.follow_up_years = Slot(uri=DENTMATMECH.follow_up_years, name="follow_up_years", curie=DENTMATMECH.curie('follow_up_years'),
                   model_uri=DENTMATMECH.follow_up_years, domain=None, range=Optional[float])

slots.population = Slot(uri=DENTMATMECH.population, name="population", curie=DENTMATMECH.curie('population'),
                   model_uri=DENTMATMECH.population, domain=None, range=Optional[str])

slots.comparator = Slot(uri=DENTMATMECH.comparator, name="comparator", curie=DENTMATMECH.curie('comparator'),
                   model_uri=DENTMATMECH.comparator, domain=None, range=Optional[str])

slots.adverse_effects = Slot(uri=DENTMATMECH.adverse_effects, name="adverse_effects", curie=DENTMATMECH.curie('adverse_effects'),
                   model_uri=DENTMATMECH.adverse_effects, domain=None, range=Optional[Union[dict[Union[str, AdverseEffectName], Union[dict, AdverseEffect]], list[Union[dict, AdverseEffect]]]])

slots.effect_category = Slot(uri=DENTMATMECH.effect_category, name="effect_category", curie=DENTMATMECH.curie('effect_category'),
                   model_uri=DENTMATMECH.effect_category, domain=None, range=Union[str, "AdverseEffectCategoryEnum"])

slots.effect_term = Slot(uri=DENTMATMECH.effect_term, name="effect_term", curie=DENTMATMECH.curie('effect_term'),
                   model_uri=DENTMATMECH.effect_term, domain=None, range=Optional[Union[dict, PhenotypeDescriptor]])

slots.frequency = Slot(uri=DENTMATMECH.frequency, name="frequency", curie=DENTMATMECH.curie('frequency'),
                   model_uri=DENTMATMECH.frequency, domain=None, range=Optional[str])

slots.regulatory_status = Slot(uri=DENTMATMECH.regulatory_status, name="regulatory_status", curie=DENTMATMECH.curie('regulatory_status'),
                   model_uri=DENTMATMECH.regulatory_status, domain=None, range=Optional[Union[Union[dict, RegulatoryStatus], list[Union[dict, RegulatoryStatus]]]])

slots.agency = Slot(uri=DENTMATMECH.agency, name="agency", curie=DENTMATMECH.curie('agency'),
                   model_uri=DENTMATMECH.agency, domain=None, range=Union[str, "RegulatoryAgencyEnum"])

slots.jurisdiction = Slot(uri=DENTMATMECH.jurisdiction, name="jurisdiction", curie=DENTMATMECH.curie('jurisdiction'),
                   model_uri=DENTMATMECH.jurisdiction, domain=None, range=Optional[str])

slots.status = Slot(uri=DENTMATMECH.status, name="status", curie=DENTMATMECH.curie('status'),
                   model_uri=DENTMATMECH.status, domain=None, range=Union[str, "RegulatoryStatusEnum"])

slots.regulation_number = Slot(uri=DENTMATMECH.regulation_number, name="regulation_number", curie=DENTMATMECH.curie('regulation_number'),
                   model_uri=DENTMATMECH.regulation_number, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{3}\.\d{4}$'))

slots.regulation_title = Slot(uri=DENTMATMECH.regulation_title, name="regulation_title", curie=DENTMATMECH.curie('regulation_title'),
                   model_uri=DENTMATMECH.regulation_title, domain=None, range=Optional[str])

slots.device_class = Slot(uri=DENTMATMECH.device_class, name="device_class", curie=DENTMATMECH.curie('device_class'),
                   model_uri=DENTMATMECH.device_class, domain=None, range=Optional[Union[str, "DeviceClassEnum"]])

slots.product_codes = Slot(uri=DENTMATMECH.product_codes, name="product_codes", curie=DENTMATMECH.curie('product_codes'),
                   model_uri=DENTMATMECH.product_codes, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Z]{3}$'))

slots.pathways = Slot(uri=DENTMATMECH.pathways, name="pathways", curie=DENTMATMECH.curie('pathways'),
                   model_uri=DENTMATMECH.pathways, domain=None, range=Optional[Union[Union[str, "RegulatoryPathwayEnum"], list[Union[str, "RegulatoryPathwayEnum"]]]])

slots.special_controls = Slot(uri=DENTMATMECH.special_controls, name="special_controls", curie=DENTMATMECH.curie('special_controls'),
                   model_uri=DENTMATMECH.special_controls, domain=None, range=Optional[Union[str, list[str]]])

slots.identification = Slot(uri=DENTMATMECH.identification, name="identification", curie=DENTMATMECH.curie('identification'),
                   model_uri=DENTMATMECH.identification, domain=None, range=Optional[str])

slots.approved_uses = Slot(uri=DENTMATMECH.approved_uses, name="approved_uses", curie=DENTMATMECH.curie('approved_uses'),
                   model_uri=DENTMATMECH.approved_uses, domain=None, range=Optional[Union[dict[Union[str, ApprovedUseName], Union[dict, ApprovedUse]], list[Union[dict, ApprovedUse]]]])

slots.restrictions = Slot(uri=DENTMATMECH.restrictions, name="restrictions", curie=DENTMATMECH.curie('restrictions'),
                   model_uri=DENTMATMECH.restrictions, domain=None, range=Optional[Union[str, list[str]]])

slots.effective_date = Slot(uri=DENTMATMECH.effective_date, name="effective_date", curie=DENTMATMECH.curie('effective_date'),
                   model_uri=DENTMATMECH.effective_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.source_url = Slot(uri=DENTMATMECH.source_url, name="source_url", curie=DENTMATMECH.curie('source_url'),
                   model_uri=DENTMATMECH.source_url, domain=None, range=Optional[Union[str, URI]])

slots.products = Slot(uri=DENTMATMECH.products, name="products", curie=DENTMATMECH.curie('products'),
                   model_uri=DENTMATMECH.products, domain=None, range=Optional[Union[dict[Union[str, CommercialProductName], Union[dict, CommercialProduct]], list[Union[dict, CommercialProduct]]]])

slots.manufacturer = Slot(uri=DENTMATMECH.manufacturer, name="manufacturer", curie=DENTMATMECH.curie('manufacturer'),
                   model_uri=DENTMATMECH.manufacturer, domain=None, range=Optional[str])

slots.submissions = Slot(uri=DENTMATMECH.submissions, name="submissions", curie=DENTMATMECH.curie('submissions'),
                   model_uri=DENTMATMECH.submissions, domain=None, range=Optional[Union[Union[dict, RegulatorySubmission], list[Union[dict, RegulatorySubmission]]]])

slots.submission_number = Slot(uri=DENTMATMECH.submission_number, name="submission_number", curie=DENTMATMECH.curie('submission_number'),
                   model_uri=DENTMATMECH.submission_number, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(K|P|DEN|N|H|BK)\d{6}(?:/S\d{3})?$'))

slots.pathway = Slot(uri=DENTMATMECH.pathway, name="pathway", curie=DENTMATMECH.curie('pathway'),
                   model_uri=DENTMATMECH.pathway, domain=None, range=Optional[Union[str, "RegulatoryPathwayEnum"]])

slots.decision = Slot(uri=DENTMATMECH.decision, name="decision", curie=DENTMATMECH.curie('decision'),
                   model_uri=DENTMATMECH.decision, domain=None, range=Optional[Union[str, "RegulatoryStatusEnum"]])

slots.decision_date = Slot(uri=DENTMATMECH.decision_date, name="decision_date", curie=DENTMATMECH.curie('decision_date'),
                   model_uri=DENTMATMECH.decision_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.product_code = Slot(uri=DENTMATMECH.product_code, name="product_code", curie=DENTMATMECH.curie('product_code'),
                   model_uri=DENTMATMECH.product_code, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]{3}$'))

slots.indications_for_use = Slot(uri=DENTMATMECH.indications_for_use, name="indications_for_use", curie=DENTMATMECH.curie('indications_for_use'),
                   model_uri=DENTMATMECH.indications_for_use, domain=None, range=Optional[str])

slots.standards = Slot(uri=DENTMATMECH.standards, name="standards", curie=DENTMATMECH.curie('standards'),
                   model_uri=DENTMATMECH.standards, domain=None, range=Optional[Union[Union[dict, Standard], list[Union[dict, Standard]]]])

slots.identifier = Slot(uri=DENTMATMECH.identifier, name="identifier", curie=DENTMATMECH.curie('identifier'),
                   model_uri=DENTMATMECH.identifier, domain=None, range=str)

slots.title = Slot(uri=DENTMATMECH.title, name="title", curie=DENTMATMECH.curie('title'),
                   model_uri=DENTMATMECH.title, domain=None, range=Optional[str])

slots.organization = Slot(uri=DENTMATMECH.organization, name="organization", curie=DENTMATMECH.curie('organization'),
                   model_uri=DENTMATMECH.organization, domain=None, range=Optional[str])

slots.url = Slot(uri=DENTMATMECH.url, name="url", curie=DENTMATMECH.curie('url'),
                   model_uri=DENTMATMECH.url, domain=None, range=Optional[Union[str, URI]])

slots.evidence = Slot(uri=DENTMATMECH.evidence, name="evidence", curie=DENTMATMECH.curie('evidence'),
                   model_uri=DENTMATMECH.evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.reference = Slot(uri=DENTMATMECH.reference, name="reference", curie=DENTMATMECH.curie('reference'),
                   model_uri=DENTMATMECH.reference, domain=None, range=Union[str, ReferenceIdentifier])

slots.reference_title = Slot(uri=DENTMATMECH.reference_title, name="reference_title", curie=DENTMATMECH.curie('reference_title'),
                   model_uri=DENTMATMECH.reference_title, domain=None, range=Optional[str])

slots.supports = Slot(uri=DENTMATMECH.supports, name="supports", curie=DENTMATMECH.curie('supports'),
                   model_uri=DENTMATMECH.supports, domain=None, range=Union[str, "EvidenceItemSupportEnum"])

slots.evidence_source = Slot(uri=DENTMATMECH.evidence_source, name="evidence_source", curie=DENTMATMECH.curie('evidence_source'),
                   model_uri=DENTMATMECH.evidence_source, domain=None, range=Optional[Union[str, "EvidenceSourceEnum"]])

slots.snippet = Slot(uri=DENTMATMECH.snippet, name="snippet", curie=DENTMATMECH.curie('snippet'),
                   model_uri=DENTMATMECH.snippet, domain=None, range=Optional[str])

slots.explanation = Slot(uri=DENTMATMECH.explanation, name="explanation", curie=DENTMATMECH.curie('explanation'),
                   model_uri=DENTMATMECH.explanation, domain=None, range=Optional[str])

slots.DentalMaterialDescriptor_term = Slot(uri=DENTMATMECH.term, name="DentalMaterialDescriptor_term", curie=DENTMATMECH.curie('term'),
                   model_uri=DENTMATMECH.DentalMaterialDescriptor_term, domain=DentalMaterialDescriptor, range=Union[dict, Term])

slots.DentalProcedureDescriptor_term = Slot(uri=DENTMATMECH.term, name="DentalProcedureDescriptor_term", curie=DENTMATMECH.curie('term'),
                   model_uri=DENTMATMECH.DentalProcedureDescriptor_term, domain=DentalProcedureDescriptor, range=Optional[Union[dict, Term]])

slots.ChemicalEntityDescriptor_term = Slot(uri=DENTMATMECH.term, name="ChemicalEntityDescriptor_term", curie=DENTMATMECH.curie('term'),
                   model_uri=DENTMATMECH.ChemicalEntityDescriptor_term, domain=ChemicalEntityDescriptor, range=Optional[Union[dict, Term]])

slots.AnatomicalEntityDescriptor_term = Slot(uri=DENTMATMECH.term, name="AnatomicalEntityDescriptor_term", curie=DENTMATMECH.curie('term'),
                   model_uri=DENTMATMECH.AnatomicalEntityDescriptor_term, domain=AnatomicalEntityDescriptor, range=Optional[Union[dict, Term]])

slots.PhenotypeDescriptor_term = Slot(uri=DENTMATMECH.term, name="PhenotypeDescriptor_term", curie=DENTMATMECH.curie('term'),
                   model_uri=DENTMATMECH.PhenotypeDescriptor_term, domain=PhenotypeDescriptor, range=Optional[Union[dict, Term]])

slots.QualityDescriptor_term = Slot(uri=DENTMATMECH.term, name="QualityDescriptor_term", curie=DENTMATMECH.curie('term'),
                   model_uri=DENTMATMECH.QualityDescriptor_term, domain=QualityDescriptor, range=Optional[Union[dict, Term]])

slots.Component_name = Slot(uri=DENTMATMECH.name, name="Component_name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.Component_name, domain=Component, range=Union[str, ComponentName])

slots.MaterialProperty_name = Slot(uri=DENTMATMECH.name, name="MaterialProperty_name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.MaterialProperty_name, domain=MaterialProperty, range=Union[str, MaterialPropertyName])

slots.ClinicalUse_name = Slot(uri=DENTMATMECH.name, name="ClinicalUse_name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.ClinicalUse_name, domain=ClinicalUse, range=Union[str, ClinicalUseName])

slots.ClinicalPerformance_name = Slot(uri=DENTMATMECH.name, name="ClinicalPerformance_name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.ClinicalPerformance_name, domain=ClinicalPerformance, range=Union[str, ClinicalPerformanceName])

slots.AdverseEffect_name = Slot(uri=DENTMATMECH.name, name="AdverseEffect_name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.AdverseEffect_name, domain=AdverseEffect, range=Union[str, AdverseEffectName])

slots.ApprovedUse_name = Slot(uri=DENTMATMECH.name, name="ApprovedUse_name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.ApprovedUse_name, domain=ApprovedUse, range=Union[str, ApprovedUseName])

slots.ApprovedUse_use_context = Slot(uri=DENTMATMECH.use_context, name="ApprovedUse_use_context", curie=DENTMATMECH.curie('use_context'),
                   model_uri=DENTMATMECH.ApprovedUse_use_context, domain=ApprovedUse, range=Union[str, "ClinicalUseContextEnum"])

slots.CommercialProduct_name = Slot(uri=DENTMATMECH.name, name="CommercialProduct_name", curie=DENTMATMECH.curie('name'),
                   model_uri=DENTMATMECH.CommercialProduct_name, domain=CommercialProduct, range=Union[str, CommercialProductName])
