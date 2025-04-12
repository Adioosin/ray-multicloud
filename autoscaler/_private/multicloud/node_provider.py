import copy
from ray.autoscaler.node_provider import NodeProvider
from ray.autoscaler._private.aws.node_provider import AWSNodeProvider


class MulticloudProvider(NodeProvider):

    def __init__(self, provider_config, cluster_name):
        NodeProvider.__init__(self, provider_config, cluster_name)
        self.provider_config = provider_config
        self.cluster_name = cluster_name

        print(type(provider_config))
        self.providers = {}

        for node_config in provider_config["available_node_types"]:
            config = copy.deepcopy(provider_config)
            config["provider"] = node_config["provider"]
            del config["provider"]["resource_id"]
            self.providers[node_config["provider"]["resource_id"]] = AWSNodeProvider(config, cluster_name)
