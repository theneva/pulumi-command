// Copyright 2016-2022, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//	http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package remote

import (
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource/archive"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource/asset"
)

type Copy struct{}

var _ = (infer.Annotated)((*Copy)(nil))

// Copy implements Annotate which allows you to attach descriptions to the Copy resource.
func (c *Copy) Annotate(a infer.Annotator) {
	a.Describe(&c, "Copy an Asset or Archive to a remote host.")
}

type CopyInputs struct {
	Connection   *Connection      `pulumi:"connection" provider:"secret"`
	Triggers     *[]interface{}   `pulumi:"triggers,optional" providers:"replaceOnDelete"`
	LocalAsset   *asset.Asset     `pulumi:"localAsset,optional"`
	LocalArchive *archive.Archive `pulumi:"localArchive,optional"`
	RemotePath   string           `pulumi:"remotePath"`
}

func (c *CopyInputs) Annotate(a infer.Annotator) {
	a.Describe(&c.Connection, "The parameters with which to connect to the remote host.")
	a.Describe(&c.Triggers, "Trigger replacements on changes to this input.")
	a.Describe(&c.LocalAsset, "An asset to upload. It must be a path based asset. Only one of LocalAsset or LocalArchive can be set.")
	a.Describe(&c.LocalArchive, "An archive to upload. It must be a path based archive. Only one of LocalAsset or LocalArchive can be set.")
	a.Describe(&c.RemotePath, "The destination path in the remote host.")
}

func (c *CopyInputs) sourcePath() string {
	if c.LocalAsset != nil {
		return c.LocalAsset.Path
	}
	return c.LocalArchive.Path
}

func (c *CopyInputs) hash() string {
	if c.LocalAsset != nil {
		return c.LocalAsset.Hash
	}
	return c.LocalArchive.Hash
}

type CopyOutputs struct {
	CopyInputs
}
