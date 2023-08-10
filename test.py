from src.oscal_pydantic.core import datatypes, properties

ns = datatypes.Uri(root="http://csrc.nist.gov/ns/oscal")
name = datatypes.Token("marking")
value = datatypes.String("test")

oscal_prop_dict = {"name": "marking", "value": "test"}

# Should Succeed
# test_prop = properties.OscalProperty.model_validate(oscal_prop_dict)

test_prop = properties.OscalProperty(name="marking", value="test")

# Should also succeed
test_prop_loc = properties.LocationProperty(name=name, value=value)

name = datatypes.Token("type")
value = datatypes.String("data-center")
loc_class = datatypes.Token("primary")

# Should succeed
test_loc = properties.LocationProperty(
    ns=ns, name=name, value=value, prop_class=loc_class
)

# Should fail
# test_bad = properties.PartyProperty(name=name, value=value)

name = datatypes.Token("version")
test_resource_version = properties.ResourceProperty(name=name, value=value)

name = datatypes.Token("type")
value = datatypes.String("logo")
test_resource_type = properties.ResourceProperty(name=name, value=value)

pass
