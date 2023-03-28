// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Command.Remote.Inputs
{

    /// <summary>
    /// Instructions for how to connect to a remote endpoint.
    /// </summary>
    public sealed class ConnectionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        /// </summary>
        [Input("agentSocketPath")]
        public Input<string>? AgentSocketPath { get; set; }

        /// <summary>
        /// Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
        /// </summary>
        [Input("dialErrorLimit")]
        public Input<int>? DialErrorLimit { get; set; }

        /// <summary>
        /// The address of the resource to connect to.
        /// </summary>
        [Input("host", required: true)]
        public Input<string> Host { get; set; } = null!;

        /// <summary>
        /// The password we should use for the connection.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
        /// </summary>
        [Input("perDialTimeout")]
        public Input<int>? PerDialTimeout { get; set; }

        /// <summary>
        /// The port to connect to.
        /// </summary>
        [Input("port")]
        public Input<double>? Port { get; set; }

        /// <summary>
        /// The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        /// <summary>
        /// The password to use in case the private key is encrypted.
        /// </summary>
        [Input("privateKeyPassword")]
        public Input<string>? PrivateKeyPassword { get; set; }

        /// <summary>
        /// The connection settings for the bastion/proxy host.
        /// </summary>
        [Input("proxy")]
        public Input<Inputs.ProxyConnectionArgs>? Proxy { get; set; }

        /// <summary>
        /// The user that we should use for the connection.
        /// </summary>
        [Input("user")]
        public Input<string>? User { get; set; }

        public ConnectionArgs()
        {
            DialErrorLimit = 10;
            PerDialTimeout = 15;
            Port = 22;
            User = "root";
        }
        public static new ConnectionArgs Empty => new ConnectionArgs();
    }
}
