# Problem 00: AI Harm (10 points / 40 points)

Edit this file to solve problem 00. Problem 00 will not be auto-graded.

This question is most aligned to our first class, where we discussed motivations for this course along with the benefits and risks that modern AI methods are bringing to society.

## Problem 00 - Part A

Modern AI techniques stand to bring great benefits to society, but these benefits come with risks of causing harm to individuals, organizations, and societies. This is particularly true for deep learning algorithms, which are composed of several layers of linear and nonlinear processing. This makes deep learning algorithms exceptionally capable for detecting subtle patterns in data and making inferences therefrom, often achieving human-like or even super-human performance. However, the deep layers of linear and nonlinear processing which comprise deep learned algorithms also make it hard for those deploying them to ensure they behave as expected. Deep learning algorithms might learn the right results for the wrong reason, might appear to perform well initially and then degrade in performance when the input data drifts, and might have unintended biases towards producing particular results.

List five examples in recent years (2010 onward) where AI capabilities have causes harm to people, organizations, or society:

* Example 1: In 2018, an Uber self-driving test vehicle in Tempe, Arizona struck and killed pedestrian Elaine Herzberg after the perception/planning stack failed to classify her in time and did not brake autonomously.
* Example 2: ProPublica’s 2016 investigation of COMPAS found that the recidivism-risk tool used in U.S. courts was much more likely to falsely flag Black defendants as high risk than White defendants, affecting bail and sentencing decisions.
* Example 3: Amazon scrapped an internal hiring model (reported in 2018) after it learned to penalize resumes that indicated women, because historical hiring data were biased toward men.
* Example 4: In 2016, Microsoft’s Twitter chatbot Tay was manipulated by users into posting racist and offensive content within hours of public release.
* Example 5: In 2020, Detroit police arrested Robert Williams after a facial-recognition match to low-quality surveillance video; he was innocent, illustrating harm from biased/unreliable biometric identification.

## Problem 00 - Part B

For one of the examples you chose, describe a best practice we have discussed so far that could have helped to prevent the negative outcomes. You do not need to know how to implement the best practice you reference in code here or guarantee that the best practice you would recommend would fix the problem completely.

For the Uber crash: a best practice we discussed is treating the AI as part of a larger socio-technical system and evaluating it continuously in its real operational design domain, not only in a controlled demo. That includes monitoring for data drift and unexpected percepts (night, crossing pedestrians outside typical training cases), requiring fallback behavior when the model is uncertain, and checking that the system learned the right result for the right reason (true pedestrian detection) rather than a shortcut that fails off the training distribution. NIST-style risk management—define context of use, test robustness, and keep humans/safety systems in the loop—would not guarantee zero accidents, but it would have made it less likely to deploy a stack that neither classified the pedestrian nor braked.

## Problem 00 - Part C

While the risks associated with AI are exacerbated by the prevalence of powerful deep architectures which started to gain popularity in the 2010s for image processing and in the 2020s for natural language processing, the risks of AI are not specific to deep neural networks. There are many other capabilities that would be considered AI by the Russell and Norvig definition that are not neural networks, and have been in use long before neural networks became popular.

List a time where an AI capability caused harm to an individual, organization, or society **before the year 2000**.

In 1988, the Aegis combat system aboard the USS Vincennes misclassified Iran Air Flight 655 as a hostile military aircraft; the ship fired and killed 290 civilians. The automated tracking/classification pipeline, not a neural network, was central to the decision.

Why does it make sense to describe this example as being caused by AI? Reference the Russell and Norvig definition of AI (*"AI agents are those which receive percepts from the environment and take actions"*).

Russell and Norvig define AI agents as systems that receive percepts from the environment and take actions to achieve goals. The Aegis system sensed radar and IFF signals (percepts), computed a threat classification, and recommended/enabled a weapons action. Harm followed from that perceive–act loop even though the internals were conventional/expert-system style, not deep learning.