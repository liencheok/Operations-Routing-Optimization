# Waste Collection CVRP Optimization

This project focuses on optimizing municipal waste collection routes in Langkawi, Malaysia,
using the Capacitated Vehicle Routing Problem (CVRP) and heuristic algorithms.

The goal is to generate efficient vehicle routes that reduce total travel distance and
improve operational efficiency for waste collection.

## Project Overview

Waste collection in Langkawi faces challenges due to increasing waste volume from tourism
and inefficient manual routing schedules.

This project models the waste collection process as a CVRP and applies optimization techniques
to find improved routing solutions under real-world constraints (vehicle capacity, service locations).

## Methods Used

- CVRP (Capacitated Vehicle Routing Problem)
- Google OR-Tools for optimization
- Custom heuristic for route improvement
- Geographic distance modeling
- Visualization using Folium

## Files Description

- `cvrp_solution.py`  
  Main Python script that formulates and solves the CVRP using OR-Tools and heuristics.

- `distance_matrix.py`  
  Generates the distance matrix between all waste collection locations based on geographic coordinates.

- `location_coordinates.py`  
  Contains the coordinates of the depot, landfill, and waste collection points in Langkawi.

- `dataset_waste_collection_langkawi.xlsx`  
  Dataset containing waste collection locations and related operational data.

- `route_visualization.html`  
  Interactive map visualizing the optimized waste collection routes.

## Results

The optimized routes produced using CVRP methodologies demonstrate improved
efficiency compared to baseline routing. The interactive visualization map shows
the planned collection paths for each vehicle.

## Notes

This project was developed as part of academic coursework and final year research,
using real-world-inspired data for waste collection routing in Langkawi.
