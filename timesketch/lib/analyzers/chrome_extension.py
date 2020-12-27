"""Sketch analyzer plugin for installed Chrome extensions"""
from __future__ import unicode_literals

import logging
import re
import mechanize
import requests

from timesketch.lib import emojis
from timesketch.lib.analyzers import interface
from timesketch.lib.analyzers import manager



class ChromeExtensionsSketchPlugin(interface.BaseSketchAnalyzer):
    """Sketch analyzer for installed Chrome extensions"""

    NAME = 'chrome_extensions'


    def __init__(self, index_name, sketch_id):
        """Initialize The Sketch Analyzer.
        Args:
            index_name: Elasticsearch index name
            sketch_id: Sketch ID
        """
        self.index_name = index_name
        super(ChromeExtensionsSketchPlugin, self).__init__(
            index_name, sketch_id)

    def find_in_store(self,extension)
    """Finds extension page in Webstore and extracts title.
    Args:
        extension_id: Extension ID 
    """



    def run(self):
        """Entry point for the analyzer.
        Returns:
            String with summary of the analyzer result
        """
        # Elasticsearch query to find Chrome extensions from filestat
        query = ('(data_type:"fs:stat"'
                 'AND (filename:"Chrome" AND filename:"Extensions)')

        # Specify what returned fields you need for your analyzer.
        return_fields = ['filename', 'data_type']
        question_emoji = emojis.get_emoji('QUESTION')

        # Generator of events based on your query.
        events = self.event_stream(
            query_string=query, return_fields=return_fields)

        #  Add analyzer logic here.
        # Methods available to use for sketch analyzers:
        # sketch.get_all_indices()
        # sketch.add_view(name, query_string, query_filter={})
        # event.add_attributes({'foo': 'bar'})
        # event.add_tags(['tag_name'])
        # event_add_label('label')
        # event.add_star()
        # event.add_comment('comment')

        login_count = 0

        for event in events:
            data_type = event.source.get('data_type')
            filename = event.source.get('message')
            extension_id = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', message)
              if extension_id = 0
                continue
            title = find_in_store(extension_id)
              if title = "Error 404 (Not Found)!!1"
                 event.add_comment(
                             'Not found in Webstore')
                 event.add_emojis([question_emoji])
                 event.add_tags(['not_found'])
                 continue
         if extension_count > 0:
             self.sketch.add_view(
		 view_name='Chrome Extensions', analyzer_name=self.NAME,
		 query_string=query)


        # TODO: Return a summary from the analyzer.
        return 'Chrome Extension analyzer completed, {0:d} Chrome Extensions found'.format(
    extension_count)



manager.AnalysisManager.register_analyzer(ChromeExtensionsSketchPlugin)



"Extract extension ID from Chrome folders"


"Create a request to Chrome Webstore"

"Extract title from Chrome webstore"
