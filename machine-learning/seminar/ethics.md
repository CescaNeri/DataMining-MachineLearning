# AI Ethics

*Gabriele Graffieti* - CV Algorithm Engineer at Ambarella

Case Study:

You work in a large company which receives thousands of CVs daily.
The openings are many and different from each other. Of course, skimming through CVs requires a lot of time and effort.

Good candidates can be erroneously discarded in this preliminary phase.

The idea is to develop an AI system that analyzes the CVs continuously.

**Solution**

Use the CVs of the current employees as ground truth data, in order to select candidates similar to the people that already work in the company.

**Results**

The selected people are very good candidates and the system performs better than our HRs in selecting good candidates.

*Are we happy about this system?*

This system was used by Amazon and it showed bias against women.

**Issues**

This problem is not easily detectable in the first place.
On other hand, if we remove all the gender info from the CV, the model is still able to infer on that information.

*Are you sure about your data?*

- Have you checked the labels?
- Do you know how the data is labeled?
- Do you know who labeled the data?

Some tools like **amazon mechanical turk** can be used to label data but, some issues can be found with this tool:
For example, emotion recognition can be labelled wrongly due to different cultures.

This aspect is particularly relevant with high risk AI applications, like:

- Diagnosis applications
- Control of critical infrastructure
- Law enforcement
- Scoring
- Hiring

Many people say that critical decisions should be taken by humans, however, humans are not perfect.

*In the US, the best day to have a trial is Monday after a victory of the local football team*

Human decision making is highly affected by mood, personal concerns, stress, level of sleep, affinity with the assessed person, stereotypes and so on.

**What about human-AI collaboration?**

It seems the perfect solution but humans can be biased by the fact they that believe that AI is always right so they tend to trust it.

Also, after some time, humans unconsciously trust AI and they no longer be able to spot errors.

On the other hand, what if AI is right but the human overcome the decision?
And what if AI is wrong but it is so powerful that it can convince humans?

*Are we sure that we are completely free of biases?*





