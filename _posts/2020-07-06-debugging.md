---
layout: post
title: Announcements and debugging
tags: phase-3 phase-3-fe phase-3-be
---

## Announcements

- The due date on your cross-class API/React project has been moved to _Thursday_. You will present it as a pair at that time and answer questions. This is where your ability to move to Phase 4 will be determined. If your app does not work and/or you cannot answer questions about how it works, you may have to repeat Phase 3.
- We are considering not providing recordings in the future except in the case of absence.

## Resources

- [10 Debugging Tips for Beginners](https://blog.hartleybrody.com/debugging-code-beginner/). Read this thoroughly.

## Debugging tips

(taken from ["Debugging for absolute beginners" from the Visual Studio docs](https://docs.microsoft.com/en-us/visualstudio/debugger/debugging-absolute-beginners?view=vs-2019)):

---

### Clarify the problem by asking yourself the right questions

It helps to clarify the problem that you ran into before you try to fix it. We expect that you already ran into a problem in your code, otherwise you wouldn't be here trying to figure out how to debug it! So, before you start debugging, make sure you've identified the problem you're trying to solve:

- What did you expect your code to do?
- What happened instead?

If you ran into an error (exception) while running your app, that can be a good thing! An exception is an unexpected event encountered when running code, typically an error of some kind. A debugging tool can take you to the exact place in your code where the exception occurred and can help you investigate possible fixes.

If something else happened, what is the symptom of the problem? Do you already suspect where this problem occurred in your code? For example, if your code displays some text, but the text is incorrect, you know that either your data is bad or the code that set the display text has some kind of bug. By stepping through the code in a debugger, you can examine each and every change to your variables to discover exactly when and how incorrect values are assigned.

### Examine your assumptions

Before you investigate a bug or an error, think of the assumptions that made you expect a certain result. Hidden or unknown assumptions can get in the way of identifying a problem even when you are looking right at the cause of the problem in a debugger. You may have a long list of possible assumptions! Here are a few questions to ask yourself to challenge your assumptions.

- Are you using the right API (that is, the right object, function, method, or property)? An API that you're using might not do what you think it does. (After you examine the API call in the debugger, fixing it may require a trip to the documentation to help identify the correct API.)
- Are you using an API correctly? Maybe you used the right API but didn't use it in the right way.
- Does your code contain any typos? Some typos, like a simple misspelling of a variable name, can be difficult to see, especially when working with languages that don’t require variables to be declared before they’re used.
- Did you make a change to your code and assume it is unrelated to the problem that you're seeing?
- Did you expect an object or variable to contain a certain value (or a certain type of value) that's different from what really happened?
- Do you know the intent of the code? It is often more difficult to debug someone else's code. If it's not your code, it's possible you might need to spend time learning exactly what the code does before you can debug it effectively.

#### Tip

When writing code, start small, and start with code that works! (Good sample code is helpful here.) Sometimes, it is easier to fix a large or complicated set of code by starting with a small piece of code that demonstrates the core task you are trying to achieve. Then, you can modify or add code incrementally, testing at each point for errors.

By questioning your assumptions, you may reduce the time it takes to find a problem in your code. You may also reduce the time it takes to fix a problem.
