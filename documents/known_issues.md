# Known Issues

At the time of submission to the Code Challenge, due to time constraints, the following were known issues or features not yet implemented.
Tickets were being tracked in a Jira instance, but those could not be included in the submission.

## Bugs

* DBCC-49: Map - Mobile - Layer icon overlap with "close" button from popup
* DBCC-50: Map - Mobile - Selecting Drag and Drop pin should close the popup automatically
* DBCC-51: Map - Mobile performance - Webcam photos not showing systematically
* DBCC-52: Map - Mobile - Events and Webcams - Popups should open content centered on screen
* DBCC-54: Map - Mobile - Advisories, Webcam and Events, Routes are not displayed if not on http://localhost:3000
* DBCC-43: Admin - Remove extra title on message view page

## Features Not Implemented

1. Recalling and deleting routes

   Due to time constraints, we de-prioritized the feature of saving, recalling and deleting routes as it was not in the three user stories but just in the description. We also felt other features better demonstrated our core competencies.

2. Multiple base layers

   The free mapping library we are using only included the single base tile layer. Other libraries may include additional layers, but we felt this was not the purpose of the challenge.

3. Non-truck routing

   The user story specifically stated a commercial truck driver, and due to time contstraints, we focused on that use case. Given more time, we could implement truck routes as a toggle for the user.

4. More advanced event matching

   The current back-end method of matching road events to routes (using bbox) is overly simplified for the purposes of the coding challenge. A further improvement would need to do more exact matching using shape padding and intersection.

## Enhancements

* DBCC-48: Add route title text field in "add route" overlay
* DBCC-44: Admin - Improvements in UI if time
