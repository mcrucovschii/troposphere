# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer
from .validators.iottwinmaker import validate_listvalue, validate_nestedtypel


class LambdaFunction(AWSProperty):
    """
    `LambdaFunction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-lambdafunction.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
    }


class DataConnector(AWSProperty):
    """
    `DataConnector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-dataconnector.html>`__
    """

    props: PropsDictType = {
        "IsNative": (boolean, False),
        "Lambda": (LambdaFunction, False),
    }


class Function(AWSProperty):
    """
    `Function <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-function.html>`__
    """

    props: PropsDictType = {
        "ImplementedBy": (DataConnector, False),
        "RequiredProperties": ([str], False),
        "Scope": (str, False),
    }


class DataValue(AWSProperty):
    """
    `DataValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html>`__
    """

    props: PropsDictType = {
        "BooleanValue": (boolean, False),
        "DoubleValue": (double, False),
        "Expression": (str, False),
        "IntegerValue": (integer, False),
        "ListValue": (validate_listvalue, False),
        "LongValue": (double, False),
        "MapValue": (dict, False),
        "RelationshipValue": (dict, False),
        "StringValue": (str, False),
    }


class Relationship(AWSProperty):
    """
    `Relationship <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-relationship.html>`__
    """

    props: PropsDictType = {
        "RelationshipType": (str, False),
        "TargetComponentTypeId": (str, False),
    }


class DataType(AWSProperty):
    """
    `DataType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datatype.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": ([DataValue], False),
        "NestedType": (validate_nestedtypel, False),
        "Relationship": (Relationship, False),
        "Type": (str, True),
        "UnitOfMeasure": (str, False),
    }


class PropertyDefinition(AWSProperty):
    """
    `PropertyDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html>`__
    """

    props: PropsDictType = {
        "Configurations": (dict, False),
        "DataType": (DataType, False),
        "DefaultValue": (DataValue, False),
        "IsExternalId": (boolean, False),
        "IsRequiredInEntity": (boolean, False),
        "IsStoredExternally": (boolean, False),
        "IsTimeSeries": (boolean, False),
    }


class ComponentType(AWSObject):
    """
    `ComponentType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html>`__
    """

    resource_type = "AWS::IoTTwinMaker::ComponentType"

    props: PropsDictType = {
        "ComponentTypeId": (str, True),
        "Description": (str, False),
        "ExtendsFrom": ([str], False),
        "Functions": (dict, False),
        "IsSingleton": (boolean, False),
        "PropertyDefinitions": (dict, False),
        "Tags": (dict, False),
        "WorkspaceId": (str, True),
    }


class Property(AWSProperty):
    """
    `Property <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-property.html>`__
    """

    props: PropsDictType = {
        "Definition": (dict, False),
        "Value": (DataValue, False),
    }


class Status(AWSProperty):
    """
    `Status <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-status.html>`__
    """

    props: PropsDictType = {
        "Error": (dict, False),
        "State": (str, False),
    }


class Component(AWSProperty):
    """
    `Component <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html>`__
    """

    props: PropsDictType = {
        "ComponentName": (str, False),
        "ComponentTypeId": (str, False),
        "DefinedIn": (str, False),
        "Description": (str, False),
        "Properties": (dict, False),
        "Status": (Status, False),
    }


class Entity(AWSObject):
    """
    `Entity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html>`__
    """

    resource_type = "AWS::IoTTwinMaker::Entity"

    props: PropsDictType = {
        "Components": (dict, False),
        "Description": (str, False),
        "EntityId": (str, False),
        "EntityName": (str, True),
        "ParentEntityId": (str, False),
        "Tags": (dict, False),
        "WorkspaceId": (str, True),
    }


class Scene(AWSObject):
    """
    `Scene <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html>`__
    """

    resource_type = "AWS::IoTTwinMaker::Scene"

    props: PropsDictType = {
        "Capabilities": ([str], False),
        "ContentLocation": (str, True),
        "Description": (str, False),
        "SceneId": (str, True),
        "Tags": (dict, False),
        "WorkspaceId": (str, True),
    }


class Workspace(AWSObject):
    """
    `Workspace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html>`__
    """

    resource_type = "AWS::IoTTwinMaker::Workspace"

    props: PropsDictType = {
        "Description": (str, False),
        "Role": (str, True),
        "S3Location": (str, True),
        "Tags": (dict, False),
        "WorkspaceId": (str, True),
    }