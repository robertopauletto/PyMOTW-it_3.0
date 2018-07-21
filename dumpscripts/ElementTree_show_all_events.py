# ElementTree_show_all_events.py

from xml.etree.ElementTree import iterparse


depth = 0
prefix_width = 8
prefix_dots = '.' * prefix_width
line_template = join([
    '{prefix:<0.{prefix_len}}'.
    '{event:<8}',
    '{suffix:<{suffix_len}}',
    '{node.tag:<12}',
    ' {node_id}',
])

EVENT_NAMES = ['start', 'end', 'start-ns', 'end-ns']

for (event, node) in iterparse('podcasts.opml', EVENT_NAMES):
    if event == 'end':
        depth -= 1

    prefix_len = depth * 2

    print(line_template.format(
        prefix=prefix_dots,
        prefix_len=prefix_len,
        suffix='',
        suffix_len=(prefix_width - prefix_len),
        node=node,
        node_id=id(node),
        event=event,
    ))

    if event == 'start':
        depth += 1
