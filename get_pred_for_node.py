import networkx as nx
import json
import hashlib
from dateutil import parser


def get_pred_for(targetNode):
    f = open('dataset.json')
    data = json.load(f)
    f.close()

    nodes = []
    tags = set()

    G = nx.Graph()

    for i in data:
        nodeId = i['id']
        nodes.append(i['id'])
        G.add_node(nodeId, title = i['title'],content = i['content'], datetime = parser.parse(i['date']))
        for tag in i['tags']:
            tagId = str(int(hashlib.md5(tag.encode('utf-8')).hexdigest(), 16))[0:12]
            tags.add(tagId)
            G.add_edge(nodeId, tagId)


    pairs = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes) - 1):
            pairs.append((nodes[i], nodes[j]))

    # preds = nx.jaccard_coefficient(G, pairs)
    preds = nx.adamic_adar_index(G, pairs)
    filtered_preds = [pred for pred in preds if pred[2] > 0]
    sorted_preds = sorted(filtered_preds, key=lambda x: x[2])

    predNodesFirst = [(u, p) for v, u, p in sorted_preds if v == targetNode]
    predNodesSecond = [(v, p) for v, u, p in sorted_preds if u == targetNode]

    sortedPredNodes = sorted(predNodesFirst + predNodesSecond, key=lambda x: x[1])

    topPreds = sortedPredNodes[-199:]
    topPredsWithDatetime = [(v, G.nodes[targetNode]['datetime']) for v, p in topPreds]
    sortedTopPreds = sorted(topPredsWithDatetime, key=lambda x: x[1])

    top = sortedTopPreds[-3:]
    topIds = [v for v, p in top]
    return topIds

get_pred_for('20168')