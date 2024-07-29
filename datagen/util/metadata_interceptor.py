import grpc

class MetadataInterceptor(grpc.UnaryUnaryClientInterceptor):
    def __init__(self, metadata):
        self.metadata = metadata

    def intercept_unary_unary(self, continuation, client_call_details, request):
        new_client_call_details = client_call_details._replace(metadata=self.metadata)
        return continuation(new_client_call_details, request)
