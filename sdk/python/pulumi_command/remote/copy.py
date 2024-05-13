# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CopyArgs', 'Copy']

@pulumi.input_type
class CopyArgs:
    def __init__(__self__, *,
                 connection: pulumi.Input['ConnectionArgs'],
                 remote_path: pulumi.Input[str],
                 local_archive: Optional[pulumi.Input[pulumi.Archive]] = None,
                 local_asset: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None):
        """
        The set of arguments for constructing a Copy resource.
        :param pulumi.Input['ConnectionArgs'] connection: The parameters with which to connect to the remote host.
        :param pulumi.Input[str] remote_path: The destination path in the remote host.
        :param pulumi.Input[pulumi.Archive] local_archive: An archive to upload. It must be a path based archive. Only one of LocalAsset or LocalArchive can be set.
        :param pulumi.Input[Union[pulumi.Asset, pulumi.Archive]] local_asset: An asset to upload. It must be a path based asset. Only one of LocalAsset or LocalArchive can be set.
        :param pulumi.Input[Sequence[Any]] triggers: Trigger replacements on changes to this input.
        """
        pulumi.set(__self__, "connection", connection)
        pulumi.set(__self__, "remote_path", remote_path)
        if local_archive is not None:
            pulumi.set(__self__, "local_archive", local_archive)
        if local_asset is not None:
            pulumi.set(__self__, "local_asset", local_asset)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Input['ConnectionArgs']:
        """
        The parameters with which to connect to the remote host.
        """
        return pulumi.get(self, "connection")

    @connection.setter
    def connection(self, value: pulumi.Input['ConnectionArgs']):
        pulumi.set(self, "connection", value)

    @property
    @pulumi.getter(name="remotePath")
    def remote_path(self) -> pulumi.Input[str]:
        """
        The destination path in the remote host.
        """
        return pulumi.get(self, "remote_path")

    @remote_path.setter
    def remote_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "remote_path", value)

    @property
    @pulumi.getter(name="localArchive")
    def local_archive(self) -> Optional[pulumi.Input[pulumi.Archive]]:
        """
        An archive to upload. It must be a path based archive. Only one of LocalAsset or LocalArchive can be set.
        """
        return pulumi.get(self, "local_archive")

    @local_archive.setter
    def local_archive(self, value: Optional[pulumi.Input[pulumi.Archive]]):
        pulumi.set(self, "local_archive", value)

    @property
    @pulumi.getter(name="localAsset")
    def local_asset(self) -> Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]:
        """
        An asset to upload. It must be a path based asset. Only one of LocalAsset or LocalArchive can be set.
        """
        return pulumi.get(self, "local_asset")

    @local_asset.setter
    def local_asset(self, value: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]):
        pulumi.set(self, "local_asset", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[Any]]]:
        """
        Trigger replacements on changes to this input.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[Any]]]):
        pulumi.set(self, "triggers", value)


class Copy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection: Optional[pulumi.Input[pulumi.InputType['ConnectionArgs']]] = None,
                 local_archive: Optional[pulumi.Input[pulumi.Archive]] = None,
                 local_asset: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = None,
                 remote_path: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 __props__=None):
        """
        Copy an Asset or Archive to a remote host.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConnectionArgs']] connection: The parameters with which to connect to the remote host.
        :param pulumi.Input[pulumi.Archive] local_archive: An archive to upload. It must be a path based archive. Only one of LocalAsset or LocalArchive can be set.
        :param pulumi.Input[Union[pulumi.Asset, pulumi.Archive]] local_asset: An asset to upload. It must be a path based asset. Only one of LocalAsset or LocalArchive can be set.
        :param pulumi.Input[str] remote_path: The destination path in the remote host.
        :param pulumi.Input[Sequence[Any]] triggers: Trigger replacements on changes to this input.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CopyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Copy an Asset or Archive to a remote host.

        :param str resource_name: The name of the resource.
        :param CopyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CopyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection: Optional[pulumi.Input[pulumi.InputType['ConnectionArgs']]] = None,
                 local_archive: Optional[pulumi.Input[pulumi.Archive]] = None,
                 local_asset: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = None,
                 remote_path: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CopyArgs.__new__(CopyArgs)

            if connection is None and not opts.urn:
                raise TypeError("Missing required property 'connection'")
            __props__.__dict__["connection"] = None if connection is None else pulumi.Output.secret(connection)
            __props__.__dict__["local_archive"] = local_archive
            __props__.__dict__["local_asset"] = local_asset
            if remote_path is None and not opts.urn:
                raise TypeError("Missing required property 'remote_path'")
            __props__.__dict__["remote_path"] = remote_path
            __props__.__dict__["triggers"] = triggers
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["connection"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Copy, __self__).__init__(
            'command:remote:Copy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Copy':
        """
        Get an existing Copy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CopyArgs.__new__(CopyArgs)

        __props__.__dict__["connection"] = None
        __props__.__dict__["local_archive"] = None
        __props__.__dict__["local_asset"] = None
        __props__.__dict__["remote_path"] = None
        __props__.__dict__["triggers"] = None
        return Copy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Output['outputs.Connection']:
        """
        The parameters with which to connect to the remote host.
        """
        return pulumi.get(self, "connection")

    @property
    @pulumi.getter(name="localArchive")
    def local_archive(self) -> pulumi.Output[Optional[pulumi.Archive]]:
        """
        An archive to upload. It must be a path based archive. Only one of LocalAsset or LocalArchive can be set.
        """
        return pulumi.get(self, "local_archive")

    @property
    @pulumi.getter(name="localAsset")
    def local_asset(self) -> pulumi.Output[Optional[Union[pulumi.Asset, pulumi.Archive]]]:
        """
        An asset to upload. It must be a path based asset. Only one of LocalAsset or LocalArchive can be set.
        """
        return pulumi.get(self, "local_asset")

    @property
    @pulumi.getter(name="remotePath")
    def remote_path(self) -> pulumi.Output[str]:
        """
        The destination path in the remote host.
        """
        return pulumi.get(self, "remote_path")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Trigger replacements on changes to this input.
        """
        return pulumi.get(self, "triggers")

