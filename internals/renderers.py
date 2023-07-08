from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = {} if not data else data
        new_data = {
            'status': True,
            'message': 'Success',
        }
        if renderer_context is not None:
            response = renderer_context['response']
            if response.exception or (
                response.status_code >= 400 and response.status_code < 600
            ):
                # An exception occured, so we want to add the exception
                # message to the response.
                new_data['status'] = False
                new_data['message'] = data.get('detail', 
                    data.get('message', 'An error occured'))
                # remove the detail key from the data, now that we have
                # added it to the response.
                if 'detail' in data:
                    del data['detail']
                new_data['errors'] = data.get('errors', None)
                # check the data for error "messages", if they exist, add them
                # if not, we pass the entire data object
                if not new_data['errors']:
                    messages = list(map(lambda x: [x.get('message', '')], 
                        list(data.get('messages', []))))
                    # convert the list of messages to a dictionary
                    # to maintain consistency with the errors format
                    new_data['errors'] = dict(enumerate(messages))
                # passing the entire data object
                if not new_data['errors']:
                    new_data['errors'] = data
            else:
                new_data['data'] = data.get('data', data)
                new_data['message'] = data.get('message', new_data['message'])

        # Now we can let the superclass render the data.
        return super(CustomJSONRenderer, self).render(new_data)