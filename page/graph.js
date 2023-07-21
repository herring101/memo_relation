// graph.js
d3.json('graph.json').then(function(graph) {
  var svg = d3.select("#my_graph"),
      width = +svg.attr("width"),
      height = +svg.attr("height");

  var simulation = d3.forceSimulation()
      .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(200))
      .force("charge", d3.forceManyBody())
      .force("center", d3.forceCenter(width / 2, height / 2));

  var link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(graph.links)
    .join("line")
      .attr("stroke-width", function(d) { return Math.sqrt(d.value)*20; });  // Stroke width based on value

  var node = svg.append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
    .selectAll("circle")
    .data(graph.nodes)
    .join("circle")
      .attr("r", 20)  // Bigger nodes
      .attr("fill", "#6699cc")
      .call(drag(simulation));

  // Display group name as label
  var labels = svg.append("g")
      .attr("class", "labels")
    .selectAll("text")
      .data(graph.nodes)
    .enter().append("text")
      .attr("text-anchor", "middle")
      .attr("alignment-baseline", "middle")
      .style("font-size", 12)
      .style("pointer-events", "none")
      .text(function(d) { return d.group; });

  node.append("title")
      .text(function(d) { return d.id; });

  simulation.nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(graph.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });

    labels
        .attr("x", function(d) { return d.x; })
        .attr("y", function(d) { return d.y; });
  }

  function drag(simulation) {
    function dragstarted(event) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      event.subject.fx = event.subject.x;
      event.subject.fy = event.subject.y;
    }

    function dragged(event) {
      event.subject.fx = event.x;
      event.subject.fy = event.y;
    }

    function dragended(event) {
      if (!event.active) simulation.alphaTarget(0);
      event.subject.fx = null;
      event.subject.fy = null;
    }

    return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
  }
});
